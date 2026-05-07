# fastapi (python)

**Registry:** PyPI
**Repository:** https://github.com/fastapi/fastapi
**Security Contact:** security@tiangolo.com
**Disclosure Policy:** https://github.com/fastapi/fastapi/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-07 | OpenClaw recurring review | package advisory history | manual | 2 unique public FastAPI vulnerability classes normalized from OSV / GHSA / PYSEC records, public CVE aliases, upstream release notes, fix commits, PyPI metadata, and upstream security policy; duplicate PYSEC and withdrawn GHSA aliases kept with their canonical records | https://osv.dev/list?ecosystem=PyPI&q=fastapi |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-32677 / GHSA-8h2j-cgx8-6xv7 / PYSEC-2021-100 | High | FastAPI parsed request bodies as JSON even when browsers sent a non-JSON `Content-Type` such as `text/plain`; applications using cookie authentication on JSON endpoints could therefore accept CSRF-able simple requests that avoided CORS preflight. | 0.65.2 | https://github.com/advisories/GHSA-8h2j-cgx8-6xv7 |
| CVE-2024-24762 / GHSA-2jv5-9r88-3w3p / PYSEC-2024-38 | High | Form-data endpoints could inherit a `python-multipart` `Content-Type` header ReDoS, allowing crafted multipart headers to consume CPU and stall the event loop; FastAPI 0.109.1 raised the minimum `python-multipart` version to the patched 0.0.7 line. | 0.109.1 | https://github.com/advisories/GHSA-2jv5-9r88-3w3p |

*Full public advisory query: https://osv.dev/list?ecosystem=PyPI&q=fastapi*

## Security Posture Notes

- FastAPI's direct public package history is small but important: one framework request-parsing trust-boundary issue and one dependency-mediated multipart parser denial-of-service issue.
- The 2021 CSRF advisory is specifically about browser behavior, cookie-authenticated JSON endpoints, and permissive `Content-Type` handling. FastAPI 0.65.2 introduced stricter JSON content-type checks, while 0.65.3 restored compatibility for requests with no `Content-Type` header without re-accepting explicit `text/plain` JSON as safe.
- The 2024 ReDoS record should not be counted as an independent FastAPI parser bug. The canonical GHSA record is for `python-multipart <= 0.0.6`; FastAPI's relevant remediation was pinning / requiring `python-multipart >= 0.0.7` in 0.109.1 for applications that use forms or file uploads.
- `GHSA-qf9m-vfgh-m389` was a FastAPI-scoped duplicate advisory for the 2024 `python-multipart` ReDoS and was withdrawn on 2024-02-16. It appears in PYSEC aliases but should not be tracked as a separate vulnerability row.
- The current upstream security policy says only the latest FastAPI version is supported and asks reporters to use `security@tiangolo.com`, so pinned deployments should not assume backported fixes for older branches.

## Dependencies of Note

- FastAPI applications commonly inherit lower-level behavior from Starlette, Pydantic, Uvicorn, and optional parsers such as `python-multipart`; review those pages or packages separately rather than treating this page as complete ASGI-stack coverage.
- Applications that use `Form`, `File`, or `UploadFile` should verify the installed `python-multipart` version directly, especially in environments where dependency constraints can override FastAPI's minimum.
- Applications using cookie authentication on state-changing JSON endpoints should keep normal CSRF controls in place even after upgrading; the fixed FastAPI behavior removes one bypass condition but does not make cookie-authenticated APIs inherently CSRF-proof.

## Open Questions

- Should the KB add a dedicated `python-multipart` page so the 2024 ReDoS is tracked at its root package with FastAPI and Starlette listed as affected consumers?
- Are there high-quality public postmortems from FastAPI users affected by either the 2021 JSON `Content-Type` behavior or the 2024 multipart parser ReDoS?
- Which common FastAPI deployment templates or lockfiles still pin FastAPI below 0.109.1 or allow `python-multipart <= 0.0.6`?

## Related Pages

- [[python/starlette]]
- [[python/aiohttp]]
- [[python/flask]]
- [[python/werkzeug]]
- [[python/index]]

---
*Last updated: 2026-05-07 | Sources: OSV package query and vulnerability details, GitHub Advisory Database records, public CVE aliases, upstream FastAPI release notes / fix commits / security policy, PyPI metadata, and local proxy synthesis used as a drafting aid only.*
