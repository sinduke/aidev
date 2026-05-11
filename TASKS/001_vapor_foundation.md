# 001 Vapor Foundation

Status: example

Execution Type: Reference example, not executed in this repository.

## 1. Goal

Create the first runnable Vapor backend foundation for the cross-border B2B2C
commerce system.

The foundation should include:

- Vapor project skeleton.
- PostgreSQL configuration.
- Redis configuration.
- Docker Compose local development.
- Health check API.
- Unified API response envelope.
- Central error mapping.
- Request ID and baseline logging.
- Initial test and verification gates.

## 2. Non-Goals

- Do not implement auth/RBAC.
- Do not implement merchant, catalog, order, payment, or fulfillment business
  modules.
- Do not create production deployment infrastructure.
- Do not connect to real Stripe, Mabang, or external providers.
- Do not build admin frontend pages.

## 3. Business Context

- First-phase business line: this task creates the backend foundation required
  before admin login, merchant management, product import, mobile APIs, payment,
  and fulfillment can be implemented.
- User value: future API tasks can be built and verified against a running local
  service instead of only planned contracts.
- Operational value: health, config, logging, error mapping, database, and Redis
  conventions become stable before business modules depend on them.

## 4. Mode History

- Exploration: inspect current repo, enabled presets, project Git workflow,
  planned source roots, and foundation feature `F-001`.
- Decision: confirm PostgreSQL/Redis defaults, Docker layout, API envelope shape,
  error response shape, and module bootstrap boundary.
- Task: persist this file under `TASKS/001_vapor_foundation.md`.
- Build: execute only after the user confirms Build mode.
- Review: verify source layout, API contract, indexes, tests, and local commands.
- Close: record completion evidence and update feature/test status.

## 5. Dependencies

- Prior tasks:
  - `000_project_rules_and_architecture`
  - `000A_ai_development_workflow`
  - `000D_aidev_layered_template`
  - `000E_aidev_contract_indexes`
  - `000F_git_workflow_modes`
  - `000G_aidev_validation_tooling`
- Required decisions:
  - D-0002 Vapor modular monolith.
  - D-0004 PostgreSQL default unless compatibility requires MySQL.
- Required credentials/services:
  - local PostgreSQL container.
  - local Redis container.
- Required docs:
  - `PRESETS/vapor-backend/ARCHITECTURE.md`
  - `PRESETS/vapor-backend/SECURITY_RULES.md`
  - `PRESETS/vapor-backend/OBSERVABILITY_RULES.md`
  - `PRESETS/vapor-backend/TESTING_RULES.md`
  - `PROJECT/FEATURE_MAP.md`
  - `PROJECT/API_ROUTE_MAP.md`
  - `PROJECT/FUNCTION_SIGNATURE_INDEX.md`
  - `PROJECT/DTO_CONTRACT_INDEX.md`
  - `PROJECT/CONFIG_ENV_INDEX.md`
  - `PROJECT/TEST_VERIFICATION_MATRIX.md`

## 6. Assumptions and Open Questions

- Type: assumption
  Question: Should v1 use PostgreSQL?
  Current default: yes, unless the user explicitly switches to MySQL for
  ECShopX compatibility.
  Owner: user / technical decision.
  Required before: creating migrations.

- Type: assumption
  Question: Should Redis be introduced in the foundation task?
  Current default: yes for cache/queue readiness, but no business queues are
  implemented yet.
  Owner: technical decision.
  Required before: Docker Compose finalization.

- Type: later_decision
  Question: What is the production deployment platform?
  Current default: local Docker only in this task.
  Owner: user / operations.
  Required before: production deployment work.

## 7. Affected Areas

- Modules: Foundation.
- Domain concepts: health status, API response, application error.
- Database: connection configuration only.
- API: health check endpoint.
- Functions/contracts: app configuration, health service, response envelope,
  error mapper.
- DTO/data: health response, error response, API envelope.
- Permissions: none.
- State machines: none.
- Integrations: PostgreSQL, Redis.
- Security: error redaction, secret handling, safe config defaults.
- Observability: request ID, structured logs, health event.
- Admin frontend: none.
- Config/env: database, Redis, JWT placeholder if needed later, app environment.
- Tests: health route, response envelope, error mapping, config loading.

