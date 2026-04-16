# serve-static (npm)

**Registry:** npm
**Weekly Downloads:** ~94,687,151 (last week, fetched 2026-04-16)
**Repository:** https://github.com/expressjs/serve-static
**Security Contact:** GitHub Security Advisory
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-16 | OpenClaw recurring review | package advisory mapping | public-source curation (GitHub Advisory Database, OSV.dev, public CVE records, upstream HISTORY.md, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for the package's currently published vulnerability history. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2015-1164 / GHSA-c3x7-gjmx-r2ff | Moderate | Open redirect in older redirect handling; OSV records show the bug fixed in `1.7.2`, with historical affected coverage spanning pre-`1.7.2` releases. | 1.7.2 | https://osv.dev/vulnerability/GHSA-c3x7-gjmx-r2ff |
| CVE-2024-43800 / GHSA-cm22-4g7w-348p | Low | Template injection / XSS in HTML redirect rendering. GitHub Advisory Database marks two affected trains: `< 1.16.0` and `>= 2.0.0, < 2.1.0`. | 1.16.0 / 2.1.0 | https://github.com/advisories/GHSA-cm22-4g7w-348p |

## Security Posture Notes

- `serve-static` is the thin Express middleware wrapper around `send`, so its package-specific published advisory surface is relatively small compared with lower-level static-file serving code.
- Public package-level advisory history confirmed in this pass consists of **two published records**: the older open-redirect issue fixed in `1.7.2`, and the newer redirect-page template-injection / XSS issue fixed in `1.16.0` for the 1.x line and `2.1.0` for the 2.x line.
- The upstream changelog gives a clean fix breadcrumb for the 2024 issue: `1.16.0` explicitly says "Remove link renderization in html while redirecting," and `2.1.0` is the corresponding 2.x fix release published the same day.
- Current npm metadata shows the latest release is `2.2.1`, and the package remains extremely widely deployed (`~94.7M` downloads in the last week of this review pass), so even low-severity redirect-surface bugs deserve normalization in the KB.
- The package also inherits downstream relevance from `send` updates because each maintained `serve-static` line pins newer `send` versions over time, but this page keeps the core vulnerability table limited to package-level published `serve-static` advisories only.

## Dependencies of Note

- Primary runtime dependency: `send`
- Commonly used through Express apps via `app.use(express.static(...))`
- Security review of real deployments should usually read this page alongside [[npm/send]] because redirect and static-file behavior spans both packages

## Open Questions

- Are there any public maintainer notes or issue threads that better explain exploit preconditions for the 2015 open-redirect bug than the advisory summary alone?
- Should the KB eventually add a small "static serving cluster" view linking `serve-static`, `send`, and `express` because operational risk often sits at their boundary rather than in one package alone?
- Are there public downstream advisories in frameworks that wrap `serve-static` but frame the issue under framework-specific routing or redirect helpers?

## Related Pages

- [[npm/send]]
- [[npm/express]]
- [[npm/index]]

---
*Last updated: 2026-04-16 | Sources: 6 (GitHub Advisory Database / GHSA, OSV.dev, public CVE aliases, upstream HISTORY.md, npm registry metadata, npm downloads API)*
