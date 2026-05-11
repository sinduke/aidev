# AI Development Workflow

## 1. Purpose

This document defines how AI agents must work in this repository.

The goal is to make AI-assisted development reliable enough for a large
cross-border B2B2C commerce system. The workflow must prevent vague planning,
uncontrolled implementation, missing verification, and context drift.

This is the control plane for:

- Divergence.
- Convergence.
- Task decomposition.
- Task execution.
- Review.
- Closure.

## 2. Workflow Overview

The standard workflow is:

```text
Orientation
-> Divergence / Exploration
-> Convergence / Decision
-> Task Decomposition
-> Build
-> Review
-> Close
```

Chinese shorthand:

```text
定位上下文 -> 发散 -> 收敛 -> 分解任务 -> 执行任务 -> Review -> 关闭
```

No Build work may start from conversation memory alone. Build work requires an
approved task file under `ai_dev/TASKS/`.

## 3. Mode Rules

### 3.1 Orientation

Purpose:

- Understand the current repository state before proposing or changing anything.

Required input:

- User request.
- Current repository files.
- Relevant `ai_dev` rules.

Required actions:

- Read `ai_dev/PROJECT_RULES.md`.
- Read `ai_dev/CORE/AI_WORKFLOW.md`.
- Read `ai_dev/CORE/INDEX_REGISTRY.md` when the task may change contracts.
- Read `ai_dev/PROJECT/GIT_WORKFLOW.md` when source edits, branches, or parallel
  AI work are involved.
- Read task file if the user references one.
- Read affected index documents.
- Check current file state before editing.

Forbidden actions:

- Do not assume a task exists.
- Do not invent current implementation details.
- Do not write business code.

Output:

- Short status of what context was checked.
- Whether the request is planning, decision, build, or review.

Exit condition:

- The next mode is clear.

### 3.2 Divergence / Exploration

Purpose:

- Explore options, risks, business constraints, architecture impact, and unknowns.

Required input:

- User goal.
- Current rules/docs/code.
- Relevant business context.

Required actions:

- Identify affected modules.
- Identify data model impact.
- Identify API impact.
- Identify function/DTO/data contract impact.
- Identify permission, state machine, test, config, and admin frontend impact.
- Identify integration impact.
- Identify security and observability impact.
- List assumptions and unknowns.
- List multiple reasonable approaches when the problem space is open.

Forbidden actions:

- Do not implement code.
- Do not create migrations.
- Do not finalize a task as approved.
- Do not silently choose a high-risk option.

Output format:

```text
Goal
Affected Areas
Options
Risks
Open Questions
Recommended Direction
Next Mode
```

Exit condition:

- User asks to converge/decide, or the next decision is obvious and low risk.

### 3.3 Convergence / Decision

Purpose:

- Choose one implementation direction from explored options.

Required actions:

- State the chosen option.
- State rejected alternatives and why.
- State assumptions.
- State blockers.
- State acceptance criteria.
- State required index/doc updates.
- Add or update `ai_dev/PROJECT/DECISION_LOG.md` for durable decisions.

Forbidden actions:

- Do not start Build.
- Do not leave critical blockers hidden.
- Do not mark an assumption as fact.

Output format:

```text
Decision
Rationale
Rejected Alternatives
Assumptions
Blockers
Acceptance Criteria
Required Task
```

Exit condition:

- User confirms the decision and asks to create/update a task file.

### 3.4 Task Decomposition

Purpose:

- Convert the approved decision into a precise executable task file.

Required actions:

- Create or update a file under `ai_dev/TASKS/`.
- Use `ai_dev/CORE/TASK_TEMPLATE.md`.
- Define Step IDs.
- Define Git workflow mode when source files may change.
- Define write scope.
- Define dependencies.
- Define per-step verification.
- Define pause points.
- Define index updates.
- Define API, function signature, DTO/data, permission, state machine, file, test,
  config, and admin frontend contract updates when affected.
- Define rollback/compensation notes.

Forbidden actions:

