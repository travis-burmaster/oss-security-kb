# passport (npm)

**Registry:** npm
**Weekly Downloads:** ~6,414,726 (last week, fetched 2026-04-20)
**Repository:** https://github.com/jaredhanson/passport
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-20 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database via OSV records, public CVE / NVD records, upstream PR / commit references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for Passport's published package security history, centered on the pre-`0.6.0` session-fixation issue in login / logout session handling. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-25896 / GHSA-v923-w3x8-wh69 | Moderate | Public advisory records describe a session-fixation issue before `0.6.0`: when users logged in or out, the session was regenerated rather than being cleanly closed, allowing a pre-authenticated session identifier to persist across the trust-boundary transition. | 0.6.0 | https://github.com/advisories/GHSA-v923-w3x8-wh69 |

## Security Posture Notes

- `passport` has a **small published package-advisory footprint** in this review pass: one public package-level session-fixation record rather than a long chain of parser, crypto, or transport bugs.
- Even a single package-level flaw matters here because Passport sits on a high-value authentication boundary in many Node.js applications. Session lifecycle mistakes can have outsized downstream impact compared with more isolated helper-library bugs.
- The public advisory trail is straightforward: OSV, GHSA, NVD, and the linked upstream PR / fix commit all align on the same `<0.6.0` affected range and `0.6.0` remediation point.
- Exposure is still **deployment-context-sensitive**. Passport is only part of the session story; real-world risk also depends on Express session configuration, cookie handling, store setup, and surrounding authentication flow design.
- Current npm metadata in this review showed `latest=0.7.0`, which is newer than the published fix point.

## Recommendations for Developers

1. **Upgrade to `0.6.0` or newer**; current npm metadata in this pass showed `0.7.0` as the latest release.
2. **Review full session-lifecycle handling**, not just Passport itself: logout/login transitions, store invalidation, cookie rotation, and session-store hardening all matter.
3. **Cross-check surrounding middleware** such as `express-session` and cookie settings, because Passport often depends on the broader session stack for its real security boundary.
4. **Treat older long-lived authentication stacks as worth inventorying** even if Passport was not upgraded recently; auth-boundary bugs age badly in production.

## Dependencies of Note

- Often deployed alongside `express-session`, cookie middleware, and application-specific session-store adapters.
- The main practical risk surface is the authentication/session boundary rather than pure request parsing.

## Open Questions

- Which still-maintained starter kits or tutorials continue to pin Passport below `0.6.0` or document older session-handling patterns?
- Are there good public maintainer notes around the operational impact of the `0.6.0` change for existing deployments with custom session stores?
- Should a future KB pass add a pattern-focused cross-link page for Passport + Express session-boundary hardening?

## Related Pages

- [[npm/express]]
- [[npm/express-session]]
- [[npm/cookie]]
- [[npm/cookie-parser]]
- [[npm/index]]

---
*Last updated: 2026-04-20 | Sources: 7 (OSV.dev package query for npm/passport, OSV vulnerability record for GHSA-v923-w3x8-wh69, GitHub Advisory Database entry for the same GHSA ID, public CVE / NVD record, upstream PR / commit references linked from OSV, npm registry metadata, npm downloads API)*
