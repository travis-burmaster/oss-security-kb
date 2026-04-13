# semver (npm)

**Registry:** npm
**Weekly Downloads:** unknown (as of 2026-04-07)
**Repository:** https://github.com/npm/node-semver
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-c2qf-rxjj-qqgw / CVE-2022-25883 | High | Regular expression denial of service (ReDoS) in semver range processing | 7.5.2 / 6.3.1 / 5.7.2 | https://github.com/advisories/GHSA-c2qf-rxjj-qqgw |
| GHSA-x6fg-f45m-jf5q / CVE-2015-8855 | High | Earlier ReDoS issue in semver's regex handling, fixed in the 4.x line | 4.3.2 | https://github.com/advisories/GHSA-x6fg-f45m-jf5q |

## Security Posture Notes

- Critical infrastructure package for dependency resolution and version gating across the JavaScript ecosystem.
- Public advisory history spans at least two distinct parser-complexity failure modes rather than one repeated bug: CVE-2015-8855 affected parsing of extremely long version strings in older releases, while CVE-2022-25883 / GHSA-c2qf-rxjj-qqgw affected `new Range()` handling of untrusted range expressions across the modern 5.x / 6.x / 7.x lines.
- The public fix record is unusually traceable: GitHub Advisory / OSV references point to separate fixes and backports, and the linked upstream PRs show maintainers landing the range-handling remediation on `main`, `release/v5`, and `release/v6` rather than only patching the latest branch.
- Advisory references point directly to `Range` parsing and regex-heavy internals, making semver a useful package for documenting parser-complexity failure modes in ecosystem-critical infrastructure.
- Small surface area but unusually high ecosystem leverage.

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
*Last updated: 2026-04-13 | Sources: 6 (GitHub Advisory Database / GHSA, OSV, CVE records, upstream public PR / release history)*
