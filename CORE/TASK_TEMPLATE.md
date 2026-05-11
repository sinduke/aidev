# Task Template

Use this template for every task under `ai_dev/TASKS/`.

```markdown
# <TASK_ID> <Task Name>

Status: draft | proposed | approved | in_progress | blocked | in_review | completed | superseded

## 1. Goal

<What this task must accomplish.>

## 2. Non-Goals

- <Explicitly excluded scope.>

## 3. Business Context

- First-phase business line:
- User value:
- Operational value:

## 4. Mode History

- Exploration:
- Decision:
- Task:
- Build:
- Review:

## 5. Dependencies

- Prior tasks:
- Required decisions:
- Required credentials/services:
- Required docs:

## 6. Assumptions and Open Questions

- Type: blocker | assumption | later_decision | research_required
  Question:
  Current default:
  Owner:
  Required before:

## 7. Affected Areas

- Modules:
- Domain concepts:
- Database:
- API:
- Functions/contracts:
- DTO/data:
- Permissions:
- State machines:
- Integrations:
- Security:
- Observability:
- Admin frontend:
- Config/env:
- Tests:

## 8. Write Scope

Allowed files/directories:

- `<path>`

Forbidden files/directories:

- `<path>`

Scope expansion rule:

- Stop and update this task before editing files outside allowed scope.

## 9. Git Workflow

- Branch Mode: simple | feature_branch | parallel_ai
- Base Branch:
- Working Branch:
- Merge Target:
- Branch Required: yes/no
- Reason:

## 10. Implementation Steps

| Step ID | Status | Description | Allowed Files | Verification | Pause After |
| --- | --- | --- | --- | --- | --- |
| S1 | pending |  |  |  | yes/no |

## 11. Data Model Changes

- Tables:
- Columns:
- Indexes:
- Constraints:
- Migrations:
- Seed/test data:

## 12. API Changes

- Endpoints:
- Auth:
- Permissions:
- Request DTOs:
- Response DTOs:
- Error codes:
- Curl examples:

## 13. Function and Data Contract Changes

- Function signatures:
- Use case inputs/results:
- Repository protocol methods:
- Provider protocol methods:
- DTO fields:
- Sensitive fields:
- State machine transitions:
- Config/env keys:

## 14. Integration Changes

- Provider:
- Protocol:
- Mock/fake implementation:
- Real implementation:
- Outbox/inbox:
- Retry/dead-letter:
- Manual compensation:

## 15. Security Requirements

- Auth:
- RBAC:
- Object-level authorization:
- PII:
- Secret handling:
- Upload/webhook validation:

## 16. Observability Requirements

- Request logs:
- Audit logs:
- Business events:
- Integration attempts:
- Payment events:
- Metrics:

## 17. Index Updates

- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`:
- `ai_dev/PROJECT/GIT_WORKFLOW.md`:
- `ai_dev/PROJECT/FILE_MAP.md`:
- `ai_dev/PROJECT/FEATURE_MAP.md`:
- `ai_dev/PROJECT/API_ROUTE_MAP.md`:
- `ai_dev/PROJECT/FUNCTION_SIGNATURE_INDEX.md`:
- `ai_dev/PROJECT/DTO_CONTRACT_INDEX.md`:
- `ai_dev/PROJECT/PERMISSION_INDEX.md`:
- `ai_dev/PROJECT/STATE_MACHINE_INDEX.md`:
- `ai_dev/PROJECT/TEST_VERIFICATION_MATRIX.md`:
- `ai_dev/PROJECT/ADMIN_FRONTEND_MAP.md`:
- `ai_dev/PROJECT/CONFIG_ENV_INDEX.md`:
- `ai_dev/PRESETS/cross-border-ecommerce/DOMAIN_MODEL.md`:
- `ai_dev/PRESETS/cross-border-ecommerce/DATABASE_SCHEMA_INDEX.md`:
- `ai_dev/PRESETS/cross-border-ecommerce/API_SIGNATURE_INDEX.md`:
- `ai_dev/PRESETS/cross-border-ecommerce/INTEGRATION_MAP.md`:
- `ai_dev/PRESETS/vapor-backend/SECURITY_RULES.md`:
- `ai_dev/PRESETS/vapor-backend/OBSERVABILITY_RULES.md`:
- `ai_dev/PRESETS/vapor-backend/TESTING_RULES.md`:
- `ai_dev/PROJECT/TRACEABILITY_MATRIX.md`:
- `ai_dev/PROJECT/DECISION_LOG.md`:
- `ai_dev/PROJECT/RISK_REGISTER.md`:

## 18. Verification Gates

Required:

- <command or review gate>

Optional / not available:

- <gate and reason>

## 19. Rollback / Compensation

- Code rollback:
- Migration rollback:
- Data compensation:
- Provider compensation:

## 20. Review Plan

- Review mode:
- Required reviewer focus:
- P0/P1 blocking criteria:

## 21. Learning / Extension Impact

- Did this task encounter a meaningful error, repeated issue, P0/P1 finding,
  failed critical verification, or scope drift?
- Learning record required: yes/no
- Error knowledge base entry:
- Pattern library update:
- Workflow improvement update:
- Preventive rule/test/check:
- Similar risks checked:

## 22. Completion Evidence

- Files changed:
- Commands run:
- Results:
- Remaining risks:
```
