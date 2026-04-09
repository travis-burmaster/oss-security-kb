# requests (python)

**Registry:** PyPI
**Weekly Downloads:** ~311,677,866 (as of 2026-04-09)
**Repository:** https://github.com/psf/requests
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| Review pending | — | This page has not yet been populated with package-specific advisory history. Use OSV, PyPI release notes, and upstream issue history as starting points. | — | https://osv.dev/list?ecosystem=PyPI&q=requests |

*Full CVE history: https://osv.dev/list?ecosystem=PyPI&q=requests*

## Security Posture Notes

- Requests is one of the most widely installed Python HTTP client libraries, so parser, redirect, proxy, TLS, and credential-handling bugs can have unusually broad impact.
- The package sits on a security-sensitive boundary: outbound HTTP, authentication headers, redirects, certificate validation, and proxy environment interactions.
- High-value future ingest target because many downstream tools inherit its transport defaults and edge-case handling assumptions.

## Dependencies of Note

- `urllib3` is the most obvious follow-on page because transport-layer behavior and many historical HTTP client bugs land there first.
- Optional dependency interactions around certificates and character-set handling may matter for later deepening, but are not curated on this stub yet.

## Open Questions

- Has anyone published a modern public full-source review of Requests core or its redirect / proxy handling paths?
- Which historical advisories belong to `requests` itself versus `urllib3` or higher-level misuse patterns?
- Should this page track default-hardening guidance for authentication, redirects, and certificate verification alongside raw vulnerability history?

## Related Pages

- [[python/index]]

---
*Last updated: 2026-04-09 | Sources: 3 (PyPI metadata API, pypistats recent download API, OSV package query)*
