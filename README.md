# AI_DEV Layered System

## How To Use

这一节是实际使用入口。以后不管是新项目、新任务、修复、Review，还是开启
feature 分支 / 多 AI 并行开发，都先看这里。

### 1. 先理解四层结构

AI_DEV 不是一个大规则文件，而是分层的 AI 开发控制系统：

```text
CORE
-> PRESETS
-> PROJECT
-> TASKS
```

四层职责：

| 层级 | 作用 | 常看文件 |
| --- | --- | --- |
| `CORE/` | 通用 AI 工作流、任务模板、Review、索引规则、Git 模式、学习机制 | `AI_WORKFLOW.md`, `TASK_TEMPLATE.md`, `REVIEW_RULES.md`, `INDEX_REGISTRY.md`, `GIT_WORKFLOW.md` |
| `PRESETS/` | 技术栈或业务域通用规则 | `vapor-backend/`, `cross-border-ecommerce/` |
| `PROJECT/` | 当前项目强相关规则、地图、索引、决策、风险 | `PROJECT_PROFILE.md`, `PROJECT_RULES.md`, `*_MAP.md`, `*_INDEX.md` |
| `TASKS/` | 每次真正要执行的任务文件 | `000...md`, `001...md` |

最重要的执行规则：

```text
先发散 -> 再收敛 -> 写入 TASKS -> 按任务执行 -> Review -> 关闭任务
```

不要从聊天记忆直接 Build。
只要进入实现，就必须有明确任务文件。

### 2. 常见入口

| 你要做什么 | 先看什么 | 通常要更新什么 |
| --- | --- | --- |
| 开新项目 | `AIDEV_MANIFEST.md`, `CORE/`, 相关 `PRESETS/` | `PROJECT/PROJECT_PROFILE.md`, `PROJECT/PROJECT_RULES.md`, 项目索引 |
| 开新任务 | `CORE/TASK_TEMPLATE.md`, 当前 `PROJECT/*` 索引 | `TASKS/<task>.md` |
| 做功能 | 当前任务文件、功能/API/函数/DTO/权限/状态机索引 | 源码、测试、相关索引 |
| 修 bug | 当前任务、失败命令、相关索引、学习机制 | 修复、测试、必要时写入 `EXTENSIONS/` |
| 做 Review | `CORE/REVIEW_RULES.md` | findings、风险、任务修正 |
| 多 AI 并行 | `PROJECT/GIT_WORKFLOW.md` | Git 模式、分支、任务 Write Scope |

### 3. 新项目怎么使用

从这套 AI_DEV 开一个新项目时，不要复制后就直接开写代码。先建项目覆盖层。

步骤：

1. 复用 `CORE/`。
2. 选择需要的 `PRESETS/`。
3. 新建或调整 `AIDEV_MANIFEST.md`。
4. 新建 `PROJECT/PROJECT_PROFILE.md`。
5. 新建 `PROJECT/PROJECT_RULES.md`。
6. 按项目类型保留或裁剪 `PROJECT/` 下的索引。
7. 在 `PROJECT/GIT_WORKFLOW.md` 里选择初始 Git 模式。
8. 在 `TASKS/` 下创建第一个任务。

推荐的最小结构：

```text
ai_dev/
  AIDEV_MANIFEST.md
  PROJECT_RULES.md
  CORE/
  PRESETS/
  PROJECT/
    PROJECT_PROFILE.md
    PROJECT_RULES.md
    GIT_WORKFLOW.md
    FEATURE_MAP.md
    FILE_MAP.md
    IMPLEMENTATION_MAP.md
    API_ROUTE_MAP.md
    FUNCTION_SIGNATURE_INDEX.md
    DTO_CONTRACT_INDEX.md
    PERMISSION_INDEX.md
    STATE_MACHINE_INDEX.md
    TEST_VERIFICATION_MATRIX.md
    DECISION_LOG.md
    RISK_REGISTER.md
  TASKS/
```

可以直接这样对 AI 说：

```text
进入 Exploration 模式。
我要基于当前 ai_dev 开一个新的 <项目类型> 项目。
请先读取 AIDEV_MANIFEST、PROJECT_PROFILE、PROJECT_RULES、GIT_WORKFLOW 和相关 PRESETS。
然后告诉我：
1. 哪些 CORE 可以直接复用
2. 需要选择哪些 PRESETS
3. PROJECT 层需要新增、删除、改名哪些文件
4. 第一个 TASK 应该是什么
先不要写代码。
```

