# Index Registry

## 1. Purpose

This file defines the generic index system every AI_DEV project should use.

Core defines index types and review expectations. Project-specific values belong
under `ai_dev/PROJECT/`. Framework or domain presets may add reusable guidance,
but the current project owns the active contracts.

## 2. Contract Levels

Use these levels for every indexed item:

| Level | Meaning | Allowed Use |
| --- | --- | --- |
| L0 planned | Name or intent is known, but contract is not stable. | Exploration and early planning. |
| L1 contracted | Inputs, outputs, ownership, and boundaries are documented. | Task decomposition and code generation. |
| L2 implemented | Source code exists and maps to the contract. | Build review. |
| L3 verified | Tests or verification evidence prove the contract. | Task close and release confidence. |

Build tasks should not create public API, shared functions, schema, permissions,
or integration behavior from L0 only. Move the affected item to L1 first or in
the same approved task.

## 3. Required Index Types

Every project should have these active indexes, even if some begin as empty
templates:

| Index Type | Generic Purpose | Typical Owner |
| --- | --- | --- |
| Project profile | Project identity, active layers, first-phase route. | `PROJECT/PROJECT_PROFILE.md` |
| Feature map | Feature IDs, business value, dependencies, lifecycle status. | `PROJECT/FEATURE_MAP.md` |
| File map | Source files and ownership by layer/module. | `PROJECT/FILE_MAP.md` or implementation map |
| Implementation map | Implemented files and architecture placement. | `PROJECT/IMPLEMENTATION_MAP.md` |
| API route map | Endpoints, auth, permissions, DTO links, errors, examples. | `PROJECT/API_ROUTE_MAP.md` |
| Function signature index | Public use case/service/repository/provider function contracts. | `PROJECT/FUNCTION_SIGNATURE_INDEX.md` |
| DTO/data contract index | Request/response/input/result field contracts. | `PROJECT/DTO_CONTRACT_INDEX.md` |
| Database schema index | Tables, columns, indexes, migrations, constraints. | Project or domain preset |
| Permission index | Permission codes, roles, endpoint mapping, object boundary policy. | `PROJECT/PERMISSION_INDEX.md` |
| State machine index | States, transitions, triggers, guards, side effects. | `PROJECT/STATE_MACHINE_INDEX.md` |
| Integration map | Provider protocols, adapters, retry, idempotency, attempts. | Project or domain preset |
| Config/env index | Environment variables, defaults, secret handling. | `PROJECT/CONFIG_ENV_INDEX.md` |
| Test verification matrix | Feature-to-test and command coverage. | `PROJECT/TEST_VERIFICATION_MATRIX.md` |
| Traceability matrix | Business goal to domain/data/API/test coverage. | `PROJECT/TRACEABILITY_MATRIX.md` |
| Decision log | Durable decisions and consequences. | `PROJECT/DECISION_LOG.md` |
| Risk register | Open risks, assumptions, blockers, deferred decisions. | `PROJECT/RISK_REGISTER.md` |

## 4. Minimum Fields by Index Type

### Feature

- Feature ID.
- Name.
- Business goal.
- Actor.
- Owning module.
- API routes.
- Use cases/functions.
- Data contracts.
- Database tables.
- Permissions.
- Observability events.
- Tests.
- Status.
- Related task.

### File

- Path.
- Module.
- Layer.
- Owner task.
- Public symbols.
- Depends on.
- Referenced by.
- Status.

### API Route

- Route ID.
- Method and path.
- Surface.
- Auth label.
- Required permission.
- Object boundary policy.
- Request DTO.
- Response DTO.
- Error codes.
- Idempotency key requirement.
- Pagination/filtering.
- Curl/example requirement.
- Status.

### Function Signature

- Function ID.
- Module.
- Layer.
- Symbol.
- File path.
- Swift signature or planned signature.
- Parameters.
- Return type.
- Throws/errors.
- Side effects.
- Transaction boundary.
- Authorization/idempotency requirements.
- Observability.
- Tests.
- Status.

### DTO/Data Contract

- DTO ID.
- Direction: request, response, internal input, internal result, provider payload.
- Owner API/function.
- Fields with name, type, required, validation, default, sensitivity.
- Example JSON or Swift shape when useful.
- Version/status.

### Permission

- Permission code.
- Actor types.
- Endpoint/function usage.
- Object boundary policy.
- Seed role mapping.
- Negative test requirement.

### State Machine

- State machine ID.
- States.
- Transition from/to.
- Trigger.
- Guard.
- Side effects.
- Audit/tracking event.
- Error on invalid transition.
- Tests.

## 5. Update Rules

Update indexes in the same task when:

- An endpoint is added, removed, or changed.
- A public DTO or internal use case input/result changes.
- A public use case/service/repository/provider function changes.
- A source file is created, moved, or deleted.
- A table, column, index, constraint, or migration changes.
- A permission, role, or object boundary rule changes.
- A state transition or invariant changes.
- A provider operation, retry policy, or idempotency rule changes.
- A new environment variable or secret is introduced.
- A test gate is added, removed, or skipped.

## 6. Review Rules

Review mode should treat missing contract indexes as findings:

- P1 when code changed a critical path without updating API/function/data/schema
  contracts.
- P1 when auth, permission, merchant boundary, payment, order, fulfillment, or
  webhook behavior is missing from the relevant index.
- P2 when a non-critical source file or DTO is missing from an index.
- P3 when naming/status metadata is stale but behavior remains clear.

## 7. Reuse Boundary

Core must not define current project endpoint paths, ecommerce table fields,
Vapor-specific signatures, or provider names.

Core may define the required shape of indexes. Projects and presets fill the
content.
