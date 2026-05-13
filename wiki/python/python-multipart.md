# python-multipart (python)

**Registry:** PyPI
**Weekly Downloads:** ~93,969,759 (last week, as of 2026-05-13; PyPIStats)
**Repository:** https://github.com/Kludex/python-multipart
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/Kludex/python-multipart/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | package advisory history | public-source advisory mapping using OSV package queries, GitHub Advisory Database / GitHub Security Advisories, public CVE aliases, upstream releases / changelog, PyPI metadata, PyPIStats, and upstream SECURITY.md; local proxy synthesis used only as a drafting aid | 5 public advisories normalized across multipart/form-data parsing denial-of-service, Content-Type regex ReDoS, unbounded part-header parsing, large preamble / epilogue handling, and a non-default upload filename path-traversal/arbitrary-write condition | https://osv.dev/list?ecosystem=PyPI&q=python-multipart |

## Known Vulnerabilities

The table below is a package-level public advisory map from OSV.dev for `python-multipart`, cross-checked against GHSA records, public CVE aliases where available, upstream releases, PyPI metadata, and the repository security policy. PyPI reported `0.0.28` as the current release during this pass.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-24762 / GHSA-2jv5-9r88-3w3p / GHSA-qf9m-vfgh-m389 / PYSEC-2024-38 | High / ReDoS | `Content-Type` header option parsing used a regex that could be forced into excessive CPU work when applications parsed form data, stalling event-loop based services. | 0.0.7 | https://github.com/Kludex/python-multipart/security/advisories/GHSA-2jv5-9r88-3w3p |
| CVE-2024-53981 / GHSA-59g5-xgcq-4qw3 | High / DoS | Deformed `multipart/form-data` boundaries with large data before the first boundary or after the final boundary could drive excessive CPU / logging work while parsing. | 0.0.18 | https://github.com/Kludex/python-multipart/security/advisories/GHSA-59g5-xgcq-4qw3 |
| CVE-2026-24486 / GHSA-wp53-j4wj-2cfg | High / arbitrary file write under non-default configuration | When `UPLOAD_DIR` and `UPLOAD_KEEP_FILENAME=True` were both enabled, absolute or traversal-style filenames could escape the intended upload directory because paths were joined without stripping directory components. | 0.0.22 | https://github.com/Kludex/python-multipart/security/advisories/GHSA-wp53-j4wj-2cfg |
| CVE-2026-40347 / GHSA-mj87-hwqh-73pj | Moderate / DoS | Crafted requests with large multipart preamble or epilogue sections could trigger inefficient parser paths and consume request-processing time. | 0.0.26 | https://github.com/Kludex/python-multipart/security/advisories/GHSA-mj87-hwqh-73pj |
| CVE-2026-42561 / GHSA-pp6c-gr5w-3c5g | High / DoS | Multipart part-header parsing lacked limits on header count or individual header size, allowing many repeated headers or one very large header to cause CPU exhaustion before rejection or completion. | 0.0.27 | https://github.com/Kludex/python-multipart/security/advisories/GHSA-pp6c-gr5w-3c5g |

*Full OSV package listing: https://osv.dev/list?ecosystem=PyPI&q=python-multipart*

## Security Posture Notes

- `python-multipart` is a small but high-blast-radius parser dependency because FastAPI, Starlette, and other ASGI / WSGI stacks invoke it for `multipart/form-data` and form parsing.
- The public advisory pattern is concentrated in **parser resource-exhaustion boundaries**: Content-Type parsing, multipart boundary scanning, preamble / epilogue handling, and part-header parsing all received public fixes between `0.0.7` and `0.0.27`.
- The file-write advisory is narrower than the DoS issues because it depends on non-default `UPLOAD_DIR` plus `UPLOAD_KEEP_FILENAME=True`; it should still be tracked because file-upload handlers are security-sensitive and the fix shipped in `0.0.22`.
- `0.0.27` is the minimum version that closes all five public advisories reviewed here. `0.0.28` adds further parser-boundary hardening noted in the upstream release notes, including partial-boundary tail-scan performance and a multipart boundary-length cap.
- Upstream provides a GitHub security policy and publishes GitHub Security Advisories; downstream framework users should still verify their framework pins because FastAPI / Starlette advisories may express dependency-mediated exposure separately.
- No private, embargoed, or speculative vulnerability claims were used in this pass.

## Dependencies of Note

- `python-multipart` has no runtime dependencies listed in current PyPI metadata during this pass.
- Frameworks and applications that parse attacker-controlled form uploads inherit the relevant parser and upload-path boundaries, especially FastAPI and Starlette deployments that accept file uploads.

## Open Questions

- Which supported FastAPI / Starlette release trains still allow `python-multipart` versions below `0.0.27` through loose dependency constraints?
- Should the KB add a cross-page note for multipart parser resource-exhaustion issues across Werkzeug, Starlette, aiohttp, and python-multipart?
- Are there public fuzzing or parser-audit reports for `python-multipart` beyond the maintainer GHSA / release-note trail?

## Related Pages

- [[python/fastapi]]
- [[python/starlette]]
- [[python/werkzeug]]
- [[python/index]]

---
*Last updated: 2026-05-13 | Sources: 7 (OSV package query and individual vulnerability records, GitHub Advisory Database / GitHub Security Advisories, public CVE / NVD aliases, upstream release notes / changelog, upstream SECURITY.md, PyPI metadata, PyPIStats downloads)*
