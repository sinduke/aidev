# Function Signature Index

## 1. Purpose

This file records public function contracts that AI agents must preserve when
generating or changing code.

It covers use cases, application services, repository protocols, provider
protocols, policies, state machines, middleware, and controllers when the symbol
is part of a cross-file contract.

## 2. Status Values

- `planned`
- `contracted`
- `implemented`
- `verified`
- `changed`
- `deprecated`

## 3. Function Contract Template

```text
Function ID:
Module:
Layer:
Kind:
Symbol:
File:
Swift Signature:
Parameters:
Return:
Throws / Errors:
Side Effects:
Transaction:
Authorization:
Idempotency:
Observability:
Related API Routes:
Related DTOs:
Related Tests:
Owner Task:
Status:
```

## 4. Signature Rules

- Prefer one primary `execute(...)` method per use case.
- Use case inputs and outputs should be named structs, not loose dictionaries.
- Application and domain layers must not accept Vapor `Request` directly.
- Repository protocols should express business operations, not generic query
  helpers.
- Provider protocols should return internal result types, not raw provider SDK
  payloads.
- Async functions should declare meaningful typed errors or documented error
  mapping.

## 5. Planned Foundation Functions

| Function ID | Module | Layer | Symbol | Planned Signature | Return | Status |
| --- | --- | --- | --- | --- | --- | --- |
| FN-FOUNDATION-001 | Foundation | Bootstrap | `ConfigureApplication` | `static func configure(_ app: Application) async throws` | `Void` | planned |
| FN-FOUNDATION-002 | Foundation | API | `GetHealthStatus` | `func execute(context: RequestContext) async throws -> HealthCheckResult` | `HealthCheckResult` | planned |
| FN-FOUNDATION-003 | Foundation | Middleware | `RequestContextMiddleware.respond` | `func respond(to request: Request, chainingTo next: Responder) async throws -> Response` | `Response` | planned |
| FN-FOUNDATION-004 | Foundation | API/Error | `APIErrorMapper.map` | `func map(_ error: Error, context: RequestContext) -> APIErrorResponse` | `APIErrorResponse` | planned |

## 6. Planned Auth, RBAC, Audit Functions

| Function ID | Module | Layer | Symbol | Planned Signature | Return | Status |
| --- | --- | --- | --- | --- | --- | --- |
| FN-AUTH-001 | Auth | Application | `AdminLogin` | `func execute(input: AdminLoginInput, context: RequestContext) async throws -> AdminLoginResult` | `AdminLoginResult` | planned |
| FN-AUTH-002 | Auth | Application | `GetAdminMe` | `func execute(context: AdminRequestContext) async throws -> AdminMeResult` | `AdminMeResult` | planned |
| FN-RBAC-001 | RBAC | Domain Policy | `PermissionPolicy.require` | `func require(_ permission: PermissionCode, context: AdminRequestContext) throws` | `Void` | planned |
| FN-AUDIT-001 | Audit | Application | `RecordAuditLog` | `func execute(input: RecordAuditLogInput, context: RequestContext) async throws -> AuditLogRecord` | `AuditLogRecord` | planned |

## 7. Planned Merchant Functions

| Function ID | Module | Layer | Symbol | Planned Signature | Return | Status |
| --- | --- | --- | --- | --- | --- | --- |
| FN-MERCHANT-001 | Merchant | Application | `CreateMerchant` | `func execute(input: CreateMerchantInput, context: AdminRequestContext) async throws -> MerchantResult` | `MerchantResult` | planned |
| FN-MERCHANT-002 | Merchant | Application | `UpdateMerchantStatus` | `func execute(input: UpdateMerchantStatusInput, context: AdminRequestContext) async throws -> MerchantResult` | `MerchantResult` | planned |
| FN-MERCHANT-003 | Merchant | Application | `ListMerchants` | `func execute(query: MerchantListQueryInput, context: AdminRequestContext) async throws -> PagedResult<MerchantSummary>` | `PagedResult<MerchantSummary>` | planned |
| FN-MERCHANT-004 | Merchant | Application | `GetMerchantDetail` | `func execute(id: MerchantID, context: AdminRequestContext) async throws -> MerchantResult` | `MerchantResult` | planned |

