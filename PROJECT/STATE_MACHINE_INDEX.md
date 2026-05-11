# State Machine Index

## 1. Purpose

This file records explicit state machines for the current project.

State transitions must not be implemented by raw string assignment scattered
across controllers or repositories. State-changing use cases must reference the
state machine rows here.

## 2. Status Values

- `planned`
- `contracted`
- `implemented`
- `verified`
- `changed`

## 3. Transition Template

```text
State Machine:
From:
To:
Trigger:
Guard:
Use Case / Function:
Side Effects:
Audit / Tracking:
Invalid Transition Error:
Tests:
Status:
```

## 4. Merchant State Machine

States:

```text
draft
pending_review
active
suspended
closed
```

| From | To | Trigger | Guard | Function | Audit/Event | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `draft` | `pending_review` | submit merchant for review | required profile fields present | `FN-MERCHANT-002` | merchant_status_changed | planned |
| `pending_review` | `active` | approve merchant | platform_admin | `FN-MERCHANT-002` | merchant_status_changed | planned |
| `active` | `suspended` | suspend merchant | platform_admin, reason required | `FN-MERCHANT-002` | merchant_status_changed | planned |
| `suspended` | `active` | reinstate merchant | platform_admin, reason required | `FN-MERCHANT-002` | merchant_status_changed | planned |
| `active` | `closed` | close merchant | platform_admin, no unsafe active operations | `FN-MERCHANT-002` | merchant_status_changed | planned |
| `suspended` | `closed` | close merchant | platform_admin, reason required | `FN-MERCHANT-002` | merchant_status_changed | planned |

## 5. Product Selling State Machine

States:

```text
draft
active
inactive
sold_out
archived
```

| From | To | Trigger | Guard | Function | Audit/Event | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `draft` | `active` | publish product | merchant active, valid SKU/price/media | `FN-CATALOG-003` | product_status_changed | planned |
| `active` | `inactive` | unpublish product | authorized admin | `FN-CATALOG-003` | product_status_changed | planned |
| `inactive` | `active` | republish product | merchant active, valid SKU/price | `FN-CATALOG-003` | product_status_changed | planned |
| `active` | `sold_out` | stock unavailable | stock policy | inventory/order flow later | product_status_changed | planned |
| `sold_out` | `active` | stock restored | stock > 0 | inventory/order flow later | product_status_changed | planned |
| any non-archived | `archived` | archive product | no unsafe active sale dependency | `FN-CATALOG-003` | product_status_changed | planned |

## 6. Product Visibility State Machine

States:

```text
public
hidden
```

| From | To | Trigger | Guard | Function | Audit/Event | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `public` | `hidden` | hide product | authorized admin, reason required | `FN-VISIBILITY-001` | product_visibility_changed | planned |
| `hidden` | `public` | publish visibility | authorized admin, product sellable | `FN-VISIBILITY-001` | product_visibility_changed | planned |

Rules:

- Hidden products are excluded from search and recommendation.
- Hidden products require approved visibility context for detail/cart/checkout.

## 7. Product Import Batch State Machine

States:

```text
created
uploaded
parsing
parsed
validation_failed
preview_ready
committing
completed
completed_with_errors
failed
cancelled
```

| From | To | Trigger | Guard | Function | Audit/Event | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `created` | `uploaded` | upload file | file validation passes | `FN-IMPORT-003` | import_file_uploaded | planned |
| `uploaded` | `parsing` | start parse | batch owns file | `FN-IMPORT-004` | import_parse_started | planned |
| `parsing` | `parsed` | parse success | rows parsed | `FN-IMPORT-004` | import_parse_completed | planned |
| `parsed` | `validation_failed` | validation has blocking errors | validation result | `FN-IMPORT-004` | import_validation_failed | planned |
| `parsed` | `preview_ready` | validation ok or non-blocking warnings | preview rows available | `FN-IMPORT-004` | import_preview_ready | planned |
| `preview_ready` | `committing` | admin commit | idempotency key and state guard | `FN-IMPORT-006` | import_commit_started | planned |
| `committing` | `completed` | all rows imported | transaction success | `FN-IMPORT-006` | import_committed | planned |
| `committing` | `completed_with_errors` | partial non-blocking row errors | documented row errors | `FN-IMPORT-006` | import_committed_with_errors | planned |
| any active state | `failed` | unrecoverable failure | safe failure handling | relevant import function | import_failed | planned |
| `created`/`uploaded`/`preview_ready` | `cancelled` | admin cancel | no commit started | import cancel later | import_cancelled | planned |

## 8. Order State Machine

States:

```text
created
pending_payment
paid
cancelled
fulfillment_pending
fulfillment_processing
partially_shipped
shipped
delivered
completed
closed
```

