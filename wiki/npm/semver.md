# semver (npm)

**Registry:** npm
**Weekly Downloads:** ~632,658,124 (last week, fetched 2026-04-14)
**Repository:** https://github.com/npm/node-semver
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-refreshed

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-14 | OpenClaw recurring review | package advisory refresh | public-source curation (GitHub Advisory Database, OSV.dev, public CVE records, npm registry metadata, upstream release metadata) | Refreshed published advisory coverage, current package metadata, and public release/backport breadcrumbs for the 2022 ReDoS fixes across the 5.x / 6.x / 7.x lines. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-c2qf-rxjj-qqgw / CVE-2022-25883 | High | Regular expression denial of service (ReDoS) in semver range processing; GitHub Advisory data maps the affected modern release lines to `>= 7.0.0, < 7.5.2`, `>= 6.0.0, < 6.3.1`, and `>= 2.0.0-alpha, < 5.7.2`. | 7.5.2 / 6.3.1 / 5.7.2 | https://github.com/advisories/GHSA-c2qf-rxjj-qqgw |
| GHSA-x6fg-f45m-jf5q / CVE-2015-8855 | High | Earlier ReDoS issue in semver's regex handling; public GHSA records mark versions `>= 1.0.4, < 4.3.2` as affected. | 4.3.2 | https://github.com/advisories/GHSA-x6fg-f45m-jf5q |

## Security Posture Notes

- Critical infrastructure package for dependency resolution and version gating across the JavaScript ecosystem.
- Public advisory history spans **at least two distinct parser-complexity failure modes** rather than one repeated bug: CVE-2015-8855 affected older releases before 4.3.2, while CVE-2022-25883 affected modern range parsing across the 5.x / 6.x / 7.x lines.
- The public remediation trail for the 2022 issue is unusually traceable: the GitHub Advisory references upstream PR `#564` and its fix commit, while GitHub release metadata for `v7.5.2`, `v6.3.1`, and `v5.7.2` all publicly note the same "better handling of whitespace" bug-fix theme tied to the backport set.
- That release trail matters operationally because it shows maintainers shipped the ReDoS hardening across three active lines rather than only on the newest major branch.
- Current npm metadata shows `semver` remains one of the highest-leverage parser dependencies in the ecosystem (`~632,658,124` downloads in the last week of this review pass; latest release `7.7.4`), so even parser-only denial-of-service issues have unusually broad downstream relevance.
- No newer published GHSA advisories were identified in this review pass beyond the 2015 and 2022 ReDoS records above.

## Dependencies of Note

- Commonly embedded in package managers, build tooling, and release automation.

## Open Questions

- Are there additional pathological range expressions not covered by the published 5.7.2 / 6.3.1 / 7.5.2 fixes?
- Has a focused parser-complexity review ever been published that covers both version-string and range-string attack surfaces together?
- Which package managers or build tools still bundle pre-fix semver versions across the 4.x, 5.x, 6.x, or early 7.x lines?
- Can we systematically catalog the highest-risk user-controlled semver parsing entry points across popular tooling?

## Related Pages

- [[npm/index]]
- [[npm/lodash]]
- [[npm/minimist]]

---
*Last updated: 2026-04-14 | Sources: 8 (GitHub Advisory Database / GHSA, OSV.dev, public CVE records, npm registry metadata, npm downloads API, upstream PR / fix-commit history, and GitHub release metadata for v5.7.2, v6.3.1, and v7.5.2)*
