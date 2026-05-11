# Error Review Template

Use this template when a meaningful error, review finding, or failed verification
requires a learning record.

```markdown
### E-XXXX <Short Title>

Status: open | fixed | prevented | accepted_risk | superseded
Date: YYYY-MM-DD
Source:
Severity: P0 | P1 | P2 | P3
Category:
Module:
Layer:
Pattern ID:
Learning Decision: no_record | light_note | full_learning_record | workflow_extension
Detection Signal:

Concrete Issue:

- <What happened exactly?>

Impact:

- <What could break?>

Root Cause:

- <Why did it happen?>

Abstraction:

- <What reusable class of problem does this represent?>

Similar Risks Checked:

- <Same module/layer/provider/state/API/security boundary/etc.>

Search Scope:

- <Files/modules/docs checked for similar risks.>

Fix Applied:

- <Immediate fix or reason it is deferred.>

Preventive Rule:

- <Rule/checklist/template/test update that prevents recurrence.>

Regression Gate:

- <Test, command, review check, automation, or documented reason impossible.>

Superseded By:

- <Entry/rule/pattern that replaces this, or None.>

Review After:

- <Task, date, phase, or condition.>

Follow-up Task:

- <Task id or None.>

Related Files:

- `<path>`

Related Tasks:

- `<task id>`
```
