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
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| No package-level GHSA / OSV record clearly confirmed in this review pass | — | Public-source review did **not** surface a clean, package-scoped OSV entry for `npm/express-session`. Some public search results and third-party references appear to mix in typosquats, downstream misuse, or unrelated packages, so this page intentionally avoids attributing unverified advisories to `express-session` itself. | — | https://osv.dev/ |

## Security Posture Notes

- `express-session` is widely deployed and sits directly on the authentication/session boundary in many Node.js applications, so even small behavior changes can matter operationally.
- In this review pass, the strongest package-specific public evidence was **upstream history**, not a clean advisory-database record set. The upstream changelog shows `1.5.2` updated `cookie-signature@1.0.4` with a note that it included a **fix for timing attacks**.
- The project has long documented that the default **MemoryStore is not intended for production use**. That is a design/operational warning rather than a confirmed package-level CVE in this pass, but it remains important context because session persistence, memory growth, and reliability/security expectations are often misunderstood.
- The package's practical risk profile is heavily shaped by **deployment choices**: cookie settings (`secure`, `httpOnly`, `sameSite`), secret management, proxy trust configuration, store selection, and session lifecycle flags such as `resave` and `saveUninitialized`.
- Current public metadata in this pass showed `latest=1.19.0`, with active maintenance and regular releases through 2024-2026.

## Dependencies of Note

- `cookie`
- `cookie-signature`
- Session-store choice is security-relevant in practice even when it is outside the package's own vulnerability record

## Open Questions

- Are there any package-scoped GitHub Advisory Database records for `express-session` that are currently hard to retrieve anonymously but can be cleanly confirmed in a future pass?
- Should the KB eventually add a broader session-management cluster view linking `express-session`, `cookie`, and `cookie-signature` because real-world risk often sits at their boundary?
- Which public maintainer issues or release notes best explain the historical timing-attack fix trail beyond the short HISTORY.md note?

## Related Pages

- [[npm/cookie]]
- [[npm/cookie-signature]]
- [[npm/express]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 6 (npm registry metadata, npm downloads API, OSV.dev package query, expressjs/session releases, expressjs/session HISTORY.md, and spot-checks of public GHSA/CVE pages to avoid misattribution)*
