# http-proxy (npm)

**Registry:** npm
**Weekly Downloads:** ~23,751,158 (last week, fetched 2026-04-22)
**Repository:** https://github.com/http-party/node-http-proxy
**Security Contact:** none listed
**Disclosure Policy:** none listed (no public `SECURITY.md` found in this pass)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-22 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev package query, GitHub Advisory Database / public GHSA pages, public CVE / NVD record, upstream changelog, npm registry metadata, npm downloads API) | Added a new advisory-mapped page for `http-proxy`'s currently published package-level security history. Public evidence in this pass cleanly confirmed two direct denial-of-service records and tied the newer one to the `v1.18.1` fix release. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-6x33-pw7p-hmpq | High | A crafted HTTP request with a long body could trigger an unhandled `ERR_HTTP_HEADERS_SENT` exception and crash affected proxy servers when the application used `proxyReq.setHeader`, resulting in denial of service. Public evidence ties the fix to upstream PR `#1447`, and the changelog explicitly marks `v1.18.1` as the release carrying that change. | 1.18.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-6x33-pw7p-hmpq) |
| GHSA-9xw9-pvgv-6p76 / CVE-2017-16014 | High | Older versions had insufficient error handling, allowing an attacker who could force an error path to crash the server and cause denial of service. Public advisory and NVD records both point to upstream PR `#101` as the key fix reference. | 0.7.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-9xw9-pvgv-6p76) |

## Security Posture Notes

- The public package-level history gathered in this pass is **small but direct**: the OSV package query returned two published advisories, and both are denial-of-service issues rather than ambiguous downstream misconfiguration concerns.
- `http-proxy` sits on a high-value trust boundary because it is used to forward requests, rewrite headers, and bridge traffic between clients and upstream services. Even advisory counts that look small matter more here than they would in a low-impact utility library.
- The newer 2020 advisory is especially operationally relevant because it only becomes reachable when an application uses the `proxyReq.setHeader` path, so real-world exploitability depends partly on how the library is integrated rather than on a one-size-fits-all request pattern.
- Upstream changelog material lines up cleanly with the advisory trail reviewed here: `v1.18.1` is the security-relevant release for the long-body crash path, and the maintained npm `latest` tag in this pass was also `1.18.1`.
- No public repository-level `SECURITY.md` or separate disclosure-policy URL was confirmed in this pass. That documentation gap is worth recording for a package with this download volume, but it is **not** being presented as a vulnerability by itself.

## Recommendations for Developers

1. **Use `1.18.1` or newer** if you rely on the currently published `http-proxy` release line, because the latest public npm metadata reviewed here already includes the newest confirmed package-level fix.
2. **Treat proxy error paths and request-rewrite hooks as security-relevant behavior**, not just operational plumbing; both published issues in this pass are availability failures triggered by exceptional request handling.
3. **Review any code that uses `proxyReq.setHeader` or other request mutation hooks** when testing upgrades, because the 2020 denial-of-service issue was specifically tied to that integration path.
4. **Add explicit error-handling and resilience testing around malformed or oversized requests** instead of validating only success cases, since both public records reviewed here are fundamentally crash / DoS stories.

## Dependencies of Note

- Commonly deployed behind reverse proxies, gateways, developer tooling, and service meshes built in Node.js, so package-level stability bugs can have broad downstream blast radius.
- Frequently appears underneath higher-level wrappers and middleware, which means some downstream packages may inherit the practical impact of `http-proxy` issues even when the GHSA is scoped only to this package.

## Open Questions

- Are there maintainer-authored postmortems or issue discussions beyond PR `#1447` that better explain the boundary conditions for the 2020 long-body crash path?
- Which widely used downstream wrappers still pin `http-proxy` below `1.18.1` in long-lived support branches?
- Would a future proxy-cluster review benefit from a comparison page linking `http-proxy`, `http-proxy-middleware`, `follow-redirects`, and `node-fetch` around request-routing and trust-boundary failure patterns?

## Related Pages

- [[npm/http-proxy-middleware]]
- [[npm/follow-redirects]]
- [[npm/undici]]
- [[npm/express]]
- [[npm/index]]

---
*Last updated: 2026-04-22 | Sources: 8 (OSV.dev package query for npm/http-proxy, detailed OSV records for GHSA-6x33-pw7p-hmpq and GHSA-9xw9-pvgv-6p76, public GitHub Advisory Database / GHSA pages, public NVD record for CVE-2017-16014, upstream CHANGELOG.md, npm registry metadata, npm downloads API)*