### 4. 新任务怎么使用

任何有意义的实现或文档升级，都应该落成任务文件。

标准流程：

1. `Exploration`：发散，分析目标、影响范围、风险、选项。
2. `Decision`：收敛，选定方案，必要时更新 `DECISION_LOG.md` / `RISK_REGISTER.md`。
3. `Task`：写入 `TASKS/<task-id>.md`。
4. `Build`：只按已批准任务文件执行。
5. `Review`：检查 findings、索引、验证、边界、Git workflow。
6. `Close`：补齐完成证据，关闭任务。

任务文件至少要写清楚：

- 目标和非目标。
- 业务背景。
- 影响范围。
- Git Workflow。
- Write Scope。
- Step-by-step 执行步骤。
- API / 函数 / DTO / 权限 / 状态机 / 配置变化。
- 需要更新的索引。
- 验证命令。
- 回滚方式。
- Review 重点。
- Completion Evidence。

创建任务时可以这样说：

```text
进入 Task 模式。
请为 001_vapor_foundation 创建任务文件。
必须使用 CORE/TASK_TEMPLATE.md。
需要覆盖 Vapor 项目骨架、PostgreSQL、Redis、Docker、健康检查、统一响应、错误处理。
任务里要写清楚 Git Workflow、Write Scope、Step IDs、索引更新、验证命令。
只创建 TASKS 文件，创建后暂停，不进入 Build。
```

执行任务时可以这样说：

```text
进入 Build 模式。
严格按照 ai_dev/TASKS/001_vapor_foundation.md 的 Step 顺序执行。
不要跳步。
不要从聊天上下文自由发挥。
如果需要改出 Write Scope 之外的文件，先停下来说明并更新任务。
```

### 5. 修复 / Bug 怎么使用

修 bug 不只是“把当前错误修掉”。
如果错误有复用价值，还要抽象成规则、测试或学习记录。

修复流程：

1. 复现或确认失败现象。
2. 定位失败层级：API、Application、Domain、Infrastructure、Provider、Database、Config、Test、Workflow。
3. 判断是否是索引或契约过期。
4. 在任务范围内修复。
5. 至少检查一个类似风险点。
6. 补测试或验证命令。
7. 判断是否需要写入 `CORE/EXTENSIONS/ERROR_KNOWLEDGE_BASE.md`。

先分析不修改：

```text
进入 Review/Fix 分析模式。
当前 <命令/接口/测试> 失败，错误是：<错误信息>。
请先定位原因，不要直接修改。
需要判断是否影响 API_ROUTE_MAP、FUNCTION_SIGNATURE_INDEX、DTO_CONTRACT_INDEX、
STATE_MACHINE_INDEX、TEST_VERIFICATION_MATRIX 或 GIT_WORKFLOW。
```

确认修复：

```text
确认修复。
请把 finding 转成任务变更或更新当前任务，然后进入 Build。
修复后必须运行相关验证，并检查是否需要写入 EXTENSIONS/ERROR_KNOWLEDGE_BASE.md。
```

### 6. Review 怎么使用

Review 模式只负责发现问题。除非明确说“确认修复”，否则不要改文件。

Review 必查：

- 任务状态和 Step 完成情况。
- Write Scope 是否越界。
- Git Workflow 和分支使用是否符合当前模式。
- `FILE_MAP.md` / `IMPLEMENTATION_MAP.md` 是否同步。
- `FEATURE_MAP.md` 是否同步。
- API / 函数 / DTO / 权限 / 状态机 / 测试 / 配置索引是否同步。
- 领域规则是否被破坏。
- 权限和对象级边界是否完整。
- 幂等性、事务边界、Webhook、支付、履约是否安全。
- 日志、审计、追踪是否覆盖关键路径。
- 验证命令是否真实执行。
- 是否需要学习记录。

Review 示例：

```text
进入 Review 模式。
请 review 当前 ai_dev 和本次变更。
重点看：
1. 是否有空谈
2. 是否有模糊边界
3. 是否缺少索引更新
4. 任务是否可执行
5. Git workflow 是否漏接入
6. 是否能支撑 AI 从 0 到 1 开发大型电商项目
不要修改文件。
```

### 7. Git Workflow 怎么使用

当前项目默认：

```text
git_workflow_mode: simple
```

可选模式：

| 模式 | 什么时候用 |
| --- | --- |
| `simple` | 单人开发、文档阶段、小改动。可不开分支。 |
| `feature_branch` | 正常源码功能开发，需要 Review 后再合并。 |
| `parallel_ai` | 多个 AI 或多个模块并行开发，必须分支或 worktree 隔离。 |

