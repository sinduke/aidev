# Admin Frontend Map

## 1. Purpose

This file maps the future backend management UI without choosing or forcing a
frontend stack yet.

The admin frontend must be API-first. It consumes admin APIs and must not own
business rules that belong to the backend.

## 2. Page Status Values

- `planned`
- `contracted`
- `implemented`
- `verified`
- `deferred`

## 3. Page Contract Template

```text
Page ID:
Route:
Page Name:
Actors:
Permissions:
Primary API Routes:
Primary Data Contracts:
Tables:
Forms:
Actions:
Empty/Error/Loading States:
Audit/Tracking:
Status:
```

## 4. First-Phase Admin Pages

| Page ID | Route | Name | Permission | Primary APIs | Actions | Status |
| --- | --- | --- | --- | --- | --- | --- |
| ADMIN-AUTH-001 | `/login` | Admin login | public | `API-AUTH-001` | login | planned |
| ADMIN-MERCHANT-001 | `/merchants` | Merchant list | `merchant.read` | `API-MERCHANT-001` | search/filter/open/create | planned |
| ADMIN-MERCHANT-002 | `/merchants/new` | Create merchant | `merchant.create` | `API-MERCHANT-002` | create | planned |
| ADMIN-MERCHANT-003 | `/merchants/:id` | Merchant detail | `merchant.read` | `API-MERCHANT-003`, `API-MERCHANT-004` | view/update status | planned |
| ADMIN-PRODUCT-001 | `/products` | Product list | `product.read` | `API-CATALOG-001` | search/filter/open/create | planned |
| ADMIN-PRODUCT-002 | `/products/new` | Create product | `product.create` | `API-CATALOG-002` | create | planned |
| ADMIN-PRODUCT-003 | `/products/:id` | Product detail | `product.read` | `API-CATALOG-003`, `API-CATALOG-004` | edit/status/visibility/link | planned |
| ADMIN-IMPORT-001 | `/imports/products` | Product import | `product.import` | `API-IMPORT-001` to `API-IMPORT-007` | download template/upload/parse/preview/commit | planned |
| ADMIN-ORDER-001 | `/orders` | Order list | `order.read` | `API-ORDER-ADMIN-001` | search/filter/open | planned |
| ADMIN-ORDER-002 | `/orders/:id` | Order detail | `order.read` | `API-ORDER-ADMIN-002` | view order/payment/fulfillment | planned |
| ADMIN-PAYMENT-001 | `/payments` | Payment list | `payment.read` | `API-PAYMENT-ADMIN-001` | search/filter/open | planned |
| ADMIN-PAYMENT-002 | `/payments/:id` | Payment detail | `payment.read` | `API-PAYMENT-ADMIN-002` | view events/reconciliation notes later | planned |
| ADMIN-FULFILLMENT-001 | `/fulfillments` | Fulfillment list | `fulfillment.read` | `API-FULFILLMENT-001` | search/filter/retry/manual resolution | planned |
| ADMIN-LOG-001 | `/audit-logs` | Audit logs | `audit.read` | later admin audit API | search/filter/view | planned |
| ADMIN-INTEGRATION-001 | `/integrations/attempts` | Integration attempts | `integration.read` | later/admin integration APIs | search/filter/retry/manual resolution | planned |

## 5. UI Contract Rules

- Page permissions must mirror backend permissions.
- Page route guards are not a substitute for backend authorization.
- Tables must use API pagination and allowlisted sort/filter fields.
- Forms must follow DTO validation rules from `DTO_CONTRACT_INDEX.md`.
- State-changing actions must show backend error messages from the safe API error
  envelope.
- Admin state changes should create audit logs on the backend.
- Do not create admin-only business behavior in frontend state.

## 6. Required States

Every implemented admin page should define:

- Loading state.
- Empty state.
- Permission denied state.
- Validation error state.
- API failure state.
- Success confirmation state for state-changing actions.

## 7. Review Rules

Before admin frontend implementation:

- Decide frontend stack in `DECISION_LOG.md`.
- Confirm target page exists in this map.
- Confirm API route and DTO contracts are at least `contracted`.
- Confirm permission mapping exists in `PERMISSION_INDEX.md`.
