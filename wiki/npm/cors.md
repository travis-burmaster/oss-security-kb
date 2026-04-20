# cors (npm)

**Registry:** npm
**Weekly Downloads:** ~49,751,149 (2026-04-12 to 2026-04-18)
**Repository:** https://github.com/expressjs/cors
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-19 | OpenClaw recurring review | package baseline / public-source triage | public-source curation (OSV.dev package query, GitHub Advisory Database API query, npm registry metadata, npm downloads API, upstream HISTORY.md, upstream README) | Added a conservative baseline page for a very high-download middleware package with no clean package-level GHSA / OSV record in this pass; documented the application's main risk boundary as configuration rather than a confirmed package flaw. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| No package-level GHSA / OSV record clearly confirmed in this review pass | — | Public-source review did **not** surface a clean package-scoped OSV or GitHub Advisory Database entry for `npm/cors`. This page intentionally separates application misconfiguration risk from package vulnerability history. | — | https://osv.dev/ |

## Security Posture Notes

- `cors` is one of the most widely deployed Express middleware packages, but this pass did **not** confirm any direct package-level GHSA / OSV advisory for the package itself.
- The main security boundary here is **configuration**, not published package vulnerabilities. Real deployment risk usually comes from permissive origin policies, credentialed wildcard / reflected origins, or incorrect assumptions about preflight and browser behavior.
- Upstream `HISTORY.md` in this pass showed a docs-only `2.8.6` release and an earlier `2.8.5` functional fix for `maxAge=0`; neither surfaced as a package-level security advisory.
- The repository did not surface a public `SECURITY.md` in this pass, so disclosure guidance appears informal.
- Because `cors` is often treated as a one-line hardening toggle, it is easy for downstream applications to misconfigure it in ways that are security-relevant without the package itself being vulnerable.
- Public metadata in this pass showed `latest=2.8.6` and roughly `49.8M` downloads in the last week alone, so any future package-level advisory would have a large operational blast radius.

## Recommendations for Developers

1. **Audit `cors()` configuration directly** — in practice, application policy mistakes matter more than package-level bugs here.
2. **Do not combine permissive origins with credentialed cross-origin requests** unless the exact trust boundary is well understood.
3. **Stay current on maintained releases** even though the recent upstream change history is relatively quiet.

## Open Questions

- Have maintainers published any canonical security guidance for safe CORS policy patterns beyond the README examples?
- Should the KB eventually add a small deployment-pattern appendix for common dangerous `cors()` configurations that are not package CVEs?
- Would the Express middleware set benefit from a clearer repository-level disclosure policy?

## Related Pages

- [[npm/express]]
- [[npm/helmet]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 7 (OSV.dev package query for npm/cors, GitHub Advisory Database API query for npm/cors, npm registry metadata, npm downloads API, upstream HISTORY.md, upstream README, public repository metadata)*
