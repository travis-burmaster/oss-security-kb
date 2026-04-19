# got (npm)

**Registry:** npm
**Weekly Downloads:** ~32,459,963 (2026-04-12 to 2026-04-18)
**Repository:** https://github.com/sindresorhus/got
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-19 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream PR / commit / compare references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for Got's currently published package security history, centered on the 2022 redirect-to-UNIX-socket issue fixed in `11.8.5` and `12.1.0`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-33987 / GHSA-pfrx-2q88-qq97 | Moderate | Public advisory records say Got could follow a redirect to a UNIX socket, breaking expected network-boundary assumptions for affected applications. OSV and GitHub Advisory Database map the fix to `11.8.5` and `12.1.0`, with upstream PR / commit references linked from the advisory record. | 11.8.5, 12.1.0 | https://github.com/advisories/GHSA-pfrx-2q88-qq97 |

## Security Posture Notes

- Got has a **small currently published package-advisory footprint** in this pass: one public package-level record rather than a long advisory chain.
- Even so, the issue is worth tracking because Got sits on a request-routing trust boundary. Redirect behavior can cut across assumptions about host allowlists, network egress expectations, and what destinations an HTTP client should ever reach.
- The public evidence gathered here is straightforward: OSV, GitHub Advisory Database, the CVE alias, and upstream PR / commit / compare links all point at the same redirect-to-UNIX-socket fix train.
- The package remains heavily deployed (~32.5M weekly downloads in this review window), often beneath SDKs, API clients, and automation tooling rather than only as an obvious direct dependency.
- Public evidence from this pass supports **`12.1.0+` as the clean modern floor**; older `11.x` consumers should use at least `11.8.5`.

## Recommendations for Developers

1. **Upgrade to `12.1.0` or newer**; if you remain on `11.x`, use at least `11.8.5`.
2. **Review redirect handling assumptions** anywhere applications use Got with trusted-host, proxy, or service-boundary expectations.
3. **Check transitive usage in SDKs and internal client wrappers** because downstream teams may not realize Got is the HTTP engine underneath.
4. **Treat redirect behavior as security-relevant**, not just convenience logic, when clients can access privileged internal services or local sockets.

## Dependencies of Note

- Commonly used beneath higher-level API clients, CLI tooling, automation scripts, and internal service wrappers.
- Security-sensitive deployments include systems with strong egress assumptions, internal metadata exposure concerns, or mixed trust levels across redirect targets.

## Open Questions

- Are there good public maintainer writeups that explain realistic exploit preconditions for the UNIX-socket redirect issue beyond the advisory summary and fix references?
- Which still-maintained downstream packages most commonly pin Got below `11.8.5` or `12.1.0`?
- Should the KB eventually build a small cluster view for redirect-sensitive HTTP clients such as `got`, `node-fetch`, `follow-redirects`, and `undici`?

## Related Pages

- [[npm/node-fetch]]
- [[npm/follow-redirects]]
- [[npm/undici]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 7 (OSV.dev package query for npm/got, OSV vulnerability record for GHSA-pfrx-2q88-qq97, GitHub Advisory Database entry for the same GHSA ID, public CVE record, upstream PR / commit / compare references, npm registry metadata, npm downloads API)*