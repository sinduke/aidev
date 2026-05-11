# Test Verification Matrix

## 1. Purpose

This file maps features and contracts to required tests and verification gates.

Passing a broad command is not enough when a feature has money, merchant boundary,
visibility, payment, fulfillment, import, or webhook risk. The specific risk path
must be covered here.

## 2. Verification Status Values

- `planned`
- `required`
- `implemented`
- `passing`
- `skipped_with_reason`
- `blocked`

## 3. Command Baseline

Before Vapor code exists:

```text
git diff --check
find ai_dev -name '.DS_Store' -print
rg -n "[ \t]+$" ai_dev || true
```

After Vapor foundation exists:

```text
swift build
swift test
git diff --check
```

When Docker changes:

```text
docker compose config
docker compose up --build
```

Exact Docker commands may be adjusted by `001_vapor_foundation`.

## 4. Feature Verification Matrix

| Feature ID | Required Tests | Required Commands/Gates | Required Index Evidence | Status |
| --- | --- | --- | --- | --- |
| F-001 | health check API test, response envelope test, error mapping test, request ID middleware test | `swift build`, `swift test`, health curl after server run | API route, DTO, function, config indexes | planned |
| F-002 | login success/failure, JWT expiry, permission check, object boundary negative tests, audit record test | `swift test`, auth curl examples | permission, DTO, API, function indexes | planned |
| F-003 | create merchant, status transitions, merchant boundary policy, audit log | `swift test`, admin merchant curl examples | state machine, permission, API, DTO, DB indexes | planned |
| F-004 | public product detail, hidden product excluded from list/search, hidden token access, cart/checkout recheck | `swift test`, mobile/admin product curl examples | state machine, permission, API, DTO, function indexes | planned |
| F-005 | upload validation, parser row errors, preview, commit idempotency, failed state handling | `swift test`, import curl examples | state machine, DTO, DB, API indexes | planned |
| F-006 | cart ownership, stock/sellability recheck, create order snapshots, duplicate idempotency key | `swift test`, mobile order curl examples | state machine, DTO, DB, API indexes | planned |
| F-007 | create payment intent, webhook signature reject, webhook dedupe, order paid transition, provider error mapping | `swift test`, webhook replay test, curl/signed request notes | integration, state machine, DTO, API indexes | planned |
| F-008 | fulfillment outbox, provider fake success/failure, retry policy, manual resolution audit | `swift test`, queue/retry verification | integration, state machine, permission, API indexes | planned |
| F-009 | request ID propagation, audit redaction, business event record, integration attempt record | `swift test`, log review where applicable | observability, DTO, DB indexes | planned |
| F-010 | page route renders, page permission guard, table/form API contract tests when admin frontend exists | frontend test command chosen later | admin frontend map, API/DTO indexes | planned |

## 5. Test Record Template

```text
Test ID:
Feature ID:
Risk Covered:
Test File:
Command:
Expected Evidence:
Required Before:
Status:
Notes:
```

## 6. Critical Negative Tests

These negative paths are required before related features can be considered
verified:

- Merchant admin cannot read another merchant's products/orders/payments.
- Customer cannot read another customer's order/payment/cart.
- Hidden product cannot be listed, searched, recommended, carted, or ordered
  without valid visibility context.
- Duplicate order idempotency key does not create a second order.
- Duplicate payment webhook event does not apply state transition twice.
- Invalid webhook signature is rejected.
- Import commit cannot run from the wrong batch state.
- Provider retry exhaustion creates manual review path.

## 7. Review Rules

For every Build task:

- Add or update rows for changed features.
- Mark skipped tests only with a reason and follow-up.
- Do not mark a feature verified unless the specific tests pass or the accepted
  verification evidence is recorded.
