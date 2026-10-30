"""Turn a photo into a soft-pastel drawing on toothed paper.

Usage:
    python pastel.py photo.jpg -o pastel.png [--size 1400] [--seed 7] [--gif timelapse.gif]

How it works:
    1. The photo is fitted onto a sheet of paper with a grain (tooth) texture.
    2. Strokes are laid down coarse-to-fine in LAYERS. Each layer reads colors
       from a blurred copy of the photo; finer layers only go where the previous
       blur level differs a lot from this one (the "error" map), i.e. detail.
    3. Stroke direction follows the image's edges (structure tensor), and each
       stroke bends a little along that flow field.
    4. Pigment only catches on the raised parts of the paper grain, which gives
       the broken, chalky edge of a real pastel stick.
"""
import argparse
import math

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

PAPER = (236, 228, 214)          # warm off-white sheet
PAPER_TEXTURE = 0.06             # how visible the paper tooth is on bare paper
STROKE_SCALE = 1.0               # multiply every layer's stroke width
SATURATION = 1.12                # pastels read a little brighter than the photo
LAYERS = [
    # w: stroke width as a fraction of canvas height
    # density: rough coverage (1.0 ≈ the area filled once)
    # alpha: pigment opacity, len: stroke length in widths
    {"w": 0.045, "density": 2.6, "alpha": 0.80, "len": 3.0},
    {"w": 0.022, "density": 1.4, "alpha": 0.85, "len": 3.5},
    {"w": 0.011, "density": 1.2, "alpha": 0.90, "len": 4.0},
    {"w": 0.006, "density": 1.0, "alpha": 0.92, "len": 4.5},
]


def _box(arr, r, axis):
    """Box blur of half-width r along one axis, edges clamped."""
    pad = [(0, 0)] * arr.ndim
    pad[axis] = (r + 1, r)
    c = np.cumsum(np.pad(arr, pad, mode="edge"), axis=axis, dtype=np.float64)
    n = arr.shape[axis]
    hi = np.take(c, np.arange(2 * r + 1, 2 * r + 1 + n), axis=axis)
    lo = np.take(c, np.arange(0, n), axis=axis)
    return ((hi - lo) / (2 * r + 1)).astype(np.float32)


def gblur(arr, sigma):
    """Float Gaussian blur, approximated by three box passes per axis."""
    r = max(1, int(round(math.sqrt(12 * sigma * sigma / 3 + 1) / 2)))
    out = arr.astype(np.float32)
    for axis in (0, 1):
        for _ in range(3):
            out = _box(out, r, axis)
    return out


def make_grain(w, h, rng):
    """Paper tooth: fine noise plus a softer, larger fiber pattern, normalized to [0, 1]."""
    fine = gblur(rng.random((h, w), dtype=np.float32), 0.8)
    coarse = gblur(rng.random((h, w), dtype=np.float32), 3.0)
    grain = 0.65 * fine + 0.35 * coarse
    grain -= grain.min()
    return grain / (grain.max() + 1e-6)