## 8. Planned Catalog and Visibility Functions

| Function ID | Module | Layer | Symbol | Planned Signature | Return | Status |
| --- | --- | --- | --- | --- | --- | --- |
| FN-CATALOG-001 | Catalog | Application | `CreateProduct` | `func execute(input: CreateProductInput, context: AdminRequestContext) async throws -> ProductResult` | `ProductResult` | planned |
| FN-CATALOG-002 | Catalog | Application | `UpdateProduct` | `func execute(input: UpdateProductInput, context: AdminRequestContext) async throws -> ProductResult` | `ProductResult` | planned |
| FN-CATALOG-003 | Catalog | Application | `UpdateProductStatus` | `func execute(input: UpdateProductStatusInput, context: AdminRequestContext) async throws -> ProductResult` | `ProductResult` | planned |
| FN-CATALOG-005 | Catalog | Application | `ListAdminProducts` | `func execute(query: ProductListQueryInput, context: AdminRequestContext) async throws -> PagedResult<ProductSummary>` | `PagedResult<ProductSummary>` | planned |
| FN-CATALOG-006 | Catalog | Application | `GetAdminProductDetail` | `func execute(id: ProductID, context: AdminRequestContext) async throws -> ProductResult` | `ProductResult` | planned |
| FN-CATALOG-007 | Catalog | Application | `ListMobileProducts` | `func execute(query: MobileProductListQueryInput, context: CustomerRequestContext?) async throws -> PagedResult<MobileProductSummary>` | `PagedResult<MobileProductSummary>` | planned |
| FN-CATALOG-008 | Catalog | Application | `GetMobileProductDetail` | `func execute(input: GetProductDetailInput, context: CustomerRequestContext?) async throws -> MobileProductDetailResult` | `MobileProductDetailResult` | planned |
| FN-VISIBILITY-001 | Visibility | Application | `UpdateProductVisibility` | `func execute(input: UpdateProductVisibilityInput, context: AdminRequestContext) async throws -> ProductResult` | `ProductResult` | planned |
| FN-VISIBILITY-002 | Visibility | Application | `GenerateHiddenProductLink` | `func execute(input: GenerateHiddenProductLinkInput, context: AdminRequestContext) async throws -> HiddenProductLinkResult` | `HiddenProductLinkResult` | planned |
| FN-VISIBILITY-003 | Visibility | Application | `ResolveHiddenProductLink` | `func execute(token: String, context: CustomerRequestContext?) async throws -> MobileProductDetailResult` | `MobileProductDetailResult` | planned |
| FN-VISIBILITY-004 | Visibility | Domain Policy | `ProductVisibilityPolicy.canView` | `func canView(product: Product, context: VisibilityContext) -> Bool` | `Bool` | planned |

## 9. Planned Import Functions

