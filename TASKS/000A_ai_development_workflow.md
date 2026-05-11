# 000A AI Development Workflow

Status: completed

## 1. Goal

Add the workflow/control-plane layer that lets AI agents move from business idea
to implementation through controlled phases:

```text
Orientation -> Divergence -> Convergence -> Task -> Build -> Review -> Close
```

## 2. Non-Goals

- Do not create Vapor source code.
- Do not create database migrations.
- Do not implement business modules.
- Do not resolve every business/technical open question.

## 3. Business Context

This project will use AI to build a large cross-border B2B2C commerce backend
from zero to one. The process must prevent:

- Building from chat memory only.
- Starting code before the decision is clear.
- Vague tasks without step gates.
- Missing review.
- Missing traceability from business goal to implementation.

## 4. Mode History

- Exploration: Review found that architecture rules were strong but AI workflow
  rules were too shallow.
- Decision: Add dedicated workflow/control-plane documents.
- Task: This task persists the workflow expansion.
- Build: Documentation-only changes.
- Review: Documentation keyword checks and git diff checks are required.

## 5. Dependencies

- Prior tasks: `000_project_rules_and_architecture`
- Required docs: existing `ai_dev` rule/index documents.

## 6. Assumptions and Open Questions

- Type: assumption
  Question: Should AI always require an approved task before writing code?
  Current default: Yes, except explicitly approved immediate small fixes.
  Owner: project workflow
  Required before: every Build task

- Type: later_decision
  Question: Which project management tooling will mirror these task statuses?
  Current default: local Markdown files only.
  Owner: user
  Required before: team collaboration beyond local repo.

## 7. Affected Areas

- Modules: none.
- Domain concepts: none.
- Database: none.
- API: none.
- Integrations: none.
- Security: workflow only.
- Observability: workflow only.
- Tests: documentation checks.

## 8. Write Scope

Allowed files/directories:

- `ai_dev/PROJECT_RULES.md`
- `ai_dev/CORE/AI_WORKFLOW.md`
- `ai_dev/CORE/TASK_TEMPLATE.md`
- `ai_dev/CORE/REVIEW_RULES.md`
- `ai_dev/PROJECT/TRACEABILITY_MATRIX.md`
- `ai_dev/PROJECT/DECISION_LOG.md`
- `ai_dev/PROJECT/RISK_REGISTER.md`
- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`
- `ai_dev/TASKS/000_project_rules_and_architecture.md`
- `ai_dev/TASKS/000A_ai_development_workflow.md`

Forbidden files/directories:

- `Sources/`
- `Tests/`
- database migrations
- frontend source files

## 9. Implementation Steps

| Step ID | Status | Description | Allowed Files | Verification | Pause After |
| --- | --- | --- | --- | --- | --- |
| S1 | completed | Add AI workflow rules | `ai_dev/CORE/AI_WORKFLOW.md` | file exists and defines all modes | no |
| S2 | completed | Add task template | `ai_dev/CORE/TASK_TEMPLATE.md` | includes step IDs, write scope, verification, index updates | no |
| S3 | completed | Add review rules | `ai_dev/CORE/REVIEW_RULES.md` | includes severity levels and finding format | no |
| S4 | completed | Add traceability matrix | `ai_dev/PROJECT/TRACEABILITY_MATRIX.md` | maps first-phase line to domain/db/api/tests | no |
| S5 | completed | Add decision and risk records | `ai_dev/PROJECT/DECISION_LOG.md`, `ai_dev/PROJECT/RISK_REGISTER.md` | open questions classified | no |
| S6 | completed | Update rule/index entrypoints | `PROJECT_RULES.md`, `IMPLEMENTATION_MAP.md`, task files | docs list new workflow files | no |

## 10. Data Model Changes

None.

## 11. API Changes

None.

## 12. Integration Changes

None.

## 13. Security Requirements

No runtime security changes. Workflow now requires explicit review for auth,
RBAC, object-level authorization, secrets, upload, and webhook changes.

## 14. Observability Requirements

No runtime observability changes. Workflow now requires traceability and review
of logs, audit, tracking, and integration events.

## 15. Index Updates

- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`: updated with new workflow docs.
- `ai_dev/PROJECT/TRACEABILITY_MATRIX.md`: created.
- `ai_dev/PROJECT/DECISION_LOG.md`: created.
- `ai_dev/PROJECT/RISK_REGISTER.md`: created.
- `ai_dev/PROJECT_RULES.md`: updated to reference workflow documents.

## 16. Verification Gates

Required:

- Confirm files exist.
- Confirm workflow keyword coverage.
- Confirm no business code was created.
- `git diff --check`
- `git status --short`

## 17. Rollback / Compensation

- Documentation-only rollback by reverting this task's files.
- No database or provider compensation required.

## 18. Review Plan

- Review workflow clarity.
- Review whether Build mode is now gated by approved tasks.
- Review whether open questions are classified.
- Review whether traceability covers the first-phase business line.

## 19. Completion Evidence

- Files changed: workflow/control-plane docs and indexes.
- Commands run: to be listed in final response.
- Remaining risks: listed in `RISK_REGISTER.md`.
