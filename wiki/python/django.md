# Django (python)

**Registry:** PyPI
**Weekly Downloads:** unknown (PyPIStats rate-limited during this pass)
**Repository:** https://github.com/django/django
**Security Contact:** security@djangoproject.com / https://docs.djangoproject.com/en/dev/internals/security/
**Disclosure Policy:** https://docs.djangoproject.com/en/dev/internals/security/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-08 | OpenClaw recurring review | package advisory history | public-source advisory mapping using OSV package query, GitHub Advisory Database records, Django security archive, Django release notes, PyPI metadata, and public CVE aliases | 152 unique CVE/GHSA-style public records observed in OSV for `django`; representative rows curated across SQL injection, ASGI/header boundary issues, upload/resource-limit bypasses, cache/session exposure, path traversal, user enumeration, and recurrent denial-of-service surfaces | https://osv.dev/list?ecosystem=PyPI&q=django |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-w26r-rmm8-9c29 / CVE-2026-5766 | Medium | ASGI requests with missing or understated `Content-Length` could bypass `FILE_UPLOAD_MAX_MEMORY_SIZE`, potentially loading large files into memory. | 5.2.14, 6.0.5 | https://github.com/advisories/GHSA-w26r-rmm8-9c29 |
| GHSA-5hrc-gvxj-w55p / CVE-2026-6907 | Low | `UpdateCacheMiddleware` could cache responses with `Vary: *`, creating private-data exposure risk from public cache entries. | 5.2.14, 6.0.5 | https://github.com/advisories/GHSA-5hrc-gvxj-w55p |
| GHSA-7h2m-m8vj-598h / CVE-2026-35192 | Low | Session fixation risk with cached public pages when `SESSION_SAVE_EVERY_REQUEST` was enabled and cookie variation was not reflected. | 5.2.14, 6.0.5 | https://github.com/advisories/GHSA-7h2m-m8vj-598h |
| GHSA-mvfq-ggxm-9mc5 / CVE-2026-3902 | High | ASGI header spoofing via underscore / hyphen conflation could undermine header-based trust boundaries. | 4.2.30, 5.2.13, 6.0.4 | https://github.com/advisories/GHSA-mvfq-ggxm-9mc5 |
| GHSA-933h-hp56-hf7m / CVE-2026-33034 | High | ASGI requests with missing or understated `Content-Length` could bypass `DATA_UPLOAD_MAX_MEMORY_SIZE` and exhaust memory. | 4.2.30, 5.2.13, 6.0.4 | https://github.com/advisories/GHSA-933h-hp56-hf7m |
| GHSA-5mf9-h53q-7mhq / CVE-2026-33033 | Medium | `MultiPartParser` could be abused for denial of service through crafted base64-encoded file uploads. | 4.2.30, 5.2.13, 6.0.4 | https://github.com/advisories/GHSA-5mf9-h53q-7mhq |
| GHSA-6426-9fv3-65x8 / CVE-2026-1312 | Medium | Potential SQL injection through `QuerySet.order_by()` and `FilteredRelation` paths. | 4.2.28, 5.2.11, 6.0.2 | https://github.com/advisories/GHSA-6426-9fv3-65x8 |
| GHSA-gvg8-93h5-g6qq / CVE-2026-1287 | High | Potential SQL injection in column aliases via control characters. | 4.2.28, 5.2.11, 6.0.2 | https://github.com/advisories/GHSA-gvg8-93h5-g6qq |
| GHSA-mwm9-4648-f68q / CVE-2026-1207 | High | Potential SQL injection via raster lookups on PostGIS. | 4.2.28, 5.2.11, 6.0.2 | https://github.com/advisories/GHSA-mwm9-4648-f68q |
| GHSA-frmv-pr5f-9mcr / CVE-2025-64459 | Critical | SQL injection via `_connector` keyword argument in `QuerySet` and `Q` objects. | 4.2.26, 5.1.14, 5.2.8 | https://github.com/advisories/GHSA-frmv-pr5f-9mcr |
| GHSA-qw25-v68c-qjf3 / CVE-2025-64458 | High | Denial of service in `HttpResponseRedirect` and `HttpResponsePermanentRedirect` on Windows due to costly Unicode normalization. | 4.2.26, 5.1.14, 5.2.8 | https://github.com/advisories/GHSA-qw25-v68c-qjf3 |
| GHSA-hpr9-3m2g-3j9p / CVE-2025-59681 | High | Potential SQL injection in `QuerySet.annotate()`, `alias()`, `aggregate()`, and `extra()` column aliases on MySQL / MariaDB. | 4.2.25, 5.1.13, 5.2.7 | https://github.com/advisories/GHSA-hpr9-3m2g-3j9p |
| GHSA-m9g8-fxxm-xg86 / CVE-2024-53908 | High | SQL injection in `HasKey(lhs, rhs)` on Oracle. | 4.2.17, 5.0.10, 5.1.4 | https://github.com/advisories/GHSA-m9g8-fxxm-xg86 |
| GHSA-pv4p-cwwg-4rph / CVE-2024-42005 | Critical | SQL injection through `QuerySet.values()` and `values_list()` paths on `JSONField`. | 4.2.15, 5.0.8 | https://github.com/advisories/GHSA-pv4p-cwwg-4rph |
| GHSA-9jmf-237g-qf46 / CVE-2024-39330 | High | Path traversal in `django.core.files.storage.Storage.save()` with suitable file names. | 4.2.14, 5.0.7 | https://github.com/advisories/GHSA-9jmf-237g-qf46 |

