# Pattern Library

## 1. Purpose

This document stores reusable engineering and workflow patterns discovered during
the project.

Patterns are not mandatory by themselves. If a pattern becomes required, update
the relevant core rule document.

## 2. Pattern Template

```text
ID:
Status: proposed | active | deprecated | superseded
Name:
Evidence Level: principle | observed_once | repeated | enforced
Context:
Use When:
Avoid When:
Implementation Shape:
Related Rules:
Related Errors:
```

## 3. Active Patterns

### P-0001 Protocol plus mock plus real provider

Status: active
Evidence Level: principle

Name:

- Protocol + Mock/Fake + Real Provider

Context:

- External systems such as Stripe, Mabang, object storage, email, and logistics
  must not leak into domain/application code.

Use When:

- A dependency is external, replaceable, slow, expensive, unreliable, or requires
  credentials.

Avoid When:

- The behavior is pure domain logic with no external dependency.

Implementation Shape:

```text
Domain/Providers/<ProviderProtocol>.swift
Infrastructure/Providers/Mock<Provider>.swift
Infrastructure/Providers/<RealProvider>.swift
```

Related Rules:

- `ARCHITECTURE.md`
- `INTEGRATION_MAP.md`

Related Errors:

- None yet.

### P-0002 Outbox for external side effects

Status: active
Evidence Level: principle

Name:

- Outbox + Queue + Attempt Log

Context:

- Payment, fulfillment, ERP, logistics, tracking, and notification operations
  can fail or be retried.

Use When:

- A business state change must trigger an external side effect.

Avoid When:

- The operation is purely internal and can complete in one transaction.

Implementation Shape:

```text
Business transaction
-> outbox record
-> queue job
-> provider adapter
-> attempt log
-> success / retry / manual review
```

Related Rules:

- `INTEGRATION_MAP.md`
- `DATABASE_SCHEMA_INDEX.md`

Related Errors:

- None yet.

### P-0003 State machine for business state transitions

Status: active
Evidence Level: principle

Name:

- Explicit State Machine

Context:

- Order, payment, refund, import, fulfillment, and integration attempts all have
  constrained lifecycles.

Use When:

- A status controls business behavior, money, fulfillment, access, or audit.

Avoid When:

- The state is only a temporary UI display flag.

Implementation Shape:

```text
Domain/Rules/<Concept>StateMachine.swift
UseCase calls state machine
Repository persists transition
Audit/transition log records result
```

Related Rules:

- `DOMAIN_MODEL.md`
- `TESTING_RULES.md`

Related Errors:

- None yet.

### P-0004 Learning record for repeated or severe issues

Status: active
Evidence Level: enforced

Name:

- Error -> Abstraction -> Prevention

Context:

- AI can fix a local issue but miss the wider pattern unless the workflow forces
  abstraction.

Use When:

- P0/P1 finding.
- Repeated P2 finding.
- Failed critical verification.
- Scope drift.
- Human correction reveals a reusable process rule.

Avoid When:

- A typo or formatting issue has no reusable lesson.

Implementation Shape:

```text
Concrete issue
-> root cause
-> abstraction
-> similar risk search
-> preventive rule/test/check
-> update extension/core docs
```

Related Rules:

- `EXTENSIONS/LEARNING_LOOP.md`
- `REVIEW_RULES.md`

Related Errors:

- `E-0002`
