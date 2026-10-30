# 레퍼런스 — 바로 적용 가능한 검증된 템플릿

`style-catalog.md`가 "어떤 스타일로 갈지"를 정하는 표라면, 이 문서는 그 스타일로
**실제로 만들어 돌려 본 결과물**을 모아 둔 곳이다. 스타일이 확정됐을 때 여기 맞는
템플릿이 있으면, 처음부터 만들기 전에 사용자에게 먼저 보여 주고 적용 여부를 묻는다
(절차는 `../SKILL.md`의 Step 3.5).

| ID | 템플릿 | 연결 스타일 | 이럴 때 제안 | 미리보기 | 원본 |
| --- | --- | --- | --- | --- | --- |
| T1 | **Glassy Dashboard** | 글래스모피즘 (+다크모드) | 대시보드·관리자 화면·SaaS 홈, "고급스럽게", 실사 배경 위 유리 카드 | `assets/templates/glassy-dashboard.png` | `templates/glassy-dashboard/glassy-dashboard.html` |
| T2 | **Pastel Filter** | 에디토리얼, 스크랩북·파스텔, 감성 브랜드 | 히어로·커버 사진을 손그림 느낌으로 바꾸고 싶을 때, "따뜻하게/손맛 있게" | `assets/templates/pastel-filter.jpg` | `templates/pastel-filter/pastel.py` |
| T3 | **CRT Terminal** | 레트로·Y2K (+다크모드) | 질의 → 결과가 "출력"되는 조회형 도구(팩트체크·사전·진단·티켓 발급), 진지한 데이터에 놀이감 | `assets/templates/crt-terminal.jpg` | `templates/crt-terminal/` |
| T4 | **Party Pastel** | 미니멀리즘(친근한 변주) | 파티·퀴즈·보드게임 로비, 코드로 입장하는 가벼운 모임·투표, "친근하게, 유치하지 않게" | `assets/templates/party-pastel.jpg` | `templates/party-pastel/` |
| T5 | **Parchment Storybook** | 다크모드 UI (+에디토리얼) | 텍스트 RPG·인터랙티브 픽션·게임북, "기록/일지/편지" 주제의 스토리 화면 | `assets/templates/parchment-storybook.jpg` | `templates/parchment-storybook/` |
| T6 | **Mono Utility** | 미니멀리즘 | 현장 점검·시공·배송 등 사진 증빙 앱, 정확성이 장식보다 중요한 업무용 모바일 툴 | `assets/templates/mono-utility.jpg` | `templates/mono-utility/` |
| T7 | **Square Editorial** | 다크모드 UI (+에디토리얼) | 영상 편집자·모션 디자이너·크리에이터 포트폴리오, 썸네일이 많은 쇼케이스 | `assets/templates/square-editorial.jpg` | `templates/square-editorial/` |
| T8 | **Evidence Split** | 미니멀리즘 (+에디토리얼 세리프) | 규정·매뉴얼·계약서 RAG에서 답 대신 근거 원문을 보여 줄 때, 결론을 화면이 내리면 안 되는 도구 | `assets/templates/evidence-split.jpg` | `templates/evidence-split/` |

모든 템플릿에는 모바일 미리보기(`assets/templates/<id>-mobile.jpg`)가 함께 있다. T3~T8은 폴더마다
`<id>.html`(단일 파일, 외부 이미지 없음)과 `notes.md`(출처 파일:줄, 토큰, 시그니처 패턴, 적용 시 바꿀 것, 알려진 한계)가 있다.
**적용할 때는 해당 `notes.md`를 먼저 읽는다** — 이 문서에는 요약만 둔다.

## 출처

T3~T8은 2026-10-30, 작성자의 개인 프로젝트(비공개)에 있던 실제 디자인 토큰과 화면을 바탕으로 추출했다.
근거 파일 경로는 원본 프로젝트 기준이라 이 저장소에는 없다. 토큰 값은 각 템플릿 HTML의 `:root`에 그대로 들어 있다.

| ID | 원본 프로젝트 | 근거 파일 |
| --- | --- | --- |
| T3 | `rag-project` (Streamlit 데모) | `disclosure_lit/demo/static/retro.css`·`power-on.css`·`print-feed.css`, `.streamlit/config.toml` |
| T4 | `yangsaechan-game` | `docs/design-system/tokens.css`·`components.css`·`screens.css`, `frontend/card-motion.css` |
| T5 | `textRPG` | `docs/design-system/original-system.css`·`original-kit.css`, `docs/14_original_visual_design.md` |
| T6 | `snapproof` (Flutter) | `apps/snapproof_app/lib/theme/*.dart`, `.claude/skills/jjikjeung-design/tokens/` |
| T7 | `portpolio` | `portfolio/css/styles.css` (이름은 예시 이름으로 교체) |
| T8 | `LG_CNS_RAG_main` | `frontend/src/tokens.css`·`search/search.css`, `docs/design-system/principles.md` |

