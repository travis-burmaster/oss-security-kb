# flask (python)

**Registry:** PyPI
**Weekly Downloads:** ~46,392,460 (as of 2026-04-18)
**Repository:** https://github.com/pallets/flask
**Security Contact:** https://github.com/pallets/flask/security/advisories
**Disclosure Policy:** https://github.com/pallets/flask/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-18 | OpenClaw recurring review | package advisory history | manual | 5 publicly disclosed Flask package vulnerabilities curated from OSV, GHSA, CVE, PyPA advisory records, and upstream release notes | https://osv.dev/list?ecosystem=PyPI&q=flask |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-27205 / GHSA-68rp-wp8r-4726 | Low | Flask did not mark the session as accessed for some key-only operations such as `in` and `len`, so `Vary: Cookie` could be omitted in some cache-sensitive flows. | 3.1.3 | https://github.com/pallets/flask/security/advisories/GHSA-68rp-wp8r-4726 |
| CVE-2025-47278 / GHSA-4grg-w6v8-c28g | Low | Flask 3.1.0 reversed signing-key order when `SECRET_KEY_FALLBACKS` was enabled, causing new session signing to use a fallback key rather than the current key. | 3.1.1 | https://github.com/pallets/flask/security/advisories/GHSA-4grg-w6v8-c28g |
| CVE-2023-30861 / GHSA-m2qf-hxjv-5gpq / PYSEC-2023-62 | High | Responses could miss `Vary: Cookie` when a permanent session cookie was refreshed without the session being accessed or modified, allowing cache-mediated disclosure in specific proxy setups. | 2.2.5, 2.3.2 | https://github.com/pallets/flask/security/advisories/GHSA-m2qf-hxjv-5gpq |
| CVE-2019-1010083 / GHSA-5wv5-4vpf-pj6m / PYSEC-2019-179 | High | Crafted encoded JSON data could trigger unexpected memory usage and denial of service in pre-1.0 releases. Public records note this may overlap the earlier 2018 JSON-memory advisory. | 1.0 | https://github.com/advisories/GHSA-5wv5-4vpf-pj6m |
| CVE-2018-1000656 / GHSA-562c-5r94-xh97 / PYSEC-2018-66 | High | Incorrectly encoded JSON data could cause large memory usage and denial of service in Flask before 0.12.3. | 0.12.3 | https://github.com/advisories/GHSA-562c-5r94-xh97 |

*Full CVE history: https://osv.dev/list?ecosystem=PyPI&q=flask*

## Security Posture Notes

- Flask has very high downstream blast radius as one of the most widely installed Python web frameworks, so even low-severity framework behavior bugs can matter when they affect sessions, caches, or key rotation.
- The public package advisory history clusters into two themes: older JSON parsing / memory-consumption denial-of-service issues, and newer session / cookie / cache boundary mistakes around `Vary: Cookie` and session signing behavior.
- Upstream `CHANGES.rst` cleanly ties the modern fixes to released versions: `2.3.2` for the 2023 cache-disclosure issue, `3.1.1` for fallback-key signing order, and `3.1.3` for the incomplete `Vary: Cookie` follow-on fix.
- The 2018 and 2019 denial-of-service advisories appear close enough in public descriptions that maintainers or future reviewers may want a code-history pass to clarify whether they are distinct root causes or partially overlapping disclosure records.

## Dependencies of Note

- `itsdangerous` matters for session signing and key rotation behavior, especially after the 3.1.0 / 3.1.1 fallback-key ordering issue.
- `Werkzeug` remains the main lower-level HTTP and routing substrate, so some future Flask security context may belong on a dedicated Werkzeug page rather than here.

## Open Questions

- Are there public third-party Flask security audits worth adding separately from package advisories and maintainer release notes?
- Can the older 2018 / 2019 crafted-JSON denial-of-service disclosures be cleanly distinguished by root cause from public maintainer discussion or fix history?
- Does Flask have other package-scoped GHSA records that are withdrawn, disputed, or intentionally excluded from OSV package results and should be tracked in notes only?

## Related Pages

- [[python/index]]

---
*Last updated: 2026-04-18 | Sources: 9 (OSV package query, five GHSA / OSV advisory records, Flask CHANGES.rst, PyPI metadata, pypistats recent downloads)*
