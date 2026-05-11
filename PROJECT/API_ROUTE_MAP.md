# API Route Map

## 1. Purpose

This file is the current project's active API map. It turns planned endpoints
into concrete contracts for admin frontend, mobile API consumers, tests, and
Vapor route implementation.

The reusable domain preset may describe general API rules, but this file owns
the active endpoint contract for this project.

## 2. Route Status Values

- `planned`: route exists as a target but lacks full contract.
- `contracted`: method, path, auth, DTOs, errors, and examples are documented.
- `implemented`: Vapor route/controller exists.
- `verified`: tests or curl evidence verify the route.
- `changed`: implementation and docs need review.
- `deferred`: intentionally out of current scope.

## 3. Route Contract Template

```text
Route ID:
Surface:
Method:
Path:
Auth:
Permissions:
Object Boundary:
Request:
Response:
Error Codes:
Idempotency:
Pagination / Filtering:
Observability:
Curl Example:
Related Feature:
Related Function IDs:
Related DTO IDs:
Related Tests:
Status:
```

## 4. Route Prefixes

```text
Admin:   /api/admin/v1
Mobile:  /api/mobile/v1
Webhook: /api/webhooks
```

## 5. Foundation Routes

| Route ID | Method | Path | Auth | Request | Response | Function | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| API-FOUNDATION-001 | GET | `/health` | public | none | `HealthCheckResponse` | `FN-FOUNDATION-002` | planned |

## 6. Admin Routes

| Route ID | Method | Path | Auth | Permission | Request | Response | Function | Feature | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-AUTH-001 | POST | `/api/admin/v1/auth/login` | public | none | `AdminLoginRequest` | `AdminLoginResponse` | `FN-AUTH-001` | F-002 | planned |
| API-AUTH-002 | GET | `/api/admin/v1/auth/me` | platform_or_merchant_admin | none | none | `AdminMeResponse` | `FN-AUTH-002` | F-002 | planned |
| API-MERCHANT-001 | GET | `/api/admin/v1/merchants` | platform_admin | `merchant.read` | `MerchantListQuery` | `MerchantListResponse` | `FN-MERCHANT-003` | F-003 | planned |
| API-MERCHANT-002 | POST | `/api/admin/v1/merchants` | platform_admin | `merchant.create` | `CreateMerchantRequest` | `MerchantResponse` | `FN-MERCHANT-001` | F-003 | planned |
| API-MERCHANT-003 | GET | `/api/admin/v1/merchants/:id` | platform_or_merchant_admin | `merchant.read` | path `id` | `MerchantResponse` | `FN-MERCHANT-004` | F-003 | planned |
| API-MERCHANT-004 | PATCH | `/api/admin/v1/merchants/:id/status` | platform_admin | `merchant.status.update` | `UpdateMerchantStatusRequest` | `MerchantResponse` | `FN-MERCHANT-002` | F-003 | planned |
| API-CATALOG-001 | GET | `/api/admin/v1/products` | platform_or_merchant_admin | `product.read` | `ProductListQuery` | `ProductListResponse` | `FN-CATALOG-005` | F-004 | planned |
| API-CATALOG-002 | POST | `/api/admin/v1/products` | platform_or_merchant_admin | `product.create` | `CreateProductRequest` | `ProductResponse` | `FN-CATALOG-001` | F-004 | planned |
| API-CATALOG-003 | GET | `/api/admin/v1/products/:id` | platform_or_merchant_admin | `product.read` | path `id` | `ProductResponse` | `FN-CATALOG-006` | F-004 | planned |
| API-CATALOG-004 | PATCH | `/api/admin/v1/products/:id` | platform_or_merchant_admin | `product.update` | `UpdateProductRequest` | `ProductResponse` | `FN-CATALOG-002` | F-004 | planned |
| API-CATALOG-005 | PATCH | `/api/admin/v1/products/:id/status` | platform_or_merchant_admin | `product.status.update` | `UpdateProductStatusRequest` | `ProductResponse` | `FN-CATALOG-003` | F-004 | planned |
| API-CATALOG-006 | PATCH | `/api/admin/v1/products/:id/visibility` | platform_or_merchant_admin | `product.visibility.update` | `UpdateProductVisibilityRequest` | `ProductResponse` | `FN-VISIBILITY-001` | F-004 | planned |
| API-CATALOG-007 | POST | `/api/admin/v1/products/:id/visibility-links` | platform_or_merchant_admin | `product.visibility.link.create` | `CreateHiddenProductLinkRequest` | `HiddenProductLinkResponse` | `FN-VISIBILITY-002` | F-004 | planned |
| API-IMPORT-001 | GET | `/api/admin/v1/imports/product-template` | platform_or_merchant_admin | `product.import` | `ProductImportTemplateQuery` | file/metadata response | `FN-IMPORT-001` | F-005 | planned |
| API-IMPORT-002 | POST | `/api/admin/v1/imports/product-batches` | platform_or_merchant_admin | `product.import` | `CreateImportBatchRequest` | `ImportBatchResponse` | `FN-IMPORT-002` | F-005 | planned |
| API-IMPORT-003 | POST | `/api/admin/v1/imports/product-batches/:id/upload` | platform_or_merchant_admin | `product.import` | multipart file | `ImportFileUploadResponse` | `FN-IMPORT-003` | F-005 | planned |
| API-IMPORT-004 | POST | `/api/admin/v1/imports/product-batches/:id/parse` | platform_or_merchant_admin | `product.import` | path `id` | `ImportBatchResponse` | `FN-IMPORT-004` | F-005 | planned |
| API-IMPORT-005 | GET | `/api/admin/v1/imports/product-batches/:id/preview` | platform_or_merchant_admin | `product.import` | path `id`, pagination | `ImportPreviewResponse` | `FN-IMPORT-005` | F-005 | planned |
| API-IMPORT-006 | POST | `/api/admin/v1/imports/product-batches/:id/commit` | platform_or_merchant_admin | `product.import` | `CommitImportBatchRequest` | `ImportBatchResponse` | `FN-IMPORT-006` | F-005 | planned |
| API-IMPORT-007 | GET | `/api/admin/v1/imports/product-batches/:id/errors` | platform_or_merchant_admin | `product.import` | path `id`, pagination | `ImportErrorListResponse` | `FN-IMPORT-007` | F-005 | planned |
| API-ORDER-ADMIN-001 | GET | `/api/admin/v1/orders` | platform_or_merchant_admin | `order.read` | `OrderListQuery` | `OrderListResponse` | `FN-ORDER-004` | F-006 | planned |
| API-ORDER-ADMIN-002 | GET | `/api/admin/v1/orders/:id` | platform_or_merchant_admin | `order.read` | path `id` | `OrderResponse` | `FN-ORDER-005` | F-006 | planned |
| API-PAYMENT-ADMIN-001 | GET | `/api/admin/v1/payments` | platform_or_merchant_admin | `payment.read` | `PaymentListQuery` | `PaymentListResponse` | `FN-PAYMENT-004` | F-007 | planned |
| API-PAYMENT-ADMIN-002 | GET | `/api/admin/v1/payments/:id` | platform_or_merchant_admin | `payment.read` | path `id` | `PaymentResponse` | `FN-PAYMENT-005` | F-007 | planned |
| API-FULFILLMENT-001 | GET | `/api/admin/v1/fulfillments` | platform_or_merchant_admin | `fulfillment.read` | `FulfillmentListQuery` | `FulfillmentListResponse` | `FN-FULFILLMENT-003` | F-008 | planned |
| API-FULFILLMENT-002 | POST | `/api/admin/v1/fulfillments/:id/retry` | platform_admin | `fulfillment.retry` | `RetryFulfillmentRequest` | `IntegrationAttemptResponse` | `FN-INTEGRATION-002` | F-008 | planned |
| API-FULFILLMENT-003 | POST | `/api/admin/v1/fulfillments/:id/manual-resolution` | platform_admin | `fulfillment.manual_resolution` | `ManualResolutionRequest` | `IntegrationAttemptResponse` | `FN-INTEGRATION-003` | F-008 | planned |

