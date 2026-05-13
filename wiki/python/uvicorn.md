# Uvicorn (python)

**Registry:** PyPI
**Weekly Downloads:** ~126,235,318 (last week, fetched 2026-05-13; PyPIStats)
**Repository:** https://github.com/encode/uvicorn
**Security Contact:** GitHub Security Advisories / repository security policy
**Disclosure Policy:** https://github.com/encode/uvicorn/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | package advisory history | public-source curation using OSV package queries, GitHub Advisory Database records surfaced through OSV, public CVE/NVD aliases, upstream issue / commit references, upstream release notes, PyPI metadata, PyPIStats downloads, and repository security-policy evidence | Added a new advisory-mapped page for Uvicorn's published package-level advisory history: two 2020 output-injection / response-boundary records fixed in `0.11.7`. | https://osv.dev/list?ecosystem=PyPI&q=uvicorn |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-7694 / GHSA-33c7-2mpw-hg34 / PYSEC-2020-150 | High | Log injection: untrusted request data could inject misleading lines into Uvicorn logs before the logging hardening fix. OSV links the fix to upstream issue `#723` and commit `895807f`. | 0.11.7 | https://github.com/advisories/GHSA-33c7-2mpw-hg34 |
| CVE-2020-7695 / GHSA-f97h-2pfx-f59f / PYSEC-2020-151 | High | HTTP response splitting: public advisory records describe CRLF / response-boundary handling fixed in the same `0.11.7` security release window. | 0.11.7 | https://github.com/advisories/GHSA-f97h-2pfx-f59f |

## Security Posture Notes

- Uvicorn is a high-blast-radius ASGI server package; even a small direct advisory set matters because it often fronts FastAPI, Starlette, and other Python web applications.
- The public OSV query surfaces four records, but two are PYSEC duplicates of the same two GHSA/CVE vulnerabilities. This page normalizes them into two unique advisory rows.
- Both unique advisories are output-boundary issues from 2020 rather than recent parser-smuggling or upload-limit issues in the gathered public package-scoped evidence.
- Current PyPI metadata in this pass showed `latest=0.46.0`, newer than the `0.11.7` fix point.
- Operational exposure still depends on deployment context: access-log retention, log consumers, reverse proxies, and how applications construct responses or headers around ASGI server behavior.

## Dependencies of Note

- Commonly deployed below ASGI frameworks such as FastAPI and Starlette; framework-level advisories should be reviewed separately from Uvicorn's server-level record.
- Log ingestion pipelines can turn log-injection bugs into incident-response confusion, alert spoofing, or audit-trail integrity problems even without code execution.

## Open Questions

- Should the KB add a Python ASGI cluster page linking Uvicorn, Starlette, FastAPI, python-multipart, and reverse-proxy deployment boundaries?
- Are there maintained downstream distributions that backport the 0.11.7 fixes under older package version labels?
- Should future source-oriented review focus on parser-differential behavior, access-log escaping, and ASGI response-header boundaries in current Uvicorn releases?

## Related Pages

- [[python/starlette]]
- [[python/fastapi]]
- [[python/python-multipart]]
- [[python/gunicorn]]
- [[python/index]]

---
*Last updated: 2026-05-13 | Sources: 7 (OSV package query, GitHub Advisory Database / GHSA pages, public CVE/NVD records, upstream issue / commit references surfaced through OSV, upstream release notes, PyPI metadata, PyPIStats downloads, repository security policy)*
