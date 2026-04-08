# koa-router (npm)

**Registry:** npm
**Weekly Downloads:** ~652,000 (as of 2026-04-08)
**Repository:** https://github.com/koajs/router
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
| Review pending | — | This page has not yet been populated with package-specific advisory history. Use OSV and upstream issue history as starting points. | — | https://osv.dev/list?ecosystem=npm&q=koa-router |

*Full CVE history: https://osv.dev/list?ecosystem=npm&q=koa-router*

## Security Posture Notes

- Router package for the Koa ecosystem with a materially smaller install base than Express, but still security-relevant because it owns path parsing and route matching logic.
- Useful companion page to `path-to-regexp` because router-layer bugs can become authorization bypasses, route confusion, or middleware ordering mistakes.
- No obvious published security policy was found in the package metadata path reviewed for this stub.

## Dependencies of Note

- `path-to-regexp` is a natural dependency to track alongside router behavior and should stay cross-linked.

## Open Questions

- Which `koa-router` versions and forks are most widely deployed today?
- Has anyone published a targeted review of route tokenization, parameter decoding, or edge-case path handling?
- Are there upstream advisories or bug reports that should be ingested into this page next?

## Related Pages

- [[npm/path-to-regexp]]
- [[npm/express]]
- [[npm/index]]

---
*Last updated: 2026-04-08 | Sources: 2 (npm registry metadata, npm download API)*