## 7. Mobile Routes

| Route ID | Method | Path | Auth | Request | Response | Function | Feature | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-MOBILE-CATALOG-001 | GET | `/api/mobile/v1/products` | public/customer | `MobileProductListQuery` | `MobileProductListResponse` | `FN-CATALOG-007` | F-004 | planned |
| API-MOBILE-CATALOG-002 | GET | `/api/mobile/v1/products/:id` | public/customer | path `id` | `MobileProductDetailResponse` | `FN-CATALOG-008` | F-004 | planned |
| API-MOBILE-CATALOG-003 | GET | `/api/mobile/v1/hidden-products/:token` | public/customer | path `token` | `MobileProductDetailResponse` | `FN-VISIBILITY-003` | F-004 | planned |
| API-MOBILE-CART-001 | GET | `/api/mobile/v1/cart` | customer | none | `CartResponse` | `FN-CART-001` | F-006 | planned |
| API-MOBILE-CART-002 | POST | `/api/mobile/v1/cart/items` | customer | `AddCartItemRequest` | `CartResponse` | `FN-CART-002` | F-006 | planned |
| API-MOBILE-CART-003 | PATCH | `/api/mobile/v1/cart/items/:id` | customer | `UpdateCartItemRequest` | `CartResponse` | `FN-CART-003` | F-006 | planned |
| API-MOBILE-CART-004 | DELETE | `/api/mobile/v1/cart/items/:id` | customer | path `id` | `CartResponse` | `FN-CART-004` | F-006 | planned |
| API-MOBILE-ORDER-001 | POST | `/api/mobile/v1/orders` | customer | `CreateOrderRequest` | `OrderResponse` | `FN-ORDER-001` | F-006 | planned |
| API-MOBILE-ORDER-002 | GET | `/api/mobile/v1/orders` | customer | `MobileOrderListQuery` | `OrderListResponse` | `FN-ORDER-002` | F-006 | planned |
| API-MOBILE-ORDER-003 | GET | `/api/mobile/v1/orders/:id` | customer | path `id` | `OrderResponse` | `FN-ORDER-003` | F-006 | planned |
| API-MOBILE-PAYMENT-001 | POST | `/api/mobile/v1/orders/:id/payments` | customer | `CreatePaymentIntentRequest` | `CreatePaymentIntentResponse` | `FN-PAYMENT-001` | F-007 | planned |
| API-MOBILE-PAYMENT-002 | GET | `/api/mobile/v1/payments/:id` | customer | path `id` | `PaymentResponse` | `FN-PAYMENT-002` | F-007 | planned |

## 8. Webhook Routes

| Route ID | Method | Path | Auth | Request | Response | Function | Feature | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| API-WEBHOOK-STRIPE-001 | POST | `/api/webhooks/stripe` | provider_webhook | raw Stripe body + signature header | provider-safe acknowledgement | `FN-PAYMENT-003` | F-007 | planned |

## 9. Required Curl Examples

Every route must gain a curl example before moving from `implemented` to
`verified`.

Curl examples belong in the route section or in a linked API examples file once
the API surface is large enough.
