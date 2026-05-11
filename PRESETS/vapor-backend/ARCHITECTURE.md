# Architecture Rules

## 1. Purpose

This document defines the backend architecture for the Vapor service.

The project uses a modular monolith with DDD-lite and Clean Architecture. The
goal is not academic purity. The goal is to keep business rules, persistence,
HTTP APIs, and external providers separated enough for long-term ecommerce
growth.

## 2. Architecture Style

The architecture is:

- Modular Monolith
- DDD-lite
- Clean Architecture
- Repository Pattern
- Provider Adapter Pattern
- Explicit dependency injection

This means:

- Deploy one Vapor application in phase one.
- Keep modules independent in code.
- Put business concepts in domain code.
- Put workflows in application use cases.
- Put Vapor controllers/routes in API.
- Put Fluent, SQL, Redis, file storage, Stripe, Mabang, and other clients in
  infrastructure.

## 3. Source Layout

Default module layout:

```text
Sources/App/Modules/<Module>/
  API/
    Controllers/
    Routes/
    DTOs/
  Application/
    UseCases/
    Services/
  Domain/
    Entities/
    Rules/
    Policies/
    Repositories/
  Infrastructure/
    Persistence/
    Providers/
    External/
  <Module>Module.swift
```

Example:

```text
Sources/App/Modules/Order/
  API/
    Controllers/
      AdminOrderController.swift
      MobileOrderController.swift
    Routes/
      AdminOrderRoutes.swift
      MobileOrderRoutes.swift
    DTOs/
      CreateOrderRequest.swift
      OrderResponse.swift
  Application/
    UseCases/
      CreateOrder.swift
      CancelOrder.swift
      MarkOrderPaid.swift
    Services/
      OrderPricingService.swift
  Domain/
    Entities/
      Order.swift
      OrderItem.swift
    Rules/
      OrderStateMachine.swift
    Policies/
      OrderAccessPolicy.swift
    Repositories/
      OrderRepository.swift
  Infrastructure/
    Persistence/
      FluentOrderModel.swift
      FluentOrderRepository.swift
      CreateOrderTables.swift
    Providers/
    External/
  OrderModule.swift
```

## 4. Dependency Direction

Allowed direction:

```text
API -> Application -> Domain
Infrastructure -> Domain protocols
Module bootstrap -> API/Application/Infrastructure composition
```

Forbidden direction:

```text
Domain -> API
Domain -> Vapor
Domain -> Fluent
Domain -> Redis
Domain -> SQLKit
Domain -> Stripe/Mabang/other provider SDKs
Application -> Vapor Request/Response
Application -> Fluent model when avoidable
```

Domain should depend on Swift Foundation only unless an approved task documents a
specific exception.

## 5. Business Modules

Initial business modules:

- `Auth`
- `User`
- `RBAC`
- `Audit`
- `Merchant`
- `Catalog`
- `Visibility`
- `Import`
- `Cart`
- `Order`
- `Payment`
- `Refund`
- `Fulfillment`
- `Integration`
- `Tracking`

Do not create `AdminAPI` or `MobileAPI` as business modules. Admin, mobile, and
webhook APIs are route surfaces exposed by business modules.

Correct:

```text
Modules/Order/API/Controllers/AdminOrderController.swift
Modules/Order/API/Controllers/MobileOrderController.swift
Modules/Payment/API/Controllers/StripeWebhookController.swift
```

Incorrect:

```text
Modules/AdminAPI/OrderController.swift
Modules/MobileAPI/ProductController.swift
```

## 6. Module Bootstrap

Each module should own a module entrypoint:

```text
<Module>Module.swift
```

The module entrypoint may register:

- Routes.
- Migrations.
- Queue jobs.
- Repositories.
- Provider implementations.
- Module-specific configuration validation.

Module entrypoints should not contain business logic.

The application bootstrap composes modules in a predictable order. Example:

```text
Core/Foundation
Auth/User/RBAC
Audit/Tracking
Merchant
Catalog/Visibility/Import
Cart/Order
Payment/Refund
Fulfillment/Integration
```

## 7. API Layer

API layer responsibilities:

- Register routes.
- Decode request DTOs.
- Validate request shape.
- Read authentication context.
- Call application use cases.
- Convert use case output into response DTOs.
- Map domain/application errors to API errors.

API layer must not:

- Mutate Fluent models directly.
- Call external providers directly.
- Own order/payment/visibility decisions.
- Skip authorization checks.

## 8. DTO Rules

DTOs are transport objects.

- Request DTOs must not be reused as domain entities.
- Response DTOs must not expose Fluent models directly.
- Admin DTOs and mobile DTOs may be different even when they read the same
  domain concept.
- Webhook DTOs belong to the provider-specific API folder.
- Sensitive fields must be explicitly omitted or redacted.

## 9. Application Layer

Application layer owns workflows.

Prefer specific use cases:

- `CreateOrder`
- `CancelOrder`
- `CreatePaymentIntent`
- `HandlePaymentWebhook`
- `CommitProductImport`
- `PreviewProductImport`
- `SyncFulfillmentOrder`
- `RetryIntegrationAttempt`
- `GenerateHiddenProductLink`

Avoid large generic services:

