# Project Profile

## 1. Identity

Project name: undecided

Project type:

- Backend service.
- Admin API provider.
- Mobile API provider.

Primary framework:

- Swift Vapor.

Business domain:

- Cross-border B2B2C ecommerce.

## 2. Enabled Layers

Core:

- `ai_dev/CORE/`

Presets:

- `ai_dev/PRESETS/vapor-backend/`
- `ai_dev/PRESETS/cross-border-ecommerce/`

Project overlay:

- `ai_dev/PROJECT/`

## 3. First-Phase Route

The first-phase route is:

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
-> logs/tracking/audit
```

## 4. First-Phase Task Line

```text
000_project_rules_and_architecture
000A_ai_development_workflow
000B_learning_extensions
000C_extension_governance
000D_aidev_layered_template
000E_aidev_contract_indexes
000F_git_workflow_modes
001_vapor_foundation
002_auth_rbac_audit
003_merchant_foundation
004_catalog_visibility
005_product_import
006_order_payment
007_fulfillment_integration
```

## 5. Project-Specific Uniqueness

- B2B2C platform structure.
- Merchant isolation is mandatory.
- Hidden products are first-class platform capability.
- Distribution/hidden product behavior should be plugin-friendly.
- Full tracking and operational diagnostics are MVP scope.
- Product import starts in platform backend but should support future merchant
  backend rollout.
- Stripe-first payment planning, but payment provider logic must be abstracted.
- First Mabang-like integration scope is order and logistics sync only.

## 6. Current Open Decisions

See:

- `ai_dev/PROJECT/DECISION_LOG.md`
- `ai_dev/PROJECT/RISK_REGISTER.md`