class Pastel:
    def __init__(self, W, H, path, seed=7):
        self.W, self.H = W, H
        self.rng = np.random.default_rng(seed)

        src = Image.open(path).convert("RGB")
        fitted = src.copy()
        fitted.thumbnail((W, H), Image.LANCZOS)
        image = Image.new("RGB", (W, H), PAPER)
        image.paste(fitted, ((W - fitted.width) // 2, (H - fitted.height) // 2))
        self.image = image

        self.grain = make_grain(W, H, self.rng)
        paper = np.asarray(PAPER, np.float32)[None, None, :] / 255
        self.paper = paper * (1 + PAPER_TEXTURE * (self.grain[..., None] - 0.5) * 2)
        self.canvas = self.paper.copy()
        self.frames = []

    # ---- analysis -------------------------------------------------------
    @staticmethod
    def flow_angle(lum, sigma):
        """Edge-following angle per pixel from the smoothed structure tensor."""
        gy, gx = np.gradient(gblur(lum, max(1.0, sigma * 0.35)))
        jxx = gblur(gx * gx, sigma * 0.9)
        jyy = gblur(gy * gy, sigma * 0.9)
        jxy = gblur(gx * gy, sigma * 0.9)
        # Perpendicular to the gradient, so strokes run along edges.
        return 0.5 * np.arctan2(2 * jxy, jxx - jyy) + math.pi / 2

    @staticmethod
    def boost(rgb):
        lum = rgb @ np.array([0.299, 0.587, 0.114], np.float32)
        return np.clip(lum[..., None] + (rgb - lum[..., None]) * SATURATION, 0, 1)

    # ---- painting -------------------------------------------------------
    def stroke_path(self, x, y, theta, length, angle_map):
        """A short polyline that bends along the flow field."""
        pts = [(x, y)]
        steps = 4
        seg = length / steps
        # Pick the stroke direction once so the polyline doesn't flip back on itself.
        dx0, dy0 = math.cos(theta), math.sin(theta)
        for _ in range(steps):
            xi = int(min(max(x, 0), self.W - 1))
            yi = int(min(max(y, 0), self.H - 1))
            a = angle_map[yi, xi]
            dx, dy = math.cos(a), math.sin(a)
            if dx * dx0 + dy * dy0 < 0:
                dx, dy = -dx, -dy
            x, y = x + dx * seg, y + dy * seg
            dx0, dy0 = dx, dy
            pts.append((x, y))
        return pts

    def paint_layer(self, layer, col, angle, err):
        W, H, rng = self.W, self.H, self.rng
        w = max(2.0, H * layer["w"] * STROKE_SCALE)
        length = w * layer["len"]
        n = int(layer["density"] * W * H / (w * length))

        if err is None:
            ys = rng.integers(0, H, n)
            xs = rng.integers(0, W, n)
        else:
            # Spend strokes where this layer adds detail the coarser one missed.
            p = (err + 0.03).ravel()
            idx = rng.choice(p.size, size=n, p=p / p.sum())
            ys, xs = np.divmod(idx, W)

        layer_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        draw = ImageDraw.Draw(layer_img)
        jitter = rng.normal(0, 0.035, (n, 3))
        wobble = rng.normal(0, 0.18, n)
        widths = np.maximum(1, (w * rng.uniform(0.7, 1.15, n))).astype(int)
        for k in range(n):
            y, x = int(ys[k]), int(xs[k])
            c = np.clip(col[y, x] + jitter[k], 0, 1)
            theta = angle[y, x] + wobble[k]
            pts = self.stroke_path(x - math.cos(theta) * length / 2,
                                   y - math.sin(theta) * length / 2,
                                   theta, length, angle)
            rgb = tuple(int(v * 255) for v in c)
            draw.line(pts, fill=rgb + (255,), width=int(widths[k]), joint="curve")

        rgba = np.asarray(layer_img, np.float32) / 255
        # Soften the hard line edges slightly, then let pigment sit on the raised
        # tooth only, so edges break up and valleys stay paper-colored.
        sigma = max(0.8, w * 0.06)
        soft = gblur(rgba[..., 3], sigma)
        # Blur premultiplied color so transparent (black) pixels don't darken the edges.
        color = gblur(rgba[..., :3] * rgba[..., 3:], sigma) / np.maximum(soft, 1e-4)[..., None]
        tooth = np.clip((self.grain - 0.25) * 1.9, 0, 1) ** 1.2
        a = np.clip(soft * (0.55 + 0.9 * tooth) - 0.15 * (1 - tooth), 0, 1) * layer["alpha"]
        self.canvas = self.canvas * (1 - a[..., None]) + np.clip(color, 0, 1) * a[..., None]

    def build(self, gif_steps=0):
        rgb_img = self.image
        rgb = np.asarray(rgb_img, np.float32) / 255
        lum = rgb @ np.array([0.299, 0.587, 0.114], np.float32)

        prev_col = None
        for i, layer in enumerate(LAYERS):
            w = max(2.0, self.H * layer["w"] * STROKE_SCALE)
            col_k = self.boost(np.asarray(rgb_img.filter(ImageFilter.GaussianBlur(w * 0.30)), np.float32) / 255)
            err = None
            if prev_col is not None:
                err = np.abs(col_k - prev_col).mean(axis=2)
                err = np.clip(err / (np.percentile(err, 92) + 1e-6), 0, 1)
            prev_col = col_k
            angle = self.flow_angle(lum, max(1.0, w * 0.35))
            self.paint_layer(layer, col_k, angle, err)
            print(f"layer {i + 1}/{len(LAYERS)}  stroke width {w:.0f}px")
            if gif_steps:
                self.frames.append(self.result())
        return self.result()

    def result(self):
        return Image.fromarray(np.uint8(np.clip(self.canvas, 0, 1) * 255))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("input")
    ap.add_argument("-o", "--output", default="pastel.png")
    ap.add_argument("--size", type=int, default=1400, help="long edge of the output, in pixels")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--gif", help="also save a layer-by-layer timelapse GIF here")
    args = ap.parse_args()

    with Image.open(args.input) as im:
        iw, ih = im.size
    scale = args.size / max(iw, ih)
    W, H = max(64, round(iw * scale)), max(64, round(ih * scale))

    p = Pastel(W, H, args.input, seed=args.seed)
    out = p.build(gif_steps=bool(args.gif))
    out.save(args.output)
    print(f"saved {args.output} ({W}x{H})")

    if args.gif:
        frames = [Image.fromarray(np.uint8(np.clip(p.paper, 0, 1) * 255))] + p.frames
        frames[0].save(args.gif, save_all=True, append_images=frames[1:] + [frames[-1]] * 2,
                       duration=700, loop=0)
        print(f"saved {args.gif}")


if __name__ == "__main__":
    main()
