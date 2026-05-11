# 000B Learning Extensions

Status: completed

## 1. Goal

Add a project-level extension mechanism so AI agents learn from errors, review
findings, failed verification, and human corrections.

The mechanism must require abstraction beyond the immediate fix and must improve
future workflow, rules, tests, or review gates.

## 2. Non-Goals

- Do not create Vapor source code.
- Do not create database migrations.
- Do not implement business modules.
- Do not claim the model itself is trained.

## 3. Business Context

This project depends on AI-assisted development from zero to one. For a large
cross-border ecommerce system, the workflow must reduce repeated mistakes across:

- Order/payment/fulfillment state machines.
- Merchant isolation.
- Provider integration.
- API contracts.
- Database constraints.
- AI task execution.

## 4. Mode History

- Exploration: User identified that errors must be collected, abstracted, and
  used to solve similar problems.
- Decision: Add `ai_dev/CORE/EXTENSIONS/` as a learning and workflow improvement
  layer.
- Task: This task records the learning-extension expansion.
- Build: Documentation-only changes.
- Review: Check that learning loop, error KB, pattern library, and templates are
  connected to core workflow.

## 5. Dependencies

- Prior tasks:
  - `000_project_rules_and_architecture`
  - `000A_ai_development_workflow`
- Required docs:
  - `PROJECT_RULES.md`
  - `AI_WORKFLOW.md`
  - `TASK_TEMPLATE.md`
  - `REVIEW_RULES.md`

## 6. Assumptions and Open Questions

- Type: assumption
  Question: Is learning stored as repository-local docs rather than model
  training?
  Current default: Yes. Learning is versioned in `ai_dev/CORE/EXTENSIONS/`.
  Owner: workflow
  Required before: every learning extension task

- Type: later_decision
  Question: Should learning checks become automated scripts?
  Current default: Use documentation and review gates first.
  Owner: technical decision
  Required before: CI automation work

## 7. Affected Areas

- Modules: none.
- Domain concepts: none.
- Database: none.
- API: none.
- Integrations: none.
- Security: review/learning checks only.
- Observability: review/learning checks only.
- Tests: documentation checks.

## 8. Write Scope

Allowed files/directories:

- `ai_dev/PROJECT_RULES.md`
- `ai_dev/CORE/AI_WORKFLOW.md`
- `ai_dev/CORE/TASK_TEMPLATE.md`
- `ai_dev/CORE/REVIEW_RULES.md`
- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`
- `ai_dev/PROJECT/DECISION_LOG.md`
- `ai_dev/PROJECT/RISK_REGISTER.md`
- `ai_dev/CORE/EXTENSIONS/`
- `ai_dev/TASKS/000B_learning_extensions.md`

Forbidden files/directories:

- `Sources/`
- `Tests/`
- database migrations
- frontend source files

## 9. Implementation Steps

| Step ID | Status | Description | Allowed Files | Verification | Pause After |
| --- | --- | --- | --- | --- | --- |
| S1 | completed | Add extension directory and index | `ai_dev/CORE/EXTENSIONS/README.md` | extension lifecycle exists | no |
| S2 | completed | Add learning loop | `ai_dev/CORE/EXTENSIONS/LEARNING_LOOP.md` | error abstraction levels exist | no |
| S3 | completed | Add error knowledge base | `ai_dev/CORE/EXTENSIONS/ERROR_KNOWLEDGE_BASE.md` | templates and initial process lessons exist | no |
| S4 | completed | Add workflow improvements and pattern library | `WORKFLOW_IMPROVEMENTS.md`, `PATTERN_LIBRARY.md` | reusable patterns exist | no |
| S5 | completed | Add templates | `ai_dev/CORE/EXTENSIONS/templates/` | error/workflow templates exist | no |
| S6 | completed | Connect extension loop to core workflow docs | core docs | learning required in close/review/task flow | no |

## 10. Data Model Changes

None.

## 11. API Changes

None.

## 12. Integration Changes

None.

## 13. Security Requirements

Learning records must not contain secrets, tokens, raw payment credentials, or
unsafe PII.

## 14. Observability Requirements

Learning records should reference verification failures, review findings, and
task IDs so future agents can trace the reason behind rule changes.

## 15. Index Updates

- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`: add extension docs.
- `ai_dev/PROJECT/DECISION_LOG.md`: record extension mechanism decision.
- `ai_dev/PROJECT/RISK_REGISTER.md`: record risk that learning loop is not enforced.
- `ai_dev/PROJECT_RULES.md`: reference extension docs.
- `ai_dev/CORE/AI_WORKFLOW.md`: add learning loop to failure/close behavior.
- `ai_dev/CORE/TASK_TEMPLATE.md`: add learning impact section.
- `ai_dev/CORE/REVIEW_RULES.md`: add learning checks.

## 16. Verification Gates

Required:

- Confirm extension files exist.
- Confirm learning keywords are present.
- Confirm no business code was created.
- `git diff --check`
- `git status --short`

## 17. Rollback / Compensation

- Documentation-only rollback by reverting this task's files.
- No database or provider compensation required.

## 18. Review Plan

- Verify learning loop is not empty process text.
- Verify each meaningful error requires abstraction.
- Verify similar-risk search is required.
- Verify preventive rule/regression gate is required.

## 19. Completion Evidence

- Files changed: extension docs and workflow entrypoints.
- Commands run: to be listed in final response.
- Remaining risks: learning enforcement is document-based until automation exists.
