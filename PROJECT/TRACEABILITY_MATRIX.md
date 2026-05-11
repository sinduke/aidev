# Traceability Matrix

## 1. Purpose

This document maps first-phase business goals to domain concepts, database
schema, APIs, use cases, security, observability, and tests.

It ensures the project can move from business intent to implementation without
losing coverage.

For feature-level execution details, use `FEATURE_MAP.md`. For API, function,
DTO, permission, state machine, and test contract details, use the specialized
project indexes.

## 2. Status Values

- `planned`
- `in_progress`
- `implemented`
- `verified`
- `deferred`

## 3. First-Phase Business Line Coverage

| Business Goal | Domain | Database | API | Use Cases | Security | Observability | Tests | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Platform admin creates merchant/account/role | Merchant, User, RBAC, Audit | merchants, user_accounts, roles, permissions | Admin auth/merchant/RBAC APIs | CreateMerchant, UpdateMerchantStatus, AssignRole | platform_admin permissions, object boundary | audit_logs, business_events | auth/RBAC/API tests | planned |
| Platform admin imports products | Import, Catalog, Merchant | import_batches, import_rows, products, product_skus | Admin import APIs | CreateImportBatch, ParseProductImport, CommitProductImport | product.import permission, upload validation | audit_logs, import events | import parser/use case tests | planned |
| Product visibility controls public/hidden exposure | Visibility, Catalog | products.visibility, product_visibility_links | Admin visibility APIs, mobile hidden detail API | UpdateProductVisibility, GenerateHiddenProductLink, ResolveProductVisibility | hidden product server-side access | product_visibility_changed, hidden_product_link_opened | visibility policy tests | planned |
| Customer views product and adds to cart | Catalog, Visibility, Cart | products, product_skus, carts, cart_items | Mobile product/cart APIs | GetProductDetail, AddCartItem | customer ownership, visibility context | product_detail_viewed, cart_item_added | mobile API/use case tests | planned |
| Customer creates order | Cart, Order, Catalog | orders, order_items, order_amounts | Mobile order APIs | CreateOrder | customer ownership, merchant boundary | order_created, order_state_transition | order state/use case tests | planned |
| Customer starts payment | Payment, Order | payments, payment_state_transitions | Mobile payment APIs | CreatePaymentIntent | customer owns order, idempotency | payment_started | payment use case tests | planned |
| Provider webhook updates payment/order | Payment, Order | payment_provider_events, payments, orders | Stripe webhook API | HandlePaymentWebhook, MarkOrderPaid | signature verification, event dedupe | payment_event, order_state_transition | webhook replay/idempotency tests | planned |
| Backend exposes admin order operations | Order, Payment, Fulfillment | orders, payments, fulfillments | Admin order/payment/fulfillment APIs | GetAdminOrderDetail, ListOrders | platform/merchant permissions | audit/request logs | admin API tests | planned |
| Backend syncs fulfillment/logistics | Fulfillment, Integration | integration_outbox, integration_attempts, fulfillments, shipments | Admin retry/manual APIs | SyncFulfillmentOrder, RetryIntegrationAttempt | service actor, admin retry permission | integration_attempt, fulfillment_synced | queue/retry tests | planned |
| Critical operations are observable | Audit, Tracking, Integration | audit_logs, business_events, request_logs, integration_attempts | Admin log APIs later | RecordAuditLog, TrackBusinessEvent | redaction, audit permissions | all event schemas | observability tests | planned |

## 4. Update Rules

Update this file when:

- A first-phase business goal is added or changed.
- A task implements part of a business goal.
- A task defers a business goal.
- Tests verify a business goal.
- A domain/API/database decision changes coverage.
- Specialized feature/API/function/data/test indexes change in a way that affects
  first-phase business coverage.

## 5. Review Checklist

Before closing a task, confirm:

- Any affected business goal row is updated.
- Domain/API/database/test coverage remains aligned.
- Status changed only when evidence exists.
- Deferred scope has a reason and follow-up path.
