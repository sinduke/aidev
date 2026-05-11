# Project Git Workflow

## 1. Purpose

This file chooses the current Git workflow mode for this project.

The workflow is intentionally switchable. Solo development can stay lightweight,
while multi-AI or multi-feature work can enforce branch isolation.

## 2. Current Mode

```text
git_workflow_mode: simple
parallel_ai_branch_isolation: optional_off
main_branch_role: stable/release branch
integration_branch: not_required_yet
```

Current meaning:

- Documentation and early solo work may happen on the current branch.
- Build work still requires approved task files, verification, and review.
- `main` should be treated as the stable/release branch when the project becomes
  source-code active.
- Feature branch isolation becomes mandatory only when this file or the active
  task switches to `feature_branch` or `parallel_ai`.

## 3. Available Modes

| Mode | Current Project Meaning |
| --- | --- |
| `simple` | Default for solo/early work. Branch creation optional. |
| `feature_branch` | Use feature/fix/docs branches for implementation tasks. |
| `parallel_ai` | Use separate branches or worktrees for each concurrent AI task. |

## 4. Recommended Branch Names

```text
feature/001-vapor-foundation
feature/002-auth-rbac-audit
feature/003-merchant-foundation
feature/004-catalog-visibility
feature/005-product-import
feature/006-order-payment
feature/007-fulfillment-integration
fix/<task-id>-<short-name>
docs/<task-id>-<short-name>
```

For smaller work, use:

```text
feature/<module-or-capability>
fix/<bug-or-review-finding>
docs/<doc-topic>
```

## 5. When To Switch Modes

Switch from `simple` to `feature_branch` when:

- Vapor source code work begins and the task is more than documentation.
- A task changes migrations, API contracts, security, payment, order, fulfillment,
  or provider behavior.
- The user asks for stricter review/merge discipline.

Switch from `feature_branch` to `parallel_ai` when:

- More than one AI agent is implementing at the same time.
- Two or more feature tasks are active concurrently.
- Separate modules are being implemented in parallel.
- The write scopes could conflict or require merge review.

Switch back to `simple` when:

- Work returns to solo documentation or small local edits.
- The user explicitly disables branch isolation.

## 6. Branch Rules By Mode

### simple

- Branch creation is optional.
- The task file may record `Branch Mode: simple`.
- Do not use this mode as evidence that work is production-ready.
- Still run required verification gates.

### feature_branch

- Task file must record:
  - Branch Mode.
  - Base branch.
  - Working branch.
  - Merge target.
- Branch should be created before source edits.
- Review must complete before merge.
- Merge target is usually `main` until an integration branch is introduced.

### parallel_ai

- Each task/agent gets its own branch or worktree.
- Task write scopes must be disjoint where possible.
- Merge target should be an integration branch when parallel work becomes frequent.
- Agents must not merge their own work without review evidence.

## 7. Merge Policy

Current default:

```text
source branch -> review -> verification -> merge target
```

Minimum merge requirements when branch mode is enabled:

- Task status is `in_review` or `completed`.
- P0/P1 review findings are resolved or explicitly accepted.
- Verification gates are recorded.
- Contract indexes are updated.
- Risk/decision updates are recorded when applicable.

## 8. Task File Fields

Every task may include a Git section:

```text
## Git Workflow

- Branch Mode:
- Base Branch:
- Working Branch:
- Merge Target:
- Branch Required: yes/no
- Reason:
```

When mode is `feature_branch` or `parallel_ai`, this section is required before
Build mode.

## 9. Current Exceptions

- Existing documentation foundation work may remain in `simple` mode.
- Since no Vapor source code exists yet, branch isolation is not mandatory.
- The first source-code task, `001_vapor_foundation`, should decide whether to
  stay `simple` or switch to `feature_branch`.
