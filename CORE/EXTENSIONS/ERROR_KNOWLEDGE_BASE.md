# Error Knowledge Base

## 1. Purpose

This file stores concrete errors and the reusable lessons extracted from them.

Use this for project-local self-correction. Future AI agents should search this
file when similar errors, review findings, or failed verification appear.

## 2. Entry Status

- `open`
- `fixed`
- `prevented`
- `accepted_risk`
- `superseded`

## 3. Entry Template

```text
ID:
Status:
Date:
Source:
Severity:
Category:
Module:
Layer:
Pattern ID:
Concrete Issue:
Impact:
Root Cause:
Abstraction:
Similar Risks Checked:
Fix Applied:
Preventive Rule:
Regression Gate:
Superseded By:
Review After:
Related Files:
Related Tasks:
```

## 4. Entries

### E-0001 Workflow rules were initially too shallow for large AI development

Status: prevented
Date: 2026-05-11
Source: user review and workflow expansion
Severity: P1
Category: workflow
Module: ai_dev
Layer: workflow
Pattern ID: P-0004

Concrete Issue:

- The initial `ai_dev` rules defined architecture and high-level workflow, but
  did not fully define how AI should move through divergence, convergence, task
  decomposition, build, review, close, and learning.

Impact:

- Future AI work could still drift from chat context, skip task approval, or
  close work without durable traceability.

Root Cause:

- Workflow was described as phases but not implemented as an executable control
  plane.

Abstraction:

- Large AI-assisted projects need a workflow system, not only architecture rules.
  The workflow system must define mode boundaries, inputs, outputs, forbidden
  actions, status transitions, and closure criteria.

Similar Risks Checked:

- Task template lacked Step IDs and write scope.
- Review rules lacked severity and closure behavior.
- Risks and decisions were not durable enough.
- Traceability from business goal to implementation was missing.

Fix Applied:

- Added `AI_WORKFLOW.md`, `TASK_TEMPLATE.md`, `REVIEW_RULES.md`,
  `TRACEABILITY_MATRIX.md`, `DECISION_LOG.md`, and `RISK_REGISTER.md`.

Preventive Rule:

- Build mode requires an approved task file.
- Review mode cannot close P0/P1 findings.
- Traceability and risk updates are part of closure.

Regression Gate:

- Review every Build task against `REVIEW_RULES.md` and `AI_WORKFLOW.md`.

Superseded By:

- None.

Review After:

- Before starting `001_vapor_foundation`.

Related Files:

- `ai_dev/CORE/AI_WORKFLOW.md`
- `ai_dev/CORE/TASK_TEMPLATE.md`
- `ai_dev/CORE/REVIEW_RULES.md`

Related Tasks:

- `000A_ai_development_workflow`

### E-0002 Error handling needed a learning loop, not only immediate fixes

Status: prevented
Date: 2026-05-11
Source: user correction about collecting and abstracting errors
Severity: P1
Category: workflow
Module: ai_dev
Layer: workflow
Pattern ID: P-0004

Concrete Issue:

- The workflow had failure handling, but it focused on stopping, fixing, or
  documenting blockers. It did not require abstraction from each meaningful
  error or a search for similar risks.

Impact:

- AI could fix one bug while leaving the same pattern likely to recur in another
  module, provider, state machine, or workflow step.

Root Cause:

- The workflow lacked a project-level self-learning extension.

Abstraction:

- Error handling in AI-developed systems must include root-cause analysis,
  pattern abstraction, similar-risk search, preventive rule updates, and
  regression gates.

Similar Risks Checked:

- Review findings.
- Failed verification.
- Scope drift.
- Payment/order/fulfillment state errors.
- Provider idempotency errors.

Fix Applied:

- Added extension docs under `ai_dev/CORE/EXTENSIONS/`.
- Updated core workflow and templates to require learning impact assessment.

Preventive Rule:

- P0/P1 findings, failed critical verification, repeated issues, and scope drift
  require learning records.

Regression Gate:

- Close mode must check whether a learning record is required and whether related
  workflow/risk/test docs were updated.

Superseded By:

- None.

Review After:

- Before starting `001_vapor_foundation`.

Related Files:

- `ai_dev/CORE/EXTENSIONS/LEARNING_LOOP.md`
- `ai_dev/CORE/EXTENSIONS/ERROR_KNOWLEDGE_BASE.md`
- `ai_dev/PROJECT_RULES.md`
- `ai_dev/CORE/AI_WORKFLOW.md`

Related Tasks:

- `000B_learning_extensions`
