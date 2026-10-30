---
name: design-interview
description: "디자인 생성 전 사전 인터뷰 스킬. 프로젝트에 이미 기획 문서(docs/00_project_brief.md 등)가 있는지 먼저 확인하고, 없거나 빈틈이 있으면 요구사항 인터뷰(discovery-interview)로 채운 다음, 원하는 디자인 스타일(업종별 10종 카탈로그, style-picker)까지 인터뷰로 정한다. Use at the START of a new app/feature or redesign, before any UI is generated — to confirm existing planning docs, fill gaps via structured requirements interview, and pin down a concrete style direction. Triggers: \"기획부터\", \"요구사항 정의\", \"뭘 만들지 정하자\", \"어떤 스타일로 갈지\", \"예쁘게 만들어줘\" (스타일 미정 상태), \"홈페이지 새로 시작\", \"PRD\", \"디자인 방향 정하기\"."
---

> **[공개판 안내]** 이 저장소에는 `design-interview`(요구사항 인터뷰 `discovery-interview` + 스타일 인터뷰 `style-picker` + 템플릿 8종)만 들어 있다.
> 본문에 나오는 `design-generation`·`design-review`·`reference-analysis`·`taste-skill`·`handoff` 등은 작성자 개인 도구함의 스킬이라 포함되지 않았다.
> 설치돼 있지 않으면 그 단계는 건너뛰고, 확정한 요구사항·스타일(또는 적용한 템플릿)로 바로 구현을 진행한다.

> **[커스텀 노트 — 통합 이력 및 권장 모델]**
> - **2026-08-08 스킬 통합**: `discovery-interview`(요구사항 인터뷰) + `style-picker`(업종별 스타일 인터뷰)를 이 스킬 아래로 옮겼다. 두 스킬은 "무엇을 만들지"와 "어떻게 보일지"를 각각 담당하며, 이 오케스트레이터가 순서를 관리한다.
> - **2026-10-16 `reference-analysis` 연계**: 디자인 흐름이 `design-interview`(요구사항·스타일 확정, 레퍼런스 신호 수집) → `design-generation/reference-analysis`(레퍼런스 실측·차용 판단) → `design-system-docs`(위계·팔레트·상태 색 문서) → 구현으로 확장됐다. 이 스킬은 Step 3에서 레퍼런스 목록을 기록하고 Step 4에서 `reference-analysis`로 넘기는 역할만 추가했다(하위 스킬 `discovery-interview`/`style-picker`는 수정 없음).
> - **권장 모델**: 두 하위 스킬 모두 정해진 표/템플릿을 채우는 조회+판단형 작업이라 **Sonnet**으로 충분. 업종/타깃이 카탈로그 조합에 없어 브랜드 톤을 새로 만들어야 하면 `design-generation/taste-skill`(Opus 권장)로 넘긴다.

# Design Interview — 사전 문서 확인 + 요구사항/스타일 인터뷰

디자인 생성(`design-generation`)이나 검토(`design-review`)에 들어가기 전, "무엇을 만들지"와 "어떤 스타일로 보일지"가 확정됐는지 먼저 점검하고 빈틈만 인터뷰로 채우는 앞단 스킬이다.

## Workflow

### Step 1 — 사전 문서 확인

프로젝트에 이미 기획 문서가 있는지 먼저 확인한다:
- `docs/00_project_brief.md` ~ `docs/06_open_questions.md` (discovery-interview 산출물 명명 규칙) 또는 이에 준하는 PRD/스펙 문서가 있는지 찾는다.
- `.agent/PROJECT_CONTEXT.md`, `.agent/DECISIONS.md` (handoff 스킬 산출물)가 있으면 함께 읽는다.
- 있으면 내용을 요약해서 사용자에게 확인만 받는다("이 내용으로 진행할까요, 바뀐 부분이 있나요"). **이미 있는 내용을 다시 묻지 않는다.**
- 없거나 일부만 있으면 Step 2로 간다(빈 영역만 인터뷰).

### Step 2 — 요구사항 인터뷰 (필요한 만큼만)

빠진 영역이 있으면 `discovery-interview/SKILL.md`를 읽고 그 안의 8영역 인터뷰 절차·원칙(한 번에 한 주제, 선택지로 묻기, 가정은 Open Questions로, 추적 ID 부여)을 그대로 따른다. 산출물은 그 문서의 "산출물" 절에 정의된 `docs/00_project_brief.md` ~ `docs/06_open_questions.md` 구조로 만든다.

### Step 3 — 디자인 스타일 인터뷰

요구사항(무엇을 만들지)이 정리되면 `style-picker/SKILL.md`를 읽고 그 워크플로우(업종·타깃 확인 → `style-picker/references/style-catalog.md` 카탈로그 매칭 → 스타일 하나로 확정 → 모호한 요청을 구체적 프롬프트로 변환)를 따른다. 이미 사용자가 스타일을 명확히 말했다면(예: "다크모드로") 카탈로그에서 확인만 하고 넘어간다.

**레퍼런스 신호 기록**: 사용자가 URL·스크린샷·"○○ 같은 느낌"처럼 레퍼런스를 언급하면 스타일 확정과 별개로 **그대로 적어 둔다** — 각 항목마다 "무엇을 배우려는지"(예: 위계가 깔끔한 가격 표, 다크 모드 상태 색)를 한 줄 묻는다. 이 목록은 Step 4에서 `design-generation/reference-analysis`의 입력이 된다(후보 선정의 출발점). 레퍼런스를 하나도 못 대면 억지로 만들지 않고 그대로 넘긴다 — `reference-analysis`가 확정한 스타일 키워드로 후보를 직접 찾는다.

### Step 4 — 핸드오프

두 산출물(스펙 문서 + 확정 스타일)을 한 번에 요약하고 다음 단계를 제안한다:
- **레퍼런스가 있거나 "닮고 싶은 사이트부터 찾자"면 → `design-generation/reference-analysis`부터** (Step 3에서 적어 둔 레퍼런스 목록과 확정 스타일 키워드를 넘긴다. 분석 산출물 `docs/design-reference/`는 이후 `design-system-docs`의 입력이 된다)
- 화면/코드를 실제로 만들 차례면 → `design-generation`
- 이미 있는 화면을 점검/개선할 차례면 → `design-review`

## 언제 안 쓰는지

- 기획 문서와 스타일이 이미 둘 다 확정된 상태에서 바로 만들기만 하면 될 때 → `design-generation`으로 직행 (단, 레퍼런스 분석이 필요하면 `design-generation/reference-analysis`를 먼저)