T1·T2는 2026-10-30, 인스타그램 릴스 두 편을 보고 만든 것이다. 원본 영상은 없고 위 미리보기가 근거 이미지다.
- T1: "Glassy Dashboard V5" (code.xr) — React + framer-motion `StatsCard` 코드가 나오는 영상
- T2: `flower.py`의 `Pastel` 클래스가 나오는 화면 녹화 영상. 코드 일부만 보였기 때문에, 보이지 않은 부분(레이어 수치, 획 그리기, 종이 결)은 새로 설계했다.

## T1. Glassy Dashboard

- **구성**: 상단 알약 내비 + 왼쪽 세로 아이콘 레일 + 12열 카드 그리드
  (스탯 카드 4 · 매출 영역 차트 · 목표 링 · 최근 주문 표 · 메시지)
- **배경**: 외부 이미지를 못 쓰는 환경을 고려해 통유리창 거실 노을 장면을 Canvas로 그린다.
  Dawn/Dusk/Night 전환 버튼이 있다. 실제 프로젝트에서는 `#scene` 캔버스를 사진 한 장(`background: url(...) center/cover`)으로 바꿔도 된다.
- **유리 질감**: `.glass` 클래스 하나 — `backdrop-filter: blur(22px) saturate(150%)`,
  반투명 배경 `rgba(28,26,32,.34)` + 위쪽 하이라이트 그라디언트 + 1px 밝은 테두리 + inset 하이라이트.
- **색**: `--ink:#f6f1ea` `--ember:#ff9a4d`(주 포인트) `--ember-2:#ffc785`
  `--good:#6fe3b0` `--bad:#ff8a8a`. 단일 다크 룩(사진 배경 위라 라이트 테마 없음).
- **타입**: Instrument Serif(인사말 헤드라인, 이탤릭 이름) · Geist(본문·숫자) · Geist Mono(라벨·축·증감률)
- **인터랙션**: 스탯 카드 호버 시 `translateY(-5px)`(영상의 `whileHover={{ y: -5 }}`), 차트 7D/30D/90D 전환,
  `prefers-reduced-motion` 대응. 720px 이하에서는 레일이 하단 플로팅 바로 바뀐다.
- **적용 시 바꿀 것**: 브랜드명(`Atrium`), 사용자 이름, 스탯 4종 라벨, 내비 항목, `--ember` 계열 포인트 색.
  예시 데이터는 "Example data"로 표시돼 있으니 실제 데이터로 교체한다.
- **React로 옮길 때**: `.stat` 카드를 `StatsCard({ title, value, change, icon, gradient })`로 빼고,
  호버는 `motion.div whileHover={{ y: -5 }}`로 바꾼다.

## T2. Pastel Filter

- **무엇**: 사진 → 종이 결 위 소프트 파스텔 그림. Python + numpy + Pillow.
- **실행**: `python pastel.py photo.jpg -o pastel.png --size 1400 [--seed 7] [--gif timelapse.gif]`
  (1400px 기준 약 4초. numpy가 없으면 venv에 `pip install numpy pillow`)
- **원리**: 굵은 획 → 가는 획 4레이어. 레이어마다 블러한 사진에서 색을 뽑고, 두 번째 레이어부터는
  직전 레이어와 색 차이가 큰 곳(디테일)에만 획을 몰아 준다. 획 방향은 structure tensor로 윤곽을 따르고,
  안료는 종이 결의 튀어나온 부분에만 묻는다.
- **조정 손잡이**(파일 맨 위): `LAYERS`(획 굵기·밀도·불투명도·길이), `SATURATION`, `PAPER`, `PAPER_TEXTURE`.
- **알려진 함정**: 획 가장자리를 블러할 때 premultiplied 색을 쓰지 않으면 모든 획에 검은 테두리가 생긴다
  (이미 수정됨, `paint_layer`). 바탕 레이어 밀도가 낮으면 종이가 네모 모양으로 비어 보인다.
- **웹 디자인에 쓰는 법**: 히어로·커버 이미지를 미리 변환해 정적 에셋으로 넣는다. 에디토리얼 레이아웃이나
  감성 브랜드·초대장 페이지의 사진 톤을 맞출 때 잘 어울린다.
- **검증 범위**: 그라디언트 풍경 사진(macOS Sonoma 배경화면)으로만 확인했다. 인물·꽃처럼 윤곽이 뚜렷한 사진은 아직이다.
