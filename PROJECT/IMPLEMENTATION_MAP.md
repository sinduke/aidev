# Implementation Map

## 1. Purpose

This file maps implemented source files to modules and architectural layers.
It prevents the project from drifting away from `AIDEV_MANIFEST.md`, root
`PROJECT_RULES.md`, project overlay rules, and active presets.

Every task that adds, moves, or deletes source files must update this file.

## 2. Current Implementation Status

Status: documentation foundation only.

No Vapor source code exists yet.

Current files:

```text
ai_dev/AIDEV_MANIFEST.md
ai_dev/PROJECT_RULES.md
ai_dev/README.md
ai_dev/CORE/README.md
ai_dev/CORE/AI_WORKFLOW.md
ai_dev/CORE/TASK_TEMPLATE.md
ai_dev/CORE/REVIEW_RULES.md
ai_dev/CORE/INDEX_REGISTRY.md
ai_dev/CORE/GIT_WORKFLOW.md
ai_dev/CORE/EXTENSIONS/README.md
ai_dev/CORE/EXTENSIONS/GOVERNANCE.md
ai_dev/CORE/EXTENSIONS/LEARNING_LOOP.md
ai_dev/CORE/EXTENSIONS/ERROR_KNOWLEDGE_BASE.md
ai_dev/CORE/EXTENSIONS/WORKFLOW_IMPROVEMENTS.md
ai_dev/CORE/EXTENSIONS/PATTERN_LIBRARY.md
ai_dev/CORE/EXTENSIONS/templates/ERROR_REVIEW_TEMPLATE.md
ai_dev/CORE/EXTENSIONS/templates/WORKFLOW_EXTENSION_TEMPLATE.md
ai_dev/PRESETS/README.md
ai_dev/PRESETS/vapor-backend/ARCHITECTURE.md
ai_dev/PRESETS/vapor-backend/SECURITY_RULES.md
ai_dev/PRESETS/vapor-backend/OBSERVABILITY_RULES.md
ai_dev/PRESETS/vapor-backend/TESTING_RULES.md
ai_dev/PRESETS/cross-border-ecommerce/DOMAIN_MODEL.md
ai_dev/PRESETS/cross-border-ecommerce/DATABASE_SCHEMA_INDEX.md
ai_dev/PRESETS/cross-border-ecommerce/API_SIGNATURE_INDEX.md
ai_dev/PRESETS/cross-border-ecommerce/INTEGRATION_MAP.md
ai_dev/PROJECT/PROJECT_PROFILE.md
ai_dev/PROJECT/PROJECT_RULES.md
ai_dev/PROJECT/GIT_WORKFLOW.md
ai_dev/PROJECT/FEATURE_MAP.md
ai_dev/PROJECT/FILE_MAP.md
ai_dev/PROJECT/IMPLEMENTATION_MAP.md
ai_dev/PROJECT/API_ROUTE_MAP.md
ai_dev/PROJECT/FUNCTION_SIGNATURE_INDEX.md
ai_dev/PROJECT/DTO_CONTRACT_INDEX.md
ai_dev/PROJECT/PERMISSION_INDEX.md
ai_dev/PROJECT/STATE_MACHINE_INDEX.md
ai_dev/PROJECT/TEST_VERIFICATION_MATRIX.md
ai_dev/PROJECT/ADMIN_FRONTEND_MAP.md
ai_dev/PROJECT/CONFIG_ENV_INDEX.md
ai_dev/PROJECT/TRACEABILITY_MATRIX.md
ai_dev/PROJECT/DECISION_LOG.md
ai_dev/PROJECT/RISK_REGISTER.md
ai_dev/TASKS/000_project_rules_and_architecture.md
ai_dev/TASKS/000A_ai_development_workflow.md
ai_dev/TASKS/000B_learning_extensions.md
ai_dev/TASKS/000C_extension_governance.md
ai_dev/TASKS/000D_aidev_layered_template.md
ai_dev/TASKS/000E_aidev_contract_indexes.md
ai_dev/TASKS/000F_git_workflow_modes.md
```

## 3. Planned Source Roots

Expected Vapor root:

```text
Sources/App/
```

Expected test root:

```text
Tests/AppTests/
```

Expected module root:

```text
Sources/App/Modules/
```

Expected shared foundation root:

```text
Sources/App/Foundation/
```

## 4. Planned Foundation Areas

Foundation should eventually include:

- App bootstrap and module registration.
- Configuration loading.
- Database setup.
- Redis/queue setup.
- Request ID middleware.
- Error response mapping.
- API response envelope.
- Logging/redaction helpers.
- Authentication middleware.
- Permission middleware.
- Testing utilities.

