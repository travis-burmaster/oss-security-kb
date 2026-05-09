# koa (npm)

**Registry:** npm
**Weekly Downloads:** ~8,409,856 (npm downloads API, 2026-05-02 through 2026-05-08)
**Repository:** https://github.com/koajs/koa
**Security Contact:** GitHub Security Advisory private reporting / project disclosure guidance
**Disclosure Policy:** https://github.com/koajs/koa/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-09 | OpenClaw recurring review | package advisory history | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database records, public CVE aliases, upstream history / release notes, npm registry metadata, npm downloads API, and local proxy synthesis as drafting aid only) | Added advisory-mapped coverage for five public `koa` advisories spanning ReDoS, `ctx.redirect()` XSS, open redirects, and host-header-driven redirect behavior across the 2.x and 3.x lines. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-25200 / GHSA-593f-38f6-jp5m | Moderate | Koa 2.x `ctx.host` / related host or protocol parsing used an inefficient regular expression that could be driven into excessive CPU work, creating denial-of-service risk. | 2.15.4 | https://github.com/advisories/GHSA-593f-38f6-jp5m |
| CVE-2025-32379 / GHSA-x2rg-q646-7m2v | Moderate | `ctx.redirect()` could reflect attacker-controlled input into the redirect response in a way that created cross-site scripting risk. | 2.16.1 | https://github.com/advisories/GHSA-x2rg-q646-7m2v |
| CVE-2025-8129 / GHSA-jgmv-j7ww-jx2x | Moderate | Koa 2.x redirect-back behavior could trust a user-controlled `Referrer` / `Referer` header, enabling open redirect when applications used that redirect path. | 2.16.2 | https://github.com/advisories/GHSA-jgmv-j7ww-jx2x |
| CVE-2025-62595 / GHSA-g8mr-fgfg-5qpc | Moderate | Koa 3.0.1 through 3.0.2 could produce open redirects involving trailing double-slash (`//`) behavior in redirect-back logic. | 3.0.3 | https://github.com/advisories/GHSA-g8mr-fgfg-5qpc |
| CVE-2026-27959 / GHSA-7gcc-r8m5-44qm | Moderate | Koa 3.0.0 through 3.1.1 could use an untrusted `Host` header through `ctx.hostname`, enabling host-header injection in redirect or URL-construction contexts. | 3.1.2 | https://github.com/advisories/GHSA-7gcc-r8m5-44qm |

*Full advisory history (OSV): https://osv.dev/list?ecosystem=npm&q=koa*

## Security Posture Notes

- Koa's direct public advisory history is concentrated in **request metadata and redirect boundaries**: host / protocol parsing, `ctx.redirect()`, redirect-back behavior, and browser interpretation of redirect targets.
- The 2.x line and 3.x line need separate triage. Public OSV / GHSA records in this pass point to `2.16.2` as the safer floor for 2.x users and `3.1.2` as the safer floor for 3.x users.
- Several records are application-mode sensitive. They matter most when applications pass user-influenced values into redirect helpers, trust forwarded host/protocol metadata, or expose redirect-back flows to untrusted clients.
- The upstream history includes an explicit `3.0.0-alpha.3` note to avoid ReDoS in host and protocol getters, which aligns with the later public advisory theme around host/protocol parsing.
- The `CVE-2026-27959` identifier is future-dated relative to this review window, but the linked public GHSA / OSV record and fixed version are concrete enough to include conservatively.
- No active vulnerability hunting was performed in this pass; the page records only already-published public advisory and maintainer evidence.

## Dependencies of Note

- Real-world redirect safety also depends on reverse-proxy configuration, trusted proxy headers, and application-level allowlists for post-login / return URLs.
- Koa middleware packages may introduce their own security history; this page only covers direct package advisories for `koa` itself.
- Applications using `app.proxy`, `X-Forwarded-*` headers, or custom redirect wrappers should review those trust boundaries alongside package upgrades.

## Open Questions

- Which popular Koa middleware packages deserve dedicated pages next, especially those handling routing, sessions, body parsing, or authentication?
- Are common Koa starter templates using redirect-back patterns that should be documented as downstream posture notes?
- Should the KB add a cross-framework note comparing host-header and redirect-helper vulnerabilities across Koa, Express, Fastify, and Go routers?

## Related Pages

- [[npm/koa-router]]
- [[npm/express]]
- [[npm/fastify]]
- [[npm/index]]

---
*Last updated: 2026-05-09 | Sources: OSV package query and vulnerability details, GitHub Advisory Database records, public CVE aliases, upstream history / release notes, npm registry metadata, npm downloads API, and local proxy synthesis used as a drafting aid only.*
