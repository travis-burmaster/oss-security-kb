# micromatch (npm)

**Registry:** npm
**Weekly Downloads:** ~141,663,345 (2026-04-12 to 2026-04-18)
**Repository:** https://github.com/micromatch/micromatch
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-19 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream issue / PR / commit references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for micromatch's published package security history, centered on the ReDoS issue fixed in `4.0.8` after earlier mitigation work proved incomplete. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-4067 / GHSA-952p-6rrq-rcjv | Moderate | Public advisory records describe a regular-expression denial-of-service issue in `micromatch.braces()` where greedy matching could cause heavy backtracking on crafted input. The advisory notes that earlier mitigation work existed, but the issue persisted until the later fix line that landed before `4.0.8`. | 4.0.8 | https://github.com/advisories/GHSA-952p-6rrq-rcjv |

## Security Posture Notes

- `micromatch` has a **small but meaningful published package-advisory history** in this pass: one modern ReDoS issue affecting a package that sits deep in many build, tooling, and file-matching stacks.
- The public evidence is unusually clear: OSV, GitHub Advisory Database, the CVE alias, and the linked upstream issue / PR / commit trail all point to the same `4.0.8` fix point.
- The advisory's mention of earlier incomplete mitigation work matters operationally because it warns against assuming that a prior partial patch was enough; public records normalize the safe floor at `4.0.8`.
- Even though the impact is "only" denial of service, the package is heavily deployed (~141.7M weekly downloads in this review window), and glob / pattern matching often sits in build systems, CLIs, import pipelines, and server-side filtering paths where malformed input can still be attacker-reachable.
- Public evidence gathered in this pass supports **`4.0.8+` as the clean current floor** for the published advisory history captured here.

## Recommendations for Developers

1. **Upgrade to `4.0.8` or newer**; the current latest release at review time is `4.0.8`.
2. **Treat glob and brace expansion as attacker-adjacent parsing surfaces** when patterns can come from user input, config files, API payloads, or repository content.
3. **Do not rely on older partial mitigation assumptions**; use the explicit fixed version tracked in the public advisory trail.
4. **Audit transitive copies in build tooling and developer infrastructure** because `micromatch` frequently arrives indirectly.

## Dependencies of Note

- Commonly inherited through file watchers, bundlers, test runners, linters, task runners, and glob-processing helpers.
- Security-sensitive usage includes any path where applications or tooling evaluate attacker-influenced glob or brace patterns instead of only developer-authored patterns.

## Open Questions

- Which still-popular build and tooling stacks most often pin `micromatch` below `4.0.8` transitively?
- Are there strong public downstream writeups showing realistic production exploit paths beyond the advisory and upstream patch references?
- Should a future KB pass cross-link `micromatch` with other glob / pattern-matching packages so recurring ReDoS bug classes are easier to compare?

## Related Pages

- [[npm/braces]]
- [[npm/glob-parent]]
- [[npm/path-to-regexp]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 8 (OSV.dev package query for npm/micromatch, OSV vulnerability record for GHSA-952p-6rrq-rcjv, GitHub Advisory Database entry for the same GHSA ID, public CVE record, upstream issue / PR / commit references, upstream release reference for 4.0.8, npm registry metadata, npm downloads API)*