切换到 feature 分支模式：

```text
把当前项目 Git workflow 切换到 feature_branch。
后续 001_vapor_foundation 需要从合适基线创建 feature/001-vapor-foundation。
请更新 PROJECT/GIT_WORKFLOW.md 和相关任务文件。
```

切换到多 AI 并行模式：

```text
开启 parallel_ai 模式。
为 auth、catalog、import 三个任务规划独立 feature 分支或 worktree。
每个任务必须有独立 Write Scope，完成后先 Review 再合并。
```

### 8. 完整示例：开始 001_vapor_foundation

Step 1：发散。

```text
进入 Exploration 模式。
我们准备开始 001_vapor_foundation。
请读取 ai_dev/AIDEV_MANIFEST.md、PROJECT_RULES.md、PROJECT/PROJECT_PROFILE.md、
PROJECT/GIT_WORKFLOW.md、CORE/AI_WORKFLOW.md、CORE/INDEX_REGISTRY.md、
PRESETS/vapor-backend/*。
然后发散分析：
1. 需要创建哪些 Vapor 文件
2. 需要哪些配置
3. 需要哪些 API
4. 哪些索引需要更新
5. 风险和未知点是什么
先不要写代码。
```

Step 2：收敛。

```text
进入 Decision 模式。
请基于刚才的探索，收敛 001_vapor_foundation 的技术方向。
需要明确 PostgreSQL、Redis、Docker、健康检查、统一响应、错误处理的边界。
把需要持久化的决定写入 DECISION_LOG，风险写入 RISK_REGISTER。
```

Step 3：创建任务。

```text
进入 Task 模式。
请创建 ai_dev/TASKS/001_vapor_foundation.md。
必须使用 CORE/TASK_TEMPLATE.md。
任务里要写清楚 Git Workflow、Write Scope、Step IDs、索引更新、验证命令。
创建后暂停，不进入 Build。
```

Step 4：执行。

```text
确认进入 Build。
严格按照 ai_dev/TASKS/001_vapor_foundation.md 的 Step 顺序执行。
如果发现任务外范围，先停下来说明。
```

Step 5：Review。

```text
进入 Review 模式。
请检查 001_vapor_foundation 是否满足任务文件、索引、Git workflow、架构边界和验证要求。
Findings 放最前面，不要直接修复。
```

Step 6：关闭任务。

```text
确认修复 Findings 并关闭任务。
请补齐 Completion Evidence，确认 Verification Gates、Index Updates、
Risk/Decision、Learning Impact 都已经处理。
```

### 9. 常用检查命令

文档阶段常用：

```bash
find ai_dev -name '.DS_Store' -print
git diff --check
rg -n "[ \t]+$" ai_dev || true
git status --short
```

Vapor 源码创建后，通常还需要：

```bash
swift build
swift test
git diff --check
```

This directory is split into reusable and project-specific layers.

## Structure

```text
ai_dev/
  AIDEV_MANIFEST.md
  PROJECT_RULES.md
  CORE/
  PRESETS/
    vapor-backend/
    cross-border-ecommerce/
  PROJECT/
  TASKS/
```

## Why

The project previously used one large `ai_dev` folder. That works for one
project, but it causes duplication when starting new mobile, admin, backend, or
frontend projects.

The new structure separates:

- Generic AI development workflow.
- Reusable technical/domain presets.
- Current project business overlay.
- Current project contract indexes.
- Current project Git workflow mode.
- Current project tasks.

## New Project Usage

For a new project:

1. Reuse `CORE/`.
2. Pick presets from `PRESETS/`.
3. Create a new `AIDEV_MANIFEST.md`.
4. Create a small `PROJECT/PROJECT_PROFILE.md`.
5. Add only project-specific overlay docs, Git workflow choice, and contract
   indexes.

You should not need to regenerate all AI_DEV files for every project.

## Current Project

This project uses:

- `CORE/`
- `PRESETS/vapor-backend/`
- `PRESETS/cross-border-ecommerce/`
- `PROJECT/` overlay for the current cross-border B2B2C Vapor backend.
- `PROJECT/GIT_WORKFLOW.md` with default `simple` mode and optional branch
  isolation.

## Current Project Indexes

The active project contract indexes are under `PROJECT/`:

```text
FEATURE_MAP.md
GIT_WORKFLOW.md
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
DECISION_LOG.md
RISK_REGISTER.md
```
