# Learning Loop

## 1. Purpose

This document defines how the project learns from errors.

The required behavior is:

```text
Error -> Root Cause -> Abstraction -> Similar Risk Search -> Prevention -> Regression Gate -> Workflow Update
```

Fixing the immediate error is not enough for a large AI-developed ecommerce
system.

## 2. Triggers

Before running the full learning loop, classify the issue using
`ai_dev/CORE/EXTENSIONS/GOVERNANCE.md`.

Decision levels:

- `no_record`
- `light_note`
- `full_learning_record`
- `workflow_extension`

Run the full learning loop when governance selects `full_learning_record` or
`workflow_extension`.

Potential triggers:

- A task fails verification.
- Review finds P0/P1 issues.
- The same type of P2 issue repeats.
- The AI edits outside approved scope.
- A requirement is misunderstood.
- A missing rule causes implementation drift.
- A domain invariant is violated.
- An integration/payment/security issue appears.
- A human correction reveals a reusable workflow improvement.

Do not run the full learning loop for every harmless typo, formatting correction,
or one-off low-risk command failure.

## 3. Required Abstraction Levels

Every learning entry must move at least one level above the concrete bug.

### L0 Concrete Incident

What happened exactly?

Example:

- `OrderService` updated order status directly without using the state machine.

### L1 Root Cause

Why did it happen?

Example:

- The task did not explicitly require `OrderStateMachine` usage.

### L2 Reusable Pattern

What class of problem is this?

Example:

- State transition code can bypass domain invariants when use case instructions
  mention only persistence updates.

### L3 Rule or Checklist Update

What rule prevents recurrence?

Example:

- Any task changing order/payment/fulfillment state must list the state machine
  and transition test in verification gates.

### L4 Automation or Regression Gate

What test/check catches it?

Example:

- Add unit test for invalid transition.
- Add review checklist item for direct status assignment.

## 4. Similar Risk Search

For each error, search similar risk areas:

- Same module.
- Same layer.
- Same state machine.
- Same provider pattern.
- Same API surface.
- Same database constraint.
- Same security boundary.
- Same task workflow phase.

Example:

If the bug is duplicate payment webhook processing, search:

- Payment event uniqueness.
- Integration inbox dedupe.
- Fulfillment retry idempotency.
- Order creation idempotency.

## 5. Learning Record Requirements

Learning entries must include:

- ID.
- Category.
- Module.
- Layer.
- Date.
- Source task or review.
- Concrete issue.
- Impact.
- Root cause.
- Abstraction.
- Similar risks checked.
- Fix applied.
- Preventive rule added.
- Regression gate.
- Pattern ID.
- Superseded By.
- Review After.
- Status.

Use `ai_dev/CORE/EXTENSIONS/templates/ERROR_REVIEW_TEMPLATE.md`.

## 6. Prevention Options

A learning loop should produce at least one of:

- Rule update.
- Task template update.
- Review checklist update.
- Test rule update.
- Traceability update.
- Risk register update.
- Decision log update.
- New regression test.
- New automation/tooling.

If none is possible, document why.

## 7. Mandatory Learning Cases

Learning record is mandatory for:

- P0 review finding.
- P1 review finding.
- Failed payment/order/fulfillment verification.
- Cross-merchant data exposure risk.
- Webhook signature or idempotency failure.
- Data migration failure.
- Scope drift outside approved task.
- Repeated test failure pattern.

Light note is enough for one-off low-risk issues when governance says no full
record is required.

## 8. Close Criteria

A learning record can close only when:

- Immediate issue is fixed or explicitly deferred.
- Abstraction is documented.
- Similar risks were checked.
- Preventive action is applied or tracked.
- Regression gate exists or is explicitly impossible.

## 9. Anti-Patterns

Avoid:

- "Fixed it" with no root cause.
- "Need to be careful" with no rule.
- Adding a note that future agents will not read.
- Treating a symptom as the abstraction.
- Creating a learning entry but not updating mandatory workflow docs.
