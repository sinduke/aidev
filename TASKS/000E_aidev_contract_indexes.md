# 000E AI_DEV Contract Indexes

Status: completed

## 1. Goal

Upgrade the current AI_DEV system from broad architecture/workflow rules into a
contract-indexed execution system.

The task adds the missing maps required for stable AI-assisted implementation:

- API route map.
- File map.
- Feature map.
- Function signature index.
- DTO/data contract index.
- Permission index.
- State machine index.
- Test verification matrix.
- Admin frontend map.
- Config/env index.
- Generic index registry.

## 2. Non-Goals

- Do not create Vapor source code.
- Do not create migrations.
- Do not finalize all endpoint payload fields.
- Do not choose the admin frontend stack.
- Do not build automation scripts yet.

## 3. Business Context

- First-phase business line: platform admin -> merchant/account/role -> product
  import/visibility -> mobile cart/order/payment -> fulfillment/integration ->
  observability.
- User value: future AI work can start from durable contracts instead of chat
  memory.
- Operational value: API, backend, admin frontend, mobile API, and tests can
  stay aligned.

## 4. Mode History

- Review: current AI_DEV was reviewed for API/file/function/data and broader
  workflow completeness.
- Decision: add contract indexes before `001_vapor_foundation`.
- Task: this file records the documentation-only upgrade.
- Build: completed as documentation/index changes only.
- Review: pending future review if requested.

## 5. Dependencies

- Prior tasks:
  - `000_project_rules_and_architecture`
  - `000A_ai_development_workflow`
  - `000B_learning_extensions`
  - `000C_extension_governance`
  - `000D_aidev_layered_template`
- Required decisions:
  - AI_DEV remains layered: Core, Presets, Project overlay, Tasks.
- Required credentials/services:
  - none.
- Required docs:
  - existing AI_DEV docs.

## 6. Assumptions and Open Questions

- Type: assumption
  Question: Should contract indexes live under project overlay instead of presets?
  Current default: yes, because endpoint/function/DTO details are project-specific.
  Owner: AI agent.
  Required before: this task.

- Type: later_decision
  Question: Should index consistency be automated?
  Current default: document first, add tooling after source conventions exist.
  Owner: user / future tooling.
  Required before: scaling parallel implementation.

## 7. Affected Areas

- Modules: all planned modules.
- Domain concepts: feature, API, function, DTO, permission, state machine, config.
- Database: no schema changes.
- API: documentation/index changes only.
- Functions/contracts: new function signature index.
- DTO/data: new DTO/data contract index.
- Permissions: new permission index.
- State machines: new state machine index.
- Integrations: referenced by function and state indexes.
- Security: permission and object boundary mapping.
- Observability: feature/test/event mappings.
- Admin frontend: new admin frontend map.
- Config/env: new config/env index.
- Tests: new verification matrix.

## 8. Write Scope

Allowed files/directories:

- `ai_dev/CORE/`
- `ai_dev/PROJECT/`
- `ai_dev/PRESETS/cross-border-ecommerce/API_SIGNATURE_INDEX.md`
- `ai_dev/AIDEV_MANIFEST.md`
- `ai_dev/PROJECT_RULES.md`
- `ai_dev/README.md`
- `ai_dev/TASKS/000E_aidev_contract_indexes.md`

Forbidden files/directories:

- Vapor source files.
- migrations.
- frontend source files.

Scope expansion rule:

- Stop and update this task before editing files outside allowed scope.

## 9. Implementation Steps

| Step ID | Status | Description | Allowed Files | Verification | Pause After |
| --- | --- | --- | --- | --- | --- |
| S1 | completed | Add generic index registry | `ai_dev/CORE/INDEX_REGISTRY.md` | registry defines required index types | no |
| S2 | completed | Add project feature/file/API/function/DTO indexes | `ai_dev/PROJECT/*.md` | maps exist and have templates/status rules | no |
| S3 | completed | Add permission/state/test/admin/config indexes | `ai_dev/PROJECT/*.md` | indexes exist and cover first-phase route | no |
| S4 | completed | Wire indexes into manifest, rules, workflow, review, task template | AI_DEV docs | updated docs reference new indexes | no |
| S5 | completed | Record decision/risk/task | `DECISION_LOG.md`, `RISK_REGISTER.md`, this task | D-0009 and R-0009 exist | no |
| S6 | completed | Clean `.DS_Store` files | `ai_dev/` | no `.DS_Store` under `ai_dev` | no |

## 10. Data Model Changes

- Tables: none.
- Columns: none.
- Indexes: none.
- Constraints: none.
- Migrations: none.
- Seed/test data: none.

## 11. API Changes

- Endpoints: none implemented.
- Auth: none.
- Permissions: permission index added.
- Request DTOs: DTO contract index added.
- Response DTOs: DTO contract index added.
- Error codes: no registry change.
- Curl examples: no implemented endpoint yet.

## 11A. Function and Data Contract Changes

- Function signatures: planned function signature index added.
- Use case inputs/results: named in planned signatures and DTO/data contracts.
- Repository protocol methods: template added; concrete rows deferred until source
  tasks.
