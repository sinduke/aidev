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

## 8. Current Tooling File Inventory

These are aidev template tooling files, not Vapor application source files.

```text
Path: bin/aidev
Module: aidev tooling
Layer: CLI
Kind: shell wrapper
Owner Task: 000G_aidev_validation_tooling
Public Symbols: aidev check command entrypoint
Depends On: tools/aidev_check.py, python3
Referenced By: README.md, .github/workflows/aidev-check.yml
Related API Routes: none
Related Function IDs: none
Related DTO IDs: none
Related Tables: none
Related Tests: ./bin/aidev check
Status: implemented
Notes: Generic wrapper; no project-specific business logic.

Path: tools/aidev_check.py
Module: aidev tooling
Layer: Validator
Kind: Python script
Owner Task: 000G_aidev_validation_tooling
Public Symbols: check command, task/index/git/source validation functions
Depends On: Python standard library, git command when available
Referenced By: bin/aidev, .github/workflows/aidev-check.yml
Related API Routes: none
Related Function IDs: none
Related DTO IDs: none
Related Tables: none
Related Tests: python3 -m py_compile tools/aidev_check.py; ./bin/aidev check
Status: implemented
Notes: Checks Markdown workflow contracts and basic source map drift.

Path: .github/workflows/aidev-check.yml
Module: aidev tooling
Layer: CI
Kind: GitHub Actions workflow
Owner Task: 000G_aidev_validation_tooling
Public Symbols: aidev-check job
Depends On: bin/aidev
Referenced By: GitHub pull_request and main push events
Related API Routes: none
Related Function IDs: none
Related DTO IDs: none
Related Tables: none
Related Tests: git diff --check; ./bin/aidev check
Status: implemented
Notes: Generic workflow validation.

Path: .github/workflows/vapor-ci.yml
Module: aidev tooling
Layer: CI
Kind: GitHub Actions workflow
Owner Task: 000G_aidev_validation_tooling
Public Symbols: vapor-ci job
Depends On: Package.swift when present, swift-actions/setup-swift
Referenced By: GitHub pull_request and main push events
Related API Routes: none
Related Function IDs: none
Related DTO IDs: none
Related Tables: none
Related Tests: swift build; swift test
Status: implemented
Notes: Conditional; skips when Package.swift is absent.
```
