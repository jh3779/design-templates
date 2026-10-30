# evidence-split

## 한 줄 요약
검색·RAG 결과를 "판정 없이 근거만" 보여 주는 두 칸 화면입니다. 왼쪽 결과 목록, 오른쪽 원문 발췌(세리프)·출처 키-값·점선 구분 확인 항목, 맨 위 유리 알약 도구막대.

## 출처
- 프로젝트: LG_CNS_RAG_main (읽기만 함)
- 토큰: docs/design-system/tokens/tokens.css:5-66 (frontend/src/tokens.css와 값 동일)
- 검색 화면 레이아웃·컴포넌트: frontend/src/search/search.css:5-102(목록·상태 배지·상세·kv·점선), :163-215(두 칸·모바일 전환)
- 유리 알약: frontend/src/styles.css:71-80(model-tabs), :196-201(dock 그림자·blur 16px)
- 원칙: docs/design-system/principles.md:7-11(판정 색 금지, 원문 그대로, 말한 주체·출처 표기)
- 문구 규칙: docs/design-system/copy/ui-text.md(꼬리표·확인 항목 도움말, 금지 문구)
- 상세 순서·바이라인: docs/design-system/components/precedent-detail.md:3-35

## 연결 스타일
미니멀리즘(주) + 에디토리얼 세리프 원문(보조). 유리 질감은 도구막대·목록에만 포인트로 씁니다.

## 이럴 때 제안
- 사내 규정·매뉴얼·계약서·논문 RAG에서 "답" 대신 근거 원문을 보여 줘야 할 때
- 감사·품질·법무처럼 출처 추적(파일·sha256·판본)이 필요한 도구
- 결론을 화면이 내리면 안 되는 의사결정 보조 화면

## 토큰
- 색: bg #f5f6f8 / #d9dee5, ink #15181d · #5b6370 · #636b78, surface #fff · #f0f3f7, accent 남색 #1f3a68 · #2c5aa0 · soft #e9eef6, 선 rgba(21,24,29,.10/.18), glass rgba(255,255,255,.72), 꼬리표 밑줄 #3d4f6e
- 상태 3단계: 실선 #1f3a68 / 회색 바탕 #eef0f3+#d5dae1 / 점선 #b7bec9 (빨강·초록 없음)
- 타입: UI Pretendard Variable, 원문 Source Serif 4 15px·1.65·72ch, ID JetBrains Mono. 12/13/14/16/20/28px
- 반경: 18px(큰 판) · 10px(블록·카드) · 999px(알약)
- 간격: 4/8/12/16/24/32/48px, 블록 사이 18px, 상세 안쪽 22~26px

## 시그니처 패턴
1. 두 칸 나눔: 목록(유리 + blur 10px) | 상세(bg-1). 선택 항목은 남색 테두리 + 왼쪽 3px inset 막대
2. 근거 상태 배지: 색이 아닌 모양(채운 점·반칠·빈 점, 실선·회색·점선)으로 3단계 구분
3. 원문 블록: 라벨 11px 굵게 → 세리프 원문. 글자 색은 바꾸지 않고 밑줄(점선=불명확, 물결=유보)로만 꼬리표
4. 바이라인 "말한 주체 **누구** · 번호"를 모든 원문 블록에
5. "＋ 출처 자세히" 접기 → 110px | 1fr 모노 키-값 격자
6. 점선(1px dashed) 구분의 확인 항목·연결 조항, 맨 아래 모노 출처 꼬리(build·sha·snapshot·질의)
7. 맨 위 유리 알약 도구막대(blur 16px, dock 그림자) — 보조 요소

## 적용 시 바꿀 것
- DOCS 배열(예시 데이터)과 그룹 이름(사내 규정/제품 매뉴얼), 상태 문구 3종
- 브랜드명·탭·판본 표시, 출처 꼬리 항목 이름
- mark.hit(질의 구간 옅은 남색 바탕)은 이 템플릿에서 추가한 것 — 원 프로젝트는 꼬리표 밑줄만 씁니다. 필요 없으면 제거
- 원문이 한국어면 Source Serif 4에 한글 글리프가 없으므로 Noto Serif KR 등을 --font-source 앞에 추가

## 알려진 한계
- 단일 밝은 테마(원 프로젝트 검색 화면과 동일, 의도적). 다크 없음
- 검색·탭은 동작 흉내만(실제 질의 없음), 로딩·오류·첫 화면 상태 미포함
- headless Chrome 최소 창 폭(500px) 때문에 preview-mobile.png는 375px iframe으로 목록·상세 두 화면을 나란히 찍었습니다
- backdrop-filter 미지원 브라우저는 반투명 흰 판으로 보입니다(prefers-reduced-transparency도 동일 처리)
