# design-templates

Codex용 디자인 스킬 플러그인입니다. 새 화면을 만들기 전에 **무엇을 만들지**(요구사항)와 **어떻게 보일지**(스타일)를 인터뷰로 정합니다. 스타일이 정해지면 맞는 템플릿의 미리보기를 보여 주고 **"이 템플릿을 적용할까요?"** 라고 묻습니다.

## 설치

```bash
codex plugin marketplace add jh3779/design-templates
codex plugin add design-templates@design-templates
```

설치한 뒤 Codex를 재시작합니다. `codex plugin list`에서 `design-templates@design-templates`가 `installed, enabled`로 보이면 설치가 끝난 것입니다.

## 사용

Codex에게 이렇게 말하면 `design-interview` 스킬이 시작됩니다.

- "홈페이지 새로 만들자"
- "어떤 스타일로 갈지 정하자"
- "예쁘게 만들어줘"

진행 순서는 다음과 같습니다.

1. **요구사항:** 프로젝트에 기획 문서(`docs/00_project_brief.md` 등)가 있으면 먼저 읽고, 빈 부분만 묻습니다.
2. **스타일:** 업종·타깃에 맞춰 10종 카탈로그에서 하나로 정합니다.
3. **템플릿 제안:** 맞는 템플릿이 있으면 미리보기를 띄우고 세 가지 중 하나를 고르게 합니다.
   - **적용:** 템플릿 파일을 프로젝트에 복사하고 브랜드명·색·데이터만 바꿉니다.
   - **참고만:** 레이아웃과 질감만 참고해서 새로 만듭니다.
   - **사용 안 함:** 템플릿 없이 진행합니다.

## 템플릿 8종

| 템플릿 | 스타일 | 어울리는 곳 | 미리보기 |
| --- | --- | --- | --- |
| Glassy Dashboard | 글래스모피즘 | 관리자 화면·SaaS 대시보드 | [보기](plugin/skills/design-interview/style-picker/references/assets/templates/glassy-dashboard.png) |
| Pastel Filter | 이미지 효과(Python) | 사진을 파스텔화로 바꾼 히어로·커버 이미지 | [보기](plugin/skills/design-interview/style-picker/references/assets/templates/pastel-filter.jpg) |
| CRT Terminal | 레트로·Y2K | 질문 → 결과 출력형 조회 도구 | [보기](plugin/skills/design-interview/style-picker/references/assets/templates/crt-terminal.jpg) |
| Party Pastel | 친근한 미니멀 (라이트·다크) | 파티·퀴즈·모임 로비 | [보기](plugin/skills/design-interview/style-picker/references/assets/templates/party-pastel.jpg) |
| Parchment Storybook | 다크 판타지 | 텍스트 게임·스토리 화면 | [보기](plugin/skills/design-interview/style-picker/references/assets/templates/parchment-storybook.jpg) |
| Mono Utility | 미니멀 | 사진 증빙·현장 점검 모바일 앱 | [보기](plugin/skills/design-interview/style-picker/references/assets/templates/mono-utility.jpg) |
| Square Editorial | 다크 에디토리얼 | 크리에이터 포트폴리오 | [보기](plugin/skills/design-interview/style-picker/references/assets/templates/square-editorial.jpg) |
| Evidence Split | 미니멀 | 근거 원문을 보여 주는 검색·RAG 화면 | [보기](plugin/skills/design-interview/style-picker/references/assets/templates/evidence-split.jpg) |

각 템플릿은 `plugin/skills/design-interview/style-picker/references/` 아래에 있습니다.

- `templates/<이름>/`: 원본 파일. HTML은 단일 파일이라 브라우저로 바로 열립니다. Pastel Filter는 Python 스크립트입니다(`pip install numpy pillow` 필요).
- `templates/<이름>/notes.md`: 색·폰트 토큰, 적용할 때 바꿀 것, 알려진 한계.
- `assets/templates/`: 데스크톱·모바일 미리보기.

## 업데이트

```bash
codex plugin marketplace upgrade design-templates
```

## 참고

- 이 저장소에는 `design-interview` 스킬만 들어 있습니다. 스킬 본문에 나오는 다음 단계 스킬(`design-generation`, `design-review` 등)은 포함되지 않았습니다. 없으면 그 단계를 건너뛰고 바로 구현합니다.
- 템플릿의 예시 데이터와 이름은 모두 가상입니다.

## 라이선스

[MIT](LICENSE). 템플릿을 복사·수정해 상업 프로젝트에 써도 됩니다. 저작권 표시와 라이선스 문구만 함께 남겨 주세요.
