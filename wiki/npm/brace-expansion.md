# brace-expansion (npm)

**Registry:** npm
**Weekly Downloads:** 479,698,988 (last week, fetched 2026-05-10)
**Repository:** https://github.com/juliangruber/brace-expansion
**Security Contact:** GitHub Security Advisories / maintainer advisory history
**Disclosure Policy:** GitHub Security Advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-10 | OpenClaw recurring advisory review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / GHSA API, public CVE / NVD records, upstream issues / PRs / commits, npm registry metadata, npm downloads API) | Added a new advisory-mapped page for `brace-expansion`, covering the 2017 ReDoS record, the 2025 multi-major ReDoS fix train, and the 2026 zero-step sequence hang / memory-exhaustion advisory. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-18077 / GHSA-832h-xg76-4gv6 | Moderate | Regular expression denial of service in affected `brace-expansion` versions when crafted brace patterns drive inefficient parsing behavior; public records mark versions before `1.1.7` as affected. | 1.1.7 | [GHSA](https://github.com/advisories/GHSA-832h-xg76-4gv6), [OSV.dev](https://osv.dev/vulnerability/GHSA-832h-xg76-4gv6), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2017-18077), [upstream issue #33](https://github.com/juliangruber/brace-expansion/issues/33), [upstream PR #35](https://github.com/juliangruber/brace-expansion/pull/35), [fix commit](https://github.com/juliangruber/brace-expansion/pull/35/commits/b13381281cead487cbdbfd6a69fb097ea5e456c3) |
| CVE-2025-5889 / GHSA-v6h2-p8h4-qcjw | Moderate | ReDoS / inefficient regular-expression complexity in `expand()` across multiple maintained major lines; public records list fixes for the 1.x, 2.x, 3.x, and 4.x lines. | 1.1.12, 2.0.2, 3.0.1, 4.0.1 | [GHSA](https://github.com/advisories/GHSA-v6h2-p8h4-qcjw), [OSV.dev](https://osv.dev/vulnerability/GHSA-v6h2-p8h4-qcjw), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-5889), [patch commit](https://github.com/juliangruber/brace-expansion/pull/65/commits/a5b98a4f30d7813266b221435e1eaaf25a1b0ac5) |
| CVE-2026-33750 / GHSA-f886-m6hf-6m8v | High | A zero-step sequence such as `{1..2..0}` can prevent the sequence-generation loop from advancing, causing process hang and high memory consumption when untrusted brace patterns are expanded. | 1.1.13, 2.0.3, 3.0.2, 5.0.5 | [maintainer GHSA](https://github.com/juliangruber/brace-expansion/security/advisories/GHSA-f886-m6hf-6m8v), [GHSA](https://github.com/advisories/GHSA-f886-m6hf-6m8v), [OSV.dev](https://osv.dev/vulnerability/GHSA-f886-m6hf-6m8v), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-33750), [upstream issue #98](https://github.com/juliangruber/brace-expansion/issues/98), [PR #95](https://github.com/juliangruber/brace-expansion/pull/95), [PR #96](https://github.com/juliangruber/brace-expansion/pull/96), [PR #97](https://github.com/juliangruber/brace-expansion/pull/97) |

## Security Posture Notes

- `brace-expansion` is a very high-blast-radius parser utility: this review measured about `479,698,988` npm downloads in the prior week, and it is commonly reached indirectly through globbing / path-matching stacks rather than as an explicit application dependency.
- The public advisory history is compact but important because every confirmed package-level record is a **parser-complexity / denial-of-service** issue. That makes the package most security-relevant when attacker-controlled strings can flow into brace expansion.
- The 2025 and 2026 advisories are especially useful for dependency-management triage because they identify fixes across several maintained major lines instead of forcing all consumers onto only one branch.
- The 2026 maintainer advisory documents the core failure mode directly: a zero step makes the sequence increment evaluate to zero, so the loop variable does not advance. This is a good example of non-regex parser complexity risk in small utility packages.
- Current public evidence from this pass points to `1.1.13+`, `2.0.3+`, `3.0.2+`, or `5.0.5+` as the relevant fixed baselines for the published vulnerability set, depending on the consumer's major version line.

## Dependencies of Note

- Frequently appears transitively beneath globbing / minimatch-style dependency trees, build tools, and file-matching stacks.
- Downstream applications should assess whether user-controlled pattern strings reach brace expansion; package presence alone is not the same as exploitability.

## Open Questions

- Which high-download packages still pin vulnerable `brace-expansion` versions transitively after the 2025 and 2026 multi-line fix trains?
- Are there public maintainer notes or changelogs that map the 2026 fixes to release tags beyond the GHSA issue / PR / commit trail?
- Should this page later be linked into a broader parser-complexity cluster covering `braces`, `minimatch`, `micromatch`, `path-to-regexp`, and similar pattern parsers?

## Related Pages

- [[npm/braces]]
- [[npm/minimatch]]
- [[npm/micromatch]]
- [[npm/path-to-regexp]]
- [[npm/index]]

---
*Last updated: 2026-05-10 | Sources: 10 (OSV.dev package query and vulnerability records, GitHub Advisory Database / GHSA API records, public CVE / NVD records, upstream maintainer GHSA, upstream issue / PR / commit history, npm registry metadata, npm downloads API)*
