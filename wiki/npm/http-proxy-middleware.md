# http-proxy-middleware (npm)

**Registry:** npm
**Weekly Downloads:** ~24,138,318 (2026-04-11 to 2026-04-17)
**Repository:** https://github.com/chimurai/http-proxy-middleware
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/chimurai/http-proxy-middleware/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-18 | OpenClaw recurring review | package advisory review | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream changelog / release metadata, npm registry metadata, npm downloads API) | 3 published package advisories mapped | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-c7qv-q95q-8v27 / CVE-2024-21536 | High | A denial-of-service condition in path filtering let crafted request paths trigger an unhandled promise rejection from `micromatch`, which could crash the Node.js process. Public records mark releases before `2.0.7` and `3.0.0`-`3.0.2` as affected. | 2.0.7 / 3.0.3 | [GitHub Advisory Database](https://github.com/advisories/GHSA-c7qv-q95q-8v27) |
| GHSA-4www-5p9h-95mh / CVE-2025-32996 | Medium | `fixRequestBody` could call `writeBody` twice because the relevant logic used separate `if` branches rather than an `if` / `else if` chain, creating request-forwarding instability on the maintained 2.x and 3.x lines. | 2.0.8 / 3.0.4 | [GitHub Advisory Database](https://github.com/advisories/GHSA-4www-5p9h-95mh) |
| GHSA-9gqv-wp59-fq42 / CVE-2025-32997 | Medium | `fixRequestBody` could proceed even after upstream body parsing had failed, so malformed request-body state could still be forwarded to the target server. | 2.0.9 / 3.0.5 | [GitHub Advisory Database](https://github.com/advisories/GHSA-9gqv-wp59-fq42) |

## Security Posture Notes

- The public package history in this pass is compact but coherent: one 2024 denial-of-service issue and two 2025 `fixRequestBody` correctness / request-forwarding flaws.
- All three advisories sit on security-sensitive proxy boundaries. Even when the 2025 records are not described as classic RCE or SSRF bugs, they still matter because `http-proxy-middleware` commonly sits in front of internal APIs, development backends, auth gateways, and admin surfaces.
- Upstream changelog entries line up cleanly with the published advisory set gathered here: `v3.0.3` fixes `pathFilter` error handling, `v3.0.4` adds the multiple-`.write()` prevention, and `v3.0.5` adds the `readableLength` / invalid-request handling follow-up. The same fix train is reflected in the maintained 2.x line via `2.0.7`, `2.0.8`, and `2.0.9`.
- npm download data gathered in this pass was ~24.1M for the prior week, which keeps this package squarely in the "high blast radius if pinned behind" category even though its published advisory count is smaller than some peer HTTP-client libraries.
- Public evidence collected here did not justify forcing pages for the two comparison candidates reviewed in the same window: package-scoped OSV queries for `express-session` and `cookie-parser` both returned zero vulnerabilities at review time, so they remain follow-up candidates rather than speculative KB entries.

## Recommendations for Developers

1. **Use `2.0.9` or newer on the 2.x line, or `3.0.5` or newer on the 3.x line** to cover the full currently published advisory set gathered in this pass.
2. **Treat proxy middleware as part of your trust boundary** rather than simple plumbing; request-rewrite helpers and path filters can become security issues when they mishandle malformed input.
3. **Review any explicit use of `fixRequestBody`** in apps that combine proxying with body-parsing middleware, because both 2025 advisories center on that interoperability path.
4. **Exercise path-filter and error paths in tests** instead of validating only the happy path; the 2024 DoS issue came from an exception path rather than ordinary proxy success cases.
5. **Audit transitive usage** in developer tooling as well as production services, because this package often appears behind dev servers, frontend toolchains, and gateway helper wrappers.

## Dependencies of Note

- `micromatch` mattered directly in the 2024 DoS advisory because path-filter handling was part of the vulnerable execution path.
- The package historically wrapped `http-proxy`; upstream's unreleased `next` changelog notes a move toward `httpxy`, which is worth tracking in future KB maintenance once that major line ships and accumulates public security history.

## Open Questions

- Did upstream publish any maintainer-authored security hardening guidance for `fixRequestBody` beyond the release-note and advisory trail gathered here?
- Which high-download developer tools still pin `http-proxy-middleware` below `2.0.9` or `3.0.5` in long-lived support branches?
- Once the `next` line lands with the `httpxy` swap, does the package's proxy-boundary advisory profile materially change?

## Related Pages

- [[npm/node-fetch]]
- [[npm/follow-redirects]]
- [[npm/undici]]
- [[npm/express]]
- [[npm/index]]

---
*Last updated: 2026-04-18 | Sources: 8 (OSV.dev package query for npm/http-proxy-middleware, OSV vulnerability records for GHSA-c7qv-q95q-8v27 / GHSA-4www-5p9h-95mh / GHSA-9gqv-wp59-fq42, GitHub Advisory Database entries for the same GHSA IDs, public CVE records for CVE-2024-21536 / CVE-2025-32996 / CVE-2025-32997 via advisory aliases, upstream CHANGELOG.md / release metadata for v2.0.7-v2.0.9 and v3.0.3-v3.0.5, npm registry metadata, npm downloads API)*