- Provider protocol methods: planned payment and fulfillment provider signatures.
- DTO fields: initial DTO contracts for core first-phase APIs.
- Sensitive fields: token, password, client secret, visibility token marked.
- State machine transitions: merchant, product, visibility, import, order,
  payment, fulfillment, integration attempts added.
- Config/env keys: planned application/database/auth/provider/storage keys added.

## 12. Integration Changes

- Provider: no implementation.
- Protocol: planned provider method signatures documented.
- Mock/fake implementation: no implementation.
- Real implementation: no implementation.
- Outbox/inbox: no implementation.
- Retry/dead-letter: state/index documentation only.
- Manual compensation: admin/API/index documentation only.

## 13. Security Requirements

- Auth: no implementation.
- RBAC: permission index added.
- Object-level authorization: boundary policies documented.
- PII: DTO sensitivity markers added.
- Secret handling: config/env index and redaction rules added.
- Upload/webhook validation: referenced in route/test/security indexes.

## 14. Observability Requirements

- Request logs: referenced in feature/test indexes.
- Audit logs: permission/state changes require audit.
- Business events: feature and state indexes map events.
- Integration attempts: state/test/function indexes map attempt behavior.
- Payment events: state/test/function indexes map webhook behavior.
- Metrics: no implementation.

## 15. Index Updates

- `ai_dev/CORE/INDEX_REGISTRY.md`: added.
- `ai_dev/PROJECT/FEATURE_MAP.md`: added.
- `ai_dev/PROJECT/FILE_MAP.md`: added.
- `ai_dev/PROJECT/API_ROUTE_MAP.md`: added.
- `ai_dev/PROJECT/FUNCTION_SIGNATURE_INDEX.md`: added.
- `ai_dev/PROJECT/DTO_CONTRACT_INDEX.md`: added.
- `ai_dev/PROJECT/PERMISSION_INDEX.md`: added.
- `ai_dev/PROJECT/STATE_MACHINE_INDEX.md`: added.
- `ai_dev/PROJECT/TEST_VERIFICATION_MATRIX.md`: added.
- `ai_dev/PROJECT/ADMIN_FRONTEND_MAP.md`: added.
- `ai_dev/PROJECT/CONFIG_ENV_INDEX.md`: added.
- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`: updated.
- `ai_dev/PROJECT/TRACEABILITY_MATRIX.md`: updated.
- `ai_dev/PROJECT/DECISION_LOG.md`: D-0009 added.
- `ai_dev/PROJECT/RISK_REGISTER.md`: R-0009 added.
- `ai_dev/PRESETS/cross-border-ecommerce/API_SIGNATURE_INDEX.md`: linked to project API route map.
- `ai_dev/CORE/AI_WORKFLOW.md`: updated.
- `ai_dev/CORE/REVIEW_RULES.md`: updated.
- `ai_dev/CORE/TASK_TEMPLATE.md`: updated.
- `ai_dev/AIDEV_MANIFEST.md`: updated.
- `ai_dev/PROJECT_RULES.md`: updated.
- `ai_dev/README.md`: updated.

## 16. Verification Gates

Required:

- Confirm new index files exist.
- Confirm no `.DS_Store` files remain under `ai_dev`.
- `git diff --check`.
- Tail whitespace check for `ai_dev`.
- Stale path/reference check.
- `git status --short`.

Optional / not available:

- `swift build`: not available because Vapor source does not exist yet.
- `swift test`: not available because Vapor source does not exist yet.

## 17. Rollback / Compensation

- Code rollback: documentation-only rollback by reverting this task's files.
- Migration rollback: none.
- Data compensation: none.
- Provider compensation: none.

## 18. Review Plan

- Review mode: architecture/workflow/documentation review.
- Required reviewer focus:
  - Does Core stay generic?
  - Are project contracts specific enough to guide code generation?
  - Are new indexes wired into workflow and task templates?
  - Is the system too heavy for small tasks?
- P0/P1 blocking criteria:
  - Missing function/API/DTO contract indexes.
  - New indexes not referenced by workflow/review/task template.
  - Project-specific contracts placed in Core.

## 19. Learning / Extension Impact

- Meaningful issue encountered: yes.
- Learning record required: no full record; this task is a workflow improvement
  from review findings.
- Error knowledge base entry: not required.
- Pattern library update: not required.
- Workflow improvement update: not required beyond updated Core rules.
- Preventive rule/test/check: index registry, task template, workflow, and review
  rules now require contract index updates.
- Similar risks checked: API, files, functions, DTOs, permissions, state machines,
  tests, admin frontend, config/env.

## 20. Completion Evidence

- Files changed: AI_DEV core/project/preset/task docs.
- Commands run:
  - `find ai_dev -maxdepth 5 -type f -print | sort`
  - `find ai_dev -name '.DS_Store' -print`
  - `git diff --check`
  - `rg -n "[ \t]+$" ai_dev || true`
  - stale path/reference `rg` check
  - index wiring `rg` check
  - `git status --short`
- Results:
  - Required index files exist.
  - No `.DS_Store` remains under `ai_dev`.
  - `git diff --check` passed.
  - Tail whitespace check passed.
  - Stale path/reference check passed.
  - Index wiring check found the new indexes in entrypoint/workflow/template docs.
- Remaining risks: index consistency is manual until automation exists.