| Function ID | Module | Layer | Symbol | Planned Signature | Return | Status |
| --- | --- | --- | --- | --- | --- | --- |
| FN-IMPORT-001 | Import | Application | `GetProductImportTemplate` | `func execute(query: ProductImportTemplateQueryInput, context: AdminRequestContext) async throws -> ImportTemplateResult` | `ImportTemplateResult` | planned |
| FN-IMPORT-002 | Import | Application | `CreateImportBatch` | `func execute(input: CreateImportBatchInput, context: AdminRequestContext) async throws -> ImportBatchResult` | `ImportBatchResult` | planned |
| FN-IMPORT-003 | Import | Application | `UploadImportFile` | `func execute(input: UploadImportFileInput, context: AdminRequestContext) async throws -> ImportFileUploadResult` | `ImportFileUploadResult` | planned |
| FN-IMPORT-004 | Import | Application | `ParseProductImport` | `func execute(batchId: ImportBatchID, context: AdminRequestContext) async throws -> ImportBatchResult` | `ImportBatchResult` | planned |
| FN-IMPORT-005 | Import | Application | `PreviewProductImport` | `func execute(query: ImportPreviewQueryInput, context: AdminRequestContext) async throws -> ImportPreviewResult` | `ImportPreviewResult` | planned |
| FN-IMPORT-006 | Import | Application | `CommitProductImport` | `func execute(input: CommitImportBatchInput, context: AdminRequestContext) async throws -> ImportBatchResult` | `ImportBatchResult` | planned |
| FN-IMPORT-007 | Import | Application | `ListImportErrors` | `func execute(query: ImportErrorQueryInput, context: AdminRequestContext) async throws -> PagedResult<ImportRowError>` | `PagedResult<ImportRowError>` | planned |

## 10. Planned Cart, Order, Payment Functions

| Function ID | Module | Layer | Symbol | Planned Signature | Return | Status |
| --- | --- | --- | --- | --- | --- | --- |
| FN-CART-001 | Cart | Application | `GetCart` | `func execute(context: CustomerRequestContext) async throws -> CartResult` | `CartResult` | planned |
| FN-CART-002 | Cart | Application | `AddCartItem` | `func execute(input: AddCartItemInput, context: CustomerRequestContext) async throws -> CartResult` | `CartResult` | planned |
| FN-CART-003 | Cart | Application | `UpdateCartItem` | `func execute(input: UpdateCartItemInput, context: CustomerRequestContext) async throws -> CartResult` | `CartResult` | planned |
| FN-CART-004 | Cart | Application | `RemoveCartItem` | `func execute(itemId: CartItemID, context: CustomerRequestContext) async throws -> CartResult` | `CartResult` | planned |
| FN-ORDER-001 | Order | Application | `CreateOrder` | `func execute(input: CreateOrderInput, context: CustomerRequestContext) async throws -> OrderResult` | `OrderResult` | planned |
| FN-ORDER-002 | Order | Application | `ListCustomerOrders` | `func execute(query: CustomerOrderListQueryInput, context: CustomerRequestContext) async throws -> PagedResult<OrderSummary>` | `PagedResult<OrderSummary>` | planned |
| FN-ORDER-003 | Order | Application | `GetCustomerOrderDetail` | `func execute(id: OrderID, context: CustomerRequestContext) async throws -> OrderResult` | `OrderResult` | planned |
| FN-ORDER-004 | Order | Application | `ListAdminOrders` | `func execute(query: AdminOrderListQueryInput, context: AdminRequestContext) async throws -> PagedResult<OrderSummary>` | `PagedResult<OrderSummary>` | planned |
| FN-ORDER-005 | Order | Application | `GetAdminOrderDetail` | `func execute(id: OrderID, context: AdminRequestContext) async throws -> OrderResult` | `OrderResult` | planned |
| FN-PAYMENT-001 | Payment | Application | `CreatePaymentIntent` | `func execute(input: CreatePaymentIntentInput, context: CustomerRequestContext) async throws -> CreatePaymentIntentResult` | `CreatePaymentIntentResult` | planned |
| FN-PAYMENT-002 | Payment | Application | `GetCustomerPaymentDetail` | `func execute(id: PaymentID, context: CustomerRequestContext) async throws -> PaymentResult` | `PaymentResult` | planned |
| FN-PAYMENT-003 | Payment | Application | `HandlePaymentWebhook` | `func execute(input: PaymentWebhookInput, context: ProviderWebhookContext) async throws -> PaymentWebhookResult` | `PaymentWebhookResult` | planned |
| FN-PAYMENT-004 | Payment | Application | `ListAdminPayments` | `func execute(query: PaymentListQueryInput, context: AdminRequestContext) async throws -> PagedResult<PaymentSummary>` | `PagedResult<PaymentSummary>` | planned |
| FN-PAYMENT-005 | Payment | Application | `GetAdminPaymentDetail` | `func execute(id: PaymentID, context: AdminRequestContext) async throws -> PaymentResult` | `PaymentResult` | planned |

