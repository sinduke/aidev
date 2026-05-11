# 000F Git Workflow Modes

Status: completed

## 1. Goal

Add a switchable Git workflow mode system so the project can support both
lightweight solo development and stricter feature-branch isolation for multi-AI
or multi-module work.

## 2. Non-Goals

- Do not create or switch local Git branches in this task.
- Do not require every future task to use feature branches.
- Do not introduce a mandatory `develop` branch yet.
- Do not change source code.

## 3. Business Context

- First-phase business line: AI-assisted backend/admin/mobile API development.
- User value: solo work remains fast, but stricter branch discipline is available
  when useful.
- Operational value: parallel AI work can be isolated and reviewed before merge.

## 4. Mode History

- Exploration: user raised optional feature-branch workflow for AI/multi-module
  development.
- Decision: use switchable modes instead of mandatory branch rules.
- Task: add Core and Project Git workflow docs and wire them into task/review.
- Build: documentation-only implementation completed.
- Review: pending future review if requested.

## 5. Dependencies

- Prior tasks:
  - `000D_aidev_layered_template`
  - `000E_aidev_contract_indexes`
- Required decisions:
  - Branch discipline should be optional by default.
- Required credentials/services:
  - none.
- Required docs:
  - `ai_dev/CORE/AI_WORKFLOW.md`
  - `ai_dev/CORE/TASK_TEMPLATE.md`
  - `ai_dev/CORE/REVIEW_RULES.md`

## 6. Assumptions and Open Questions

- Type: assumption
  Question: Should the current default be `simple`?
  Current default: yes, because the user often develops solo and wants branch
  discipline mainly for parallel AI work.
  Owner: user / AI agent.
  Required before: this task.

- Type: later_decision
  Question: Should the project introduce `develop` or `integration`?
  Current default: not required yet.
  Owner: user / future workflow decision.
  Required before: frequent parallel feature merges.

## 7. Affected Areas

- Modules: none.
- Domain concepts: none.
- Database: none.
- API: none.
- Functions/contracts: none.
- DTO/data: none.
- Permissions: none.
- State machines: none.
- Integrations: none.
- Security: none.
- Observability: none.
- Admin frontend: none.
- Config/env: none.
- Git workflow: branch mode docs and task template fields.
- Tests: documentation consistency checks only.

## 8. Write Scope

Allowed files/directories:

- `ai_dev/CORE/GIT_WORKFLOW.md`
- `ai_dev/PROJECT/GIT_WORKFLOW.md`
- `ai_dev/AIDEV_MANIFEST.md`
- `ai_dev/README.md`
- `ai_dev/PROJECT_RULES.md`
- `ai_dev/CORE/README.md`
- `ai_dev/CORE/AI_WORKFLOW.md`
- `ai_dev/CORE/TASK_TEMPLATE.md`
- `ai_dev/CORE/REVIEW_RULES.md`
- `ai_dev/PROJECT/PROJECT_PROFILE.md`
- `ai_dev/PROJECT/PROJECT_RULES.md`
- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`
- `ai_dev/PROJECT/DECISION_LOG.md`
- `ai_dev/PROJECT/RISK_REGISTER.md`
- `ai_dev/TASKS/000F_git_workflow_modes.md`

Forbidden files/directories:

- Vapor source files.
- migrations.
- frontend source files.

Scope expansion rule:

- Stop and update this task before editing files outside allowed scope.

## 9. Git Workflow

- Branch Mode: simple
- Base Branch: current branch
- Working Branch: current branch
- Merge Target: none for this documentation-only task
- Branch Required: no
- Reason: this task defines the branch workflow and intentionally does not
  require branch creation.

## 10. Implementation Steps

| Step ID | Status | Description | Allowed Files | Verification | Pause After |
| --- | --- | --- | --- | --- | --- |
| S1 | completed | Add reusable Git workflow modes | `ai_dev/CORE/GIT_WORKFLOW.md` | modes are defined | no |
| S2 | completed | Add current project Git workflow choice | `ai_dev/PROJECT/GIT_WORKFLOW.md` | default mode is `simple` | no |
| S3 | completed | Wire Git workflow into manifest, workflow, task template, review, and project rules | AI_DEV docs | docs reference Git workflow | no |
| S4 | completed | Record decision and risk | `DECISION_LOG.md`, `RISK_REGISTER.md` | D-0010 and R-0010 exist | no |
| S5 | completed | Run documentation consistency checks | docs only | checks pass | no |

## 11. Data Model Changes

- Tables: none.
- Columns: none.
- Indexes: none.
- Constraints: none.
- Migrations: none.
- Seed/test data: none.

## 12. API Changes

- Endpoints: none.
- Auth: none.
- Permissions: none.
- Request DTOs: none.
- Response DTOs: none.
- Error codes: none.
- Curl examples: none.

## 13. Function and Data Contract Changes

- Function signatures: none.
- Use case inputs/results: none.
- Repository protocol methods: none.
- Provider protocol methods: none.
- DTO fields: none.
- Sensitive fields: none.
- State machine transitions: none.
- Config/env keys: none.

## 14. Integration Changes

- Provider: none.
- Protocol: none.
- Mock/fake implementation: none.
- Real implementation: none.
- Outbox/inbox: none.
- Retry/dead-letter: none.
- Manual compensation: none.

## 15. Security Requirements

- Auth: none.
- RBAC: none.
- Object-level authorization: none.
- PII: none.
- Secret handling: none.
- Upload/webhook validation: none.

## 16. Observability Requirements

- Request logs: none.
- Audit logs: none.
- Business events: none.
- Integration attempts: none.
- Payment events: none.
- Metrics: none.

## 17. Index Updates

- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`: updated.
- `ai_dev/PROJECT/GIT_WORKFLOW.md`: added.
- `ai_dev/PROJECT/FILE_MAP.md`: no source file change.
- `ai_dev/PROJECT/FEATURE_MAP.md`: no business feature change.
- `ai_dev/PROJECT/API_ROUTE_MAP.md`: no API change.
- `ai_dev/PROJECT/FUNCTION_SIGNATURE_INDEX.md`: no function change.
- `ai_dev/PROJECT/DTO_CONTRACT_INDEX.md`: no DTO change.
- `ai_dev/PROJECT/PERMISSION_INDEX.md`: no permission change.
- `ai_dev/PROJECT/STATE_MACHINE_INDEX.md`: no state machine change.
- `ai_dev/PROJECT/TEST_VERIFICATION_MATRIX.md`: no test contract change.
- `ai_dev/PROJECT/ADMIN_FRONTEND_MAP.md`: no admin page change.
- `ai_dev/PROJECT/CONFIG_ENV_INDEX.md`: no runtime config change.
- `ai_dev/PROJECT/TRACEABILITY_MATRIX.md`: no first-phase business coverage
  change.
