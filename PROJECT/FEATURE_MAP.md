# Feature Map

## 1. Purpose

This file is the current project's feature-level map. It connects business
capabilities to APIs, use cases, data contracts, database tables, permissions,
observability, tests, and tasks.

Use this when deciding what to build next and when reviewing whether a task
actually advanced the first-phase route.

## 2. Status Values

- `planned`
- `contracted`
- `in_progress`
- `implemented`
- `verified`
- `deferred`
- `superseded`

## 3. Feature Contract Template

```text
Feature ID:
Name:
Business Goal:
Primary Actor:
Owning Modules:
Dependencies:
API Routes:
Use Cases / Functions:
DTO/Data Contracts:
Database:
Permissions:
State Machines:
Integrations:
Observability:
Tests:
Related Tasks:
Status:
```

## 4. First-Phase Feature Map

| Feature ID | Name | Actor | Modules | Key APIs | Key Use Cases | Data | Permissions | Events | Task | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | Vapor foundation | system/admin | Foundation | Health check | ConfigureApplication, GetHealthStatus | HealthCheckResponse | none | request_log | 001_vapor_foundation | planned |
| F-002 | Admin auth, RBAC, audit | platform_admin, merchant_admin | Auth, User, RBAC, Audit | Admin auth APIs | AdminLogin, GetAdminMe, AssignRole, RecordAuditLog | AdminLoginRequest, AdminLoginResponse, AdminMeResponse | auth.*, rbac.*, audit.read | admin_login_succeeded, audit_recorded | 002_auth_rbac_audit | planned |
| F-003 | Merchant foundation | platform_admin, merchant_admin | Merchant, User, RBAC, Audit | Admin merchant APIs | CreateMerchant, UpdateMerchantStatus, GetMerchantDetail | MerchantCreateRequest, MerchantResponse | merchant.* | merchant_created, merchant_status_changed | 003_merchant_foundation | planned |
| F-004 | Catalog visibility | platform_admin, merchant_admin, customer | Catalog, Visibility | Admin product APIs, mobile product APIs | CreateProduct, GetProductDetail, UpdateProductVisibility, GenerateHiddenProductLink | ProductResponse, ProductVisibilityUpdateRequest, HiddenProductLinkResponse | product.*, product.visibility.update | product_visibility_changed, hidden_product_link_opened | 004_catalog_visibility | planned |
| F-005 | Product import | platform_admin | Import, Catalog, Merchant | Admin import APIs | CreateImportBatch, UploadImportFile, ParseProductImport, CommitProductImport | ImportBatchResponse, ImportPreviewResponse, ImportErrorResponse | product.import | import_created, import_committed | 005_product_import | planned |
| F-006 | Cart and order | customer | Cart, Order, Catalog, Visibility | Mobile cart/order APIs | AddCartItem, CreateOrder, GetOrderDetail | CartResponse, AddCartItemRequest, CreateOrderRequest, OrderResponse | customer ownership | cart_item_added, order_created, order_state_transition | 006_order_payment | planned |
| F-007 | Payment | customer, provider_webhook, platform_admin | Payment, Order | Mobile payment APIs, Stripe webhook | CreatePaymentIntent, HandlePaymentWebhook, MarkOrderPaid | CreatePaymentIntentResponse, PaymentResponse, StripeWebhookEvent | payment.read, payment.reconcile | payment_started, payment_event, payment_succeeded | 006_order_payment | planned |
| F-008 | Fulfillment integration | service, platform_admin | Fulfillment, Integration, Order | Admin fulfillment APIs | SyncFulfillmentOrder, RetryIntegrationAttempt, MarkIntegrationResolved | FulfillmentResponse, IntegrationAttemptResponse | fulfillment.retry, integration.read | fulfillment_synced, integration_attempt_failed | 007_fulfillment_integration | planned |
| F-009 | Observability baseline | system, platform_admin | Audit, Tracking, Integration | Admin log APIs later | TrackBusinessEvent, RecordAuditLog, RecordIntegrationAttempt | AuditLogResponse, BusinessEventRecord | audit.read | all critical business events | 001-007 | planned |
| F-010 | Admin frontend map | platform_admin, merchant_admin | Admin UI, API consumers | Admin pages consume admin APIs | Render list/detail/form pages, submit API actions | Page contracts, table/form schemas | page permission mirrors API permission | page_viewed, admin_action_submitted | later admin task | planned |

## 5. Update Rules

Update this file when:

- A new first-phase feature is added or removed.
- A task changes the feature's API, use cases, permissions, data, events, or tests.
- A feature moves between statuses.
- A feature is intentionally deferred.

Do not mark a feature `implemented` without source files and updated indexes.
Do not mark a feature `verified` without test or verification evidence in
`TEST_VERIFICATION_MATRIX.md`.
