# mono-utility

## 한 줄 요약
무채색 잉크 램프와 의미 전용 유채 3종(danger/caution/affirm)으로 만든, 카드 없는 헤어라인 리스트 + 하단 고정 검정 알약 버튼의 현장 기록형 모바일 유틸리티 UI입니다.

## 출처
- 프로젝트: snapproof (찍증, Flutter, 라이트 전용)
- 색: apps/snapproof_app/lib/theme/app_colors.dart:10-31(램프·유채), :92-116(시맨틱·카메라)
- 카메라·워터마크 CSS 값: .claude/skills/jjikjeung-design/tokens/colors.css:87-97
- 타입: app_typography.dart:31-55, tokens/typography.css:6-8(폰트 스택·tnum)
- 간격·반경·그림자·크기: app_dimens.dart:7-28 / :38-44 / :67-80 / :91-137
- 모션: tokens/motion.css:4-8
- 패턴: widgets/bottom_action_bar.dart:36-88, segmented_control.dart:50-72, watermark_painter.dart:32-58·89-135, location_badge.dart:60-140, app_theme.dart:34-57·235-250
- 화면 참고: docs/archive/simulator-screenshot/SCR-001_content.png, SCR-002_dirty-complete.png, ui_kits/jjikjeung_app/screens.jsx:325-445(ScrCamera)

## 연결 스타일
미니멀리즘(Minimalism) — 여백·헤어라인·단일 잉크 primary로 내용(증빙 데이터)에 집중시킵니다.

## 이럴 때 제안
- 현장 점검·청소·시공·배송 등 "사진으로 남기는 증빙" 앱
- 체크리스트·작업 건 관리처럼 정확성·신뢰가 장식보다 중요한 업무용 모바일 툴
- 좌표·시각·수량 같은 숫자를 많이 보여 주는 화면(tabular figures)

## 토큰
- 색: ink 0~900(#FFFFFF~#1A1A1D), 캔버스 #F7F7F8, 헤어라인 #E4E4E7, primary = ink-900. 유채는 danger #A8342B / caution #8A6212 / affirm #2C6349(+100 배경)뿐입니다.
- 카메라: 셸 #101012, 명판 rgba(16,16,18,.72) + 외곽선 rgba(255,255,255,.28), 칩 rgba(255,255,255,.92)
- 타입: Pretendard 단일, 전역 "tnum","lnum". titleMedium 17/24 w600, bodyMedium 14/22, bodySmall 13/20, label 14~16 w600, overline 11/16 w700 +.6, stamp 13/19 w600
- 반경: 4·8·12·16·20·28·999 (7단, 스케일 밖 금지). 버튼·세그먼트·배지 = full
- 간격: 4px 그리드(2는 리스트 행 줄 간격 전용), 화면 좌우 16 고정, 하단 바 패딩 12/16/20
- 크기: 앱바 56, 버튼 48/52, 3줄 행 최소 102, 셔터 72, 배지 28. 그림자보다 헤어라인(바텀 바만 위로 0 -2 12)

## 시그니처 패턴
1. 하단 고정 액션 바: 흰 바 + 상단 헤어라인 + 위 그림자, 한 줄 안내(note) + 행동 최대 2개(보조 외곽선 알약 + 주요 검정 알약), safe-area 대응
2. 세그먼트 컨트롤: sunken 트랙 2px 패딩, 선택 = ink-900 알약/흰 글자, 카운트는 opacity .7. 카메라 위에서는 트랙 90% 흰색
3. 카메라 셸 + 워터마크 명판: 상·하 보호 그라데이션, 좌하단 명판에 `YYYY-MM-DD HH:mm:ss ±HH:MM` + 좌표. 소수 자릿수 = 정밀도(5/4/3)
4. 위치 배지: 채운 원/링/경고 삼각/점선 링 — 형태로 상태 구분(색 단독 의미 금지)
5. 카드 없는 리스트: 흰 표면 + 행 사이 1px 헤어라인, 3줄(제목·요약·메타+상태 배지)

## 적용 시 바꿀 것
- 앱바 제목·리스트 항목(공간 → 매장·호실·단계 등), 세그먼트 옵션(전/후 → 입고/출고 등)
- 워터마크 두 줄의 내용(예: 작업자 ID·시리얼) — 단, 숫자는 tabular 유지
- 장면 그림(.scene)은 실제 카메라 스트림/사진으로 교체
- 컬럼 폭 --column(430px)과 데스크톱 바깥 배경(ink-200)

## 알려진 한계
- 원본이 라이트 전용이라 다크 모드는 의도적으로 넣지 않았습니다(카메라 셸만 어둡습니다).
- 아이콘은 Material Symbols Rounded 대신 인라인 SVG 근사치입니다.
- 사진·브랜드 이미지는 복사하지 않고 CSS 그라데이션으로 그렸습니다.
- 숫자(카운트·좌표·체크)는 모두 예시이며, 워터마크 시각은 현재 시각을 표시합니다.
- 헤드리스 Chrome의 390px 캡처는 최소 창 폭(~500px) 때문에 잘려 보이며, 375px iframe으로 별도 확인했습니다.
