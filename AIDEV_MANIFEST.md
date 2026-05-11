# AIDEV Manifest

## 1. Purpose

This manifest declares which reusable AI_DEV layers this project uses.

AI_DEV is split into:

```text
CORE
-> PRESETS
-> PROJECT overlay
-> TASKS
-> optional tooling
```

The goal is to reuse the generic AI development system across projects while
keeping project-specific business rules small and explicit.

## 2. Layer Priority

When instructions conflict, follow this order:

1. Current user instruction.
2. Current task file under `ai_dev/TASKS/`.
3. Project overlay under `ai_dev/PROJECT/`.
4. Presets listed in this manifest.
5. Core rules under `ai_dev/CORE/`.
6. Existing codebase patterns.
7. Tool output from `aidev check` for validation feedback.

## 3. Core Layer

Core is project-type independent.

Core files:

```text
ai_dev/CORE/AI_WORKFLOW.md
ai_dev/CORE/TASK_TEMPLATE.md
ai_dev/CORE/REVIEW_RULES.md
ai_dev/CORE/INDEX_REGISTRY.md
ai_dev/CORE/GIT_WORKFLOW.md
ai_dev/CORE/EXTENSIONS/
```

Reusable tooling:

```text
ai_dev/bin/aidev
ai_dev/tools/aidev_check.py
ai_dev/.github/workflows/
```

Core owns:

- AI workflow.
- Task structure.
- Review rules.
- Required index types and update expectations.
- Optional Git workflow modes.
- Learning/extensions.
- Generic mode boundaries.
- Validation command behavior.

Core must not contain project-specific ecommerce, Vapor, Flutter, backend,
mobile, admin, payment, or database decisions.

## 4. Preset Layers

Presets are reusable by project type or domain.

Enabled presets for this project:

```text
ai_dev/PRESETS/vapor-backend/
ai_dev/PRESETS/cross-border-ecommerce/
```

Preset ownership:

- `vapor-backend`: Swift Vapor service architecture, backend testing, security,
  observability.
- `cross-border-ecommerce`: cross-border commerce domain, database/API/integration
  baseline.

Presets should be reusable by future projects. If a rule is only true for the
current project, put it under `ai_dev/PROJECT/`.

## 5. Project Overlay

Project overlay files:

```text
ai_dev/PROJECT/PROJECT_PROFILE.md
ai_dev/PROJECT/PROJECT_RULES.md
ai_dev/PROJECT/GIT_WORKFLOW.md
ai_dev/PROJECT/FEATURE_MAP.md
ai_dev/PROJECT/FILE_MAP.md
ai_dev/PROJECT/IMPLEMENTATION_MAP.md
ai_dev/PROJECT/API_ROUTE_MAP.md
ai_dev/PROJECT/FUNCTION_SIGNATURE_INDEX.md
ai_dev/PROJECT/DTO_CONTRACT_INDEX.md
ai_dev/PROJECT/PERMISSION_INDEX.md
ai_dev/PROJECT/STATE_MACHINE_INDEX.md
ai_dev/PROJECT/TEST_VERIFICATION_MATRIX.md
ai_dev/PROJECT/ADMIN_FRONTEND_MAP.md
ai_dev/PROJECT/CONFIG_ENV_INDEX.md
ai_dev/PROJECT/TRACEABILITY_MATRIX.md
ai_dev/PROJECT/DECISION_LOG.md
ai_dev/PROJECT/RISK_REGISTER.md
```

Project overlay owns:

- Current project identity.
- First-phase route.
- Project-specific business uniqueness.
- Current Git workflow mode.
- Current feature/API/file/function/data/permission/state/test/config maps.
- Current implementation file map.
- Current risks and decisions.
- Current traceability matrix.

## 6. Task Layer

Task files live in:

```text
ai_dev/TASKS/
```

Build mode must execute from an approved task file.

Reference tasks may use `Status: example`. They demonstrate the workflow and are
not evidence that the task was executed in the current repository.

## 7. Tooling Layer

The optional tooling layer provides executable checks for the Markdown contract:

```text
./bin/aidev check
```

Current checks are intentionally conservative:

- Required files and indexes exist.
- Task statuses use allowed values.
- Active/example/completed tasks contain required sections.
- Completed tasks contain Review, Verification, Index Update, and Completion
  Evidence.
- Project Git workflow mode is valid.
- Source files under `Sources/` or `Tests/` appear in file/implementation maps.

Tooling must remain generic. Project-specific business rules belong in
`PROJECT/` or selected `PRESETS/`.

## 8. Reuse Policy

For a new project:

1. Reuse `CORE/`.
2. Select one or more `PRESETS/`.
3. Create a new `AIDEV_MANIFEST.md`.
4. Create a small `PROJECT/PROJECT_PROFILE.md`.
5. Create project-specific overlay docs only when needed.

Do not regenerate the whole AI_DEV system for every new project.

## 9. Current Project

Current project profile:

```text
Project kind: Vapor backend service
Business domain: Cross-border B2B2C ecommerce
Current phase: ai_dev foundation
Next intended task: 001_vapor_foundation exploration
```
