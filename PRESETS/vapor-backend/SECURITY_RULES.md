# Security Rules

## 1. Purpose

This document defines security rules for authentication, authorization, data
protection, webhook safety, uploads, and admin auditability.

Security is a foundation requirement, not a later hardening phase.

## 2. Actor Types

Supported actor types:

- `platform_admin`
- `merchant_admin`
- `customer`
- `service`
- `provider_webhook`

Every authenticated request should resolve actor type and actor ID.

## 3. Authentication

Rules:

- Passwords must be hashed with a secure password hashing algorithm.
- Password hashes must never be exposed in API responses or logs.
- Tokens must expire.
- Refresh/session strategy must be approved before implementation.
- Login endpoints require rate limiting when infrastructure supports it.
- Failed login attempts should be logged safely.

## 4. Authorization

Authorization has two layers:

1. Permission check.
2. Object-level ownership/boundary check.

Permission alone is not enough.

Examples:

- A merchant admin with `product.read` can only read products owned by their
  merchant unless platform permission is present.
- A customer can only read their own orders.
- Hidden product access requires valid visibility context.

## 5. RBAC Naming

Permission names should follow:

```text
<resource>.<action>
```

Examples:

- `merchant.read`
- `merchant.update`
- `product.create`
- `product.update`
- `product.import`
- `product.visibility.update`
- `order.read`
- `order.cancel`
- `payment.read`
- `payment.reconcile`
- `fulfillment.retry`
- `integration.configure`
- `audit.read`

Resource names should be stable and singular.

## 6. Boundary Policies

Object-level authorization should live in policies, not scattered `if` checks.

Examples:

- `MerchantBoundaryPolicy`
- `OrderAccessPolicy`
- `ProductVisibilityPolicy`
- `PaymentAccessPolicy`

Policies should be testable without HTTP.

## 7. Secrets

Never commit:

- API keys.
- JWT secrets.
- Stripe secrets.
- Webhook signing secrets.
- Database passwords.
- Provider credentials.
- Private keys.

Secrets must come from environment variables or a secret manager.

Secrets must be redacted in logs and admin displays.

## 8. PII and Sensitive Data

PII may include:

- Name.
- Email.
- Phone.
- Address.
- Payment identifiers.
- IP address.
- Device identifiers.

Rules:

- Store only what is needed.
- Redact PII in logs unless an approved diagnostic path requires it.
- Admin APIs should expose the minimum required PII.
- Audit access to sensitive data where practical.

## 9. Webhook Security

Webhook endpoints must:

- Verify provider signatures when supported.
- Reject invalid signatures.
- Deduplicate provider event IDs.
- Avoid doing long work directly in webhook request handling once queues exist.
- Return safe responses without leaking internal details.

## 10. File Upload Security

File upload endpoints must validate:

- Size.
- Type.
- Extension.
- Content parse result.
- Row count limits for imports.
- Virus/malware scanning if production risk requires it.

Uploaded files must not be executed.

Import parsing errors must be safe to show to admin users.

## 11. Logging Redaction

Always redact:

- `Authorization`
- `Cookie`
- `Set-Cookie`
- `password`
- `token`
- `secret`
- `api_key`
- `client_secret`
- `webhook_secret`
- payment card data

Provider payload logging must be summarized or redacted.

## 12. Admin Audit

Audit logs should record:

- Actor type.
- Actor ID.
- Merchant ID when applicable.
- Action.
- Resource type.
- Resource ID.
- Before/after summary when safe.
- Request ID.
- IP/user agent when available.
- Timestamp.

Admin audit logs must not expose secrets.

## 13. Review Checklist

Before merging security-sensitive work, confirm:

- Auth requirement is declared.
- Permission check is present.
- Object-level authorization is present.
- Sensitive fields are redacted.
- Webhook signatures are verified where applicable.
- File upload validation is present where applicable.
- Audit log is written for admin state changes.
- Tests cover forbidden access where practical.
