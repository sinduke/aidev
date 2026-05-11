# Domain Model

## 1. Purpose

This document defines the first-phase business model, states, and invariants.
It is the source of truth for domain concepts before database tables and API DTOs
are finalized.

## 2. Actors

### Platform Admin

Owns platform-level operations:

- Merchant creation/review/suspension.
- Platform product import in v1.
- Role and permission management.
- Integration configuration.
- Payment/order/fulfillment operation review.

### Merchant Admin

Owns merchant-scoped operations when merchant backend is introduced:

- Merchant profile maintenance.
- Merchant product management.
- Merchant order visibility.
- Merchant fulfillment and after-sales workflows.

V1 may start from platform backend only, but data must preserve merchant
ownership so merchant backend can be introduced later.

### Customer

Uses mobile APIs:

- Product listing/detail.
- Hidden product access through approved context.
- Cart.
- Checkout.
- Order tracking.

### Service Actor

Represents trusted system actions:

- Payment webhook.
- Fulfillment sync job.
- Import queue job.
- Tracking processor.

Service actors must still be auditable.

## 3. Merchant

Merchant is a business ownership boundary.

Recommended merchant states:

- `draft`
- `pending_review`
- `active`
- `suspended`
- `closed`

Invariants:

- Merchant-scoped data must have `merchant_id` or an equivalent ownership path.
- Suspended merchants cannot publish new products.
- Suspended merchants may still need order/refund/fulfillment access for existing
  orders.
- Merchant deletion should not hard-delete historical order/payment records.

## 4. Product, SPU, and SKU

Product/SPU represents the product family.

SKU represents the sellable variant.

Product owns:

- Merchant.
- Title/description.
- Category/brand.
- Media.
- Compliance fields.
- Visibility.
- Sale restrictions.

SKU owns:

- Variant/spec combination.
- Price.
- Currency.
- Stock.
- Barcode/SKU code.
- Weight/dimensions when needed for logistics.

Recommended product selling states:

- `draft`
- `active`
- `inactive`
- `sold_out`
- `archived`

Recommended visibility states:

- `public`
- `hidden`

Invariants:

- Selling state and visibility state are separate.
- `hidden` means not searchable and not recommendable.
- Hidden product detail access must require approved access context.
- Inactive or archived products must not be purchasable.
- SKU price and stock must be checked again during checkout.
- Order records must store product/SKU snapshots.

## 5. Product Visibility

Visibility is a domain capability, not a frontend display flag.

Visibility contexts may include:

- Public browsing.
- Hidden link token.
- Campaign/distribution context.
- Authorized customer group.
- Admin preview.

Rules:

- Search APIs must exclude hidden products unless explicitly designed otherwise.
- Recommendation APIs must exclude hidden products.
- Detail APIs must check visibility context.
- Cart and checkout must re-check visibility and selling state.
- Hidden product links should be revocable and auditable when implemented.

## 6. Product Import

Bulk import lifecycle:

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

Invariants:

- Upload success is not import success.
- Import commit must be explicit.
- Validation errors must be visible per row.
- Import batch must record actor, merchant, template version, and source file.
- Re-running or retrying a commit must be idempotent.

## 7. Cart

Cart is customer-scoped.

Rules:

- Cart item stores product/SKU references but checkout must revalidate current
  sellability.
- Hidden product cart actions require valid visibility context.
- Cart price display may be stale, but checkout price must be authoritative.
- Cart item quantity must respect stock and purchase limits.

## 8. Order

Order is the commercial contract snapshot.

Recommended order states:

- `created`
- `pending_payment`
- `paid`
- `cancelled`
- `fulfillment_pending`
- `fulfillment_processing`
- `partially_shipped`
- `shipped`
- `delivered`
- `completed`
- `closed`

Recommended transitions:

```text
created -> pending_payment
pending_payment -> paid
pending_payment -> cancelled
paid -> fulfillment_pending
fulfillment_pending -> fulfillment_processing
fulfillment_processing -> partially_shipped
fulfillment_processing -> shipped
partially_shipped -> shipped
shipped -> delivered
delivered -> completed
paid -> cancelled only if no fulfillment has started and payment reversal is safe
any active state -> closed only through approved compensation/admin workflow
```

Invariants:

- Order state is not payment state.
- Order state is not fulfillment state.
- Every state transition must be recorded.
- Order amount and item snapshots cannot be recomputed from current product data.
- Order ownership must include customer and merchant context.

## 9. Payment

Payment state is separate from order state.

Recommended payment states:

- `created`
- `requires_action`
- `processing`
- `succeeded`
- `failed`
- `cancelled`
- `refund_pending`
- `partially_refunded`
- `refunded`

Invariants:

- Provider event ID must be processed once.
- Provider idempotency key must be stored.
- Payment success may update order state, but only through approved use case.
- Payment failure must not delete order records.
- Payment webhook payloads must be stored or referenced safely for audit/debug.

## 10. Refund and Dispute

Refund is not required for the first foundation but must be anticipated.

Recommended refund states:

- `requested`
- `approved`
- `rejected`
- `processing`
- `succeeded`
- `failed`
- `cancelled`

Rules:

- Refund amount cannot exceed refundable amount.
- Refund decision must be audited.
- Provider refund state and internal refund state must be reconciled.

## 11. Fulfillment

Fulfillment state is separate from order state.

Recommended fulfillment states:

- `not_required`
- `pending`
- `syncing`
- `synced`
- `failed`
- `manual_review`
- `shipped`
- `in_transit`
- `delivered`

Invariants:

- Fulfillment is asynchronous.
- External sync failure must not corrupt order/payment state.
- Every provider call must create an attempt record.
- Manual compensation must be possible for failed syncs.

## 12. Integration Attempt

Integration attempts represent calls to external providers.

Core fields:

- Provider.
- Operation.
- Related business object.
- Request ID/idempotency key.
- Attempt number.
- Status.
- Request summary.
- Response summary.
- Error code/message.
- Next retry time.

Recommended states:

- `pending`
- `running`
- `succeeded`
- `failed_retryable`
- `failed_final`
- `manual_review`

## 13. Tracking and Audit

Tracking event records business behavior.

Audit log records who changed what.

Diagnostic log records system behavior.

These must not be collapsed into a single vague log table.

## 14. Domain Review Checklist

Before implementing a domain feature, confirm:

- Which actor performs the action?
- Which merchant/customer owns the data?
- Which state machine is affected?
- Which invariants must be enforced?
- Which event/audit record is required?
- Which API surfaces expose the behavior?
- Which database constraints support the invariant?
