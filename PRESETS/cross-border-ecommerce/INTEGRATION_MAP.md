# Integration Map

## 1. Purpose

This document defines how external systems are connected. It must be updated
when a task adds or changes payment, ERP, OMS, logistics, object storage, email,
SMS, analytics, or other provider integrations.

## 2. Integration Principle

External systems must be behind adapters.

The internal business flow must not directly depend on provider SDKs, provider
payload shapes, or provider error messages.

Default flow:

```text
Domain/Application Event
-> Outbox Record
-> Queue Job
-> Provider Adapter
-> Attempt Log
-> Success / Retry / Dead Letter / Manual Review
```

Inbound provider flow:

```text
Webhook/Callback
-> Signature Verification
-> Inbox/Event Record
-> Deduplication
-> Use Case
-> State Transition
-> Audit/Tracking
```

## 3. Provider Protocol Rules

Provider protocols live in domain/application boundary folders.

Provider implementations live in infrastructure.

Every real provider must have:

- Protocol.
- Real implementation.
- Mock/fake implementation.
- Configuration object.
- Error mapping.
- Attempt logging.
- Tests or documented local verification.

## 4. Planned Providers

### Payment

First provider:

- Stripe.

Abstraction:

- `PaymentProvider`
- `StripePaymentProvider`
- `MockPaymentProvider`

Required operations:

- Create payment intent/session.
- Retrieve payment status when needed.
- Verify webhook signature.
- Parse webhook event.
- Create refund when refund scope is introduced.

### Fulfillment / ERP / OMS

First Mabang-like scope:

- Order sync.
- Logistics number sync.
- Logistics status sync.
- Retry.
- Manual compensation.

Abstraction:

- `FulfillmentProvider`
- `MabangFulfillmentProvider`
- `MockFulfillmentProvider`

Out of v1 unless approved:

- Deep inventory sync.
- Product master data sync.
- ERP-driven pricing.
- Full warehouse management.
- Multi-ERP routing.

### Object Storage

Planned storage use:

- Product images.
- Import files.
- Export files.
- Provider debug payload attachments when needed.

Abstraction:

- `ObjectStorageProvider`
- `LocalObjectStorageProvider`
- `S3CompatibleObjectStorageProvider`

Do not store large binary files in the primary relational database.

### Messaging

Planned future use:

- Email.
- SMS.
- Admin notification.

Abstraction:

- `NotificationProvider`
- Provider-specific implementations when needed.

## 5. Configuration Rules

Provider credentials:

- Must come from environment/secret management.
- Must not be committed.
- Must not be returned by APIs.
- Must be redacted in logs.

Integration config records may store:

- Provider enabled/disabled state.
- Public provider configuration.
- Merchant/platform scope.
- Credential reference or encrypted secret reference.
- Last validation status.

## 6. Retry Rules

External calls must define retry behavior:

- Retryable errors.
- Non-retryable errors.
- Max attempts.
- Backoff strategy.
- Next retry time.
- Final failure state.
- Manual review state.

Default suggested attempt policy for provider calls:

- 1 immediate attempt.
- 3 retry attempts with backoff.
- Move to `manual_review` or dead letter after final failure.

The exact policy can vary by provider and must be documented in the task.

## 7. Idempotency and Deduplication

Outbound:

- Store idempotency key where provider supports it.
- Use stable business operation keys.
- Do not generate a new external operation for duplicate internal requests.

Inbound:

- Store provider event ID.
- Ignore already-processed provider event IDs.
- Store raw event reference or sanitized summary for audit/debug.

## 8. Attempt Log Fields

Every provider call should record:

- Provider.
- Operation.
- Business object type and ID.
- Request ID or idempotency key.
- Attempt number.
- Started/finished timestamps.
- Status.
- HTTP status when applicable.
- Provider code.
- Safe error message.
- Redacted request/response summary.
- Next retry time.

## 9. Manual Compensation

Admin tools must eventually support:

- View failed integration attempts.
- Retry a failed attempt.
- Mark as manually resolved.
- Attach resolution note.
- See related order/payment/fulfillment records.

Manual compensation must be audited.

## 10. Review Checklist

Before adding an integration, confirm:

- Protocol and real/mock implementations exist.
- Provider credentials are configured safely.
- Outbox/inbox behavior is defined.
- Idempotency is defined.
- Retry/dead-letter behavior is defined.
- Attempt logs are persisted.
- Admin/manual compensation path is documented.
- `SECURITY_RULES.md`, `OBSERVABILITY_RULES.md`, and API docs are updated.
