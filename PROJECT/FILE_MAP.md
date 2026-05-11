# File Map

## 1. Purpose

This file is the path-level source file map for the current project.

`IMPLEMENTATION_MAP.md` explains architecture placement and implemented source
coverage. `FILE_MAP.md` is the more mechanical inventory that future AI agents
should update whenever files are created, moved, or deleted.

## 2. Current Status

Status: documentation foundation only.

No Vapor source files exist yet.

## 3. Source File Record Template

```text
Path:
Module:
Layer:
Kind:
Owner Task:
Public Symbols:
Depends On:
Referenced By:
Related API Routes:
Related Function IDs:
Related DTO IDs:
Related Tables:
Related Tests:
Status:
Notes:
```

## 4. Planned Source Roots

```text
Sources/App/
Sources/App/Foundation/
Sources/App/Modules/
Tests/AppTests/
```

## 5. Planned Layer Roots

| Path Pattern | Layer | Rule |
| --- | --- | --- |
| `Sources/App/Foundation/` | Foundation | Shared app bootstrap, config, response, errors, middleware, test helpers. |
| `Sources/App/Modules/<Module>/API/` | API | Routes, controllers, request/response DTOs. |
| `Sources/App/Modules/<Module>/Application/` | Application | Use cases and workflow services. |
| `Sources/App/Modules/<Module>/Domain/` | Domain | Entities, value objects, rules, policies, repository/provider protocols. |
| `Sources/App/Modules/<Module>/Infrastructure/` | Infrastructure | Fluent models, migrations, repository/provider implementations, external clients. |
| `Tests/AppTests/` | Tests | Unit, API, repository, integration, and workflow tests. |

## 6. Planned Module Roots

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

## 7. Current Source File Inventory

No application source files are implemented.

When source files are created, add records here and update
`IMPLEMENTATION_MAP.md`.
