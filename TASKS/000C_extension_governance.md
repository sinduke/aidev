# 000C Extension Governance

Status: completed

## 1. Goal

Fix the review findings for `ai_dev/EXTENSIONS` by preventing the learning system
from becoming too heavy and by adding governance for trigger levels, promotion,
knowledge base growth, pattern evidence, and review quick exits.

## 2. Non-Goals

- Do not create Vapor source code.
- Do not create database migrations.
- Do not implement business modules.
- Do not automate governance checks yet.

## 3. Business Context

The extension system is meant to help AI agents learn from important errors. It
must not force full root-cause analysis for every small typo or harmless command
failure.

## 4. Mode History

- Review: `EXTENSIONS` review found risk of process weight, vague meaningful
  error boundary, missing promotion rules, knowledge base growth risk, weak
  evidence levels, and missing quick exit.
- Decision: Add governance instead of removing the extension system.
- Build: Documentation-only changes.

## 5. Dependencies

- Prior task: `000B_learning_extensions`
- Required docs:
  - `ai_dev/CORE/EXTENSIONS/README.md`
  - `ai_dev/CORE/EXTENSIONS/LEARNING_LOOP.md`
  - `ai_dev/CORE/REVIEW_RULES.md`

## 6. Assumptions and Open Questions

- Type: assumption
  Question: Should low-risk one-off issues avoid full learning records?
  Current default: Yes, use `no_record` or `light_note`.
  Owner: workflow
  Required before: every review close

- Type: later_decision
  Question: Should governance checks become scripts?
  Current default: keep document-based until implementation and CI exist.
  Owner: future tooling
  Required before: parallel/multi-agent scale

## 7. Affected Areas

- Workflow docs.
- Extension docs.
- Review rules.
- Task records.

## 8. Write Scope

Allowed files/directories:

- `ai_dev/CORE/EXTENSIONS/`
- `ai_dev/CORE/AI_WORKFLOW.md`
- `ai_dev/PROJECT_RULES.md`
- `ai_dev/CORE/REVIEW_RULES.md`
- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`
- `ai_dev/TASKS/000C_extension_governance.md`

Forbidden files/directories:

- `Sources/`
- `Tests/`
- database migrations
- frontend source files

## 9. Implementation Steps

| Step ID | Status | Description | Allowed Files | Verification | Pause After |
| --- | --- | --- | --- | --- | --- |
| S1 | completed | Add governance matrix | `EXTENSIONS/GOVERNANCE.md` | matrix contains no_record/light_note/full/workflow levels | no |
| S2 | completed | Update learning trigger docs | `README.md`, `LEARNING_LOOP.md` | low-risk quick exit exists | no |
| S3 | completed | Update KB/template metadata | `ERROR_KNOWLEDGE_BASE.md`, templates | category/module/layer/pattern/review fields exist | no |
| S4 | completed | Add pattern evidence levels | `PATTERN_LIBRARY.md` | each pattern has evidence level | no |
| S5 | completed | Update review quick exit | `REVIEW_RULES.md`, `AI_WORKFLOW.md` | review includes learning required yes/no reason | no |
| S6 | completed | Update indexes | `PROJECT_RULES.md`, `IMPLEMENTATION_MAP.md` | governance file is referenced | no |

## 10. Data Model Changes

None.

## 11. API Changes

None.

## 12. Integration Changes

None.

## 13. Security Requirements

No runtime security changes.

## 14. Observability Requirements

No runtime observability changes.

## 15. Index Updates

- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`: add `EXTENSIONS/GOVERNANCE.md`.
- `ai_dev/PROJECT_RULES.md`: reference governance.

## 16. Verification Gates

Required:

- Confirm governance file exists.
- Confirm keyword coverage for decision matrix, quick exit, promotion, evidence,
  dedup, archive, consolidation.
- Confirm no business code was created.
- `git diff --check`
- `git status --short`

## 17. Rollback / Compensation

Documentation-only rollback by reverting this task's files.

## 18. Review Plan

- Confirm extension flow is now lighter for low-risk issues.
- Confirm full learning records remain mandatory for severe/systemic issues.
- Confirm pattern evidence levels prevent unverified patterns becoming hard
  rules.

## 19. Learning / Extension Impact

- Learning record required: no
- Reason: this task improves governance directly and is already tracked as a
  workflow improvement/follow-up from review findings.

## 20. Completion Evidence

- Files changed: extension governance and entrypoint docs.
- Commands run: to be listed in final response.
- Remaining risks: automation still deferred.
