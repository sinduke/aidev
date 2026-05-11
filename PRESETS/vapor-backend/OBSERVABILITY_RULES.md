# Observability Rules

## 1. Purpose

This document defines logging, audit, tracking, metrics, and diagnostic behavior.

For this project, observability is MVP scope.

## 2. Three Separate Event Types

Do not collapse all observability into one vague log.

Use separate concepts:

- Diagnostic logs: system behavior for developers/operators.
- Audit logs: who changed what.
- Business tracking events: product/order/customer/business behavior.

Additional specialized records:

- Request logs.
- Integration attempts.
- Payment events.
- Order state transitions.

## 3. Request Context

Every request should have:

- Request ID.
- Trace/correlation ID when available.
- Actor type and ID when authenticated.
- Merchant ID when applicable.
- API surface.
- Route/method.
- Client IP/user agent when available and safe.

Request ID must be propagated into logs, audit records, tracking events, and
integration attempts where possible.

## 4. Diagnostic Logs

Development logs should make key flows visible.

Examples:

- Request started/completed.
- Use case started/completed.
- Payment webhook received/deduplicated/processed.
- Import parse started/completed.
- Queue job started/retried/failed.
- Provider call started/succeeded/failed.

Production logs must be structured and redacted.

## 5. Audit Log Schema

Audit log should include:

- `id`
- `request_id`
- `actor_type`
- `actor_id`
- `merchant_id`
- `action`
- `resource_type`
- `resource_id`
- `before_summary`
- `after_summary`
- `result`
- `ip_address`
- `user_agent`
- `created_at`

Audit examples:

- Merchant status changed.
- Product visibility changed.
- Product import committed.
- Order manually cancelled.
- Fulfillment retry triggered.
- Integration config updated.

## 6. Business Event Schema

Business event should include:

- `id`
- `request_id`
- `actor_type`
- `actor_id`
- `merchant_id`
- `customer_id`
- `event_name`
- `resource_type`
- `resource_id`
- `properties`
- `created_at`

Business event examples:

- `product_detail_viewed`
- `hidden_product_link_opened`
- `cart_item_added`
- `order_created`
- `payment_started`
- `payment_succeeded`
- `fulfillment_synced`

## 7. Integration Attempt Schema

Integration attempt should include:

- `id`
- `request_id`
- `provider`
- `operation`
- `resource_type`
- `resource_id`
- `idempotency_key`
- `attempt_number`
- `status`
- `http_status`
- `provider_code`
- `safe_error_message`
- `redacted_request_summary`
- `redacted_response_summary`
- `started_at`
- `finished_at`
- `next_retry_at`

## 8. Payment Event Schema

Payment event should include:

- `id`
- `request_id`
- `provider`
- `provider_event_id`
- `provider_payment_id`
- `payment_id`
- `order_id`
- `event_type`
- `dedupe_status`
- `processing_status`
- `safe_payload_summary`
- `created_at`
- `processed_at`

## 9. Order State Transition Schema

Order state transition should include:

- `id`
- `request_id`
- `order_id`
- `from_state`
- `to_state`
- `reason`
- `actor_type`
- `actor_id`
- `metadata`
- `created_at`

## 10. Metrics

Metrics should eventually cover:

- Request count/duration/error rate.
- Login failures.
- Import parse duration and failure count.
- Order creation count/failure count.
- Payment webhook duplicates/failures.
- Integration retry/failure/manual review counts.
- Queue depth and job failure counts.

Metrics are not a replacement for audit logs.

## 11. Redaction

Observability records must redact:

- Authorization headers.
- Cookies.
- Passwords.
- Secrets.
- API keys.
- Payment secrets.
- Raw card data.
- Sensitive PII unless explicitly required and approved.

## 12. Review Checklist

Before completing a feature, confirm:

- Request ID is available.
- Important state transitions are recorded.
- Admin state changes write audit logs.
- Business events are captured where required.
- Provider calls create integration attempts.
- Logs are redacted.
- Developer-visible diagnostics exist for complex flows.
