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
| GHSA-c2qf-rxjj-qqgw | Moderate | Regular expression denial of service (ReDoS) in semver range processing | 7.5.2 / 6.3.1 / 5.7.2 | https://github.com/advisories/GHSA-c2qf-rxjj-qqgw |

## Security Posture Notes

- Critical infrastructure package for dependency resolution and version gating across the JavaScript ecosystem.
- ReDoS history makes it a strong candidate for targeted input-complexity analysis.
- Advisory references point directly to `Range` parsing and regex-heavy internals, making semver a useful package for documenting parser-complexity failure modes in ecosystem-critical infrastructure.
- Small surface area but unusually high ecosystem leverage.

## Dependencies of Note

- Commonly embedded in package managers, build tooling, and release automation.

## Open Questions

- Are there additional pathological range expressions not covered by current fixes?
- Has a focused parser-complexity review ever been published?
- Which package managers or build tools still bundle old versions?
- Can we systematically catalog the highest-risk user-controlled semver parsing entry points across popular tooling?

## Related Pages

- [[npm/index]]
- [[npm/lodash]]
- [[npm/minimist]]

---
*Last updated: 2026-04-07 | Sources: 2*