Foundation code must not contain merchant/product/order/payment business rules.

## 4.1 Workflow Control Plane

Current workflow documents:

```text
ai_dev/CORE/AI_WORKFLOW.md
ai_dev/CORE/TASK_TEMPLATE.md
ai_dev/CORE/REVIEW_RULES.md
ai_dev/CORE/INDEX_REGISTRY.md
ai_dev/CORE/GIT_WORKFLOW.md
ai_dev/CORE/EXTENSIONS/README.md
ai_dev/CORE/EXTENSIONS/GOVERNANCE.md
ai_dev/CORE/EXTENSIONS/LEARNING_LOOP.md
ai_dev/CORE/EXTENSIONS/ERROR_KNOWLEDGE_BASE.md
ai_dev/CORE/EXTENSIONS/WORKFLOW_IMPROVEMENTS.md
ai_dev/CORE/EXTENSIONS/PATTERN_LIBRARY.md
```

These files control how AI agents explore, decide, decompose tasks, build,
review, close work, and learn from errors.

Project execution state lives in:

```text
ai_dev/PROJECT/GIT_WORKFLOW.md
ai_dev/PROJECT/FEATURE_MAP.md
ai_dev/PROJECT/FILE_MAP.md
ai_dev/PROJECT/API_ROUTE_MAP.md
ai_dev/PROJECT/FUNCTION_SIGNATURE_INDEX.md
ai_dev/PROJECT/DTO_CONTRACT_INDEX.md
ai_dev/PROJECT/PERMISSION_INDEX.md
ai_dev/PROJECT/STATE_MACHINE_INDEX.md
ai_dev/PROJECT/TEST_VERIFICATION_MATRIX.md
ai_dev/PROJECT/ADMIN_FRONTEND_MAP.md
ai_dev/PROJECT/CONFIG_ENV_INDEX.md
ai_dev/PROJECT/TRACEABILITY_MATRIX.md
ai_dev/PROJECT/DECISION_LOG.md
ai_dev/PROJECT/RISK_REGISTER.md
ai_dev/TASKS/
```

## 5. Planned Business Modules

Each module should follow
`ai_dev/PRESETS/vapor-backend/ARCHITECTURE.md`.

```text
Sources/App/Modules/Auth/
Sources/App/Modules/User/
Sources/App/Modules/RBAC/
Sources/App/Modules/Audit/
Sources/App/Modules/Merchant/
Sources/App/Modules/Catalog/
Sources/App/Modules/Visibility/
Sources/App/Modules/Import/
Sources/App/Modules/Cart/
Sources/App/Modules/Order/
Sources/App/Modules/Payment/
Sources/App/Modules/Refund/
Sources/App/Modules/Fulfillment/
Sources/App/Modules/Integration/
Sources/App/Modules/Tracking/
```

## 6. Module File Map Template

When a module is implemented, add entries like:

```text
Module: Order
API:
  - Sources/App/Modules/Order/API/Controllers/AdminOrderController.swift
  - Sources/App/Modules/Order/API/Routes/AdminOrderRoutes.swift
  - Sources/App/Modules/Order/API/DTOs/CreateOrderRequest.swift
Application:
  - Sources/App/Modules/Order/Application/UseCases/CreateOrder.swift
Domain:
  - Sources/App/Modules/Order/Domain/Entities/Order.swift
  - Sources/App/Modules/Order/Domain/Rules/OrderStateMachine.swift
  - Sources/App/Modules/Order/Domain/Repositories/OrderRepository.swift
Infrastructure:
  - Sources/App/Modules/Order/Infrastructure/Persistence/FluentOrderModel.swift
  - Sources/App/Modules/Order/Infrastructure/Persistence/FluentOrderRepository.swift
Module Bootstrap:
  - Sources/App/Modules/Order/OrderModule.swift
Tests:
  - Tests/AppTests/Modules/Order/CreateOrderTests.swift
```

## 7. Update Rules

Update this file when:

- A new module is created.
- A file is moved between layers.
- A use case is added.
- A provider implementation is added.
- A repository/protocol implementation is added.
- A migration is added.
- A shared foundation component is introduced.
- Workflow/control-plane documents change.
- Git workflow mode or branch policy changes.
- Any contract index under `ai_dev/PROJECT/` changes.

## 8. Review Checklist

Before completing a build task, confirm:

- Every created source file appears here.
- Every created source file appears in `FILE_MAP.md`.
- Layer placement matches `ai_dev/PRESETS/vapor-backend/ARCHITECTURE.md`.
- Tests appear under the corresponding test section.
- New database/API/integration changes are reflected in their own indexes.
