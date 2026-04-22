# path-parse (npm)

**Registry:** npm
**Weekly Downloads:** ~117,196,974 (2026-04-14 to 2026-04-20)
**Repository:** https://github.com/jbgutierrez/path-parse
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-21 | OpenClaw recurring review | package comparison pass | public-source curation (OSV.dev, GitHub Advisory Database, npm registry metadata) | Confirmed one older public package advisory, but intentionally deferred because the package was already on latest `1.0.7` and the maintenance window prioritized larger gaps. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| 2026-04-22 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public upstream issue / PR / fix-commit references, npm registry metadata, npm downloads API, local Claude-compatible proxy used only as a drafting aid) | Added a new advisory-mapped page for `path-parse`'s single currently published package vulnerability: the pre-`1.0.7` ReDoS issue tracked as `GHSA-hj48-42vr-x3v9` / `CVE-2021-23343`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-hj48-42vr-x3v9 / CVE-2021-23343 | Medium | Public GHSA / OSV records describe polynomial-time regular-expression denial of service in `splitDeviceRe`, `splitTailRe`, and `splitPathRe`, allowing crafted invalid path strings to consume excessive CPU during parsing before `1.0.7`. | 1.0.7 | https://github.com/advisories/GHSA-hj48-42vr-x3v9 |

## Security Posture Notes

- `path-parse` is a very small package with a **single currently published package-scoped advisory** in this review pass rather than a broad vulnerability history.
- The public issue trail is unusually crisp: issue `#8` reported ReDoS behavior with a simple crafted path-string reproducer, PR `#10` was explicitly titled `fixed regexes to avoid ReDoS attacks`, and merge commit `eca63a7` replaced the earlier regex structure with less explosive alternatives.
- OSV and the GitHub Advisory Database agree on the affected range (`< 1.0.7`) and the remediation point (`1.0.7`), while npm registry metadata shows `1.0.7` is still the current latest release.
- The package remains worth tracking despite the old fix because its install base is still large in transitive dependency graphs (**~117.2M weekly downloads** in this review window).
- No additional package-scoped OSV records were surfaced for `path-parse` in this pass.
- No public `SECURITY.md`, dedicated security contact, or separate disclosure-policy URL was confirmed in the upstream repository during this review.

## Recommendations for Developers

1. **Upgrade to `1.0.7` or later** anywhere `path-parse` can still be pulled transitively below the fixed release.
2. **Check lockfiles and bundled dependencies**, not just direct `package.json` entries, because this package commonly lands as a tiny transitive utility.
3. **Treat parser-only ReDoS bugs as real operational risk** when path-like input can be attacker-controlled at scale.

## Dependencies of Note

- Commonly appears as a small transitive path utility rather than a consciously selected direct dependency.
- Path-handling helpers like this can matter disproportionately in build tooling, bundlers, and file-processing pipelines that accept untrusted or user-shaped path strings.

## Open Questions

- Which still-popular toolchains or packages continue to pin `path-parse` below `1.0.7` transitively?
- Has any later public review revisited path-parser edge cases beyond the fixed regex-complexity bug?
- Should a future KB pass cross-link small, high-blast-radius parser utilities with similar one-advisory-but-huge-install-base profiles?

## Related Pages

- [[npm/path-to-regexp]]
- [[npm/minimist]]
- [[npm/index]]

---
*Last updated: 2026-04-22 | Sources: 7 (OSV.dev package query, OSV vulnerability record for GHSA-hj48-42vr-x3v9, GitHub Advisory Database / public GHSA page, public upstream issue jbgutierrez/path-parse#8, public upstream PR jbgutierrez/path-parse#10, public fix commit eca63a7, npm registry / downloads metadata)*
