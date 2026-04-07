# minimist (npm)

**Registry:** npm
**Weekly Downloads:** unknown (as of 2026-04-07)
**Repository:** https://github.com/minimistjs/minimist
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
| CVE-2020-7598 | High | Prototype pollution via argument parsing | 1.2.3 / 0.2.1 | https://github.com/advisories/GHSA-vh95-rmgr-6w4m |

## Security Posture Notes

- Tiny package, huge blast radius because it sits in CLI parsing paths throughout the npm ecosystem.
- Historically important because the bug class is simple, common, and widely propagated through transitive dependencies.
- High-value candidate for surface mapping beyond just known CVEs.

## Dependencies of Note

- Often appears as a transitive dependency in CLIs and build tools.

## Open Questions

- Which currently popular packages still pin vulnerable minimist versions transitively?
- Has anyone published a modern full-source audit after the original prototype pollution fixes?
- Are there parser edge cases beyond the known CVE lineage worth cataloging?

## Related Pages

- [[npm/index]]
- [[npm/lodash]]
- [[npm/semver]]

---
*Last updated: 2026-04-07 | Sources: 1*
