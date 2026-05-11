# Risk Register

## 1. Purpose

This document tracks project risks, assumptions, blockers, and deferred
decisions.

Risks must be visible so AI agents do not silently guess.

## 2. Risk Fields

Use this format:

```text
ID:
Status: open | mitigated | accepted | closed
Severity: P0 | P1 | P2 | P3
Type: business | technical | security | data | integration | compliance | workflow
Risk:
Impact:
Mitigation:
Owner:
Required Before:
Related Docs:
Related Tasks:
```

## 3. Current Risks

### R-0001 Final project name is undecided

Status: open
Severity: P3
Type: workflow

Risk:

- Package names, database names, Docker service names, and API docs may need
  renaming later.

Impact:

- Minor churn during foundation setup.

Mitigation:

- Use neutral names until the user confirms the project name.

Owner:

- User.

Required Before:

- Public deployment and production package naming.

Related Tasks:

- `001_vapor_foundation`

### R-0002 Database choice is proposed, not final

Status: open
Severity: P2
Type: technical

Risk:

- PostgreSQL is the proposed default, but ECShopX/MySQL compatibility may become
  important.

Impact:

- Early migration and repository choices may need adjustment.

Mitigation:

- `001_vapor_foundation` must explicitly confirm PostgreSQL or document a MySQL
  decision.

Owner:

- User / technical decision.

Required Before:

- Creating production-intended migrations.

Related Docs:

- `ai_dev/PROJECT/DECISION_LOG.md`
- `ai_dev/PRESETS/cross-border-ecommerce/DATABASE_SCHEMA_INDEX.md`

### R-0003 First target markets are undecided

Status: open
Severity: P1
Type: compliance

Risk:

- Cross-border tax, customs, payment, logistics, and compliance rules depend on
  target markets.

Impact:

- Product compliance fields and order/tax behavior may be too generic or wrong
  for launch.

Mitigation:

- Keep market/tax/compliance data model extensible.
- Require market decision before production launch.

Owner:

- User / business.

Required Before:

- Production sales in a real market.

Related Docs:

- `ai_dev/PRESETS/cross-border-ecommerce/DOMAIN_MODEL.md`
- `ai_dev/PRESETS/cross-border-ecommerce/DATABASE_SCHEMA_INDEX.md`

### R-0004 Stripe Connect settlement scope is undecided

Status: open
Severity: P1
Type: payment

Risk:

- Platform-collected payments and merchant settlement via Stripe Connect have
  different data, compliance, and flow requirements.

Impact:

- Payment and merchant settlement architecture may need changes.

Mitigation:

- V1 can assume platform-collected payments unless the user decides Stripe
  Connect is required.
- Keep payment provider abstraction.

Owner:

- User / business.

Required Before:

- Implementing real payment settlement.

Related Docs:

- `ai_dev/PRESETS/cross-border-ecommerce/INTEGRATION_MAP.md`
- `ai_dev/PROJECT/DECISION_LOG.md`

### R-0005 Admin frontend stack is undecided

Status: open
Severity: P2
Type: technical

Risk:

- Admin API shape may be affected by frontend stack and table/form conventions.

Impact:

- Some DTO or pagination choices may need adjustment.

Mitigation:

- Keep API-first contracts independent from frontend implementation.
- Decide frontend stack before admin UI implementation.

Owner:

- User / technical decision.

Required Before:

- Building admin frontend pages.

Related Docs:

- `ai_dev/PRESETS/cross-border-ecommerce/API_SIGNATURE_INDEX.md`

### R-0006 AI workflow can drift if task statuses are not maintained

Status: open
Severity: P1
Type: workflow

Risk:

- AI may execute from stale context or skip step-by-step gates.

Impact:

- Scope creep, missing docs, unverified code.

Mitigation:

- Require approved task files, step statuses, write scope, and review closure.

Owner:

- AI agent / user confirmation.

Required Before:

- Every Build task.

Related Docs:

- `ai_dev/CORE/AI_WORKFLOW.md`
- `ai_dev/CORE/TASK_TEMPLATE.md`
- `ai_dev/CORE/REVIEW_RULES.md`

### R-0007 Learning loop remains document-based until automation exists

Status: open
Severity: P2
Type: workflow

Risk:

- The learning extension requires agents to update documents and checklists, but
  there is not yet automation that enforces learning records for severe findings
  or repeated failures.

Impact:

- Future agents could skip the learning loop unless review catches it.

Mitigation:

- `REVIEW_RULES.md` and `AI_WORKFLOW.md` require checking learning impact.
- Future CI/tooling can add checks once source code and task tooling exist.

Owner:

- AI agent / future tooling.

Required Before:

- Scaling to frequent parallel tasks or multi-agent development.

Related Docs:

