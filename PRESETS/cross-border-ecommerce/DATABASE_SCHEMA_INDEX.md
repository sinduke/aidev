# Database Schema Index

## 1. Purpose

This document tracks planned and implemented database schemas. It must be updated
whenever a task adds, changes, or removes a table, column, index, constraint, or
migration.

No database-related implementation is complete until this document is updated.

## 2. Database Direction

Default database for a new Vapor-first build:

- PostgreSQL.

Compatibility exception:

- MySQL may be chosen only through an approved task when ECShopX migration or
  operational compatibility requires it.

## 3. General Conventions

- Table names use `snake_case` plural nouns.
- Column names use `snake_case`.
- Primary keys use UUID unless a task documents a reason to use another type.
- Business tables include `created_at` and `updated_at`.
- Audit-sensitive tables include actor/source fields.
- Merchant-owned tables include `merchant_id` or an equivalent ownership path.
- Amounts use integer minor units plus currency code.
- Status fields use controlled enum strings.
- Avoid hard deletes for business-critical records.
- Sensitive provider credentials must not be stored in plain text.

## 4. Migration Rules

Migration naming:

```text
Create<BusinessConcept>Tables
Add<Field>To<Table>
Backfill<BusinessConcept><Reason>
```

Examples:

```text
CreateOrderTables
CreatePaymentTables
AddVisibilityToProducts
BackfillProductMerchantOwnership
```

Rules:

- Every migration must have a clear owner module.
- Every migration must be reversible unless an approved task documents why not.
- Migrations must not depend on production-only data assumptions.
- Destructive migrations require explicit approval and rollback notes.
- Seed/test fixture data must be separate from schema migrations.

## 5. Required Constraints

Use database constraints to protect invariants where practical.

Required patterns:

- Unique provider webhook event IDs.
- Unique idempotency keys within operation scope.
- Merchant-scoped unique SKU codes when SKU codes are merchant-owned.
- Foreign keys for ownership and core relations.
- Indexes on `merchant_id`, `customer_id`, `order_id`, provider IDs, state, and
  created timestamps where list/filter queries need them.

Do not rely only on application code for uniqueness or ownership constraints.

## 6. Transaction Rules

Use transactions for:

- Order creation and order item snapshot creation.
- Product import commit.
- Payment event insert plus payment/order state update.
- Refund creation plus payment/order adjustment.
- Fulfillment outbox creation after payment/order state change.

Do not call external providers inside a database transaction unless an approved
task documents why it is safe.

## 7. Concurrency Rules

Inventory and payment operations require concurrency control.

Allowed approaches:

- Atomic SQL update with condition.
- Row lock in transaction.
- Version column optimistic locking.

Required examples:

- Stock cannot go negative.
- Duplicate webhook events cannot change state twice.
- Duplicate order creation with the same idempotency key must return the prior
  result.

## 8. Planned Table Groups

Status values:

- `planned`: documented but not implemented.
- `implemented`: migration exists.
- `changed`: implemented but needs doc/code review.

### 8.1 Auth/User/RBAC

Planned tables:

- `user_accounts`: platform admins, merchant admins, customers, service actors.
- `auth_credentials`: password hash and credential metadata.
- `roles`: role definitions.
- `permissions`: permission definitions.
- `role_permissions`: role to permission mapping.
- `user_roles`: user to role mapping scoped by platform/merchant when needed.
- `auth_sessions`: optional token/session metadata.

Key constraints:

- Unique email/phone should be scoped by actor type and market rules.
- Password hash is never exposed through API responses.

### 8.2 Audit/Tracking

Planned tables:

- `audit_logs`: actor operation history.
- `request_logs`: request metadata when persisted.
- `business_events`: tracking/business analytics events.
- `order_state_transitions`: order state history.
- `payment_events`: provider/internal payment events.
- `integration_attempts`: external provider attempt history.

### 8.3 Merchant

Planned tables:

- `merchants`
- `merchant_profiles`
- `merchant_settings`
- `merchant_status_transitions`

Key constraints:

- Merchant code/name uniqueness must be defined by business requirement.
- Suspended/closed merchants remain referenced by historical orders.

### 8.4 Catalog and Visibility

Planned tables:

- `products`
- `product_skus`
- `product_media`
- `categories`
- `brands`
- `product_attributes`
- `product_market_restrictions`
- `product_visibility_links`

Key constraints:

- `products.merchant_id` required.
- `product_skus.product_id` required.
- SKU code uniqueness should usually be `(merchant_id, sku_code)`.
- Visibility links must be revocable and auditable when implemented.

### 8.5 Import

Planned tables:

- `import_batches`
- `import_files`
- `import_rows`
- `import_errors`

Key constraints:

- Import rows belong to one batch.
- Commit operation uses idempotency key or batch state guard.

### 8.6 Cart

Planned tables:

- `carts`
- `cart_items`

Key constraints:

- One active cart per customer per market/channel unless a task chooses another
  model.
- Cart items must reference product/SKU but checkout must revalidate.

### 8.7 Order

Planned tables:

- `orders`
- `order_items`
- `order_addresses`
- `order_amounts`
- `order_state_transitions`

Key constraints:

- Order number unique.
- Customer and merchant ownership indexed.
- Order item snapshots must not depend on current product data.

### 8.8 Payment and Refund

Planned tables:

- `payments`
- `payment_provider_events`
- `payment_state_transitions`
- `refunds`
- `refund_state_transitions`

Key constraints:

- Unique `(provider, provider_payment_id)` when provider ID exists.
- Unique `(provider, provider_event_id)` for webhook events.
- Unique idempotency key within payment operation scope.

### 8.9 Fulfillment and Logistics

Planned tables:

- `fulfillments`
- `shipments`
- `shipment_items`
- `logistics_events`

Key constraints:

- Fulfillment belongs to order/merchant.
- Logistics status history is append-only where possible.

### 8.10 Integration

Planned tables:

- `integration_configs`
- `integration_outbox`
- `integration_inbox`
- `integration_attempts`
- `integration_dead_letters`

Key constraints:

- Outbox records must be idempotent by business object and operation.
- Inbox records must deduplicate provider events.

## 9. Raw SQL Rules

Raw SQL is allowed for:

- Reporting.
- Aggregates.
- Lock-sensitive operations.
- Bulk import operations.
- Queries that Fluent makes unclear or inefficient.

Rules:

- Keep raw SQL centralized under infrastructure.
- Add tests for raw SQL behavior.
- Document raw SQL usage in this file or `IMPLEMENTATION_MAP.md`.

## 10. Schema Review Checklist

Before merging schema work, confirm:

- Owner module is clear.
- Indexes match expected list/filter queries.
- Merchant/customer ownership is enforceable.
- Idempotency and provider event uniqueness are protected.
- Status fields match `DOMAIN_MODEL.md`.
- Migrations are reversible or exceptions are documented.
- API and integration indexes are updated when schema changes affect them.