*Full advisory history: https://osv.dev/list?ecosystem=PyPI&q=django and https://docs.djangoproject.com/en/dev/releases/security/*

## Security Posture Notes

- Django has a mature, public security process with a documented reporting address, supported-version policy, announcement channel, security archive, and per-issue patch links.
- The public record is large and active. This page intentionally curates representative classes rather than attempting to duplicate every Django CVE from the upstream archive.
- Recent 2025-2026 records cluster around ORM / SQL-construction edge cases, ASGI request-header and upload-size trust boundaries, Windows-specific Unicode normalization DoS, admin privilege boundaries, cache/session exposure, and parser / serializer resource exhaustion.
- SQL injection advisories are often backend- or API-specific (`JSONField`, PostGIS raster lookups, Oracle `HasKey`, FilteredRelation aliases, `_connector`), so downstream risk depends heavily on database backend and whether user-controlled dictionaries / aliases / lookup expressions reach ORM construction APIs.
- Deployments should not rely solely on Django application-level upload limits; Django's 2026 advisories explicitly reinforce using web-server or gateway-level request-size limits.
- Cache middleware, session settings, ASGI header normalization, and reverse-proxy behavior remain security-sensitive deployment boundaries even when application code is otherwise straightforward.

## Dependencies of Note

- Database backends are security-relevant because several advisories are PostgreSQL-, MySQL / MariaDB-, Oracle-, or PostGIS-specific.
- ASGI server / reverse-proxy behavior affects header, `Content-Length`, and upload-limit enforcement boundaries.
- Template filters, HTML helpers, serializers, validators, and archive extraction utilities recur in DoS, traversal, XSS, and resource-exhaustion records.

## Open Questions

- Should this page be split later into a timeline page for Django's dense 2024-2026 security-release cadence?
- Which downstream frameworks and internal platforms pin unsupported Django series that were not evaluated in newer advisories?
- Are there package-specific hardening guides worth linking for common deployment profiles such as ASGI behind nginx, admin-heavy applications, and multi-tenant cache setups?

## Related Pages

- [[python/flask]]
- [[python/fastapi]]
- [[python/starlette]]
- [[python/sqlalchemy]]
- [[python/index]]

---
*Last updated: 2026-05-08 | Sources: 7 (OSV package query, GitHub Advisory Database API, Django security archive, Django 5.2 release notes, Django security policy, PyPI metadata, public CVE aliases)*
