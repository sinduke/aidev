# 000G AI_DEV Validation Tooling

Status: completed

## 1. Goal

Add a minimal automated validation layer for the `aidev` repository.

The first version must support:

- `./bin/aidev check`.
- Task status and required-section validation.
- Required index file validation.
- Git workflow mode validation.
- Basic source/index sync checks once `Sources/` or `Tests/` exist.
- GitHub Actions for `git diff --check`, `aidev check`, and conditional Vapor
  `swift build` / `swift test`.

## 2. Non-Goals

- Do not build a full task generator.
- Do not parse Swift ASTs.
- Do not infer every API/DTO/function change from source code.
- Do not require Swift CI for non-Swift projects.
- Do not change the ecommerce/Vapor architecture direction.

## 3. Business Context

- User value: AI agents and contributors can validate workflow consistency
  before Review or PR merge.
- Operational value: missing task fields, stale indexes, invalid statuses, and
  skipped Review/Verification evidence are caught earlier.
- Project value: `aidev` becomes a usable open-source workflow template with
  executable checks, not only Markdown guidance.

## 4. Mode History

- Review: missing automation was identified as P2.
- Decision: implement a conservative `aidev check` before more complex
  generators or AST-level drift checks.
- Task: this file records the validation tooling addition.
- Build: add CLI wrapper, Python validator, GitHub Actions, docs, and example
  task.
- Review: run the validator and whitespace checks locally.

## 5. Dependencies

- Prior tasks:
  - `000D_aidev_layered_template`
  - `000E_aidev_contract_indexes`
  - `000F_git_workflow_modes`
- Required decisions:
  - Keep Core reusable and keep Vapor-specific CI conditional.
- Required credentials/services:
  - none.
- Required docs:
  - `CORE/TASK_TEMPLATE.md`
  - `CORE/INDEX_REGISTRY.md`
  - `PROJECT/GIT_WORKFLOW.md`

## 6. Assumptions and Open Questions

- Type: assumption
  Question: Should validator v0.1 remain Markdown-structure based?
  Current default: yes, because source conventions are not stable before
  `001_vapor_foundation`.
  Owner: aidev maintainers.
  Required before: validator v0.1.

- Type: later_decision
  Question: Should future versions generate tasks and indexes automatically?
  Current default: defer until the Markdown contract stabilizes through more
  real tasks.
  Owner: aidev maintainers.
  Required before: `aidev new-task` or deeper index drift checks.

## 7. Affected Areas

- Modules: aidev tooling.
- Domain concepts: task status, index update, Git workflow validation.
- Database: none.
- API: none.
- Functions/contracts: CLI contract only.
- DTO/data: none.
- Permissions: none.
- State machines: none.
- Integrations: GitHub Actions.
- Security: no secrets or credentials.
- Observability: command output acts as validation evidence.
- Admin frontend: none.
- Config/env: none.
- Tests: local `aidev check` and GitHub Action validation.

## 8. Write Scope

Allowed files/directories:

- `bin/`
- `tools/`
- `.github/workflows/`
- `README.md`
- `CORE/README.md`
- `CORE/TASK_TEMPLATE.md`
- `PROJECT/IMPLEMENTATION_MAP.md`
- `PROJECT/FILE_MAP.md`
- `PROJECT/TEST_VERIFICATION_MATRIX.md`
- `PROJECT/DECISION_LOG.md`
- `PROJECT/RISK_REGISTER.md`
- `TASKS/000D_aidev_layered_template.md`
- `TASKS/000_project_rules_and_architecture.md`
- `TASKS/000G_aidev_validation_tooling.md`
- `TASKS/001_vapor_foundation.md`

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
- Merge Target: main
- Branch Required: no
- Reason: this is an aidev documentation/tooling update in the standalone
  template repository.

## 10. Implementation Steps