## 8. Write Scope

Allowed files/directories:

- `Package.swift`
- `Sources/App/`
- `Tests/AppTests/`
- `docker-compose.yml`
- `.env.example`
- `.gitignore`
- `README.md`
- `PROJECT/FILE_MAP.md`
- `PROJECT/IMPLEMENTATION_MAP.md`
- `PROJECT/API_ROUTE_MAP.md`
- `PROJECT/FUNCTION_SIGNATURE_INDEX.md`
- `PROJECT/DTO_CONTRACT_INDEX.md`
- `PROJECT/CONFIG_ENV_INDEX.md`
- `PROJECT/TEST_VERIFICATION_MATRIX.md`
- `PROJECT/DECISION_LOG.md`
- `PROJECT/RISK_REGISTER.md`
- `TASKS/001_vapor_foundation.md`

Forbidden files/directories:

- Merchant, catalog, order, payment, fulfillment business modules.
- Admin frontend source files.
- Real provider credentials.
- Production deployment manifests.

Scope expansion rule:

- Stop and update this task before editing files outside allowed scope.

## 9. Git Workflow

- Branch Mode: feature_branch
- Base Branch: main
- Working Branch: feature/001-vapor-foundation
- Merge Target: main
- Branch Required: yes
- Reason: this is the first non-trivial source-code task and should be reviewed
  before merging.

## 10. Implementation Steps

| Step ID | Status | Description | Allowed Files | Verification | Pause After |
| --- | --- | --- | --- | --- | --- |
| S1 | pending | Create Vapor package skeleton and app entrypoints | `Package.swift`, `Sources/App/`, `Tests/AppTests/` | `swift build` | no |
| S2 | pending | Add configuration loading for app, database, and Redis | `Sources/App/Foundation/Config/`, `.env.example` | config unit tests | no |
| S3 | pending | Add PostgreSQL and Redis Docker Compose services | `docker-compose.yml`, `.env.example` | `docker compose config` | no |
| S4 | pending | Add health check route and DTO | `Sources/App/Foundation/Health/` | health route test and curl example | no |
| S5 | pending | Add API response envelope and central error mapper | `Sources/App/Foundation/HTTP/` | response/error tests | no |
| S6 | pending | Add request ID middleware and baseline logging | `Sources/App/Foundation/Observability/` | request ID test/log review | no |
| S7 | pending | Update project indexes and documentation | `PROJECT/*.md`, task file, README if needed | `./bin/aidev check` | no |
| S8 | pending | Run final verification and record evidence | task file | `swift build`, `swift test`, `git diff --check`, `./bin/aidev check` | yes |

## 11. Data Model Changes

- Tables: none in foundation unless Vapor/Fluent requires migration scaffolding.
- Columns: none.
- Indexes: none.
- Constraints: none.
- Migrations: none.
- Seed/test data: none.

## 12. API Changes

- Endpoints:
  - `GET /health`
- Auth:
  - none.
- Permissions:
  - none.
- Request DTOs:
  - none.
- Response DTOs:
  - `HealthCheckResponse`
  - `APIResponse<HealthCheckResponse>`
  - `APIErrorResponse`
- Error codes:
  - `internal_error`
  - `validation_error`
  - `not_found`
  - `unauthorized`
  - `forbidden`
- Curl examples:
  - `curl http://localhost:8080/health`

## 13. Function and Data Contract Changes

- Function signatures:
  - `configure(_ app: Application) async throws`
  - `registerRoutes(_ app: Application) throws`
  - `HealthController.show(req:) async throws -> APIResponse<HealthCheckResponse>`
  - `AppErrorMiddleware.respond(to:chainingTo:) -> EventLoopFuture<Response>`
- Use case inputs/results:
  - `GetHealthStatus` returns service/database/cache readiness.
- Repository protocol methods:
  - none.
- Provider protocol methods:
  - none.
