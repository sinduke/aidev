# DTO and Data Contract Index

## 1. Purpose

This file records request DTOs, response DTOs, internal use case inputs/results,
and provider boundary data shapes.

It is the contract source for admin frontend, mobile API consumers, Vapor API
implementation, tests, and AI code generation.

## 2. Contract Status Values

- `planned`
- `contracted`
- `implemented`
- `verified`
- `changed`
- `deprecated`

## 3. Field Attributes

Use this field format:

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |

Rules:

- IDs should use UUID strings in API payloads unless a task decides otherwise.
- Money uses integer minor units plus ISO currency code.
- Timestamps use ISO 8601 strings in API responses.
- Internal provider raw payloads must not leak into public DTOs.
- Sensitive fields must be explicitly marked.

## 4. Shared DTOs

### `APIResponse<T>`

Direction: response wrapper
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `success` | Bool | yes | true for success | none | no | Present on every response. |
| `data` | T | success only | DTO-specific | none | depends | Omitted on error. |
| `error` | `APIErrorDTO` | error only | DTO-specific | none | no | Omitted on success. |
| `requestId` | String | yes | non-empty | generated | no | Correlates logs/events. |

### `APIErrorDTO`

Direction: response
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `code` | String | yes | registered error code | none | no | See API error registry. |
| `message` | String | yes | safe public text | none | no | No raw SQL/provider errors. |
| `details` | Object | no | safe fields only | none | maybe | Validation details only. |

### `PaginationDTO`

Direction: response
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `page` | Int | yes | >= 1 | 1 | no | Admin pagination. |
| `pageSize` | Int | yes | within max | 20 | no | Max enforced server-side. |
| `total` | Int | yes | >= 0 | 0 | no | May be omitted only by approved cursor route. |

## 5. Foundation DTOs

### `HealthCheckResponse`

Direction: response
Routes: `API-FOUNDATION-001`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `status` | String | yes | `ok` or degraded state | none | no | Start simple. |
| `service` | String | yes | non-empty | project service name | no | Project name may change. |
| `timestamp` | String | yes | ISO 8601 | now | no | Server time. |

## 6. Auth DTOs

### `AdminLoginRequest`

Direction: request
Routes: `API-AUTH-001`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `email` | String | yes | valid email, normalized | none | PII | Phone login can be added later. |
| `password` | String | yes | non-empty, length limits | none | secret | Never log. |

### `AdminLoginResponse`

Direction: response
Routes: `API-AUTH-001`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `accessToken` | String | yes | JWT format | none | secret | Redact in logs. |
| `expiresAt` | String | yes | ISO 8601 | none | no | Token expiration. |
| `user` | `AdminUserDTO` | yes | valid user | none | PII | No password hash. |
| `permissions` | [String] | yes | permission codes | [] | no | Effective permissions. |

### `AdminMeResponse`

Direction: response
Routes: `API-AUTH-002`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `user` | `AdminUserDTO` | yes | valid user | none | PII | Current actor. |
| `merchantId` | String? | no | UUID | none | no | Present for merchant admins. |
| `roles` | [String] | yes | role codes | [] | no | Effective roles. |
| `permissions` | [String] | yes | permission codes | [] | no | Effective permissions. |

## 7. Merchant DTOs

### `CreateMerchantRequest`

Direction: request
Routes: `API-MERCHANT-002`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | String | yes | non-empty, length limit | none | no | Display name. |
| `code` | String | no | unique if provided | generated | no | Stable merchant code. |
| `contactEmail` | String | no | email | none | PII | Admin contact. |
| `status` | String | no | merchant state | `draft` | no | Usually draft. |

### `UpdateMerchantStatusRequest`

Direction: request
Routes: `API-MERCHANT-004`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `status` | String | yes | allowed merchant state | none | no | See state machine. |
| `reason` | String | yes | non-empty | none | no | Audit required. |

### `MerchantResponse`

Direction: response
Routes: merchant admin routes
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | String | yes | UUID | none | no | Merchant ID. |
| `code` | String | yes | non-empty | none | no | Merchant code. |
| `name` | String | yes | non-empty | none | no | Merchant name. |
| `status` | String | yes | merchant state | none | no | See state machine. |
| `createdAt` | String | yes | ISO 8601 | none | no | Created time. |
| `updatedAt` | String | yes | ISO 8601 | none | no | Updated time. |

## 8. Catalog and Visibility DTOs

### `ProductResponse`

Direction: response
Routes: admin product routes
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | String | yes | UUID | none | no | Product ID. |
| `merchantId` | String | yes | UUID | none | no | Ownership boundary. |
| `title` | String | yes | non-empty | none | no | Product title. |
| `status` | String | yes | selling state | none | no | Separate from visibility. |
| `visibility` | String | yes | `public` or `hidden` | `public` | no | Server enforced. |
| `skus` | [`SkuResponse`] | yes | at least one when active | [] | no | Sellable variants. |

