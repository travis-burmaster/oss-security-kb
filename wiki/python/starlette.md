# starlette (python)

**Registry:** PyPI
**Repository:** https://github.com/encode/starlette
**Security Contact:** GitHub Security Advisory
**Disclosure Policy:** https://github.com/encode/starlette/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-07 | OpenClaw recurring review | package advisory history | manual | 5 unique public Starlette advisories normalized from OSV / GHSA records, public CVE aliases, upstream commits, and release notes; duplicate PYSEC aliases kept with their GHSA/CVE records | https://osv.dev/list?ecosystem=PyPI&q=starlette |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-30798 / GHSA-74m5-2c7w-9w3x / PYSEC-2023-48 | High | `MultipartParser` accepted an unlimited number of multipart parts, enabling CPU and memory exhaustion with many small fields or empty files. | 0.25.0 | https://github.com/advisories/GHSA-74m5-2c7w-9w3x |
| CVE-2023-29159 / GHSA-v5gw-mw7f-84px / PYSEC-2023-83 | High | `StaticFiles` used a prefix-style path containment check that could expose sibling files or directories whose names began with the configured static directory name. | 0.27.0 | https://github.com/advisories/GHSA-v5gw-mw7f-84px |
| CVE-2024-47874 / GHSA-f96h-pmfr-66vw | High | Multipart text fields without a `filename` were buffered without a size limit, enabling memory-exhaustion denial of service through large `multipart/form-data` requests. | 0.40.0 | https://github.com/advisories/GHSA-f96h-pmfr-66vw |
| CVE-2025-54121 / GHSA-2c2j-9gv5-cj73 | Moderate | Large multipart file uploads could synchronously roll over to disk and block the asyncio event loop, preventing new connections from being accepted. | 0.47.2 | https://github.com/advisories/GHSA-2c2j-9gv5-cj73 |
| CVE-2025-62727 / GHSA-7f5h-v6xp-fcq8 | High | `FileResponse` range-header parsing / merging could take quadratic time for crafted multi-range requests, causing CPU exhaustion on file-serving endpoints. | 0.49.1 | https://github.com/advisories/GHSA-7f5h-v6xp-fcq8 |

*Full public advisory query: https://osv.dev/list?ecosystem=PyPI&q=starlette*

## Security Posture Notes

- Starlette's public advisory history is concentrated in two operational surfaces: **multipart form parsing** and **file/static-file serving**.
- The multipart cluster is not a single bug class. Public records show three distinct denial-of-service boundaries: unbounded part counts before `0.25.0`, unbounded non-file text-field buffering before `0.40.0`, and blocking rollover behavior for large file uploads before `0.47.2`.
- The file-serving cluster includes one path-containment flaw in `StaticFiles` before `0.27.0` and a later `FileResponse` range-header CPU-exhaustion flaw fixed in `0.49.1`.
- Duplicate PYSEC records (`PYSEC-2023-48`, `PYSEC-2023-83`) map to the same 2023 GHSA/CVE advisories and should not be counted as separate vulnerability classes.
- A conservative current-version floor for the gathered public security history is **0.49.1**, because that closes the latest published `FileResponse` range-header advisory reviewed here.

## Dependencies of Note

- FastAPI applications commonly inherit Starlette request parsing, response, routing, and static-file behavior; FastAPI-specific advisory review should cross-link here rather than duplicating Starlette's lower-level vulnerability history.
- Deployments that accept uploads through `request.form()`, `UploadFile`, or framework wrappers should treat Starlette version floors as relevant even when application code does not import multipart parsers directly.
- Applications using `StaticFiles` or custom `FileResponse` endpoints should track the path-containment and range-header advisories separately from upload-parser hardening.

## Open Questions

- Should the KB add a dedicated FastAPI page that separates FastAPI's own package advisories from inherited Starlette / Pydantic / python-multipart security posture?
- Are there public postmortems or downstream incident write-ups for the 2024-2025 Starlette multipart DoS fixes that would add operational context beyond the maintainer advisories?
- Which common FastAPI deployment templates still pin Starlette below `0.49.1` through broad dependency constraints?

## Related Pages

- [[python/aiohttp]]
- [[python/flask]]
- [[python/werkzeug]]
- [[python/index]]

---
*Last updated: 2026-05-07 | Sources: 5 unique public OSV / GHSA records, public CVE aliases, upstream fix commits, Starlette release notes, PyPI metadata, and local proxy synthesis used as a drafting aid only.*
