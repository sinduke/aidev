# Permission Index

## 1. Purpose

This file maps permissions, roles, endpoints, and object boundary policies for
the current project.

Permission checks alone are not enough. Merchant, customer, product visibility,
order, payment, and integration records must also pass object-level boundary
checks.

## 2. Actor Types

| Actor Type | Description |
| --- | --- |
| `platform_admin` | Platform operator with cross-merchant permissions. |
| `merchant_admin` | Merchant-scoped operator. |
| `customer` | Mobile API customer. |
| `service` | Trusted internal job or system action. |
| `provider_webhook` | External provider callback after signature verification. |

## 3. Permission Contract Template

```text
Permission:
Resource:
Action:
Actors:
Default Roles:
API Routes:
Function IDs:
Object Boundary:
Audit Required:
Negative Tests:
Status:
```

## 4. Role Seeds

| Role | Actor Type | Scope | Initial Permissions | Status |
| --- | --- | --- | --- | --- |
| `platform_owner` | platform_admin | platform | all platform permissions | planned |
| `platform_operator` | platform_admin | platform | merchant/product/order/payment/fulfillment/audit read-write subset | planned |
| `merchant_owner` | merchant_admin | merchant | merchant-scoped product/order/fulfillment read-write subset | planned |
| `merchant_operator` | merchant_admin | merchant | merchant-scoped product/order read subset | planned |
| `customer` | customer | customer | customer-owned mobile operations | planned |
| `service_worker` | service | system | queue/integration/tracking actions | planned |

## 5. Permission Registry

| Permission | Resource | Action | Actors | Object Boundary | Status |
| --- | --- | --- | --- | --- | --- |
| `merchant.read` | merchant | read | platform_admin, merchant_admin | platform can read all; merchant admin reads own merchant only | planned |
| `merchant.create` | merchant | create | platform_admin | platform only | planned |
| `merchant.update` | merchant | update | platform_admin, merchant_admin | merchant admin only limited self profile fields | planned |
| `merchant.status.update` | merchant | status_update | platform_admin | platform only | planned |
| `rbac.manage` | rbac | manage | platform_admin | platform only unless later merchant-scoped RBAC is approved | planned |
| `audit.read` | audit | read | platform_admin | merchant admin only own merchant audit if approved | planned |
| `product.read` | product | read | platform_admin, merchant_admin | merchant admin own products only | planned |
| `product.create` | product | create | platform_admin, merchant_admin | merchant admin own merchant only | planned |
| `product.update` | product | update | platform_admin, merchant_admin | merchant admin own products only | planned |
| `product.status.update` | product | status_update | platform_admin, merchant_admin | merchant admin own products only | planned |
| `product.visibility.update` | product_visibility | update | platform_admin, merchant_admin | merchant admin own products only | planned |
| `product.visibility.link.create` | product_visibility | create_link | platform_admin, merchant_admin | merchant admin own products only | planned |
| `product.import` | product_import | execute | platform_admin, merchant_admin later | v1 platform admin; merchant admin later if approved | planned |
| `order.read` | order | read | platform_admin, merchant_admin | merchant admin own merchant orders only | planned |
| `order.cancel` | order | cancel | platform_admin, merchant_admin, customer | actor must own or be authorized; state guard required | planned |
| `payment.read` | payment | read | platform_admin, merchant_admin | merchant admin own merchant payments only | planned |
| `payment.reconcile` | payment | reconcile | platform_admin | platform only | planned |
| `fulfillment.read` | fulfillment | read | platform_admin, merchant_admin | merchant admin own merchant fulfillments only | planned |
| `fulfillment.retry` | fulfillment | retry | platform_admin | platform only in v1 | planned |
| `fulfillment.manual_resolution` | fulfillment | manual_resolution | platform_admin | platform only, audit required | planned |
| `integration.read` | integration | read | platform_admin | platform only in v1 | planned |
| `integration.configure` | integration | configure | platform_admin | platform only | planned |

## 6. Endpoint Permission Map

| API Route Pattern | Permission | Boundary Policy | Negative Test Required |
| --- | --- | --- | --- |
| `/api/admin/v1/merchants*` | `merchant.*` by action | `MerchantBoundaryPolicy` | yes |
| `/api/admin/v1/products*` | `product.*` by action | `MerchantBoundaryPolicy`, `ProductAccessPolicy` | yes |
| `/api/admin/v1/imports*` | `product.import` | `MerchantBoundaryPolicy`, upload validation | yes |
| `/api/admin/v1/orders*` | `order.read` | `OrderAccessPolicy` | yes |
| `/api/admin/v1/payments*` | `payment.read` | `PaymentAccessPolicy` | yes |
| `/api/admin/v1/fulfillments*` | `fulfillment.*` by action | `FulfillmentAccessPolicy` | yes |
| `/api/mobile/v1/cart*` | customer auth | `CustomerCartPolicy`, `ProductVisibilityPolicy` | yes |
| `/api/mobile/v1/orders*` | customer auth | `CustomerOrderPolicy` | yes |
| `/api/mobile/v1/payments*` | customer auth | `CustomerPaymentPolicy` | yes |
| `/api/webhooks/stripe` | provider signature | signature + provider event dedupe | yes |

## 7. Object Boundary Policies

| Policy | Purpose | Must Check | Status |
| --- | --- | --- | --- |
| `MerchantBoundaryPolicy` | Prevent cross-merchant admin access. | actor type, merchant scope, resource merchant ID | planned |
| `ProductAccessPolicy` | Product ownership and visibility access. | merchant scope, visibility context, sale status | planned |
| `ProductVisibilityPolicy` | Mobile hidden/public product exposure. | route context, token/campaign/customer group, sale status | planned |
| `OrderAccessPolicy` | Customer/merchant/platform order access. | customer ID, merchant ID, platform permission | planned |
| `PaymentAccessPolicy` | Payment access and reconciliation boundary. | order ownership, merchant scope, platform permission | planned |
| `FulfillmentAccessPolicy` | Fulfillment retry/manual boundary. | merchant/order scope, platform permission, state | planned |

## 8. Review Rules

Any new admin API must list:

- Permission code.
- Actor types.
- Object boundary policy.
- Audit requirement for state-changing actions.
- Negative authorization tests.

Any new mobile API must list:

- Customer ownership check.
- Hidden product visibility behavior when applicable.
- Negative tests for wrong customer/resource.
