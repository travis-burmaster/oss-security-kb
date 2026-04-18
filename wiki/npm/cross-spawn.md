# cross-spawn (npm)

**Registry:** npm
**Weekly Downloads:** ~173,814,017 (last week, fetched 2026-04-18)
**Repository:** https://github.com/moxystudio/node-cross-spawn
**Security Contact:** none listed
**Disclosure Policy:** GitHub Security Advisories / repository issues and PRs
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-17 | OpenClaw recurring review | package advisory curation | public-source curation (GitHub Advisory Database, OSV.dev, public CVE aliases, upstream changelog / fix commits, npm registry metadata, npm downloads API) | 1 published package advisory mapped; fix lineage shows an initial regex-backtracking hardening release followed immediately by a corrective patch release | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-21538 / GHSA-3xgq-45jj-v275 | High | Improper input sanitization in the package's escaping / regular-expression handling allowed crafted very large strings to trigger catastrophic backtracking, driving CPU usage high enough to hang or crash the process. | 6.0.6 / 7.0.5 | [GitHub Advisory Database](https://github.com/advisories/GHSA-3xgq-45jj-v275), [OSV](https://osv.dev/vulnerability/GHSA-3xgq-45jj-v275) |

## Security Posture Notes

- `cross-spawn` is a very high-fan-in transitive dependency because it underpins process-spawning behavior across a large amount of build tooling and CLI infrastructure.
- Public advisory data currently shows **one published package-level record** for the package: the 2024 ReDoS issue tracked as `CVE-2024-21538` / `GHSA-3xgq-45jj-v275`.
- The public fix trail is unusually readable: upstream changelog and commit metadata show `7.0.4` first **disabled regexp backtracking**, then `7.0.5` **fixed an escaping bug introduced by that backtracking change**, which is why `7.0.5` is the first safe 7.x version reflected in OSV / GHSA metadata.
- OSV maps two safe branches: older releases are fixed in `6.0.6`, while the 7.x line is fixed in `7.0.5`; current npm metadata shows the latest version is `7.0.6`.
- Because the package is usually transitive, real-world remediation often requires lockfile refreshes rather than only top-level `package.json` changes.

## Recommendations for Developers

1. **Run at least `7.0.5`** on the 7.x line, or **`6.0.6`** if you are constrained to the older 6.x line.
2. **Refresh lockfiles and CI caches**, not just top-level dependency constraints, because `cross-spawn` is often pulled in indirectly.
3. **Treat build / CLI dependencies as production-relevant** when they process attacker-influenced input in hosted CI, developer portals, or multi-tenant automation systems.

## Dependencies of Note

- Commonly appears transitively in CLI and build-tool chains rather than as a consciously chosen direct dependency.
- The package's security relevance is amplified by ecosystem reach rather than by a long public vulnerability list.

## Open Questions

- Are there public downstream advisories or major release notes from popular dependents that explicitly called out the `cross-spawn` fix during lockfile refreshes?
- Did upstream publish any deeper maintainer writeup beyond the advisory references and changelog breadcrumbs that would better explain exploit preconditions?

## Related Pages

- [[npm/minimist]]
- [[npm/semver]]
- [[npm/debug]]
- [[npm/index]]

---
*Last updated: 2026-04-17 | Sources: 6 (GitHub Advisory Database JSON / GHSA page, OSV.dev package query, public CVE alias, upstream CHANGELOG.md, upstream fix commit metadata, npm registry metadata, npm downloads API)*