## 11. Planned Provider Protocol Functions

| Function ID | Module | Layer | Symbol | Planned Signature | Return | Status |
| --- | --- | --- | --- | --- | --- | --- |
| FN-PROVIDER-PAYMENT-001 | Payment | Domain Provider | `PaymentProvider.createPaymentIntent` | `func createPaymentIntent(_ input: ProviderPaymentIntentInput) async throws -> ProviderPaymentIntentResult` | `ProviderPaymentIntentResult` | planned |
| FN-PROVIDER-PAYMENT-002 | Payment | Domain Provider | `PaymentProvider.verifyWebhook` | `func verifyWebhook(_ input: ProviderWebhookVerificationInput) async throws -> VerifiedPaymentWebhook` | `VerifiedPaymentWebhook` | planned |
| FN-PROVIDER-FULFILLMENT-001 | Fulfillment | Domain Provider | `FulfillmentProvider.syncOrder` | `func syncOrder(_ input: FulfillmentOrderSyncInput) async throws -> FulfillmentOrderSyncResult` | `FulfillmentOrderSyncResult` | planned |
| FN-PROVIDER-FULFILLMENT-002 | Fulfillment | Domain Provider | `FulfillmentProvider.fetchLogisticsStatus` | `func fetchLogisticsStatus(_ input: LogisticsStatusQueryInput) async throws -> LogisticsStatusResult` | `LogisticsStatusResult` | planned |

## 12. Planned Fulfillment and Integration Functions

| Function ID | Module | Layer | Symbol | Planned Signature | Return | Status |
| --- | --- | --- | --- | --- | --- | --- |
| FN-FULFILLMENT-001 | Fulfillment | Application | `SyncFulfillmentOrder` | `func execute(input: SyncFulfillmentOrderInput, context: ServiceRequestContext) async throws -> FulfillmentResult` | `FulfillmentResult` | planned |
| FN-FULFILLMENT-002 | Fulfillment | Application | `SyncLogisticsStatus` | `func execute(input: SyncLogisticsStatusInput, context: ServiceRequestContext) async throws -> ShipmentResult` | `ShipmentResult` | planned |
| FN-FULFILLMENT-003 | Fulfillment | Application | `ListFulfillments` | `func execute(query: FulfillmentListQueryInput, context: AdminRequestContext) async throws -> PagedResult<FulfillmentSummary>` | `PagedResult<FulfillmentSummary>` | planned |
| FN-INTEGRATION-001 | Integration | Application | `RecordIntegrationAttempt` | `func execute(input: RecordIntegrationAttemptInput, context: RequestContext) async throws -> IntegrationAttemptRecord` | `IntegrationAttemptRecord` | planned |
| FN-INTEGRATION-002 | Integration | Application | `RetryIntegrationAttempt` | `func execute(input: RetryIntegrationAttemptInput, context: AdminRequestContext) async throws -> IntegrationAttemptResult` | `IntegrationAttemptResult` | planned |
| FN-INTEGRATION-003 | Integration | Application | `MarkIntegrationManuallyResolved` | `func execute(input: ManualResolutionInput, context: AdminRequestContext) async throws -> IntegrationAttemptResult` | `IntegrationAttemptResult` | planned |

## 13. Update Rules

Before code generation for a function:

- Move the row from `planned` to `contracted` or update it in the same approved
  task.
- Confirm input/result DTOs exist in `DTO_CONTRACT_INDEX.md`.
- Confirm related route IDs exist when exposed through HTTP.
- Confirm required tests exist in `TEST_VERIFICATION_MATRIX.md`.
