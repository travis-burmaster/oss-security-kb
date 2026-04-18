# braces (npm)

**Registry:** npm
**Weekly Downloads:** ~142,994,269 (last week, fetched 2026-04-18)
**Repository:** https://github.com/micromatch/braces
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-18 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database via OSV, public CVE records, upstream issue / PR / commit history, upstream changelog, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for braces' published vulnerability history, including the older 2.x ReDoS issue and the newer 3.0.3 memory-exhaustion fix for imbalanced-brace parsing. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-1109 / GHSA-cwfw-4gq5-mrqx | Medium | Regular expression denial of service (ReDoS) in the 2.x parser / regex handling path; public records mark `>= 2.2.0, < 2.3.1` as affected. | 2.3.1 | https://osv.dev/vulnerability/GHSA-cwfw-4gq5-mrqx |
| CVE-2024-4068 / GHSA-grv7-fg5c-xmjg | High | Uncontrolled resource consumption / memory exhaustion when crafted imbalanced-brace input drives the parser into unbounded allocation; public records mark versions before `3.0.3` as affected. | 3.0.3 | https://osv.dev/vulnerability/GHSA-grv7-fg5c-xmjg |

## Security Posture Notes

- `braces` has an unusually large **transitive blast radius** for a small utility package: this review pass measured roughly `142,994,269` npm downloads in the prior week, and it commonly sits under globbing / file-watching stacks rather than as an obvious top-level dependency.
- The two published advisories matter because they show **distinct parser-complexity failure modes** rather than one repeated bug: the older 2.x line carried a regex-driven ReDoS bug, while the newer 2024 record describes memory exhaustion from imbalanced-brace parsing.
- Public upstream breadcrumbs are strong enough to map both fixes with confidence: the `2.3.1` changelog entry says "Remove unnecessary escape in Regex. (#14)", and the 2024 advisory trail points to issue `#35`, PRs `#37` / `#40`, and fix commit `415d660c3002d1ab7e63dbf490c9851da80596ff` for the `3.0.3` hardening release.
- The `3.0.0` changelog entry describing a "complete refactor" is useful context for readers because it indicates that part of the earlier risk surface changed materially between the 2.x and 3.x lines, even though the newer `CVE-2024-4068` still landed later in the refactored branch.
- Operationally, exploitability depends on whether attacker-controlled strings reach braces expansion / compilation paths, but the package's deep transitive use means many downstream consumers may not realize they inherited parser-complexity risk from a low-level glob helper.
- Current public evidence from this pass points to `3.0.3+` as the minimum release line that covers the known published advisory set reviewed here.

## Dependencies of Note

- Common transitive dependency in globbing, watcher, and file-matching stacks.
- Downstream exposure is often indirect through packages such as `micromatch`-adjacent tooling rather than deliberate direct use.

## Open Questions

- Are there public maintainer or researcher writeups that explain realistic exploit preconditions for the `CVE-2024-4068` memory-exhaustion path beyond the advisory / issue / PR trail?
- Which high-download packages still pin vulnerable pre-`3.0.3` braces versions transitively?
- Has anyone published a focused parser-complexity audit that looks at brace expansion utilities as a class rather than at one package at a time?

## Related Pages

- [[npm/path-to-regexp]]
- [[npm/qs]]
- [[npm/semver]]
- [[npm/index]]

---
*Last updated: 2026-04-18 | Sources: 8 (OSV.dev, GitHub Advisory Database via OSV database links, public CVE / NVD records, upstream issue / PR history, upstream fix commits, upstream changelog, npm registry metadata, npm downloads API)*
