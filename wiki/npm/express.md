# express (npm)

**Registry:** npm
**Weekly Downloads:** ~84,000,000 (as of 2026-04-08)
**Repository:** https://github.com/expressjs/express
**Security Contact:** https://expressjs.com/en/resources/security-updates.html
**Disclosure Policy:** https://expressjs.com/en/resources/security-updates.html
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| Review pending | — | This page has not yet been populated with package-specific advisory history. Use OSV and Express security updates as starting points. | — | https://osv.dev/list?ecosystem=npm&q=express |

*Full CVE history: https://osv.dev/list?ecosystem=npm&q=express*

## Security Posture Notes

- Core Node.js web framework with very high downstream exposure and a large reverse-dependency footprint.
- Public Express security update guidance exists, which makes this a strong candidate for a deeper ingest pass focused on routing, middleware defaults, and historical advisory handling.
- High-value related package because `path-to-regexp` commonly appears in Express route parsing paths.

## Dependencies of Note

- `path-to-regexp` historically sits close to the routing surface in the Express ecosystem and is already tracked in this KB.
- Middleware packages in the wider Express ecosystem often matter more than the tiny direct dependency set of `express` itself.

## Open Questions

- Has any modern public full-source review of Express core been published?
- Which historical advisories belong on the package page versus the wider middleware ecosystem?
- What routing and request-parsing assumptions should be tracked alongside `path-to-regexp` coverage?

## Related Pages

- [[npm/path-to-regexp]]
- [[npm/koa-router]]
- [[npm/index]]

---
*Last updated: 2026-04-08 | Sources: 3 (npm registry metadata, npm download API, Express security updates page)*
