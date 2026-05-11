# Review Rules

## 1. Purpose

This document defines how review mode works.

Review mode is for finding issues. It is not implementation mode unless the user
explicitly asks to fix the findings.

## 2. Review Stance

Prioritize:

1. Correctness.
2. Security.
3. Data integrity.
4. Business invariant preservation.
5. Architecture boundaries.
6. Missing verification.
7. Maintainability.

Do not lead with praise. Findings come first.

## 3. Severity Levels

### P0 Blocker

Must not ship. Examples:

- Money/payment state corruption.
- Cross-merchant data exposure.
- Auth bypass.
- Data loss.
- Irreversible migration without approval.
- Provider webhook can be forged or processed repeatedly.

### P1 High

Must be fixed before task closure. Examples:

- Missing object-level authorization.
- Order/payment/fulfillment state transition bug.
- Missing idempotency on critical operation.
- Task executed outside approved write scope.
- Required verification not run without acceptable reason.

### P2 Medium

Should be fixed soon. Examples:

- API docs incomplete.
- Index file not updated.
- Incomplete test coverage for non-critical path.
- Minor architecture drift.

### P3 Low

Nice to fix. Examples:

- Naming inconsistency.
- Small doc clarity issue.
- Non-blocking cleanup.

## 4. Finding Format

Use this format:

```text
- [P1] Short finding title
  File: path:line
  Issue:
  Impact:
  Recommendation:
```

If line numbers are not available, reference the file and section.

## 5. Required Review Checks

For every Build task, review:

- Task status and step completion.
- Write scope compliance.
- `IMPLEMENTATION_MAP.md` update.
- `FILE_MAP.md` update when files changed.
- Git workflow mode and branch usage when source files or parallel AI work are
  involved.
- Relevant index updates.
- API route map, function signature index, DTO/data contract index, permission
  index, state machine index, config index, admin frontend map, and test matrix
  updates when affected.
- Architecture dependency direction.
- Domain invariants.
- Auth and object-level authorization.
- Idempotency.
- Transaction boundaries.
- Observability.
- Test coverage.
- Verification command results.
- Whether learning records are required for severe/repeated issues.
- Whether similar-risk search was done when a meaningful error occurred.

## 6. Review Output Structure

Review response should be:

```text
Findings
Open Questions
Verification Gaps
Learning required: yes/no, reason: <short reason>
Residual Risk
Summary
```

If no issues are found, say that clearly and still list residual risk or test
gaps.

## 7. Fixing Findings

Review mode must not edit files by default.

If the user asks to fix findings:

1. Convert findings into a task or update the current task.
2. Confirm write scope if needed.
3. Enter Build mode.
4. Re-run review after fixes.

## 8. Closure Rules

A task cannot be closed when:

- Any P0 finding remains.
- Any P1 finding remains without explicit user acceptance.
- Required verification is skipped without documented reason.
- Index updates are missing.
- Task status is not `completed`.
- A mandatory learning case occurred but no learning record or accepted deferral
  exists.

## 9. Review Against AI Workflow

Also review AI process quality:

- Was there a Divergence phase for open-ended work?
- Was there a Decision phase for meaningful choices?
- Was a task file approved before Build?
- Were steps executed in order?
- Did scope expand without updating the task?
- Did Review avoid making unrequested changes?
- Did contract indexes move from planned to contracted before code generation
  where needed?
- Did the task follow the selected Git workflow mode?

## 10. Review Against Learning Loop

When a task has errors or severe findings, check:

- Did `EXTENSIONS/GOVERNANCE.md` classify the issue as no record, light note,
  full learning record, or workflow extension?
- Is the concrete issue recorded?
- Is root cause identified?
- Is there at least one abstraction above the immediate bug?
- Were similar modules/layers/providers/state machines checked?
- Was a preventive rule, test, checklist, or workflow update added?
- If no preventive action was possible, is the reason documented?
