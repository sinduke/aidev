# Git Workflow Modes

## 1. Purpose

This file defines optional Git workflow modes for AI-assisted development.

The goal is to support both lightweight solo development and stricter branch
isolation when multiple AI agents or multiple feature streams are active.

Core defines the modes. The current project chooses its active mode under
`ai_dev/PROJECT/`.

## 2. Mode Values

| Mode | Meaning | Typical Use |
| --- | --- | --- |
| `simple` | Work may happen on the current branch. Task, review, and verification are still required. | Solo development, early documentation, small fixes. |
| `feature_branch` | Each implementation task should happen on a dedicated feature branch. | Normal feature development with review before merge. |
| `parallel_ai` | Each AI agent/task must use an isolated branch or worktree. Merge only after review. | Multiple AI agents or concurrent module work. |

## 3. Branch Roles

| Branch | Role |
| --- | --- |
| `main` | Stable/release branch. Do not use for unreviewed feature development when branch mode is enabled. |
| `develop` or `integration` | Optional integration branch for active feature merges. |
| `feature/*` | Feature/task development branch. |
| `fix/*` | Bug fix branch. |
| `docs/*` | Documentation-only branch when needed. |
| `experiment/*` | Disposable experiment branch. Must not be merged without review. |

Projects may choose not to use `develop`/`integration` while the team is small.

## 4. Branch Naming

Recommended branch names:

```text
feature/<task-id>-<short-name>
feature/auth-rbac
feature/004-catalog-visibility
fix/<task-id>-<short-name>
docs/<task-id>-<short-name>
experiment/<topic>
```

Use lowercase words separated by hyphens.

## 5. Baseline Selection

Before creating a branch, choose the correct baseline:

| Situation | Baseline |
| --- | --- |
| Release hotfix | `main` |
| Normal feature work with integration branch | latest `develop` or `integration` |
| Normal feature work without integration branch | latest suitable stable branch |
| Follow-up to an unfinished feature | the existing feature branch |
| Parallel AI work | a fresh branch/worktree from the agreed integration baseline |

Do not branch from stale local state without checking git status and the intended
baseline.

## 6. Mode Rules

### simple

- Branch creation is optional.
- Current branch work is allowed.
- Build still requires an approved task file.
- Review and verification still apply.
- Do not claim release readiness from unreviewed work on `main`.

### feature_branch

- Implementation tasks should start from a named feature/fix/docs branch.
- The task file should record the branch name.
- Merge only after review findings are resolved or explicitly accepted.
- If source work accidentally happens on the wrong branch, stop and document the
  safest recovery path.

### parallel_ai

- Every concurrent task must use a separate branch or worktree.
- Each agent must own a clear write scope.
- Agents must not revert or overwrite changes from other branches.
- Integration happens through review and merge, not by sharing an untracked dirty
  working tree.
- Merge conflicts must be resolved by preserving reviewed intent from both sides.

## 7. Required Checks

Before Build mode when branch mode is `feature_branch` or `parallel_ai`:

- Check current branch.
- Check `git status --short`.
- Confirm the branch name matches the task or document the exception.
- Confirm the baseline branch is appropriate for the task.

Before merge:

- Review findings are resolved or accepted.
- Verification gates pass or skips are documented.
- Contract indexes are updated.
- The task file has completion evidence.

## 8. Switching Modes

Switching modes is allowed, but it must be explicit in the project workflow doc
or task file.

Recommended switches:

- `simple` -> `feature_branch` when source code development begins or review
  discipline becomes important.
- `feature_branch` -> `parallel_ai` when multiple AI agents work at the same
  time.
- `parallel_ai` -> `feature_branch` or `simple` when concurrency ends.

Do not silently apply strict branch rules to a project that selected `simple`.

## 9. Review Rules

Review mode should flag:

- Work on `main` when project mode requires feature branches.
- Missing branch name in task file when branch mode requires one.
- Multiple unrelated tasks mixed into one feature branch.
- Parallel AI work sharing the same dirty working tree.
- Merge without review evidence.