| From | To | Trigger | Guard | Function | Audit/Event | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `created` | `pending_payment` | order created and payable | items/prices/snapshots valid | `FN-ORDER-001` | order_created, order_state_transition | planned |
| `pending_payment` | `paid` | payment succeeded | deduped provider event | `FN-PAYMENT-003` | payment_succeeded, order_state_transition | planned |
| `pending_payment` | `cancelled` | customer/admin cancel or timeout | payment not succeeded | cancel order later | order_state_transition | planned |
| `paid` | `fulfillment_pending` | create fulfillment outbox | payment success confirmed | `FN-PAYMENT-003` or fulfillment task | fulfillment_pending_created | planned |
| `fulfillment_pending` | `fulfillment_processing` | fulfillment sync started | outbox ready | `FN-FULFILLMENT-001` | order_state_transition | planned |
| `fulfillment_processing` | `partially_shipped` | partial shipment update | provider event/attempt valid | `FN-FULFILLMENT-002` | order_state_transition | planned |
| `fulfillment_processing` | `shipped` | shipment complete | provider event/attempt valid | `FN-FULFILLMENT-002` | order_state_transition | planned |
| `partially_shipped` | `shipped` | remaining shipment complete | provider event/attempt valid | `FN-FULFILLMENT-002` | order_state_transition | planned |
| `shipped` | `delivered` | delivery confirmed | logistics event valid | `FN-FULFILLMENT-002` | order_state_transition | planned |
| `delivered` | `completed` | completion criteria met | after-sales window rules later | complete order later | order_state_transition | planned |
| any active state | `closed` | admin compensation | explicit approval and audit | compensation later | order_state_transition | planned |

## 9. Payment State Machine

States:

```text
created
requires_action
processing
succeeded
failed
cancelled
refund_pending
partially_refunded
refunded
```

| From | To | Trigger | Guard | Function | Audit/Event | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `created` | `requires_action` | provider requires customer action | provider result valid | `FN-PAYMENT-001` | payment_started | planned |
| `created` | `processing` | provider starts processing | provider result valid | `FN-PAYMENT-001` | payment_started | planned |
| `requires_action` | `processing` | customer completes action | provider webhook deduped | `FN-PAYMENT-003` | payment_event | planned |
| `processing` | `succeeded` | provider success event | signature valid, event not processed | `FN-PAYMENT-003` | payment_succeeded | planned |
| `processing` | `failed` | provider failure event | signature valid, event not processed | `FN-PAYMENT-003` | payment_failed | planned |
| `created`/`requires_action`/`processing` | `cancelled` | cancel/expire | provider/internal guard | payment cancel later | payment_cancelled | planned |
| `succeeded` | `refund_pending` | refund requested | refund scope approved | refund later | refund_requested | planned |
| `refund_pending` | `partially_refunded` | partial refund success | provider event valid | refund later | refund_succeeded | planned |
| `refund_pending`/`partially_refunded` | `refunded` | full refund success | provider event valid | refund later | refund_succeeded | planned |

## 10. Fulfillment and Integration Attempt State Machines

Fulfillment states:

```text
not_required
pending
syncing
synced
failed
manual_review
shipped
in_transit
delivered
```

Integration attempt states:

```text
pending
running
succeeded
failed_retryable
failed_final
manual_review
```

| State Machine | From | To | Trigger | Guard | Function | Audit/Event | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fulfillment | `pending` | `syncing` | sync job starts | order paid/fulfillment pending | `FN-FULFILLMENT-001` | fulfillment_sync_started | planned |
| fulfillment | `syncing` | `synced` | provider accepts order | attempt succeeded | `FN-FULFILLMENT-001` | fulfillment_synced | planned |
| fulfillment | `syncing` | `failed` | provider call fails | retry policy applies | `FN-FULFILLMENT-001` | fulfillment_sync_failed | planned |
| fulfillment | `failed` | `manual_review` | retries exhausted | final failure | `FN-INTEGRATION-001` | integration_manual_review | planned |
| fulfillment | `synced` | `shipped` | logistics number exists | provider event valid | `FN-FULFILLMENT-002` | shipment_created | planned |
| fulfillment | `shipped` | `in_transit` | logistics movement | provider event valid | `FN-FULFILLMENT-002` | logistics_event_received | planned |
| fulfillment | `in_transit` | `delivered` | delivery confirmed | provider event valid | `FN-FULFILLMENT-002` | fulfillment_delivered | planned |
| integration_attempt | `pending` | `running` | worker starts attempt | attempt not locked by other worker | `FN-INTEGRATION-001` | integration_attempt_started | planned |
| integration_attempt | `running` | `succeeded` | provider success | response mapped | `FN-INTEGRATION-001` | integration_attempt_succeeded | planned |
| integration_attempt | `running` | `failed_retryable` | retryable failure | attempts remain | `FN-INTEGRATION-001` | integration_attempt_failed | planned |
| integration_attempt | `failed_retryable` | `running` | retry starts | next_retry_at reached | `FN-INTEGRATION-002` | integration_attempt_retried | planned |
| integration_attempt | `failed_retryable` | `failed_final` | retries exhausted | max attempts reached | `FN-INTEGRATION-001` | integration_attempt_final_failed | planned |
| integration_attempt | `failed_final` | `manual_review` | admin/manual review needed | admin permission | `FN-INTEGRATION-003` | integration_manual_review | planned |

## 11. Review Rules

Any task that changes a state must update:

- This file.
- `FUNCTION_SIGNATURE_INDEX.md` for the responsible use case.
- `DTO_CONTRACT_INDEX.md` if API payloads expose the state.
- `TEST_VERIFICATION_MATRIX.md` with valid and invalid transition tests.
