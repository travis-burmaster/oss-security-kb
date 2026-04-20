# cookie-parser (npm)

**Registry:** npm
**Weekly Downloads:** ~7,777,259 (2026-04-12 to 2026-04-18)
**Repository:** https://github.com/expressjs/cookie-parser
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-19 | OpenClaw recurring review | package baseline / public-source triage | public-source curation (OSV.dev package query, GitHub Advisory Database API query, npm registry metadata, npm downloads API, upstream HISTORY.md, upstream README) | Added a conservative baseline page for a widely used middleware package with no clean package-level GHSA / OSV record in this pass; captured dependency context and disclosure gaps without forcing speculative findings. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| No package-level GHSA / OSV record clearly confirmed in this review pass | — | Public-source review did **not** surface a clean package-scoped OSV or GitHub Advisory Database entry for `npm/cookie-parser`, so this page intentionally avoids attributing dependency or ecosystem issues directly to the package itself. | — | https://osv.dev/ |

## Security Posture Notes

- `cookie-parser` remains widely deployed in Express stacks, but this pass did **not** confirm any direct package-level GHSA / OSV advisory for the package itself.
- The strongest security-relevant public signal in this review window was **dependency history**, not a direct package disclosure. Upstream `HISTORY.md` for `1.4.7` records updates to `cookie@0.7.0` / `0.7.1` / `0.7.2`, and the `cookie@0.7.0` line is where upstream tightened validation in the fix for `GHSA-pxg6-pf52-xh8x` / `CVE-2024-47764`.
- That dependency history is useful for operational risk assessment, but it is **not** being counted here as a direct `cookie-parser` vulnerability.
- The repository did not surface a public `SECURITY.md` in this pass, so coordinated disclosure guidance appears weaker than in some adjacent packages.
- Because the package sits on the HTTP cookie parsing boundary, real-world risk is often shaped more by surrounding Express middleware, proxy limits, and cookie serialization behavior than by the thin wrapper package alone.
- Public metadata in this pass showed `latest=1.4.7`, with recent maintenance focused mostly on dependency refreshes rather than feature churn.

## Dependencies of Note

- `cookie`
  - `cookie-parser` `1.4.7` updated through the `cookie@0.7.x` line, which includes the public `GHSA-pxg6-pf52-xh8x` / `CVE-2024-47764` fix in `0.7.0`
- Often deployed directly alongside [[npm/cookie]] and [[npm/express]]

## Open Questions

- Are there package-scoped GitHub Advisory Database records for `cookie-parser` that remain absent from current public API results but can be cleanly confirmed in a future pass?
- Would the Express ecosystem benefit from a clearer `SECURITY.md` or disclosure route for older middleware repositories such as this one?
- Should the KB eventually add a broader cookie-handling cluster page linking `cookie-parser`, `cookie`, and `cookie-signature` for deployment-focused review?

## Related Pages

- [[npm/cookie]]
- [[npm/cookie-signature]]
- [[npm/express]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 7 (OSV.dev package query for npm/cookie-parser, GitHub Advisory Database API query for npm/cookie-parser, npm registry metadata, npm downloads API, upstream HISTORY.md, upstream README, public repository metadata)*
