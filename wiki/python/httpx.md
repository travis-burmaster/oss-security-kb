# httpx (python)

**Registry:** PyPI  
**Weekly Downloads:** ~173,637,904 (PyPIStats last week, fetched 2026-05-13)  
**Repository:** https://github.com/encode/httpx  
**Security Contact:** none listed  
**Disclosure Policy:** none listed  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | package-level public advisory mapping for PyPI `httpx` | public-source curation from OSV.dev package and vulnerability records, GitHub Advisory Database, public CVE records, upstream issue / PR / release references, PyPI metadata, PyPIStats download data, and local proxy-assisted drafting | Added initial advisory-mapped page for HTTPX's published package vulnerability history: one unique public URL input-validation advisory, with the OSV duplicate / fixed-version discrepancy called out explicitly. | https://osv.dev/list?ecosystem=PyPI&q=httpx |

## Known Vulnerabilities

OSV currently returns two records for the same underlying issue (`GHSA-h8pj-cxx2-jfg2` and `PYSEC-2022-183`). This page treats them as one unique vulnerability and notes the public fixed-version discrepancy rather than double-counting it.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-41945 / GHSA-h8pj-cxx2-jfg2 / PYSEC-2022-183 | Critical | Public advisory records describe improper input validation in `httpx.URL`, `httpx.Client`, and functions using `httpx.URL.copy_with`. The upstream 0.23.0 changelog ties the fix to “oddly formed URL cases” in `URL.copy_with` via PR #2185. | 0.23.0 per GHSA / CVE / upstream 0.23.0 release references; OSV's separate `PYSEC-2022-183` record lists 0.20.0, so consumers should verify against their advisory feed and prefer the later fixed boundary when in doubt. | https://github.com/advisories/GHSA-h8pj-cxx2-jfg2 ; https://osv.dev/vulnerability/PYSEC-2022-183 ; https://github.com/encode/httpx/releases/tag/0.23.0 |

*Full OSV package listing: https://osv.dev/list?ecosystem=PyPI&q=httpx*

## Security Posture Notes

- HTTPX is a high-blast-radius Python HTTP client used directly by applications and transitively by API SDKs, automation tooling, and AI / service clients. URL parsing, redirect handling, proxy behavior, and transport defaults are its most security-sensitive surfaces.
- The current public package-advisory footprint is compact compared with `requests` / `urllib3`: this pass found one unique OSV/GHSA/CVE issue, represented by two OSV records with different fixed versions.
- The fixed-version discrepancy matters operationally. GHSA-derived data and the upstream 0.23.0 release reference indicate `< 0.23.0` as the affected range, while PYSEC's duplicate record lists `< 0.20.0`. This page intentionally avoids inventing a reconciliation beyond the public evidence.
- Current PyPI metadata during this review showed `latest=0.28.1`, which is newer than both published fix boundaries.
- This review did not perform active vulnerability hunting, exploit validation, or live target testing. It only normalized already-public advisory, CVE, upstream issue / PR / release, and package metadata.

## Dependencies of Note

- HTTPX depends on lower-level HTTP / transport behavior from `httpcore` plus optional environment and proxy configuration. URL validation and request-target construction should be reviewed with that boundary in mind.
- Applications that accept semi-trusted URLs should separately validate scheme, host, port, and redirect policy rather than relying on package defaults alone.

## Open Questions

- Should future maintenance split HTTPX transport-boundary guidance into a shared Python HTTP-client hardening note covering `requests`, `urllib3`, `httpx`, and `aiohttp`?
- Are there public postmortems or downstream advisories that explain real-world reachability of CVE-2021-41945 in common SDKs using HTTPX?
- If advisory feeds continue to disagree on the fixed version, should the KB add a dedicated “duplicate advisory records / conflicting fixed ranges” note for package consumers?

## Related Pages

- [[python/requests]]
- [[python/urllib3]]
- [[python/aiohttp]]
- [[python/index]]

---
*Last updated: 2026-05-13 | Sources: OSV package query and individual vulnerability records for `httpx`; GitHub Advisory Database entry for GHSA-h8pj-cxx2-jfg2; public CVE record for CVE-2021-41945; upstream HTTPX issue / PR / commit and 0.23.0 release references surfaced by OSV; upstream changelog; PyPI metadata; PyPIStats recent download data; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid.*