- `ai_dev/CORE/EXTENSIONS/LEARNING_LOOP.md`
- `ai_dev/CORE/EXTENSIONS/ERROR_KNOWLEDGE_BASE.md`
- `ai_dev/CORE/REVIEW_RULES.md`

Related Tasks:

- `000B_learning_extensions`

### R-0008 AI_DEV Core/Presets are local copies until external template strategy is decided

Status: open
Severity: P2
Type: workflow

Risk:

- `CORE/` and `PRESETS/` are now reusable in structure, but still live inside
  this repository. Other projects may copy them and drift unless a shared source
  of truth is later chosen.

Impact:

- Multiple projects could slowly develop incompatible AI_DEV core rules.

Mitigation:

- Use `AIDEV_MANIFEST.md` to make the active layers explicit.
- Treat future extraction to a standalone `aidev-template` repository as a later
  decision.

Owner:

- User / workflow.

Required Before:

- Reusing AI_DEV across many projects or a team.

Related Docs:

- `ai_dev/AIDEV_MANIFEST.md`
- `ai_dev/README.md`

Related Tasks:

- `000D_aidev_layered_template`

### R-0009 Contract indexes have only partial automated validation

Status: open
Severity: P2
Type: workflow

Risk:

- API, function, DTO, file, permission, state, and test indexes now exist. The
  first validator checks required files, task structure, Git mode, and source
  path map coverage, but it does not yet prove every API/DTO/function contract is
  synchronized with source code.

Impact:

- Future AI agents could forget to update a contract index even when rules require
  it.

Mitigation:

- `CORE/INDEX_REGISTRY.md`, `TASK_TEMPLATE.md`, `AI_WORKFLOW.md`, and
  `REVIEW_RULES.md` now require index updates.
- `./bin/aidev check` now validates required files, task status/sections, Git
  workflow mode, and basic source file map coverage.
- Add deeper route/DTO/function checks once source code and stable conventions
  exist.

Owner:

- AI agent / future tooling.

Required Before:

- Scaling to frequent parallel implementation or team handoff.

Related Docs:

- `ai_dev/CORE/INDEX_REGISTRY.md`
- `ai_dev/PROJECT/FEATURE_MAP.md`
- `ai_dev/PROJECT/API_ROUTE_MAP.md`
- `ai_dev/PROJECT/FUNCTION_SIGNATURE_INDEX.md`
- `ai_dev/PROJECT/DTO_CONTRACT_INDEX.md`
- `ai_dev/PROJECT/TEST_VERIFICATION_MATRIX.md`

Related Tasks:

- `000E_aidev_contract_indexes`
- `000G_aidev_validation_tooling`

### R-0010 Optional branch discipline can be skipped accidentally

Status: open
Severity: P2
Type: workflow

Risk:

- Because the default Git workflow mode is `simple`, future source-code work may
  continue on the current branch even when feature branch isolation would be
  safer.

Impact:

- Parallel AI work can conflict.
- Review history can become harder to isolate.
- `main` could receive unreviewed development work if branch mode is not switched
  before larger source changes.

Mitigation:

- `PROJECT/GIT_WORKFLOW.md` defines when to switch to `feature_branch` or
  `parallel_ai`.
- `TASK_TEMPLATE.md` includes a Git Workflow section.
- `AI_WORKFLOW.md` and `REVIEW_RULES.md` require branch-mode checks for source
  work and parallel AI work.

Owner:

- AI agent / user confirmation.

Required Before:

- First non-trivial Vapor source-code task or any parallel AI implementation.

Related Docs:

- `ai_dev/CORE/GIT_WORKFLOW.md`
- `ai_dev/PROJECT/GIT_WORKFLOW.md`
- `ai_dev/CORE/TASK_TEMPLATE.md`
- `ai_dev/CORE/REVIEW_RULES.md`

Related Tasks:

- `000F_git_workflow_modes`

### R-0011 Validator v0.1 is intentionally conservative

Status: open
Severity: P2
Type: workflow

Risk:

- `aidev check` validates Markdown structure and basic path map coverage, but it
  does not parse Swift ASTs, route registration, DTO fields, database migrations,
  or permission usage.

Impact:

- A future task could pass `aidev check` while still missing a deeper API,
  function, DTO, permission, or schema update.

Mitigation:

- Keep Review mode responsible for semantic checks.
- Treat validator output as a minimum gate, not full correctness proof.
- Add deeper checks incrementally after `001_vapor_foundation` establishes stable
  source layout and conventions.

Owner:

- AI agent / aidev maintainers.

Required Before:

- Scaling to frequent source-code implementation, PR handoff, or parallel AI
  development.

Related Docs:

- `ai_dev/tools/aidev_check.py`
- `ai_dev/CORE/REVIEW_RULES.md`
- `ai_dev/PROJECT/TEST_VERIFICATION_MATRIX.md`

Related Tasks:

- `000G_aidev_validation_tooling`
- `001_vapor_foundation`
