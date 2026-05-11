# AI_DEV Entry Rules

## 1. Read Order

Before any non-trivial work, read:

1. `ai_dev/AIDEV_MANIFEST.md`
2. Current task file under `ai_dev/TASKS/` when one exists.
3. `ai_dev/PROJECT/PROJECT_PROFILE.md`
4. `ai_dev/PROJECT/PROJECT_RULES.md`
5. `ai_dev/PROJECT/GIT_WORKFLOW.md` when source edits, branches, or parallel AI
   work are involved.
6. Relevant project contract indexes under `ai_dev/PROJECT/`.
7. Relevant preset docs.
8. Relevant core workflow/review/index/Git docs.

## 2. Layer Boundary

This repository uses layered AI_DEV:

```text
CORE      = reusable AI workflow and learning system
PRESETS   = reusable technical/domain rules
PROJECT   = current project-specific overlay
TASKS     = approved execution plans
```

Do not put project-specific business rules into `CORE/`.

Do not put reusable workflow rules only into `PROJECT/`.

Do not edit `PRESETS/` for a one-off project exception. Put exceptions under
`PROJECT/` and record the decision.

## 3. Execution Rule

Build mode requires an approved task file under `ai_dev/TASKS/`.

If a task changes source files, indexes, APIs, database schemas, integrations,
risks, or decisions, update the corresponding `PROJECT/` or preset document in
the same task.

If a task changes source files or coordinates multiple AI agents, check
`ai_dev/PROJECT/GIT_WORKFLOW.md` and follow the selected branch mode.

For source or contract changes, check `ai_dev/CORE/INDEX_REGISTRY.md` and update
the active project indexes:

```text
FEATURE_MAP.md
FILE_MAP.md
IMPLEMENTATION_MAP.md
API_ROUTE_MAP.md
FUNCTION_SIGNATURE_INDEX.md
DTO_CONTRACT_INDEX.md
PERMISSION_INDEX.md
STATE_MACHINE_INDEX.md
TEST_VERIFICATION_MATRIX.md
ADMIN_FRONTEND_MAP.md
CONFIG_ENV_INDEX.md
TRACEABILITY_MATRIX.md
```

## 4. Current Project Rule

For this project, the current overlay is:

```text
ai_dev/PROJECT/PROJECT_PROFILE.md
ai_dev/PROJECT/PROJECT_RULES.md
```

The active presets are:

```text
ai_dev/PRESETS/vapor-backend/
ai_dev/PRESETS/cross-border-ecommerce/
```

The active core is:

```text
ai_dev/CORE/
```
