# Workflow Improvements

## 1. Purpose

This file tracks proposed and accepted improvements to the AI development
workflow.

Use this when a human correction, review finding, repeated issue, or process
friction reveals that the workflow itself should change.

## 2. Status Values

- `proposed`
- `accepted`
- `active`
- `rejected`
- `superseded`

## 3. Improvement Template

```text
ID:
Status:
Date:
Problem:
Proposed Change:
Reasoning:
Affected Docs:
Acceptance Criteria:
Follow-up:
```

## 4. Improvements

### WI-0001 Add workflow control plane

Status: active
Date: 2026-05-11

Problem:

- Architecture rules were strong, but AI execution phases were too shallow.

Proposed Change:

- Add dedicated workflow, task template, review rules, traceability, decision log,
  and risk register.

Reasoning:

- Large AI-assisted development requires mode boundaries and durable execution
  artifacts.

Affected Docs:

- `AI_WORKFLOW.md`
- `TASK_TEMPLATE.md`
- `REVIEW_RULES.md`
- `TRACEABILITY_MATRIX.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`

Acceptance Criteria:

- Build requires approved task file.
- Review has severity and closure rules.
- Traceability exists for first-phase business line.

Follow-up:

- Use these docs for `001_vapor_foundation`.

### WI-0002 Add learning extension loop

Status: active
Date: 2026-05-11

Problem:

- Failure handling did not require abstraction, similar-risk search, or workflow
  correction.

Proposed Change:

- Add `ai_dev/CORE/EXTENSIONS/` with learning loop, error knowledge base, pattern
  library, and templates.

Reasoning:

- AI should not only fix the current problem; it should improve the project
  rules so related problems become less likely.

Affected Docs:

- `EXTENSIONS/README.md`
- `EXTENSIONS/LEARNING_LOOP.md`
- `EXTENSIONS/ERROR_KNOWLEDGE_BASE.md`
- `EXTENSIONS/PATTERN_LIBRARY.md`
- `TASK_TEMPLATE.md`
- `REVIEW_RULES.md`
- `AI_WORKFLOW.md`

Acceptance Criteria:

- P0/P1 and repeated issues require a learning record.
- Learning record includes root cause, abstraction, similar risks, preventive
  rule, and regression gate.

Follow-up:

- Apply this loop during future Build/Review tasks.
