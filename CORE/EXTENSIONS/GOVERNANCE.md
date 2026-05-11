# Extension Governance

## 1. Purpose

This document prevents the extension system from becoming too heavy.

The extension system must improve future work without forcing full root-cause
analysis for every small mistake.

## 2. Learning Decision Matrix

Use this matrix before creating a learning record.

| Case | Required Action |
| --- | --- |
| Typo, formatting issue, harmless doc wording, immediately fixed with no reusable lesson | `no_record` |
| One-off low-risk command/test failure, fixed immediately, no pattern | `light_note` in task completion evidence |
| Repeated P2 issue, unclear rule, missing checklist, or non-critical workflow friction | `light_note` plus optional `WORKFLOW_IMPROVEMENTS.md` proposal |
| P0/P1 finding, security/data/money/merchant-boundary risk, failed critical verification, scope drift, provider idempotency/signature issue | `full_learning_record` in `ERROR_KNOWLEDGE_BASE.md` |
| Repeated full learning record, affects multiple modules, or changes how AI should work | `workflow_extension` and possible core doc update |

## 3. Trigger Severity Rules

Full learning record is mandatory when any condition is true:

- P0 finding.
- P1 finding.
- Cross-merchant data exposure risk.
- Payment/order/fulfillment state corruption risk.
- Webhook signature or idempotency failure.
- Data migration failure.
- AI edited outside approved write scope.
- Same P2 pattern appears twice.
- Human correction changes workflow, architecture, or review behavior.

Light note is enough when all conditions are true:

- Issue is P2/P3 or lower.
- Issue was fixed immediately.
- No business, data, security, payment, fulfillment, or integration risk.
- Similar-risk search finds no broader pattern.

No record is allowed when:

- The issue is purely mechanical.
- No user-visible, business, data, architecture, or workflow impact exists.
- The fix does not imply any future rule.

## 4. Extension Promotion Rule

Do not promote every learning entry into core rules.

Promote an extension or lesson into `PROJECT_RULES.md`, `AI_WORKFLOW.md`,
`TASK_TEMPLATE.md`, `REVIEW_RULES.md`, `TESTING_RULES.md`, or another core doc
only when at least one condition is true:

- The issue is P0/P1.
- The issue repeated.
- The issue affects more than one module.
- The issue affects money, permissions, merchant isolation, PII, migrations, or
  provider callbacks.
- The lesson can become a concrete checklist, test, command, or template field.
- The user explicitly decides it should become project policy.

Otherwise, keep it in `ERROR_KNOWLEDGE_BASE.md` or `PATTERN_LIBRARY.md`.

## 5. Knowledge Base Governance

Each error entry should include:

- `Category`
- `Module`
- `Layer`
- `Pattern ID`
- `Superseded By`
- `Review After`

Deduplicate when:

- A new entry has the same root cause and same preventive rule as an existing
  entry.
- A new entry is only a minor variant of an existing pattern.

Archive or supersede when:

- A rule/test/check fully prevents the issue.
- A newer entry captures a broader abstraction.
- The architecture changed and the entry is no longer relevant.

Consolidate:

- After every 10 error entries.
- At the end of each major phase.
- Before starting parallel/multi-agent work.

Consolidation output should be:

- Merge duplicate entries.
- Promote repeated patterns.
- Deprecate stale patterns.
- Add missing regression gates.

## 6. Pattern Evidence Levels

Pattern entries must declare one evidence level:

- `principle`: accepted design principle, not yet observed in project failures.
- `observed_once`: seen once in this project.
- `repeated`: seen more than once.
- `enforced`: backed by rule, test, checklist, or automation.

Rules:

- `principle` patterns guide design but should not be treated as failure-proven.
- `observed_once` patterns may guide review focus.
- `repeated` patterns should usually become checklist or test gates.
- `enforced` patterns should have a linked rule/test/check.

## 7. Review Quick Exit

Every review should include one line:

```text
Learning required: yes/no, reason: <short reason>
```

Use `no` when:

- No P0/P1 finding.
- No repeated pattern.
- No critical verification failure.
- No scope drift.
- No workflow/architecture correction.

This keeps normal reviews lightweight.

## 8. Extension Task Sizing

Keep extension tasks small.

Good:

- Add one learning record.
- Promote one repeated pattern into a review rule.
- Add one regression gate.

Avoid:

- Rewriting all workflow docs because of one small issue.
- Adding multiple unrelated patterns in one extension task.
- Promoting unverified preferences into mandatory rules.

## 9. Review Checklist

Before closing an extension-related task, confirm:

- Learning decision level is correct.
- Full record is used only when required.
- Light note is enough for low-risk one-off issues.
- Promotion to core docs meets promotion criteria.
- Knowledge base entry has category/module/layer/pattern metadata.
- Pattern evidence level is declared.
- Review quick exit remains available for normal tasks.
