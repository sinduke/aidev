# ai_dev Extensions

## 1. Purpose

Extensions are project-level learning and workflow modules.

They exist because a large ecommerce project cannot rely only on static rules.
When the project encounters mistakes, repeated friction, missing checks, vague
boundaries, or workflow gaps, the AI development system must learn from them and
update the process.

This is not model training. It is repository-local, reviewable, versioned
learning through documents, templates, rules, tests, and checklists.

## 2. Extension Types

Supported extension types:

- `learning`: records errors, root causes, abstractions, and prevention rules.
- `workflow`: improves how AI agents explore, decide, build, review, and close.
- `architecture`: strengthens module/layer/source-layout rules.
- `domain`: strengthens business invariants and state machines.
- `security`: strengthens auth, RBAC, PII, upload, webhook, and secret handling.
- `testing`: adds regression checks and verification gates.
- `tooling`: adds scripts, commands, or automation once implementation exists.

## 3. Extension Lifecycle

Extension status values:

- `proposed`
- `accepted`
- `active`
- `deprecated`
- `superseded`

Lifecycle:

```text
Problem or opportunity found
-> Create learning/error record
-> Abstract the underlying pattern
-> Propose extension or rule update
-> Accept through task/review
-> Apply to templates/rules/tests
-> Verify on future tasks
```

Use `ai_dev/CORE/EXTENSIONS/GOVERNANCE.md` before creating a learning record. The
governance document decides whether the situation needs no record, a light note,
a full learning record, or a workflow extension.

## 4. When to Create an Extension Record

Create or update extension records according to `GOVERNANCE.md`.

Strong triggers:

- The same mistake happens more than once.
- A P0/P1 review finding appears.
- A verification failure reveals a missing gate.
- A task drifts from approved scope.
- A doc/rule is too vague for execution.
- A bug reveals a missing domain invariant.
- A provider/API/database issue has a reusable lesson.
- A human correction changes how AI should work.

Do not create a full learning record for a harmless typo, formatting-only issue,
or one-off low-risk command failure with no reusable lesson.

## 5. Required Learning Behavior

When an error occurs, AI must not stop at "fix the immediate bug".

The minimum learning loop is:

1. Capture the concrete error.
2. Identify root cause.
3. Abstract at least one reusable pattern.
4. Search for similar risks.
5. Apply or propose a preventive change.
6. Add a regression test/check/gate when practical.
7. Update task/review/risk documents.

## 6. Current Extension Files

```text
ai_dev/CORE/EXTENSIONS/README.md
ai_dev/CORE/EXTENSIONS/GOVERNANCE.md
ai_dev/CORE/EXTENSIONS/LEARNING_LOOP.md
ai_dev/CORE/EXTENSIONS/ERROR_KNOWLEDGE_BASE.md
ai_dev/CORE/EXTENSIONS/WORKFLOW_IMPROVEMENTS.md
ai_dev/CORE/EXTENSIONS/PATTERN_LIBRARY.md
ai_dev/CORE/EXTENSIONS/templates/ERROR_REVIEW_TEMPLATE.md
ai_dev/CORE/EXTENSIONS/templates/WORKFLOW_EXTENSION_TEMPLATE.md
```

## 7. Relationship to Core Docs

Extensions can propose updates to:

- `PROJECT_RULES.md`
- `AI_WORKFLOW.md`
- `TASK_TEMPLATE.md`
- `REVIEW_RULES.md`
- `TESTING_RULES.md`
- `RISK_REGISTER.md`
- module-specific docs

Accepted extension changes must be reflected in the relevant core docs. An
extension record alone is not enough when the behavior should become mandatory.

## 8. Review Checklist

Before closing a learning/extension task, confirm:

- The concrete issue is captured.
- A reusable abstraction exists.
- Similar risks were considered.
- Preventive rule/test/check was added or explicitly deferred.
- Related risk/decision/task docs were updated.
- The extension status is clear.
- The learning decision level is appropriate.
