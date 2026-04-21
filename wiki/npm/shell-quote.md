# shell-quote (npm)

**Registry:** npm
**Weekly Downloads:** ~46,945,151 (last week, fetched 2026-04-20)
**Repository:** https://github.com/ljharb/shell-quote
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-20 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database via OSV records, public CVE / NVD records, upstream changelog / commit references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for `shell-quote`, centered on its two published command-injection records and the later `1.7.3` Windows-drive-letter regex fix. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2016-10541 / GHSA-qg8p-v9q4-gh34 | Critical | Improper escaping of shell metacharacters such as `;`, `{`, `}`, and `>` could enable command injection when quoted output was later handed to a real shell execution path. Public advisory material specifically calls out Bash brace expansion as part of the exploit story. | 1.6.1 | https://github.com/advisories/GHSA-qg8p-v9q4-gh34 |
| CVE-2021-42740 / GHSA-g4rg-993r-mgx7 | Critical | A Windows-drive-letter regex used `[A-z]` instead of `[A-Za-z]`, letting certain shell metacharacters slip through the escaping path and enabling command injection when callers passed the quoted result into shell execution. | 1.7.3 | https://github.com/advisories/GHSA-g4rg-993r-mgx7 |

## Security Posture Notes

- `shell-quote` has a **small but severe public advisory history**: both currently published package records are command-injection issues rather than low-impact parser bugs.
- The advisories are **real package flaws**, but practical exploitability remains usage-dependent. Risk is highest when callers treat `shell-quote` as a complete safety boundary and then pass its output into shell-executing APIs such as `exec()`.
- Public upstream references line up cleanly with the advisory trail: the older npm advisory / GHSA record covers the brace-expansion-era escaping gap, while the later GHSA / OSV / changelog path points to the `1.7.3` regex correction.
- The package is still heavily consumed (~46.9M weekly downloads in this review pass), so older pinned or transitive versions below `1.7.3` continue to matter operationally even though the main advisories are not new.
- Current npm metadata showed `latest=1.8.3`, which clears both published advisory windows captured here.

## Recommendations for Developers

1. **Upgrade to `1.7.3` or newer**; current npm metadata in this pass showed `1.8.3` as the latest release.
2. **Prefer `spawn()` / `execFile()` with argument arrays over shell-string construction** when handling untrusted input; escaping libraries reduce risk but do not make shell execution a great trust boundary.
3. **Audit transitive dependencies and internal wrappers** that may still pin pre-`1.7.3` versions.
4. **Treat shell metacharacter handling as defense in depth**, not as the only control separating untrusted data from command execution.

## Dependencies of Note

- Common in developer tooling, CLI helpers, and build scripts that convert argument arrays into shell-like strings.
- Highest-risk downstream patterns are the ones that combine this package with actual shell invocation rather than mere parsing or display.

## Open Questions

- Which still-maintained build tools or wrappers pin `shell-quote` below `1.7.3` transitively?
- Are there good public maintainer notes or downstream writeups that explain how frequently `shell-quote` is used only for quoting versus being fed directly into shell execution?
- Should the KB eventually cross-link this page more explicitly with other Node.js packages whose dangerous surface depends on `child_process` execution patterns?

## Related Pages

- [[npm/cross-spawn]]
- [[npm/minimist]]
- [[npm/yargs-parser]]
- [[npm/index]]

---
*Last updated: 2026-04-20 | Sources: 8 (OSV.dev package query for npm/shell-quote, OSV vulnerability records for GHSA-qg8p-v9q4-gh34 and GHSA-g4rg-993r-mgx7, GitHub Advisory Database entries for the same GHSA IDs, public CVE / NVD records, upstream changelog / commit references linked from OSV, npm registry metadata, npm downloads API)*
