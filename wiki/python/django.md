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

### 2026 security releases added 2026-11-26 (from Django's release notes)

Every 2026 Django CVE not already listed below, through the 2026-11-03 release. Severity is Django's own rating under its security policy, which is often lower than the GHSA label on the same CVE. Releases before 6.1 final (2026-08-05) were also patched on the 6.1 pre-release branch, so 6.1.0 includes them. Django 4.2 reached end of support after 4.2.30 and is not listed for later fixes.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-108147 | Low (Django) | Potential memory exhaustion in `MultiPartParser` via base64-encoded file upload. Released 2026-11-03. | 5.2.19, 6.0.10, 6.1.3 | [Django security release](https://www.djangoproject.com/weblog/2026/nov/03/security-releases/) |
| CVE-2026-111211 | Low (Django) | Potential log injection via unescaped geometry form values. Released 2026-11-03. | 5.2.19, 6.0.10, 6.1.3 | [Django security release](https://www.djangoproject.com/weblog/2026/nov/03/security-releases/) |
| CVE-2026-111362 | Moderate (Django) | Server-side request forgery via `crs` member of GeoJSON geometries. Released 2026-11-03. | 5.2.19, 6.0.10, 6.1.3 | [Django security release](https://www.djangoproject.com/weblog/2026/nov/03/security-releases/) |
| CVE-2026-113593 | Low (Django) | Potential exposure of private data via empty and missing `Vary` headers. Released 2026-11-03. | 5.2.19, 6.0.10, 6.1.3 | [Django security release](https://www.djangoproject.com/weblog/2026/nov/03/security-releases/) |
| CVE-2026-113733 | Low (Django) | Password hash disclosure to "view only" admin users with custom user models. Released 2026-11-03. | 6.0.10, 6.1.3 | [Django security release](https://www.djangoproject.com/weblog/2026/nov/03/security-releases/) |
| CVE-2026-114582 | Low (Django) | Server-side request forgery via `SpatialReference` string input. Released 2026-11-03. | 5.2.19, 6.0.10, 6.1.3 | [Django security release](https://www.djangoproject.com/weblog/2026/nov/03/security-releases/) |
| CVE-2026-77050 | Low (Django) | Potential denial-of-service vulnerability in `get_supported_language_variant()`. Released 2026-10-06. | 5.2.18, 6.0.9, 6.1.2 | [Django security release](https://www.djangoproject.com/weblog/2026/oct/06/security-releases/) |
| CVE-2026-84429 | Moderate (Django) | Potential denial-of-service vulnerability in HTTP header parsing. Released 2026-10-06. | 5.2.18, 6.0.9, 6.1.2 | [Django security release](https://www.djangoproject.com/weblog/2026/oct/06/security-releases/) |
| CVE-2026-87890 | Moderate (Django) | Potential request forgery via spatial lookup byte values. Released 2026-10-06. | 5.2.18, 6.0.9, 6.1.2 | [Django security release](https://www.djangoproject.com/weblog/2026/oct/06/security-releases/) |
| CVE-2026-87975 | Moderate (Django) | Privilege abuse in model formsets with editable primary keys. Released 2026-10-06. | 5.2.18, 6.0.9, 6.1.2 | [Django security release](https://www.djangoproject.com/weblog/2026/oct/06/security-releases/) |
| CVE-2026-15307 | High (Django) | Server-side file-write and request forgery via spatial lookups. Released 2026-08-04. | 5.2.17, 6.0.8 | [Django security release](https://www.djangoproject.com/weblog/2026/aug/04/security-releases/) |
| CVE-2026-15337 | Low (Django) | Potential denial-of-service vulnerability in `check_for_language()`. Released 2026-08-04. | 5.2.17, 6.0.8 | [Django security release](https://www.djangoproject.com/weblog/2026/aug/04/security-releases/) |
| CVE-2026-15830 | Moderate (Django) | Potential denial-of-service vulnerability via nested geometry collections. Released 2026-08-04. | 5.2.17, 6.0.8 | [Django security release](https://www.djangoproject.com/weblog/2026/aug/04/security-releases/) |
| CVE-2026-15920 | Moderate (Django) | Potential cross-site scripting via `URLField` values in the admin. Released 2026-08-04. | 5.2.17, 6.0.8 | [Django security release](https://www.djangoproject.com/weblog/2026/aug/04/security-releases/) |
| CVE-2026-48588 | Low (Django) | Potential exposure of private data via cached `Set-Cookie` response. Released 2026-07-07. | 5.2.16, 6.0.7 | [Django security release](https://www.djangoproject.com/weblog/2026/jul/07/security-releases/) |
| CVE-2026-53877 | Low (Django) | Heap buffer over-read in `GDALRaster`. Released 2026-07-07. | 5.2.16, 6.0.7 | [Django security release](https://www.djangoproject.com/weblog/2026/jul/07/security-releases/) |
| CVE-2026-53878 | Low (Django) | Header injection possibility since `DomainNameValidator` accepted newlines in input. Released 2026-07-07. | 5.2.16, 6.0.7 | [Django security release](https://www.djangoproject.com/weblog/2026/jul/07/security-releases/) |
| CVE-2026-6873 | Low (Django) | Signed cookie salt namespace collision. Released 2026-06-03. | 5.2.15, 6.0.6 | [Django security release](https://www.djangoproject.com/weblog/2026/jun/03/security-releases/) |
| CVE-2026-7666 | Low (Django) | Potential unencrypted email transmission via `STARTTLS` in the SMTP backend. Released 2026-06-03. | 5.2.15, 6.0.6 | [Django security release](https://www.djangoproject.com/weblog/2026/jun/03/security-releases/) |
| CVE-2026-8404 | Low (Django) | Potential exposure of private data via case-sensitive `Cache-Control` directives. Released 2026-06-03. | 5.2.15, 6.0.6 | [Django security release](https://www.djangoproject.com/weblog/2026/jun/03/security-releases/) |
| CVE-2026-35193 | Low (Django) | Potential exposure of private data via missing `Vary: Authorization`. Released 2026-06-03. | 5.2.15, 6.0.6 | [Django security release](https://www.djangoproject.com/weblog/2026/jun/03/security-releases/) |
| CVE-2026-48587 | Low (Django) | Potential exposure of private data via whitespace padding in `Vary` header. Released 2026-06-03. | 5.2.15, 6.0.6 | [Django security release](https://www.djangoproject.com/weblog/2026/jun/03/security-releases/) |
| CVE-2026-4277 | Low (Django) | Privilege abuse in `GenericInlineModelAdmin`. Released 2026-04-07. | 4.2.30, 5.2.13, 6.0.4 | [Django security release](https://www.djangoproject.com/weblog/2026/apr/07/security-releases/) |
| CVE-2026-4292 | Low (Django) | Privilege abuse in `ModelAdmin.list_editable`. Released 2026-04-07. | 4.2.30, 5.2.13, 6.0.4 | [Django security release](https://www.djangoproject.com/weblog/2026/apr/07/security-releases/) |
| CVE-2026-25673 | Moderate (Django) | Potential denial-of-service vulnerability in `URLField` via Unicode normalization on Windows. Released 2026-03-03. | 4.2.29, 5.2.12, 6.0.3 | [Django security release](https://www.djangoproject.com/weblog/2026/mar/03/security-releases/) |
| CVE-2026-25674 | Low (Django) | Potential incorrect permissions on newly created file system objects. Released 2026-03-03. | 4.2.29, 5.2.12, 6.0.3 | [Django security release](https://www.djangoproject.com/weblog/2026/mar/03/security-releases/) |
| CVE-2025-13473 | Low (Django) | Username enumeration through timing difference in mod_wsgi authentication handler. Released 2026-02-03. | 4.2.28, 5.2.11, 6.0.2 | [Django security release](https://www.djangoproject.com/weblog/2026/feb/03/security-releases/) |
| CVE-2025-14550 | Moderate (Django) | Potential denial-of-service vulnerability via repeated headers when using ASGI. Released 2026-02-03. | 4.2.28, 5.2.11, 6.0.2 | [Django security release](https://www.djangoproject.com/weblog/2026/feb/03/security-releases/) |
| CVE-2026-1285 | Moderate (Django) | Potential denial-of-service vulnerability in `django.utils.text.Truncator` HTML methods. Released 2026-02-03. | 4.2.28, 5.2.11, 6.0.2 | [Django security release](https://www.djangoproject.com/weblog/2026/feb/03/security-releases/) |

### Earlier mapped records (GHSA severity)

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
- From June to November 2026 Django shipped five security releases with 22 CVEs (1 high, 6 moderate, 15 low by Django's rating). The one high, CVE-2026-15307 (2026-08-04), allows server-side file write and request forgery through GIS spatial lookups. GeoDjango (`django.contrib.gis`, including GDAL raster handling) accounts for 7 of the 22, including two SSRF fixes on 2026-11-03 (CVE-2026-111362 GeoJSON `crs`, CVE-2026-114582 `SpatialReference` strings). Cache-header private-data exposure (`Vary`, `Cache-Control`, `Set-Cookie`) recurs in 5 of them. No Django CVE is in CISA KEV (catalog 2026.11.25).
- Django's 5.2.20, 6.0.11 and 6.1.4 release notes, dated 2026-12-02, pre-announce two "high", one "moderate" and four "low" security fixes. Details are not yet published, so they are not mapped here.
- Deployments should not rely solely on Django application-level upload limits; Django's 2026 advisories explicitly reinforce using web-server or gateway-level request-size limits.
- Cache middleware, session settings, ASGI header normalization, and reverse-proxy behavior remain security-sensitive deployment boundaries even when application code is otherwise straightforward.

## Dependencies of Note

- Database backends are security-relevant because several advisories are PostgreSQL-, MySQL / MariaDB-, Oracle-, or PostGIS-specific.
- ASGI server / reverse-proxy behavior affects header, `Content-Length`, and upload-limit enforcement boundaries.
- Template filters, HTML helpers, serializers, validators, and archive extraction utilities recur in DoS, traversal, XSS, and resource-exhaustion records.

## Open Questions

- Map the 2026-12-02 Django security release (5.2.20 / 6.0.11 / 6.1.4) once its CVEs are published.
- Add GHSA IDs to the 2026-11-26 rows; this pass cited Django's own release notes and weblog posts only.
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
*Last updated: 2026-11-26 | Sources: 10 (django/django `docs/releases/security.txt` and per-release notes via GitHub, Django security weblog posts, CISA KEV catalog 2026.11.25, OSV package query, GitHub Advisory Database API, Django security archive, Django 5.2 release notes, Django security policy, PyPI metadata, public CVE aliases)*
