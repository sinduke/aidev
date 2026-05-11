# Project Overlay Rules

## 1. Purpose

This file contains only rules specific to the current cross-border B2B2C Vapor
backend project.

Reusable workflow rules belong in `ai_dev/CORE/`.

Reusable Vapor backend rules belong in `ai_dev/PRESETS/vapor-backend/`.

Reusable cross-border ecommerce rules belong in
`ai_dev/PRESETS/cross-border-ecommerce/`.

## 2. First-Phase Scope

The first phase must build one reliable route:

```text
platform admin
-> merchant/account/role
-> product/SKU/import
-> visibility
-> mobile detail/cart
-> order
-> payment
-> admin order recognition
-> fulfillment/integration
-> observability
```

Do not attempt a complete marketplace in phase one.

## 3. Project-Specific Priorities

- Merchant isolation is a hard boundary, not a UI filter.
- Hidden product visibility must be enforced server-side.
- Distribution and hidden-product mechanics must remain plugin-friendly.
- Product import starts in platform backend for v1.
- Tracking, audit, logs, and operational diagnostics are MVP scope.
- Payment starts Stripe-first but must stay behind provider abstraction.
- First fulfillment scope is order sync and logistics sync only.

## 4. Project Task Rule

Build work must use an approved task file under `ai_dev/TASKS/`.

Source-code Build work must check `ai_dev/PROJECT/GIT_WORKFLOW.md`.

The current default branch mode is `simple`, but `feature_branch` or
`parallel_ai` may be enabled per project/task when review isolation is needed.

If implementation touches the first-phase route, update
`ai_dev/PROJECT/TRACEABILITY_MATRIX.md`.

If implementation changes current project decisions or risks, update:

- `ai_dev/PROJECT/DECISION_LOG.md`
- `ai_dev/PROJECT/RISK_REGISTER.md`

If implementation creates source files, update:

- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`
- `ai_dev/PROJECT/FILE_MAP.md`

If implementation changes feature, API, function, DTO/data, permission, state,
test, admin frontend, or config contracts, update the matching project index:

- `ai_dev/PROJECT/FEATURE_MAP.md`
- `ai_dev/PROJECT/API_ROUTE_MAP.md`
- `ai_dev/PROJECT/FUNCTION_SIGNATURE_INDEX.md`
- `ai_dev/PROJECT/DTO_CONTRACT_INDEX.md`
- `ai_dev/PROJECT/PERMISSION_INDEX.md`
- `ai_dev/PROJECT/STATE_MACHINE_INDEX.md`
- `ai_dev/PROJECT/TEST_VERIFICATION_MATRIX.md`
- `ai_dev/PROJECT/ADMIN_FRONTEND_MAP.md`
- `ai_dev/PROJECT/CONFIG_ENV_INDEX.md`

## 5. Project Open Questions

Current open questions are tracked in:

- `ai_dev/PROJECT/RISK_REGISTER.md`

Do not silently decide:

- Final project name.
- Production database if ECShopX/MySQL compatibility becomes mandatory.
- First target sales markets.
- Stripe Connect vs platform-collected payment settlement.
- Admin frontend stack.
