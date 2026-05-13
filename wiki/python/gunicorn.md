# Gunicorn (python)

**Registry:** PyPI
**Weekly Downloads:** ~30,653,412 (last week, fetched 2026-05-13; PyPIStats)
**Repository:** https://github.com/benoitc/gunicorn
**Security Contact:** GitHub Security Advisories / repository security policy
**Disclosure Policy:** https://github.com/benoitc/gunicorn/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | package advisory history | public-source curation using OSV package queries, GitHub Advisory Database records surfaced through OSV, public CVE/NVD aliases, upstream issue / PR / commit references, PyPI metadata, PyPIStats downloads, and repository security-policy evidence | Added a new advisory-mapped page for Gunicorn's compact public vulnerability history across CRLF response/header injection and HTTP request/response-smuggling parser-boundary issues. | https://osv.dev/list?ecosystem=PyPI&q=gunicorn |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-1000164 / GHSA-32pc-xphx-q4f6 / PYSEC-2018-55 | High | HTTP header handling allowed CRLF sequences in header values, enabling header injection / response splitting when attacker-controlled data reached response headers. | 19.5.0 | https://github.com/advisories/GHSA-32pc-xphx-q4f6 |
| CVE-2024-1135 / GHSA-w3h3-4rj7-4ph4 | High | Public records describe request smuggling that could lead to endpoint-restriction bypass; OSV links the fix to the 22.0.0 parser hardening train and upstream PR `#3113`. | 22.0.0 | https://github.com/advisories/GHSA-w3h3-4rj7-4ph4 |
| CVE-2024-6827 / GHSA-hc5x-x2vx-497g | High | HTTP request/response-smuggling vulnerability in Gunicorn's HTTP parser behavior, relevant when front-end proxies or intermediaries interpret ambiguous requests differently. | 22.0.0 | https://github.com/advisories/GHSA-hc5x-x2vx-497g |

## Security Posture Notes

- Gunicorn's public package-advisory footprint is compact but high-impact because it sits at the Python web serving boundary.
- The two 2024 records should be read together: both land in the 22.0.0 remediation window and point to request-parser / smuggling-hardening work rather than unrelated application-layer bugs.
- The older 2018 issue is a response/header construction boundary bug; the newer 2024 issues are inbound HTTP parsing / intermediary-differential risks.
- Deployments behind reverse proxies should verify proxy normalization and reject ambiguous `Content-Length`, `Transfer-Encoding`, and malformed request framing at the edge rather than relying only on backend behavior.
- Current PyPI metadata in this pass showed `latest=26.0.0`, newer than all public fix points captured here.
- OSV returns both GHSA-derived and PYSEC-derived records for `CVE-2018-1000164`; this page treats them as one vulnerability rather than duplicate findings.

## Dependencies of Note

- Reverse proxies, load balancers, and WSGI framework behavior shape practical exposure for the request-smuggling records.
- Applications that reflect untrusted values into response headers should still sanitize at the application boundary even on fixed Gunicorn versions.

## Open Questions

- Should future KB work add a cross-package Python HTTP request-smuggling cluster linking Gunicorn, Uvicorn, Tornado, Twisted, aiohttp, and common reverse-proxy deployment notes?
- Are distro backports for long-term-supported Gunicorn packages consistently mapped to the upstream 19.5.0 and 22.0.0 fix boundaries?
- Which common deployment templates still combine older Gunicorn versions with front-end proxies in parser-differential configurations?

## Related Pages

- [[python/uvicorn]]
- [[python/tornado]]
- [[python/twisted]]
- [[python/aiohttp]]
- [[python/index]]

---
*Last updated: 2026-05-13 | Sources: 7 (OSV package query, GitHub Advisory Database / GHSA pages, public CVE/NVD records, upstream issue / PR / commit references surfaced through OSV, PyPI metadata, PyPIStats downloads, repository security policy)*