- `OrderService` with unrelated methods.
- `PaymentService` containing provider, domain, and persistence code together.
- `ProductService` doing import, visibility, search, and pricing all at once.

Application services are allowed when they coordinate shared workflow helpers,
but use cases should remain the primary unit of behavior.

## 10. Domain Layer

Domain layer owns:

- Entities/value objects.
- State machines.
- Business rules.
- Invariants.
- Policies.
- Repository protocols.
- Provider protocols when the provider action is part of domain behavior.

Domain must not know:

- HTTP status codes.
- Route paths.
- Fluent schemas.
- Redis keys.
- Provider HTTP payloads.
- Environment variables.

Examples:

- `OrderStateMachine`
- `PaymentStateMachine`
- `VisibilityPolicy`
- `MerchantBoundaryPolicy`
- `ProductSaleRestrictionRule`
- `FulfillmentProvider`
- `PaymentProvider`

## 11. Infrastructure Layer

Infrastructure layer owns:

- Fluent models.
- Migrations.
- Repository implementations.
- SQLKit/raw SQL queries.
- Redis queue/job implementations.
- Provider clients.
- File/object storage.
- Email/SMS clients.
- Provider DTO mapping.

Infrastructure can depend on Vapor, Fluent, SQLKit, Redis, provider SDKs, and
HTTP clients.

Infrastructure must implement protocols defined by Domain or Application.

## 12. Repository Rules

Repository protocols live in:

```text
Domain/Repositories/
```

Repository implementations live in:

```text
Infrastructure/Persistence/
```

Repositories should expose business-oriented operations, not generic database
helpers.

Good:

```text
findOrderForUpdate(orderId:)
savePaymentEventIfNew(provider:eventId:)
listMerchantProducts(merchantId:filter:)
```

Bad:

```text
query(_ sql: String)
updateAny(table:values:)
getModelById(_:)
```

## 13. Provider Adapter Rules

Provider protocols live near the business that needs them.

Examples:

```text
Payment/Domain/Providers/PaymentProvider.swift
Fulfillment/Domain/Providers/FulfillmentProvider.swift
Integration/Domain/Providers/IntegrationProvider.swift
```

Provider implementations live in infrastructure:

```text
Payment/Infrastructure/Providers/StripePaymentProvider.swift
Fulfillment/Infrastructure/Providers/MabangFulfillmentProvider.swift
```

Every real provider should have a mock/fake implementation for tests and local
development.

## 14. Dependency Injection

Do not use global singletons for business services.

Allowed composition options:

- App extension storage for long-lived dependencies.
- Module dependency containers registered during Vapor configure/bootstrap.
- Explicit initializer injection for controllers/use cases/services.

Dependencies should be replaceable in tests.

Provider credentials must be loaded from configuration and injected, not read
from random places inside business code.

## 15. Error Handling

Domain and application layers should throw typed errors.

API layer maps typed errors to:

- HTTP status.
- API error code.
- Safe public message.
- Request ID.

Do not throw raw provider errors or SQL errors to clients.

## 16. Transactions

Transaction boundaries belong in application use cases or repository operations
where consistency is required.

Transaction candidates:

- Create order and order items.
- Confirm product import.
- Store payment event and update payment/order state.
- Create fulfillment sync outbox record.
- Apply refund and update payment/order records.

Do not make external HTTP calls inside a database transaction unless an approved
task explicitly documents why it is safe.

## 17. Route Registration

Route files should be thin and explicit.

Example:

```text
AdminOrderRoutes.register(on: app.grouped("api", "admin", "v1"))
MobileOrderRoutes.register(on: app.grouped("api", "mobile", "v1"))
StripeWebhookRoutes.register(on: app.grouped("api", "webhooks", "stripe"))
```

Routes must show:

- API surface.
- Version.
- Auth requirement.
- Controller method.

## 18. Naming Rules

Use case names should be verbs:

- `CreateOrder`
- `CancelOrder`
- `ApplyRefund`
- `SyncFulfillmentOrder`

Domain rule/policy names should describe decisions:

- `VisibilityPolicy`
- `OrderStateMachine`
- `MerchantBoundaryPolicy`

Repository names should match aggregate or business concept:

- `OrderRepository`
- `PaymentRepository`
- `ProductRepository`

Provider names should include provider:

- `StripePaymentProvider`
- `MabangFulfillmentProvider`

## 19. Anti-Patterns

Avoid:

- One huge `Service` per module.
- Controllers that directly query Fluent models.
- Domain objects importing Vapor or Fluent.
- Reusing admin DTOs for mobile APIs.
- Static helpers containing business rules.
- External provider calls inside random use cases without provider protocols.
- State changes through raw string assignment.
- Adding a new table without updating `DATABASE_SCHEMA_INDEX.md`.
- Adding an endpoint without updating `API_SIGNATURE_INDEX.md`.
- Adding a provider without updating `INTEGRATION_MAP.md`.

## 20. Review Checklist

Before approving architecture work, check:

- Is the module boundary clear?
- Does the dependency direction remain valid?
- Are use cases specific enough?
- Are domain rules separated from persistence and HTTP?
- Are provider implementations behind protocols?
- Are state transitions explicit?
- Are indexes updated?
- Are verification gates defined in the task file?