- Do not build before the task is approved.
- Do not leave affected files as "TBD" when they can be known.
- Do not omit verification gates.

Task status values:

- `draft`
- `proposed`
- `approved`
- `in_progress`
- `blocked`
- `in_review`
- `completed`
- `superseded`

Step status values:

- `pending`
- `in_progress`
- `completed`
- `blocked`
- `skipped`

Exit condition:

- User approves the task file for Build mode.

### 3.5 Build

Purpose:

- Execute the approved task exactly and minimally.

Required input:

- Approved task file.

Required actions:

- Read the approved task file before editing.
- Check Git workflow mode before source edits.
- Execute steps in Step ID order.
- Update status as work progresses when the task spans multiple steps.
- Modify only files listed in the write scope unless a task update is made.
- Update required index docs in the same task.
- Run verification gates.
- Record commands and outcomes in the final report.

Forbidden actions:

- Do not build from chat context alone.
- Do not skip ahead to later task scope.
- Do not introduce unrelated refactors.
- Do not change architecture rules silently.
- Do not ignore failed verification.
- Do not ignore required branch isolation when branch mode is enabled.

If new scope is discovered:

1. Stop the current step.
2. Explain the scope change.
3. Update the task or request user confirmation.
4. Continue only after the scope is explicit.

Exit condition:

- All required steps and verification gates are complete, or the task is blocked.

### 3.6 Review

Purpose:

- Find bugs, architecture drift, missing verification, security issues, and doc
  inconsistencies.

Required actions:

- Use `ai_dev/CORE/REVIEW_RULES.md`.
- Report findings by severity.
- Reference exact files and lines when possible.
- Separate findings from suggestions.
- Identify unrun or impossible verification.
- Identify whether any finding requires a learning record under
  `ai_dev/CORE/EXTENSIONS/ERROR_KNOWLEDGE_BASE.md`.

Forbidden actions:

- Do not fix code unless the user asks for implementation.
- Do not bury findings under a summary.
- Do not mark a task complete when P0/P1 findings remain unresolved.

Exit condition:

- Findings are accepted, dismissed, or converted into follow-up tasks.

### 3.7 Close

Purpose:

- Mark a task as actually complete.

Required actions:

- Ensure task status is `completed`.
- Ensure indexes are updated.
- Ensure verification evidence is listed.
- Ensure `TRACEABILITY_MATRIX.md` is updated for first-phase business coverage.
- Ensure unresolved risks are listed in `RISK_REGISTER.md`.
- Ensure meaningful errors, repeated issues, P0/P1 findings, failed critical
  verification, and scope drift have learning records or explicit deferral.

Forbidden actions:

- Do not close a task with unresolved P0/P1 findings.
- Do not close a task with skipped required verification unless the skip is
  documented and accepted.

Output:

```text
Completed Work
Verification
Remaining Risks
Learning Updates
Next Suggested Task
```

## 4. User Confirmation Rules

Require explicit user confirmation before:

- Moving from Decision to Task when the decision is significant.
- Moving from Task to Build.
- Expanding scope beyond the approved task.
- Making destructive database changes.
- Changing architecture rules.
- Switching the project Git workflow mode to or from `parallel_ai`.
- Adding external provider behavior that affects money, fulfillment, or PII.

Confirmation is not required for:

- Reading files.
- Running non-destructive checks.
- Updating status/checklist in the current task.
- Fixing formatting or doc consistency within an approved documentation task.

## 5. Handling Uncertainty

Classify uncertainty as:

- `blocker`: cannot continue safely.
- `assumption`: can continue if stated clearly.
- `later_decision`: intentionally deferred.
- `research_required`: must verify with source/code/docs before deciding.

Never hide uncertainty in prose.

Open questions in task files must use this format:

```text
- Type: blocker | assumption | later_decision | research_required
  Question:
  Current default:
  Owner:
  Required before:
```

## 6. Traceability Rules

Every first-phase feature must be traceable across:

- Business goal.
- Feature ID.
- Domain concept.
- Database table/index.
- API endpoint.
- Use case.
- Function signature.
- DTO/data contract.
- Security rule.
- Permission and object boundary.
- State machine when applicable.
- Observability event.
- Test.

