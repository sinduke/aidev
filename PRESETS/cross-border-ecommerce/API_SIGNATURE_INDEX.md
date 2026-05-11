# API Signature Index

## 1. Purpose

This document tracks API surfaces, route signatures, DTOs, auth requirements,
pagination, error codes, and curl examples.

Every new or changed endpoint must update this file.

For the current project's active route-by-route contract, also update
`ai_dev/PROJECT/API_ROUTE_MAP.md`.

## 2. API Surfaces

Default route prefixes:

```text
/api/admin/v1/...
/api/mobile/v1/...
/api/webhooks/...
```

Surfaces:

- Admin API: platform and merchant management.
- Mobile API: customer-facing app APIs.
- Webhook API: provider callbacks.
- Internal API: only through approved task.

## 3. Response Envelope

Default success:

```json
{
  "success": true,
  "data": {},
  "requestId": "req_xxx"
}
```

Default error:

```json
{
  "success": false,
  "error": {
    "code": "ORDER_NOT_FOUND",
    "message": "Order not found"
  },
  "requestId": "req_xxx"
}
```

List response:

```json
{
  "success": true,
  "data": {
    "items": [],
    "pagination": {
      "page": 1,
      "pageSize": 20,
      "total": 0
    }
  },
  "requestId": "req_xxx"
}
```

Mobile cursor responses may use `nextCursor` when a task documents the reason.

## 4. Auth Labels

Each endpoint must declare one of:

- `public`
- `customer`
- `platform_admin`
- `merchant_admin`
- `platform_or_merchant_admin`
- `provider_webhook`
- `service_internal`

Admin endpoints must also list required permissions.

## 5. DTO Rules

- Request DTOs live under module API DTO folders.
- Response DTOs live under module API DTO folders.
- Admin and mobile DTOs should not be forced to share shapes.
- Webhook DTOs are provider-specific.
- DTOs must not expose Fluent models directly.
- DTOs must not include secrets, hashes, internal tokens, or unsafe provider raw
  payloads.

## 6. Error Code Registry

Error codes use uppercase snake case.

Initial categories:

- `AUTH_REQUIRED`
- `AUTH_INVALID_CREDENTIALS`
- `AUTH_FORBIDDEN`
- `RBAC_PERMISSION_DENIED`
- `MERCHANT_NOT_FOUND`
- `MERCHANT_SUSPENDED`
- `PRODUCT_NOT_FOUND`
- `PRODUCT_NOT_VISIBLE`
- `PRODUCT_NOT_PURCHASABLE`
- `SKU_NOT_FOUND`
- `SKU_OUT_OF_STOCK`
- `IMPORT_BATCH_NOT_FOUND`
- `IMPORT_BATCH_INVALID_STATE`
- `ORDER_NOT_FOUND`
- `ORDER_INVALID_STATE`
- `PAYMENT_NOT_FOUND`
- `PAYMENT_INVALID_STATE`
- `PAYMENT_WEBHOOK_INVALID_SIGNATURE`
- `FULFILLMENT_SYNC_FAILED`
- `INTEGRATION_PROVIDER_UNAVAILABLE`
- `VALIDATION_FAILED`
- `IDEMPOTENCY_CONFLICT`
- `RATE_LIMITED`
- `INTERNAL_ERROR`

New errors must be registered here before use.

## 7. Pagination and Filtering

Admin list endpoints:

- `page`
- `pageSize`
- `sort`
- explicit filter names

Mobile list endpoints:

- `page`/`pageSize` for simple lists.
- `cursor`/`limit` only when infinite scrolling or feed behavior requires it.

Rules:

- Avoid unbounded lists.
- Maximum page size must be enforced.
- Sort fields must be allowlisted.
- Filter names must map to indexed columns or documented query strategies when
  used on large tables.

## 8. Planned Admin Endpoints

Status values:

- `planned`
- `implemented`
- `changed`

### Auth

- `POST /api/admin/v1/auth/login`
  - Auth: `public`
  - Request: `AdminLoginRequest`
  - Response: `AdminLoginResponse`
  - Status: `planned`

- `GET /api/admin/v1/auth/me`
  - Auth: `platform_or_merchant_admin`
  - Response: `AdminMeResponse`
  - Status: `planned`

### Merchant

- `GET /api/admin/v1/merchants`
- `POST /api/admin/v1/merchants`
- `GET /api/admin/v1/merchants/:id`
- `PATCH /api/admin/v1/merchants/:id/status`

Status: `planned`

### Catalog and Visibility

- `GET /api/admin/v1/products`
- `POST /api/admin/v1/products`
- `GET /api/admin/v1/products/:id`
- `PATCH /api/admin/v1/products/:id`
- `PATCH /api/admin/v1/products/:id/status`
- `PATCH /api/admin/v1/products/:id/visibility`
- `POST /api/admin/v1/products/:id/visibility-links`

Status: `planned`

### Import

- `GET /api/admin/v1/imports/product-template`
- `POST /api/admin/v1/imports/product-batches`
- `POST /api/admin/v1/imports/product-batches/:id/upload`
- `POST /api/admin/v1/imports/product-batches/:id/parse`
- `GET /api/admin/v1/imports/product-batches/:id/preview`
- `POST /api/admin/v1/imports/product-batches/:id/commit`
- `GET /api/admin/v1/imports/product-batches/:id/errors`

Status: `planned`

### Order, Payment, Fulfillment

- `GET /api/admin/v1/orders`
- `GET /api/admin/v1/orders/:id`
- `GET /api/admin/v1/payments`
- `GET /api/admin/v1/payments/:id`
- `GET /api/admin/v1/fulfillments`
- `POST /api/admin/v1/fulfillments/:id/retry`
- `POST /api/admin/v1/fulfillments/:id/manual-resolution`

Status: `planned`

## 9. Planned Mobile Endpoints

### Catalog

- `GET /api/mobile/v1/products`
- `GET /api/mobile/v1/products/:id`
- `GET /api/mobile/v1/hidden-products/:token`

Status: `planned`

### Cart and Order

- `GET /api/mobile/v1/cart`
- `POST /api/mobile/v1/cart/items`
- `PATCH /api/mobile/v1/cart/items/:id`
- `DELETE /api/mobile/v1/cart/items/:id`
- `POST /api/mobile/v1/orders`
- `GET /api/mobile/v1/orders`
- `GET /api/mobile/v1/orders/:id`

Status: `planned`

### Payment

- `POST /api/mobile/v1/orders/:id/payments`
- `GET /api/mobile/v1/payments/:id`

Status: `planned`

## 10. Planned Webhook Endpoints

- `POST /api/webhooks/stripe`
  - Auth: `provider_webhook`
  - Signature verification: required.
  - Status: `planned`

## 11. Curl Requirement

Every implemented endpoint must include at least one curl example before the task
is considered complete.

Curl examples must include:

- Method.
- URL.
- Headers.
- Request body when applicable.
- Auth header when required.
- Expected success/error notes.

## 12. Review Checklist

Before adding or changing an endpoint, confirm:

- API surface is correct.
- Auth label and permissions are declared.
- Request/response DTOs are documented.
- Error codes are registered.
- Pagination/filtering is documented for lists.
- Curl example is included.
- Database and domain docs are updated if behavior changed.
