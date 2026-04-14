# koa-router (npm)

**Registry:** npm
**Weekly Downloads:** ~652,000 (as of 2026-04-08)
**Repository:** https://github.com/koajs/router
**Security Contact:** none listed (no `SECURITY.md` in repo as of 2026-04-14)
**Disclosure Policy:** none listed
**Current Status:** audit-ingested

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-14 | travis-burmaster | `@koa/router` v15.4.0 source review | Manual read of `src/router.ts`, `src/layer.ts`, and path decoding helpers against the TypeScript rewrite shipped in v15; cross-checked `package.json` against known `path-to-regexp` advisory history. | Reported a prefix-strip boundary bug in `Router.prefix()` as public issue #232; documented Allow-header method enumeration, `%2F`-in-params traversal class, and `setPrefix` strict-mode edge case as follow-on candidates. `path-to-regexp` confirmed pinned at `^8.3.0` (resolves to 8.4.2), outside historical ReDoS-affected ranges. | https://github.com/koajs/router/issues/232 |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| koajs/router#232 | Low | `Router.prefix()` strips a previously configured prefix from existing route paths using `startsWith` + `slice` with no path-segment boundary check (`src/router.ts:486-496`). When a layer's stored path does not have a `/` separator immediately after the prefix — reachable when routes are registered without a leading `/` — the strip eats characters that belong to the route. | Open | https://github.com/koajs/router/issues/232 |

*Full CVE history: https://osv.dev/list?ecosystem=npm&q=koa-router* (no package-scoped OSV entries at time of review)

## Security Posture Notes

- Router package for the Koa ecosystem with a materially smaller install base than Express, but still security-relevant because it owns path parsing and route matching logic.
- `path-to-regexp` is pinned to `^8.3.0`, resolving to 8.4.2 at audit time; the v8 rewrite replaced the backtracking engine implicated in the historical `path-to-regexp` ReDoS chain, so koa-router is not exposed to that class via this dependency path.
- Repo is actively maintained (v15.4.0 released 2026-03-16; v15 TypeScript rewrite in PR #209); maintainer has been responsive on recent issues.
- No `SECURITY.md` in the repository, so there is currently no advertised private-reporting path; vulnerability disclosures default to public issues.
- `npm audit` on the v15.4.0 tree is clean for production dependencies; a `tmp` symlink-write advisory (GHSA-52f5-9888-hmc6) reaches the tree only through the `np` release-tool devDependency and is not shipped.
- Allow-header generation in the 405 / OPTIONS branch (`src/router.ts:891` and `:912`) stamps the full method list for the matched path without checking whether upstream middleware would have gated access, so protected resources can leak method presence to unauthenticated callers. Worth a private Security Advisory once repro is confirmed against an auth-guarded router.
- Router-layer `%2F` handling: `context.path` is matched against path-to-regexp patterns before decoding, so a request path containing `%2F` in a segment can match `:id`-style captures and then decode to a value containing `/` inside `ctx.params`. Downstream middleware that treats `ctx.params` as a filesystem or URL path component can inherit traversal risk. The current test suite exercises `%2F` only in generated URLs, not in inbound request paths.

## Dependencies of Note

- `path-to-regexp` is the natural companion page: router-layer bugs often originate there or compound with koa-router's middleware ordering.
- `http-errors`, `debug`, and `koa-compose` are current at time of review; `koa-compose` has had no release since 2019 but no known advisories apply in this pass.

## Open Questions

- Will the maintainer add a `SECURITY.md` so private vulnerability reports can route through GitHub Security Advisories instead of public issues?
- What is the real-world incidence of routes registered without a leading `/` (the practical trigger for `prefix()` corruption), and does it deserve a `register()`-time guard rather than just a `prefix()` fix?
- Should koa-router offer an opt-in `decodeParams: false` (or reject-on-encoded-slash) option given the downstream traversal pattern that encoded slashes create for file-handling middleware?
- Is the Allow-header method enumeration behavior intentional, and if so should it be documented alongside an explicit recommendation to gate the `allowedMethods()` middleware behind auth?

## Related Pages

- [[npm/path-to-regexp]]
- [[npm/express]]
- [[npm/index]]

---
*Last updated: 2026-04-14 | Sources: 4 (npm registry metadata, npm downloads API, `@koa/router` v15.4.0 source, filed public issue koajs/router#232)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
