# 000D AI_DEV Layered Template

Status: completed

## 1. Goal

Split the current single-project `ai_dev` into reusable layers:

```text
CORE
PRESETS
PROJECT
TASKS
```

This lets future backend, mobile, admin, and frontend projects reuse the same
AI_DEV core without regenerating all documents.

## 2. Non-Goals

- Do not create Vapor source code.
- Do not create database migrations.
- Do not implement business modules.
- Do not design a full external package manager.

## 3. Business Context

The user already has multiple AI_DEV systems for frontend, mobile, and backend
work. The goal is to separate reusable AI workflow from project-specific business
rules so new projects need only a manifest and small project overlay.

## 4. Mode History

- Exploration: The prior flat `ai_dev` was identified as too project-specific to
  reuse directly.
- Decision: Create a layered local structure.
- Build: Documentation restructuring only.

## 5. Dependencies

- Prior tasks:
  - `000_project_rules_and_architecture`
  - `000A_ai_development_workflow`
  - `000B_learning_extensions`
  - `000C_extension_governance`

## 6. Affected Areas

- AI_DEV structure.
- Documentation paths.
- Project overlay.
- Reuse policy.

## 7. Write Scope

Allowed:

- `ai_dev/`

Forbidden:

- `Sources/`
- `Tests/`
- database migrations
- frontend source files

## 8. Implementation Steps

| Step ID | Status | Description | Verification |
| --- | --- | --- | --- |
| S1 | completed | Move generic workflow docs into `CORE/` | `CORE` files exist |
| S2 | completed | Move reusable Vapor backend docs into `PRESETS/vapor-backend/` | preset files exist |
| S3 | completed | Move cross-border ecommerce docs into `PRESETS/cross-border-ecommerce/` | preset files exist |
| S4 | completed | Move current project state docs into `PROJECT/` | project overlay files exist |
| S5 | completed | Add manifest and layered entry rules | manifest and root rules exist |
| S6 | completed | Remove mixed legacy project rules | no legacy mixed rule file remains |

## 9. Index Updates

- `ai_dev/AIDEV_MANIFEST.md`: created.
- `ai_dev/PROJECT_RULES.md`: recreated as layered entry rules.
- `ai_dev/PROJECT/PROJECT_PROFILE.md`: created.
- `ai_dev/PROJECT/PROJECT_RULES.md`: created.
- `ai_dev/PROJECT/IMPLEMENTATION_MAP.md`: updated.

## 10. Verification Gates

Required:

- Confirm layered files exist.
- Confirm no non-`ai_dev` source files exist.
- Confirm old flat references are not active.
- `git diff --check`.
- `git status --short`.

## 11. Learning / Extension Impact

- Learning record required: no.
- Reason: this is a planned structural upgrade, not an error.

## 12. Review Plan

- Review mode: documentation and workflow structure review.
- Required reviewer focus: reusable layer separation, project-specific overlay
  boundaries, manifest accuracy, and reference path consistency.
- P0/P1 blocking criteria: generic Core files contain project-specific business
  rules, project overlay files are not discoverable, or new project reuse
  guidance is missing.

## 13. Completion Evidence

- Files changed: ai_dev structure and docs.
- Commands run: listed in final response.
- Remaining risks: future extraction to a separate template repository is still a
  later decision.
