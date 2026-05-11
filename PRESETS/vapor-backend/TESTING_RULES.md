# Testing Rules

## 1. Purpose

This document defines test expectations for the Vapor backend project.

Tests should protect domain rules, state machines, security boundaries, API
contracts, migrations, and external integration behavior.

## 2. Test Levels

Use the smallest useful test level.

Required categories as the project grows:

- Domain unit tests.
- Use case tests.
- Repository/persistence tests.
- API/controller tests.
- Migration tests.
- Queue/job tests.
- Provider adapter tests with mocks/fakes.
- Security/authorization tests.
- Integration replay tests for webhooks.

## 3. Domain Tests

Domain tests should not require Vapor, Fluent, Redis, or external providers.

Examples:

- Order state transition validity.
- Payment state transition validity.
- Visibility policy behavior.
- Merchant boundary policy behavior.
- Refund amount validation.

## 4. Use Case Tests

Use case tests should verify workflows with fake repositories/providers.

Examples:

- Create order stores snapshots and rejects out-of-stock SKU.
- Commit product import rejects invalid batch state.
- Handle payment webhook deduplicates event ID.
- Sync fulfillment creates attempt log and handles retryable failure.

## 5. Repository and Migration Tests

Repository tests should use a test database, not production data.

Test:

- Constraints.
- Index-backed lookup assumptions where practical.
- Transaction behavior.
- Unique idempotency keys.
- Unique provider event IDs.
- Merchant ownership filtering.

Migrations should be verified before release.

## 6. API Tests

API tests should verify:

- Route exists.
- Auth requirement.
- Permission requirement.
- Object-level authorization.
- Request validation.
- Response envelope.
- Error code.
- DTO shape.

Every implemented endpoint also needs curl documentation in
`API_SIGNATURE_INDEX.md`.

## 7. Integration Tests

Provider integrations should have:

- Mock/fake provider tests.
- Error mapping tests.
- Retry behavior tests.
- Duplicate event/idempotency tests.
- Manual compensation path test or documented fallback.

Real provider sandbox tests may be added when credentials and environment are
available, but unit/use case tests must not depend on external network.

## 8. Security Tests

Security-sensitive features should test:

- Missing auth.
- Wrong role.
- Wrong merchant.
- Wrong customer.
- Hidden product without access context.
- Invalid webhook signature.
- Duplicate webhook event.
- Upload validation failure.

## 9. Verification Commands

Before Vapor code exists:

- Documentation consistency check.
- `git diff --check`.
- `git status --short`.

After Vapor foundation exists:

- `swift build`
- `swift test`
- Migration verification command defined by the project.
- Docker build/run check when Docker files change.
- `git diff --check`.

Feature-specific additions:

- API curl examples.
- Webhook replay tests.
- Queue job retry tests.
- Provider mock tests.

## 10. Test Data Rules

- Test data must be deterministic.
- Tests must not depend on production credentials.
- Tests must not call real payment/ERP/logistics providers by default.
- Use fake providers for normal CI.
- Isolate database state per test suite where practical.

## 11. Review Checklist

Before completing a task, confirm:

- The task file lists verification gates.
- Tests match the risk level.
- State machine changes have unit tests.
- Auth/ownership changes have negative tests.
- API changes have route/DTO tests and curl examples.
- Integration changes have retry/idempotency tests.
- Documentation indexes were updated.
