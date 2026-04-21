# ip (npm)

**Registry:** npm
**Weekly Downloads:** ~9,552,924 (last week, fetched 2026-04-20)
**Repository:** https://github.com/indutny/node-ip
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-20 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database via OSV records, public CVE / NVD records, upstream issue / PR / commit references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for `ip`, centered on the package's `isPublic()` / IP-classification SSRF-bypass history and the later incomplete-fix follow-on that still leaves the latest npm release affected in public records. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-42282 / GHSA-78xj-cgh5-2h22 | Low | `isPublic()` could misclassify certain private IP representations such as `0x7F.1` as public, creating SSRF risk when applications used the result as a security gate. Public advisory records show fixes on both the legacy `1.x` line and the `2.x` line. | 1.1.9 and 2.0.1 | https://github.com/advisories/GHSA-78xj-cgh5-2h22 |
| CVE-2024-29415 / GHSA-2p57-rm9w-gvfp | High | Public advisory records describe an incomplete fix for the earlier SSRF-bypass issue: additional non-canonical IPv4 / IPv6 forms such as `127.1`, `01200034567`, `012.1.2.3`, and `::fFFf:127.0.0.1` could still be treated as globally routable by `isPublic()`. | No fixed npm release published in the gathered public records; OSV marks versions through 2.0.1 as affected. | https://github.com/advisories/GHSA-2p57-rm9w-gvfp |

## Security Posture Notes

- `ip` has a **small but important public package-advisory history** focused on one recurring bug class: incorrect private-vs-public address classification in helper logic that downstream code may rely on for SSRF filtering or network-boundary checks.
- The public evidence is unusually important because the newer advisory is an **incomplete-fix follow-on** rather than a totally separate bug class. OSV and GHSA records explicitly tie `CVE-2024-29415` back to the earlier `CVE-2023-42282` remediation gap.
- Exposure is **highly usage-dependent**. The package flaw is real, but exploitation generally requires an application to trust `isPublic()` / related helpers as a security decision point for outbound requests, allowlists, or internal-network reachability checks.
- The package remains widely deployed (~9.6M weekly downloads in this review pass), often transitively, so the unresolved public advisory state matters even if many consumers never call the vulnerable helpers directly.
- Current npm metadata in this pass still showed `latest=2.0.1`, which means the newest published release remained within the public affected range for `CVE-2024-29415` at review time.

## Recommendations for Developers

1. **Do not rely on `ip.isPublic()` alone as an SSRF or internal-network security boundary** while the current public advisory set still marks the latest release affected.
2. **Prefer defense in depth**: normalize addresses, resolve hostnames carefully, and enforce outbound network policy separately from package-level public/private classification helpers.
3. **Audit transitive usage** in HTTP proxy, SOCKS, PAC, or request-routing stacks that may be using `ip` under the hood.
4. **Track upstream issue / PR progress** for a future release beyond `2.0.1` before treating the incomplete-fix chain as closed.

## Dependencies of Note

- Often appears transitively in proxying, SOCKS, PAC, or address-classification helper stacks rather than as an obvious top-level dependency.
- The main practical risk surface is not generic parsing alone, but downstream code that converts its classification result into an authorization or routing decision.

## Open Questions

- Has upstream published or tagged a release after `2.0.1` that cleanly closes the public incomplete-fix advisory chain?
- Which widely used transitive consumers still call `isPublic()` or adjacent helpers as a security gate rather than as a convenience utility?
- Would a future KB pass benefit from cross-linking this page to packages or frameworks where SSRF defenses often depend on IP-range filtering?

## Related Pages

- [[npm/axios]]
- [[npm/follow-redirects]]
- [[npm/node-fetch]]
- [[npm/undici]]
- [[npm/index]]

---
*Last updated: 2026-04-20 | Sources: 8 (OSV.dev package query for npm/ip, OSV vulnerability records for GHSA-78xj-cgh5-2h22 and GHSA-2p57-rm9w-gvfp, GitHub Advisory Database entries for the same GHSA IDs, public CVE / NVD records, upstream issue / PR / commit references linked from OSV, npm registry metadata, npm downloads API)*