- `ai_dev/PROJECT/DECISION_LOG.md`: D-0010 added.
- `ai_dev/PROJECT/RISK_REGISTER.md`: R-0010 added.

## 18. Verification Gates

Required:

- Confirm Git workflow docs exist.
- Confirm entrypoint/workflow/task/review docs reference Git workflow.
- `git diff --check`.
- Tail whitespace check.
- `.DS_Store` check.
- `git status --short`.

Optional / not available:

- `swift build`: not available because Vapor source does not exist yet.
- `swift test`: not available because Vapor source does not exist yet.

## 19. Rollback / Compensation

- Code rollback: documentation-only rollback by reverting this task's files.
- Migration rollback: none.
- Data compensation: none.
- Provider compensation: none.

## 20. Review Plan

- Review mode: workflow/documentation review.
- Required reviewer focus:
  - Is branch isolation optional by default?
  - Does `parallel_ai` enforce separate branch/worktree isolation?
  - Are task/review checks wired without making solo work too heavy?
- P0/P1 blocking criteria:
  - Git workflow silently forces branch mode for all tasks.
  - Parallel AI branch isolation is unclear.
  - Task template cannot record branch mode.

## 21. Learning / Extension Impact

- Meaningful issue encountered: no.
- Learning record required: no.
- Error knowledge base entry: none.
- Pattern library update: not required.
- Workflow improvement update: implemented directly in Core Git workflow docs.
- Preventive rule/test/check: Build and Review now check Git workflow when source
  edits or parallel AI work are involved.
- Similar risks checked: solo work, feature branch work, parallel AI work, merge
  review.

## 22. Completion Evidence

- Files changed: AI_DEV Git workflow and entrypoint docs.
- Commands run:
  - `find ai_dev -maxdepth 5 -type f -print | sort`
  - `git diff --check`
  - `rg -n "[ \t]+$" ai_dev || true`
  - `find ai_dev -name '.DS_Store' -print`
  - Git workflow wiring `rg` check
  - stale path/reference `rg` check
  - `git status --short`
- Results:
  - Git workflow docs exist.
  - Entry, workflow, task template, review, project, and task docs reference Git
    workflow.
  - `git diff --check` passed.
  - Tail whitespace check passed.
  - `.DS_Store` check passed.
  - Stale path/reference check passed.
- Remaining risks: branch discipline remains optional until mode is switched.
