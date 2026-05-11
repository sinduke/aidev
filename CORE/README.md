# AI_DEV Core

Core is reusable across project types.

Core owns:

- Workflow modes.
- Task structure.
- Review rules.
- Index registry.
- Git workflow modes.
- Extension and learning loop.

Core must stay free of project-specific business rules and framework-specific
implementation choices.

Current core files:

```text
AI_WORKFLOW.md
TASK_TEMPLATE.md
REVIEW_RULES.md
INDEX_REGISTRY.md
GIT_WORKFLOW.md
EXTENSIONS/
```

When starting a new project, Core can be copied, referenced, or vendored without
rewriting it.
