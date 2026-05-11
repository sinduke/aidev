# Decision Log

## 1. Purpose

This document records durable project decisions so future AI agents do not
re-litigate or silently change them.

Use this for architecture, technology, business boundary, data model, provider,
and workflow decisions.

## 2. Status Values

- `accepted`
- `proposed`
- `superseded`
- `deferred`
- `rejected`

## 3. Decision Record Template

```text
ID:
Status:
Date:
Decision:
Context:
Rationale:
Rejected Alternatives:
Consequences:
Related Tasks:
Related Docs:
```

## 4. Decisions

### D-0001 Use ai_dev as the project control plane

Status: accepted
Date: 2026-05-10

Decision:

- Use `ai_dev` as the persistent planning, decision, task, build, review, and
  traceability control plane.

Context:

- The project is a large cross-border B2B2C commerce system that will be built
  with AI assistance from zero to one.

Rationale:

- Conversation memory is not durable enough for a long-running system.
- Task files and indexes prevent scope drift.

Rejected Alternatives:

- Build directly from chat instructions.
- Keep only a README without task/index structure.

Consequences:

- Every approved implementation must have a task file.
- Index files must be updated with code changes.

Related Tasks:

- `000_project_rules_and_architecture`
- `000A_ai_development_workflow`

Related Docs:

- `ai_dev/PROJECT_RULES.md`
- `ai_dev/CORE/AI_WORKFLOW.md`

### D-0002 Use Vapor and modular monolith for phase one

Status: accepted
Date: 2026-05-10

Decision:

- Use Swift Vapor as the backend framework.
- Use a modular monolith in phase one.

Context:

- The project values long-term control, type safety, API-first design, and clear
  domain boundaries.

Rationale:

- Microservices would add operational complexity too early.
- Vapor is suitable for API-first backend development.

Rejected Alternatives:

- PHP/ECShopX direct customization as the main system.
- Java/Spring as the default backend.
- Microservices from the start.

Consequences:

- The system must define module boundaries clearly.
- External systems must use provider adapters.

Related Tasks:

- `000_project_rules_and_architecture`

Related Docs:

- `ai_dev/PRESETS/vapor-backend/ARCHITECTURE.md`

### D-0003 Treat hidden product and distribution capabilities as platform rules

Status: accepted
Date: 2026-05-10

Decision:

- Hidden product and distribution behavior are platform capabilities, not
  hardcoded frontend page behavior.

Context:

- Hidden products and distribution are core differentiators.

Rationale:

- Search, recommendation, detail, cart, checkout, and admin all need consistent
  server-side enforcement.

Rejected Alternatives:

- Hide products only in the mobile frontend.
- Implement hidden products as one-off campaign pages.

Consequences:

- Visibility must be a domain concept.
- API/server checks are mandatory.

Related Docs:

- `ai_dev/PRESETS/cross-border-ecommerce/DOMAIN_MODEL.md`
- `ai_dev/PROJECT/TRACEABILITY_MATRIX.md`

### D-0004 Start with PostgreSQL unless compatibility requires MySQL

Status: proposed
Date: 2026-05-10

Decision:

- Default to PostgreSQL for a new Vapor-first build.
- Revisit if ECShopX/MySQL compatibility becomes a hard requirement.

Context:

- The project is new, but ECShopX has been used as reference.

Rationale:

- PostgreSQL is a strong default for new backend systems with complex relational
  data and reporting.

Rejected Alternatives:

- Commit to MySQL immediately.
- Keep database choice undefined.

Consequences:

- `001_vapor_foundation` should either confirm PostgreSQL or explicitly change
  this decision.

Related Docs:

- `ai_dev/PRESETS/cross-border-ecommerce/DATABASE_SCHEMA_INDEX.md`

### D-0005 Stripe-first payment with provider abstraction

Status: accepted
Date: 2026-05-10

Decision:

- Start payment planning with Stripe, but keep payment provider behavior behind a
  protocol.

Context:

- Cross-border payments need provider-specific webhook/idempotency handling.

Rationale:

- Stripe is a practical first provider, but order/payment domain must not depend
  on Stripe directly.

Rejected Alternatives:

- Hardcode Stripe in order domain.
- Design a multi-provider marketplace settlement system in v1.

Consequences:

- `PaymentProvider`, `MockPaymentProvider`, and `StripePaymentProvider` are the
  expected pattern once payment work begins.

Related Docs:

- `ai_dev/PRESETS/cross-border-ecommerce/INTEGRATION_MAP.md`
- `ai_dev/PRESETS/cross-border-ecommerce/DOMAIN_MODEL.md`

### D-0006 First fulfillment integration scope is order and logistics sync

Status: accepted
Date: 2026-05-10

Decision:

- The first Mabang-like integration scope is order sync and logistics sync only.

Context:

- Deep ERP inventory/product integration can greatly expand v1 scope.

Rationale:

- Order and logistics sync are enough to complete the first commercial route.

Rejected Alternatives:

- Deep inventory synchronization in v1.
- Product master data sync in v1.
- Full warehouse management in v1.

Consequences:

- Fulfillment provider adapters should focus on order/logistics operations first.

Related Docs:

- `ai_dev/PRESETS/cross-border-ecommerce/INTEGRATION_MAP.md`
- `ai_dev/PROJECT/TRACEABILITY_MATRIX.md`

