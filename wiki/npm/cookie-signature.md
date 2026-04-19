# cookie-signature (npm)

**Registry:** npm
**Weekly Downloads:** ~90,111,363 (2026-04-11 to 2026-04-17)
**Repository:** https://github.com/tj/node-cookie-signature
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-18 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream fix-commit history, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for cookie-signature's published package security history, centered on the historical timing-attack fix shipped in `1.0.4`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2016-1000236 / GHSA-92vm-wfm5-mxvv | Moderate | Public advisory records describe a timing-attack weakness in cookie-signature before `1.0.4`. The linked upstream commit trail shows the fix landing together with a version bump for the repair and follow-on signing logic cleanup. | 1.0.4 | https://github.com/advisories/GHSA-92vm-wfm5-mxvv |

## Security Posture Notes

- `cookie-signature` has a **very small published package-advisory history** in this review pass: one older but still relevant timing-attack issue.
- Even though the public advisory is old, the package remains highly deployed (~90.1M weekly downloads in this pass), largely because it sits underneath session, cookie, and Express-adjacent middleware stacks.
- The public evidence bundle is straightforward: OSV, GitHub Advisory Database, the CVE alias, and the upstream commit chain all agree on the affected range and the `1.0.4` fix point.
- This package's trust boundary is narrow but sensitive: it exists specifically to sign and unsign cookie values, so subtle cryptographic- or comparison-path weaknesses matter more than the small code size might suggest.
- Because the package is frequently transitively inherited, older vulnerable copies can persist in long-lived lockfiles even when applications do not depend on it directly.

## Recommendations for Developers

1. **Upgrade to `1.0.4` or newer**; the current latest release at review time is `1.2.2`.
2. **Audit Express and session-related dependency trees** for old transitive copies of `cookie-signature`.
3. **Treat old cryptographic helper packages as worth patching even when tiny**, because low-level comparison or signing flaws can undermine broader session-integrity assumptions.
4. **Prefer current maintained releases** instead of pinning just above the historical fix boundary when practical.

## Dependencies of Note

- Commonly used under cookie, session, and Express-adjacent middleware where signed values gate authentication or state integrity.
- Security impact is tied less to broad parser exposure and more to whether downstream code uses signed cookies for privilege, identity, or anti-tamper decisions.

## Open Questions

- Are there good public writeups that characterize the practical exploit conditions for this timing issue beyond the advisory and patch trail gathered here?
- Which still-popular Express session stacks most often bring in `cookie-signature` transitively?
- Should a future KB pass map this page more explicitly against signed-cookie middleware and session packages that depend on it?

## Related Pages

- [[npm/cookie]]
- [[npm/express]]
- [[npm/jsonwebtoken]]
- [[npm/tough-cookie]]
- [[npm/index]]

---
*Last updated: 2026-04-18 | Sources: 7 (OSV.dev package query for npm/cookie-signature, OSV vulnerability record for GHSA-92vm-wfm5-mxvv, GitHub Advisory Database entry for the same GHSA ID, public CVE / NVD record, upstream fix commits, npm registry metadata, npm downloads API)*