# requests (python)

**Registry:** PyPI
**Weekly Downloads:** ~311,677,866 (as of 2026-04-09)
**Repository:** https://github.com/psf/requests
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-11 | OpenClaw recurring review | api-surface | manual | 4 publicly disclosed package vulnerabilities curated from OSV, GHSA, CVE, and upstream release notes | https://osv.dev/list?ecosystem=PyPI&q=requests |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-47081 / GHSA-9hjg-9r4m-mvj7 | Moderate | Maliciously crafted URLs could cause Requests to retrieve credentials for the wrong hostname or machine from a trusted `.netrc` environment. | 2.32.4 | https://github.com/psf/requests/security/advisories/GHSA-9hjg-9r4m-mvj7 |
| CVE-2024-35195 / GHSA-9wx4-h78v-vm56 | Moderate | A `Session` could keep TLS certificate verification disabled for a reused pooled connection after an initial request with `verify=False`, even if later requests set `verify=True`. | 2.32.0 | https://github.com/psf/requests/security/advisories/GHSA-9wx4-h78v-vm56 |
| CVE-2023-32681 / GHSA-j8r2-6x86-q33q | Moderate | Requests could leak `Proxy-Authorization` headers to destination servers on HTTPS redirects when proxy credentials were embedded in the proxy URL userinfo component. | 2.31.0 | https://github.com/psf/requests/security/advisories/GHSA-j8r2-6x86-q33q |
| CVE-2018-18074 / GHSA-x84v-xcm2-53pg | High | Authorization data could be exposed if a request was redirected from HTTPS to HTTP and sensitive headers were not stripped safely. | 2.20.0 | https://nvd.nist.gov/vuln/detail/CVE-2018-18074 |

*Full CVE history: https://osv.dev/list?ecosystem=PyPI&q=requests*

## Security Posture Notes

- Requests is a high-leverage HTTP client dependency, so redirect handling, proxy behavior, TLS verification, and ambient credential lookup (`.netrc`, environment-derived proxy settings) are its most security-sensitive surfaces.
- The public advisory history is dominated by credential-handling and transport-boundary mistakes rather than memory-safety bugs: redirect credential leakage, proxy credential forwarding, pooled TLS verification state, and hostname-to-`.netrc` credential confusion.
- Upstream release notes directly call out the 2.31.0, 2.32.0, and 2.32.4 security fixes, which makes this page a good candidate for future maintenance keyed to Requests release announcements.
- The package remains widely deployed enough that even moderate-severity behavior bugs can have large downstream exposure when applications rely on default session or redirect behavior.

## Dependencies of Note

- `urllib3` remains the most important follow-on page because proxying, redirect, and connection-management behavior often spans the Requests / urllib3 boundary.
- Environment-derived trust and credential sources such as `.netrc` and proxy configuration are operational dependencies worth mentioning even when they are not Python package dependencies.

## Open Questions

- Which historical Requests issues are best tracked here versus on a future `urllib3` page where lower-level transport behavior may actually originate?
- Are there public audits or postmortems covering Requests' credential-source precedence rules (`.netrc`, proxy URLs, environment settings) beyond individual GHSA disclosures?
- Should this page eventually add a small hardening section for safe Session usage, redirect controls, and proxy credential handling once that guidance can be sourced cleanly from upstream docs?

## Related Pages

- [[python/index]]

---
*Last updated: 2026-04-11 | Sources: 8 (OSV package query, GHSA advisory pages, upstream Requests release notes, NVD CVE record)*