- DTO fields:
  - `HealthCheckResponse.status`
  - `HealthCheckResponse.service`
  - `HealthCheckResponse.version`
  - `HealthCheckResponse.timestamp`
  - `APIResponse.success`
  - `APIResponse.data`
  - `APIResponse.error`
  - `APIResponse.requestId`
- Sensitive fields:
  - database password and Redis password must not be logged.
- State machine transitions:
  - none.
- Config/env keys:
  - `APP_ENV`
  - `APP_HOST`
  - `APP_PORT`
  - `DATABASE_URL`
  - `REDIS_URL`
  - `LOG_LEVEL`

## 14. Integration Changes

- Provider: PostgreSQL and Redis local services.
- Protocol: configuration and connection setup.
- Mock/fake implementation: test app configuration.
- Real implementation: local Docker services.
- Outbox/inbox: none.
- Retry/dead-letter: none.
- Manual compensation: restart Docker services and rerun migrations when added
  in future tasks.

## 15. Security Requirements

- Auth: none for health check.
- RBAC: none.
- Object-level authorization: none.
- PII: none.
- Secret handling: `.env.example` must not contain real credentials.
- Upload/webhook validation: none.
- Error handling: internal errors must not leak stack traces or secrets in
  production-style responses.

## 16. Observability Requirements

- Request logs: include method, path, status, duration, and request ID.
- Audit logs: none.
- Business events: none.
- Integration attempts: database/Redis readiness may be logged at startup or
  health check level without leaking secrets.
- Payment events: none.
- Metrics: defer real metrics until observability feature work.

## 17. Index Updates

- `PROJECT/FEATURE_MAP.md`: move `F-001` through implementation status when
  source is created.
- `PROJECT/FILE_MAP.md`: add every created source/test/config file.
- `PROJECT/IMPLEMENTATION_MAP.md`: add foundation architecture placement.
- `PROJECT/API_ROUTE_MAP.md`: add `GET /health`.
- `PROJECT/FUNCTION_SIGNATURE_INDEX.md`: add foundation function signatures.
- `PROJECT/DTO_CONTRACT_INDEX.md`: add health, API response, and error DTOs.
- `PROJECT/CONFIG_ENV_INDEX.md`: add app/database/Redis/log env keys.
- `PROJECT/TEST_VERIFICATION_MATRIX.md`: add health, response, error, and
  request ID tests.
- `PROJECT/DECISION_LOG.md`: confirm or revise PostgreSQL/Redis decisions.
- `PROJECT/RISK_REGISTER.md`: update database and branch workflow risks.

## 18. Verification Gates

Required:

- `swift build`
- `swift test`
- `docker compose config`
- `git diff --check`
- `./bin/aidev check`
- `curl http://localhost:8080/health` after local server starts

Optional / not available:

- Production deployment verification: not in scope.
- Real provider integration tests: not in scope.

## 19. Rollback / Compensation

- Code rollback: revert created Vapor source, tests, Docker, and config files.
- Migration rollback: none expected in this task.
- Data compensation: none.
- Provider compensation: stop local Docker services.

## 20. Review Plan

- Review mode: source foundation review.
- Required reviewer focus: Vapor layering, config safety, response/error
  consistency, health endpoint contract, source/index sync, and verification
  evidence.
- P0/P1 blocking criteria: app cannot build, tests fail, health endpoint is not
  registered, secrets are logged, errors leak internal details, or indexes are
  not updated.

## 21. Learning / Extension Impact

- Did this task encounter a meaningful error, repeated issue, P0/P1 finding,
  failed critical verification, or scope drift? To be filled during real
  execution.
- Learning record required: to be determined during Review.
- Error knowledge base entry: to be determined.
- Pattern library update: possible if Vapor foundation layout becomes reusable.
- Workflow improvement update: possible if task/check workflow is too heavy.
- Preventive rule/test/check: add tests for every foundation behavior.
- Similar risks checked: config, error mapping, and index sync.

## 22. Completion Evidence

- Files changed: not executed in this repository.
- Commands run: not executed in this repository.
- Results: this is a reference task example.
- Remaining risks: real execution must still create source files, run Swift
  commands, update indexes, and pass Review before Close.
