# Config and Environment Index

## 1. Purpose

This file records configuration and environment variables for the current
project.

Any task that introduces a new environment variable, secret, external service
configuration, or runtime flag must update this file.

## 2. Status Values

- `planned`
- `required`
- `implemented`
- `verified`
- `deprecated`

## 3. Config Contract Template

```text
Key:
Purpose:
Type:
Required In:
Default:
Secret:
Source:
Used By:
Validation:
Redaction:
Status:
```

## 4. Planned Application Config

| Key | Purpose | Type | Required In | Default | Secret | Used By | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `APP_ENV` | Runtime environment | string | all | `development` | no | bootstrap/config | planned |
| `APP_PORT` | HTTP port | int | local/deploy | `8080` | no | Vapor server | planned |
| `APP_BASE_URL` | Public base URL | string | staging/prod | none | no | links/webhooks/admin docs | planned |
| `LOG_LEVEL` | Log verbosity | string | all | `info` | no | logging | planned |
| `REQUEST_ID_HEADER` | Request ID header name | string | all | `X-Request-ID` | no | request middleware | planned |

## 5. Planned Database and Cache Config

| Key | Purpose | Type | Required In | Default | Secret | Used By | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `DATABASE_URL` | PostgreSQL connection URL | string | all non-test envs | none | yes | Fluent/Postgres | planned |
| `TEST_DATABASE_URL` | Test database URL | string | test | none | yes | tests | planned |
| `REDIS_URL` | Redis connection URL | string | dev/staging/prod | none | yes | queues/cache | planned |

## 6. Planned Auth Config

| Key | Purpose | Type | Required In | Default | Secret | Used By | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `JWT_SIGNING_SECRET` | JWT signing key | string | all non-test envs | none | yes | Auth | planned |
| `JWT_ISSUER` | JWT issuer | string | all | project service name | no | Auth | planned |
| `JWT_ACCESS_TOKEN_TTL_SECONDS` | Access token TTL | int | all | `3600` | no | Auth | planned |
| `PASSWORD_HASH_COST` | Password hash cost | int | all | framework/default chosen in task | no | Auth | planned |

## 7. Planned Stripe Config

| Key | Purpose | Type | Required In | Default | Secret | Used By | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `STRIPE_SECRET_KEY` | Stripe API secret | string | payment enabled envs | none | yes | Stripe provider | planned |
| `STRIPE_WEBHOOK_SECRET` | Stripe webhook signing secret | string | payment enabled envs | none | yes | Stripe webhook | planned |
| `STRIPE_API_VERSION` | Stripe API version override | string | optional | provider default | no | Stripe provider | planned |

## 8. Planned Fulfillment Provider Config

| Key | Purpose | Type | Required In | Default | Secret | Used By | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `FULFILLMENT_PROVIDER` | Active fulfillment provider | string | fulfillment enabled envs | `mock` | no | Integration/Fulfillment | planned |
| `MABANG_BASE_URL` | Mabang-like API base URL | string | Mabang enabled envs | none | no | Mabang provider | planned |
| `MABANG_APP_KEY` | Mabang-like app key | string | Mabang enabled envs | none | yes | Mabang provider | planned |
| `MABANG_APP_SECRET` | Mabang-like app secret | string | Mabang enabled envs | none | yes | Mabang provider | planned |

## 9. Planned Object Storage Config

| Key | Purpose | Type | Required In | Default | Secret | Used By | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `OBJECT_STORAGE_PROVIDER` | Storage provider | string | file upload envs | `local` | no | object storage | planned |
| `OBJECT_STORAGE_BUCKET` | Storage bucket/container | string | non-local storage | none | no | object storage | planned |
| `OBJECT_STORAGE_ENDPOINT` | S3-compatible endpoint | string | S3-compatible storage | none | no | object storage | planned |
| `OBJECT_STORAGE_ACCESS_KEY` | Storage access key | string | non-local storage | none | yes | object storage | planned |
| `OBJECT_STORAGE_SECRET_KEY` | Storage secret key | string | non-local storage | none | yes | object storage | planned |
| `LOCAL_STORAGE_PATH` | Local file storage path | string | local/dev | `.data/storage` | no | local storage | planned |

## 10. Redaction Rules

Always redact values whose key contains:

- `SECRET`
- `TOKEN`
- `PASSWORD`
- `ACCESS_KEY`
- `PRIVATE_KEY`
- `DATABASE_URL`
- `REDIS_URL`

Do not print full provider payloads or full connection strings in logs.

## 11. Review Rules

Before closing a task that adds config:

- Config key exists here.
- Secret status is explicit.
- Required environments are listed.
- Startup validation behavior is documented.
- Tests or local verification cover missing/invalid required config where
  practical.
