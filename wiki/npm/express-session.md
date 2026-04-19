# express-session (npm)

**Registry:** npm
**Weekly Downloads:** ~3,598,044 (last week, fetched 2026-04-19)
**Repository:** https://github.com/expressjs/session
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-19 | OpenClaw recurring review | package baseline / public-source triage | public-source curation (npm registry metadata, npm downloads API, OSV.dev package query, upstream releases, upstream HISTORY.md, spot-check of public GHSA/CVE pages) | Added a conservative baseline page for a high-usage package with no clearly confirmed package-level OSV/GHSA records in this pass; captured security-relevant upstream history and important non-advisory caveats. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| 2026-04-19 | OpenClaw recurring review | dependency-context refresh | public-source curation (OSV.dev package query, upstream HISTORY.md, npm registry metadata, npm downloads API, and comparison against public `cookie` / `cookie-signature` advisory records) | Kept the page as a baseline stub because no direct package-level advisories were confirmed, but added evidence-backed dependency-level security context for the `cookie` and `cookie-signature` update trails shipped in maintained `express-session` releases. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| No package-level GHSA / OSV record clearly confirmed in this review pass | — | Public-source review did **not** surface a clean, package-scoped OSV entry for `npm/express-session`. Some public search results and third-party references appear to mix in typosquats, downstream misuse, or unrelated packages, so this page intentionally avoids attributing unverified advisories to `express-session` itself. | — | https://osv.dev/ |

## Security Posture Notes

- `express-session` is widely deployed and sits directly on the authentication/session boundary in many Node.js applications, so even small behavior changes can matter operationally.
- Public package-level advisory mapping remained empty in this pass: the OSV package query for `npm/express-session` returned **no direct package-scoped vulnerability records**.
- The strongest security-relevant public evidence in this pass was therefore **dependency history**, not direct advisories. Upstream `HISTORY.md` shows `1.18.1` pulling in `cookie@0.7.0` / `0.7.1` / `0.7.2`, including the `0.7.0` validation tightening tied to `GHSA-pxg6-pf52-xh8x` / `CVE-2024-47764` in `cookie`.
- The upstream changelog also shows `1.5.2` updated `cookie-signature@1.0.4` with a note that it included a **fix for timing attacks**, matching the public `GHSA-92vm-wfm5-mxvv` / `CVE-2016-1000236` record on that dependency.
- These dependency notes are relevant for risk assessment, but they are **not** being counted here as direct `express-session` advisories.
- The project has long documented that the default **MemoryStore is not intended for production use**. That is a design/operational warning rather than a confirmed package-level CVE in this pass, but it remains important context because session persistence, memory growth, and reliability/security expectations are often misunderstood.
- The package's practical risk profile is heavily shaped by **deployment choices**: cookie settings (`secure`, `httpOnly`, `sameSite`), secret management, proxy trust configuration, store selection, and session lifecycle flags such as `resave` and `saveUninitialized`.
- Current public metadata in this pass showed `latest=1.19.0`, with active maintenance and regular releases through 2024-2026.

## Dependencies of Note

- `cookie`
  - `express-session` `1.18.1` updated into the `cookie@0.7.x` line, which includes the `GHSA-pxg6-pf52-xh8x` / `CVE-2024-47764` fix in `0.7.0`
- `cookie-signature`
  - `express-session` `1.5.2` updated to `cookie-signature@1.0.4`, the public timing-attack fix release for `GHSA-92vm-wfm5-mxvv` / `CVE-2016-1000236`
- Session-store choice is security-relevant in practice even when it is outside the package's own vulnerability record

## Open Questions

- Are there any package-scoped GitHub Advisory Database records for `express-session` that are currently hard to retrieve anonymously but can be cleanly confirmed in a future pass?
- Should the KB eventually add a broader session-management cluster view linking `express-session`, `cookie`, and `cookie-signature` because real-world risk often sits at their boundary?
- Which public maintainer issues or release notes best explain the historical timing-attack fix trail beyond the short HISTORY.md note?
- Would a future pass benefit from enumerating the exact `express-session` version ranges that still transitively pull pre-fix `cookie` or `cookie-signature` releases?

## Related Pages

- [[npm/cookie]]
- [[npm/cookie-signature]]
- [[npm/express]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 8 (npm registry metadata, npm downloads API, OSV.dev package query for npm/express-session, expressjs/session releases, expressjs/session HISTORY.md, public GHSA / OSV records for `cookie` and `cookie-signature`, and spot-checks of public GHSA/CVE pages to avoid misattribution)*