Use `ai_dev/PROJECT/TRACEABILITY_MATRIX.md`.

If a task affects first-phase business scope and does not update traceability,
it is incomplete.

## 7. Task Splitting Rules

Split tasks when:

- More than one major module is changed.
- Database, API, and integration work would all happen at once.
- Verification would require unrelated environments.
- A task cannot be reviewed coherently.
- The work mixes foundation and business behavior.

Do not split tasks when:

- The split would break one atomic invariant.
- Migration and repository implementation must land together.
- A small index update belongs with the code change.

## 8. Status Reporting Rules

During long work, report:

- Current mode.
- Current task and step.
- What was just learned or changed.
- Next action.
- Blockers if any.

Avoid vague status such as "working on it" without evidence.

## 9. Drift Control

Before every Build task, check:

- `ai_dev/AIDEV_MANIFEST.md`
- `ai_dev/PROJECT_RULES.md`
- `ai_dev/CORE/AI_WORKFLOW.md`
- `ai_dev/CORE/INDEX_REGISTRY.md`
- `ai_dev/PROJECT/GIT_WORKFLOW.md`
- The approved task file.
- Affected specialized docs.
- Current git status.

When branch mode is `feature_branch` or `parallel_ai`, also check:

- Current branch.
- Base branch.
- Working branch.
- Merge target.
- Whether the task file records the required Git workflow fields.

After every Build task, check:

- Source files match `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`.
- Source files match `ai_dev/PROJECT/FILE_MAP.md`.
- Feature changes match `ai_dev/PROJECT/FEATURE_MAP.md`.
- Function and DTO changes match the active function/data contract indexes.
- Permission and state changes match their active project indexes.
- Schema changes match the active database schema index.
- API changes match the active API signature index.
- Integration changes match the active integration map.
- Security/observability/testing changes match their rule docs.
- Git branch usage matches `ai_dev/PROJECT/GIT_WORKFLOW.md` when branch mode is
  enabled.

## 10. Failure Handling

If verification fails:

1. Stop and identify the failure.
2. Determine if it is caused by this task.
3. Fix if within scope.
4. If outside scope, document as risk/follow-up.
5. Run the learning loop when the failure is meaningful or recurring.
6. Do not claim completion until the status is clear.

If the task is blocked:

- Set task status to `blocked`.
- Record the blocker.
- Record the safest next action.
- Do not continue by guessing.

## 11. Learning and Extension Loop

Use `ai_dev/CORE/EXTENSIONS/LEARNING_LOOP.md` when an issue should improve future
work, not only the current patch.

Before creating a full learning record, use
`ai_dev/CORE/EXTENSIONS/GOVERNANCE.md` to classify the issue as:

- `no_record`
- `light_note`
- `full_learning_record`
- `workflow_extension`

Mandatory learning cases:

- P0/P1 review findings.
- Failed payment/order/fulfillment verification.
- Cross-merchant data exposure risk.
- Webhook signature or idempotency failure.
- Data migration failure.
- Scope drift outside approved task.
- Repeated test failure pattern.
- Human correction that changes how AI should work.

The learning loop is:

```text
Concrete error
-> root cause
-> abstraction
-> similar-risk search
-> preventive rule/test/check
-> extension/core doc update
```

Allowed outputs:

- No record, when governance allows it.
- Light note in task completion evidence.
- Entry in `ai_dev/CORE/EXTENSIONS/ERROR_KNOWLEDGE_BASE.md`.
- Update to `ai_dev/CORE/EXTENSIONS/PATTERN_LIBRARY.md`.
- Update to `ai_dev/CORE/EXTENSIONS/WORKFLOW_IMPROVEMENTS.md`.
- Update to `ai_dev/CORE/TASK_TEMPLATE.md`,
  `ai_dev/CORE/REVIEW_RULES.md`, or the active testing rules preset.
- New regression test or verification gate once code exists.

Do not treat "be more careful next time" as a valid preventive action.