| Step ID | Status | Description | Allowed Files | Verification | Pause After |
| --- | --- | --- | --- | --- | --- |
| S1 | completed | Add `./bin/aidev check` CLI wrapper and Python validator | `bin/`, `tools/` | `./bin/aidev check` runs | no |
| S2 | completed | Add GitHub Actions for aidev and conditional Vapor CI | `.github/workflows/` | workflow YAML exists and keeps Swift conditional | no |
| S3 | completed | Add `001_vapor_foundation` example task | `TASKS/001_vapor_foundation.md` | task status is `example` and has required sections | no |
| S4 | completed | Update docs and project indexes | README, project maps, decision/risk/test docs | `aidev check` validates updated docs | no |
| S5 | completed | Fix historical task metadata exposed by validator | `TASKS/000D...`, `TASKS/000_project...` | `aidev check` has no task metadata errors | no |

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

- Function signatures: `tools/aidev_check.py` adds local validator functions.
- Use case inputs/results: command input is `aidev check`; result is pass/fail
  output with errors and warnings.
- Repository protocol methods: none.
- Provider protocol methods: none.
- DTO fields: none.
- Sensitive fields: none.
- State machine transitions: none.
- Config/env keys: none.

## 14. Integration Changes

- Provider: GitHub Actions.
- Protocol: workflow YAML.
- Mock/fake implementation: not applicable.
- Real implementation: `.github/workflows/aidev-check.yml` and
  `.github/workflows/vapor-ci.yml`.
- Outbox/inbox: none.
- Retry/dead-letter: none.
- Manual compensation: rerun CI after fixing failed validation.

## 15. Security Requirements

- Auth: none.
- RBAC: none.
- Object-level authorization: none.
- PII: none.
- Secret handling: no secrets are required by the workflows.
- Upload/webhook validation: none.

## 16. Observability Requirements

- Request logs: none.
- Audit logs: none.
- Business events: none.
- Integration attempts: CI output records validation attempts.
- Payment events: none.
- Metrics: future CI badge/status can expose pass/fail state.

## 17. Index Updates

- `PROJECT/IMPLEMENTATION_MAP.md`: add CLI, tool, workflow, and task files.
- `PROJECT/FILE_MAP.md`: add local tooling inventory records.
- `PROJECT/TEST_VERIFICATION_MATRIX.md`: add validation command baseline.
- `PROJECT/DECISION_LOG.md`: record the validator v0.1 decision.
- `PROJECT/RISK_REGISTER.md`: mitigate manual-index risk and add remaining
  validator limitations.
- `README.md`: document `aidev check`, CI, and the example task.
- `CORE/README.md`: mention local tooling.

## 18. Verification Gates

Required:

- `./bin/aidev check`
- `git diff --check`
- `python3 -m py_compile tools/aidev_check.py`
- `git status --short`

Optional / not available:

- `swift build`: skipped in this repository until `Package.swift` exists.
- `swift test`: skipped in this repository until `Package.swift` exists.

## 19. Rollback / Compensation

- Code rollback: remove `bin/`, `tools/`, and `.github/workflows/` additions.
- Migration rollback: none.
- Data compensation: none.
- Provider compensation: remove or disable the GitHub Actions workflows.

## 20. Review Plan

- Review mode: tooling and workflow review.
- Required reviewer focus: validator false positives, missing required fields,
  GitHub Action portability, and whether Swift CI stays conditional.
- P0/P1 blocking criteria: `aidev check` cannot run, CI always fails on a
  non-Swift repo, or task status validation rejects valid documented states.

## 21. Learning / Extension Impact

- Did this task encounter a meaningful error, repeated issue, P0/P1 finding,
  failed critical verification, or scope drift? Yes, the first patch landed
  outside the nested `ai_dev` Git repo and was moved back before continuing.
- Learning record required: no.
- Error knowledge base entry: not required because the issue was immediately
  corrected and did not affect committed files.
- Pattern library update: not required.
- Workflow improvement update: future tooling tasks should remember that
  `apply_patch` paths are relative to the outer workspace unless prefixed.
- Preventive rule/test/check: use `git status --short` inside the intended repo
  after adding files.
- Similar risks checked: parent directory only shows the nested repo as
  untracked, with no stray generated files.

## 22. Completion Evidence

- Files changed: validator, CLI wrapper, GitHub Actions, README, project maps,
  risk/decision/test docs, and task records.
- Commands run: listed in final response.
- Results: validation commands passed after fixes.
- Remaining risks: validator v0.1 checks Markdown and path contracts; deeper
  API/DTO/function drift checks remain future work.
