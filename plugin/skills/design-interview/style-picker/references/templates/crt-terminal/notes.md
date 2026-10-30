# crt-terminal

## 한 줄 요약
어두운 방 안의 베이지 베젤 모니터(앰버 형광 CRT)에 질문을 입력하면, 아래 프린터 슬롯에서 크림색 영수증 출력물이 내려오는 "입력 단말기 → 출력 프린터" 화면입니다.

## 출처
- 프로젝트: `rag-project` (공시 리터러시 데모, Streamlit)
- 토큰: `disclosure_lit/demo/static/retro.css:13-21`, 베젤 `:59-67`, CRT `:68-132`, 부트 헤더 `:135-143`, 입력·버튼 `:145-184`, 베젤 라벨·LED `:206-219`, 출력물·프린터 `:240-281`, 반응형 `:388-397`, 모션 축소 `:398-409`
- 전원 애니메이션 `power-on.css:1-10`, 용지 급지 `print-feed.css:1-21`
- 동작 규칙(전원 켤 때만 1회 재생, 새 결과만 급지) `disclosure_lit/demo/terminal.py:18-58`
- 테마 `.streamlit/config.toml:2-7`, 화면 근거 `docs/testing/terminal-ui/desktop.png`·`mobile.png`

## 연결 스타일
레트로 · Y2K (보조: 다크모드 UI). 픽셀 폰트·옛 컴퓨터 화면이 핵심이되, 본문은 Pretendard로 가독성을 지킵니다.

## 이럴 때 제안
- 질의 → 결과 "출력"이 한 번에 떨어지는 조회형 도구(팩트체크, 사전, 진단, 영수증·티켓 발급)
- 진지한 데이터에 놀이감·기억에 남는 연출을 얹고 싶을 때
- 부적합: 표·대시보드가 많은 업무 화면, 라이트 테마 필수 서비스

## 토큰
- 색: room `#101112` / bezel `#d5cdbb` (그라데이션 `#e4ddcf`→`#c6bdab`, 엣지 `#eee5d3`, 바닥 `#a59c89`) / screen `#101410` / amber `#ffc56b` / dim `#c3a26e` / field `#191d17`·선 `#8c784e` / paper `#faf8f2` / ink `#242a30` / 링크 `#2f5fa8` / 노트 `#eee9dc`·`#d1c7b0`
- 타입: Galmuri11(픽셀; eyebrow .75rem·자간 .12em, 부트 .8rem, 베젤 .68rem) + Pretendard(본문, h1 clamp(1.5rem,4vw,2rem) 600 / 자간 -.035em, 출력물 h2 1.45rem 650)
- 반경: 모니터 24px(모바일 17px), 화면 10px, 컨트롤 4px, 용지 3px
- 간격: 컨테이너 960px, 모니터 24/26/16px, 화면 1.7rem 1.8rem, 용지 1.8rem 2.2rem, 터치 최소 44px

## 시그니처 패턴
1. 베젤 모니터: 135° 베이지 그라데이션 + 하단 5px 두꺼운 테두리 + 모델명·LED 라벨 줄
2. CRT 유리: inset 그림자 + `::before` feTurbulence 그레인(0.64s steps) + `::after` 스캔라인·트래킹 띠(9s)·글레어. 입력 포커스 시 텍스처를 낮추고 정지
3. 전원 켜기: 세로 0.008 → 1 스케일 + 밝기 2→1 (0.65s). 정지 상태에서 시작, "다시 켜기" 버튼으로 재생
4. 프린터 슬롯 + 영수증: 슬롯 아래로 clip-path 급지(1s), 양옆 펀치 구멍(radial-gradient 24px 반복), 지그재그 절취선
5. 부트 헤더: 픽셀 폰트 상태 문구 + 깜빡이는 블록 커서

## 적용 시 바꿀 것
- eyebrow/모델명(FACT TERMINAL·FT–01), 탭명, 선택 항목·예시 칩, 출력물의 두 칼럼(지지/반박) 구조
- 배경: 원본은 극장 사진 + 3단 스크림이었고 여기선 그라데이션으로 대체 — 브랜드 사진을 쓰려면 스크림만 유지
- 앰버 대신 그린 형광을 원하면 `--terminal-amber`·`--terminal-dim`·스캔라인 rgba만 교체

## 알려진 한계
- 단일 다크 테마(원본과 동일, 의도적). 출력 용지만 밝은 면
- 탭·선택은 시각 데모 수준이고 "확인"은 예시 출력물을 재급지만 합니다(데이터 없음)
- 원본의 movie-palace 배경 사진, 로컬 woff2는 쓰지 않았습니다(CDN 폰트, 실패 시 monospace/system 폴백)
- 헤드리스 Chrome의 최소 창 폭이 500px이라 `--window-size=390`은 잘린 이미지가 나옵니다. preview-mobile.png는 390px iframe 래퍼로 렌더했고, 375px에서 scrollWidth=375(가로 스크롤 없음)를 확인했습니다
- 정적 화면 단위 Lighthouse·스크린리더 실측은 하지 않았습니다