### D-0007 Use extensions for project-level self-learning

Status: accepted
Date: 2026-05-11

Decision:

- Add `ai_dev/CORE/EXTENSIONS/` as a project-level self-learning and workflow
  improvement system.

Context:

- Large AI-assisted development needs to learn from errors instead of only
  solving the immediate issue.

Rationale:

- Repeated errors should become rules, tests, review checks, or workflow updates.
- Learning must be repository-local, reviewable, and versioned.

Rejected Alternatives:

- Rely on chat memory.
- Fix each error locally without abstraction.
- Put all learning into a generic notes section with no closure criteria.

Consequences:

- P0/P1 findings, failed critical verification, repeated issues, scope drift, and
  meaningful human corrections require learning records or explicit deferral.
- Review and Close modes must check learning impact.

Related Tasks:

- `000B_learning_extensions`

Related Docs:

- `ai_dev/CORE/EXTENSIONS/README.md`
- `ai_dev/CORE/EXTENSIONS/LEARNING_LOOP.md`
- `ai_dev/CORE/EXTENSIONS/ERROR_KNOWLEDGE_BASE.md`

### D-0008 Split AI_DEV into Core, Presets, Project overlay, and Tasks

Status: accepted
Date: 2026-05-11

Decision:

- Split the project AI_DEV folder into reusable `CORE/`, reusable `PRESETS/`,
  current `PROJECT/` overlay, and current `TASKS/`.

Context:

- The user has multiple AI_DEV systems for frontend, mobile, backend, and admin
  work. Regenerating a full AI_DEV for every new project creates duplication and
  drift.

Rationale:

- Core workflow should be maintained once.
- Technical/domain presets should be reused by project type.
- Project overlay should stay small and business-specific.

Rejected Alternatives:

- Keep one flat `ai_dev` per project.
- Put all reusable and project-specific rules in one large `PROJECT_RULES.md`.
- Extract to an external template repository before proving the local structure.

Consequences:

- New projects should select Core + Presets and create a small Project overlay.
- Current work should read `AIDEV_MANIFEST.md` first.

Related Tasks:

- `000D_aidev_layered_template`

Related Docs:

- `ai_dev/AIDEV_MANIFEST.md`
- `ai_dev/README.md`
- `ai_dev/PROJECT/PROJECT_PROFILE.md`

### D-0009 Add project contract indexes before Vapor build

Status: accepted
Date: 2026-05-11

Decision:

- Add a generic index registry in `CORE/`.
- Add project-level maps for features, files, API routes, function signatures,
  DTO/data contracts, permissions, state machines, tests, admin frontend pages,
  and config/env keys.

Context:

- The existing AI_DEV rules were strong for architecture and workflow, but too
  coarse for stable code generation across a large ecommerce system.
- Future AI agents need durable contracts for function parameters, return types,
  DTO fields, permissions, routes, and test expectations.

Rationale:

- Large projects fail when implementation details live only in conversation.
- Contract indexes make API, backend, admin frontend, and mobile API work align.
- The split keeps Core reusable while project-specific contracts stay in
  `PROJECT/`.

Rejected Alternatives:

- Keep only `IMPLEMENTATION_MAP.md` and broad API docs.
- Add contracts only after code exists.
- Put project endpoint/function/DTO details into reusable Core.

Consequences:

- Build tasks that touch source or public contracts must update the specialized
  project indexes.
- Review mode should treat missing contract updates as findings.
- Future automation can validate these indexes.

Related Tasks:

- `000E_aidev_contract_indexes`

Related Docs:

- `ai_dev/CORE/INDEX_REGISTRY.md`
- `ai_dev/PROJECT/FEATURE_MAP.md`
- `ai_dev/PROJECT/API_ROUTE_MAP.md`
- `ai_dev/PROJECT/FUNCTION_SIGNATURE_INDEX.md`
- `ai_dev/PROJECT/DTO_CONTRACT_INDEX.md`

### D-0010 Use switchable Git workflow modes

Status: accepted
Date: 2026-05-11

Decision:

- Add switchable Git workflow modes:
  - `simple`
  - `feature_branch`
  - `parallel_ai`
- Use `simple` as the current project default.
- Treat `main` as the stable/release branch when branch discipline is enabled.
- Enable feature branches or parallel branch isolation only when task/project
  context requires it.

Context:

- The user mostly develops solo and may not want branch ceremony for every small
  change.
- Multi-AI or multi-module development needs branch isolation to prevent
  conflicting edits and unclear review history.

Rationale:

- Strict branch rules are useful under concurrency but too heavy for all solo
  work.
- A switchable mode keeps the workflow practical while still allowing rigorous
  branch discipline when needed.

Rejected Alternatives:

- Always require feature branches for every task.
- Always allow direct work on the current branch.
- Introduce mandatory `develop` before the project has enough source activity.

Consequences:

- Source-code tasks must check `PROJECT/GIT_WORKFLOW.md`.
- Branch fields are now available in the task template.
- `parallel_ai` mode requires explicit switching and branch/worktree isolation.

Related Tasks:

- `000F_git_workflow_modes`

Related Docs:

- `ai_dev/CORE/GIT_WORKFLOW.md`
- `ai_dev/PROJECT/GIT_WORKFLOW.md`
- `ai_dev/CORE/TASK_TEMPLATE.md`