### `UpdateProductVisibilityRequest`

Direction: request
Routes: `API-CATALOG-006`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `visibility` | String | yes | `public` or `hidden` | none | no | Search/recommendation impact. |
| `reason` | String | yes | non-empty | none | no | Audit required. |

### `HiddenProductLinkResponse`

Direction: response
Routes: `API-CATALOG-007`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `token` | String | yes | opaque, non-guessable | none | secret | Do not log raw token. |
| `url` | String | yes | valid URL/path | none | no | Mobile entry link. |
| `expiresAt` | String? | no | ISO 8601 | none | no | Optional expiration. |
| `revoked` | Bool | yes | bool | false | no | Link state. |

### `MobileProductDetailResponse`

Direction: response
Routes: mobile product detail routes
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | String | yes | UUID | none | no | Product ID. |
| `title` | String | yes | non-empty | none | no | Mobile title. |
| `visibility` | String | yes | public/hidden | none | no | May be hidden when access context is valid. |
| `purchasable` | Bool | yes | bool | false | no | Server decision. |
| `skus` | [`MobileSkuDTO`] | yes | active SKUs only | [] | no | Mobile sellable variants. |

## 9. Import DTOs

### `CreateImportBatchRequest`

Direction: request
Routes: `API-IMPORT-002`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `merchantId` | String | yes | UUID, authorized | none | no | V1 platform admin creates for merchant. |
| `templateVersion` | String | yes | supported version | current | no | Parser contract. |

### `ImportBatchResponse`

Direction: response
Routes: import routes
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | String | yes | UUID | none | no | Batch ID. |
| `merchantId` | String | yes | UUID | none | no | Ownership. |
| `state` | String | yes | import state | none | no | See state machine. |
| `totalRows` | Int | no | >= 0 | 0 | no | Parse result. |
| `errorRows` | Int | no | >= 0 | 0 | no | Validation result. |

## 10. Cart, Order, Payment DTOs

### `AddCartItemRequest`

Direction: request
Routes: `API-MOBILE-CART-002`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `productId` | String | yes | UUID | none | no | Product reference. |
| `skuId` | String | yes | UUID | none | no | SKU reference. |
| `quantity` | Int | yes | > 0, within limits | none | no | Revalidate stock. |
| `visibilityToken` | String? | no | opaque | none | secret | Required for hidden product context when applicable. |

### `CreateOrderRequest`

Direction: request
Routes: `API-MOBILE-ORDER-001`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `cartId` | String | yes | UUID, owned by customer | none | no | Source cart. |
| `shippingAddressId` | String | yes | UUID, owned by customer | none | PII | Address snapshot needed. |
| `idempotencyKey` | String | yes | unique per customer operation | none | no | Prevent duplicate orders. |

### `OrderResponse`

Direction: response
Routes: order routes
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | String | yes | UUID | none | no | Order ID. |
| `orderNumber` | String | yes | unique | none | no | Public order number. |
| `state` | String | yes | order state | none | no | See state machine. |
| `currency` | String | yes | ISO currency | none | no | Amount currency. |
| `totalAmountMinor` | Int | yes | >= 0 | none | no | Minor units. |
| `items` | [`OrderItemDTO`] | yes | snapshots | [] | no | Snapshot, not live product. |

### `CreatePaymentIntentRequest`

Direction: request
Routes: `API-MOBILE-PAYMENT-001`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `idempotencyKey` | String | yes | unique per order/payment operation | none | no | Provider and internal idempotency. |

### `CreatePaymentIntentResponse`

Direction: response
Routes: `API-MOBILE-PAYMENT-001`
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `paymentId` | String | yes | UUID | none | no | Internal payment ID. |
| `provider` | String | yes | provider code | `stripe` | no | First provider Stripe. |
| `clientSecret` | String | yes | provider token | none | secret | Return only to owning customer. |
| `expiresAt` | String? | no | ISO 8601 | none | no | Provider dependent. |

## 11. Integration DTOs

### `IntegrationAttemptResponse`

Direction: response
Routes: fulfillment/admin integration routes
Status: planned

| Field | Type | Required | Validation | Default | Sensitive | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `id` | String | yes | UUID | none | no | Attempt ID. |
| `provider` | String | yes | provider code | none | no | Example: mabang. |
| `operation` | String | yes | operation code | none | no | Sync, retry, status. |
| `status` | String | yes | attempt state | none | no | See state machine. |
| `safeErrorMessage` | String? | no | redacted | none | no | No raw secrets. |
| `nextRetryAt` | String? | no | ISO 8601 | none | no | Retry scheduling. |

## 12. Update Rules

Update this file when:

- An API request or response shape changes.
- A use case input/result becomes shared across files.
- A provider boundary input/result is introduced.
- A field becomes sensitive, required, optional, or validated differently.
- An example response or frontend contract changes.
