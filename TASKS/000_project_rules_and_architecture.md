# 000 Project Rules and Architecture

Status: completed

Completion note: expanded rules draft.

## Goal

Create the foundational ai_dev rules for a Vapor-based cross-border B2B2C
commerce backend project.

This task establishes how future AI-assisted development should work before any
business code is written.

## Non-Goals

- Do not create Vapor source code yet.
- Do not create database migrations yet.
- Do not build admin frontend pages yet.
- Do not implement payment, order, product, merchant, or integration features yet.
- Do not choose every final production vendor now.

## Business Context

The first phase must not attempt a complete marketplace. It must create a
controlled route:

platform admin -> merchant -> product/SKU -> visibility -> mobile detail/cart ->
order -> payment -> admin order recognition -> fulfillment/integration -> logs.

The project must account for common cross-border ecommerce problems:

- Multi-party ownership and merchant isolation.
- Country/market restrictions.
- Multi-currency money handling.
- Tax/duty/customs data capture.
- Payment webhook/idempotency.
- Fulfillment and logistics as asynchronous flows.
- Import workflows that need validation, preview, and error reporting.
- Admin observability for every critical state transition.

The project must also preserve our own product uniqueness:

- Hidden products are first-class business capability.
- Distribution/hidden-product mechanics should be plugin-friendly.
- Full tracking/logging is part of MVP.
- Product import starts in platform backend but must support future merchant
  rollout.
- First Mabang-like integration scope is order and logistics only.

## Technical Direction

- Backend framework: Swift Vapor.
- First architecture shape: modular monolith.
- Database direction: PostgreSQL for new Vapor-first build unless compatibility
  needs force MySQL.
- Queue direction: Redis-backed queues when async foundation is introduced.
- Payment direction: Stripe-first via provider protocol.
- Fulfillment direction: adapter-based integration.
- Admin frontend direction: API-first frontend, not server-side business logic.

## Affected Files

- `ai_dev/PROJECT_RULES.md`
- `ai_dev/PRESETS/vapor-backend/ARCHITECTURE.md`
- `ai_dev/PRESETS/cross-border-ecommerce/DOMAIN_MODEL.md`
- `ai_dev/PRESETS/cross-border-ecommerce/DATABASE_SCHEMA_INDEX.md`
- `ai_dev/PRESETS/cross-border-ecommerce/API_SIGNATURE_INDEX.md`
- `ai_dev/PRESETS/cross-border-ecommerce/INTEGRATION_MAP.md`
- `ai_dev/PRESETS/vapor-backend/SECURITY_RULES.md`
- `ai_dev/PRESETS/vapor-backend/OBSERVABILITY_RULES.md`
- `ai_dev/PRESETS/vapor-backend/TESTING_RULES.md`
- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`
- `ai_dev/TASKS/000_project_rules_and_architecture.md`

## Implementation Steps

1. Create `ai_dev/` and `ai_dev/TASKS/`.
2. Write `PROJECT_RULES.md` as the authoritative project contract.
3. Capture first-phase business line, cross-border concerns, Vapor rules,
   database rules, API rules, security rules, observability rules, and
   verification gates.
4. Write this task file so the first decision is persisted under `ai_dev/TASKS/`.
5. Expand Vapor architecture into modular monolith, DDD-lite, Clean Architecture,
   use case, repository, and provider adapter rules.
6. Create specialized index/rule documents so future tasks can update the right
   document instead of overloading `PROJECT_RULES.md`.

## Index Updates

The following indexes/rule documents were created in this task and must be kept
current by future tasks:

- `ai_dev/PRESETS/vapor-backend/ARCHITECTURE.md`
- `ai_dev/PRESETS/cross-border-ecommerce/DOMAIN_MODEL.md`
- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`
- `ai_dev/PRESETS/cross-border-ecommerce/API_SIGNATURE_INDEX.md`
- `ai_dev/PRESETS/cross-border-ecommerce/DATABASE_SCHEMA_INDEX.md`
- `ai_dev/PRESETS/cross-border-ecommerce/INTEGRATION_MAP.md`
- `ai_dev/PRESETS/vapor-backend/SECURITY_RULES.md`
- `ai_dev/PRESETS/vapor-backend/OBSERVABILITY_RULES.md`
- `ai_dev/PRESETS/vapor-backend/TESTING_RULES.md`

## Verification Gates

For this documentation-only task:

- Confirm files exist.
- Review generated content for the three requested foundations:
  - Cross-border ecommerce practices, problems, and mitigations.
  - Project-specific uniqueness.
  - Vapor/Swift service development constraints.
- Confirm no business code was created.
- Run `git status --short`.
- Run documentation keyword checks for architecture, state machine, outbox,
  RBAC, observability, and testing rules.

## Review Plan

- Review mode: architecture foundation review.
- Required reviewer focus: cross-border ecommerce risks, project-specific
  uniqueness, Vapor/backend boundaries, and whether the foundation is actionable
  for future task files.
- P0/P1 blocking criteria: unclear architecture boundary, missing first-phase
  route, no Vapor layering rule, or no documented verification gate.

## Completion Evidence

- Files changed: project rules, Vapor preset rules, ecommerce preset indexes,
  implementation map, and this task record.
- Commands run: documentation checks and git status were used during the
  original foundation pass.
- Remaining risks: final project name, database choice, target markets, and
  payment settlement scope remained open and were captured in later risk and
  decision records.

## Open Questions

- Type: later_decision
  Question: What is the final project name?
  Current default: Use neutral local/package names until the user decides.
  Owner: user
  Required before: public deployment and production naming

- Type: research_required
  Question: Is production database definitely PostgreSQL, or must it remain
  compatible with an ECShopX/MySQL migration path?
  Current default: PostgreSQL for Vapor-first build.
  Owner: user / technical decision
  Required before: production-intended migrations

- Type: later_decision
  Question: What is the preferred admin frontend stack?
  Current default: API-first backend contracts independent from frontend stack.
  Owner: user / technical decision
  Required before: admin frontend implementation

- Type: blocker
  Question: What are the first target sales markets?
  Current default: Keep country/tax/compliance model extensible.
  Owner: user / business
  Required before: production sales launch

- Type: research_required
  Question: Is Stripe Connect required for merchant settlement, or does v1 only
  need platform-collected payments?
  Current default: platform-collected payments for v1 planning.
  Owner: user / business
  Required before: real payment settlement implementation
