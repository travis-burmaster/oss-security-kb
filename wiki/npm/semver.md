# semver (npm)

**Registry:** npm
**Weekly Downloads:** ~631,089,471 (last week, fetched 2026-05-12)
**Repository:** https://github.com/npm/node-semver
**Security Contact:** opensource-security@github.com / HackerOne GitHub program
**Disclosure Policy:** https://github.com/npm/node-semver/security/policy
**Current Status:** audit-ingested

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-12 | OpenClaw agent-audit MVP | current `v7.8.0` parser / range-processing source review | hybrid metadata + source inspection + upstream tests + targeted pathological-input timing probes | No new escalation candidate found; confirmed current code uses normalized whitespace, bounded internal regexes, `MAX_LENGTH` / `MAX_SAFE_*` limits, regression coverage for the 2022 whitespace ReDoS class, and a passing upstream test/lint suite. | local source review of `npm/node-semver@efa4be6` |
| 2026-04-14 | OpenClaw recurring review | package advisory refresh | public-source curation (GitHub Advisory Database, OSV.dev, public CVE records, npm registry metadata, upstream release metadata) | Refreshed published advisory coverage, current package metadata, and public release/backport breadcrumbs for the 2022 ReDoS fixes across the 5.x / 6.x / 7.x lines. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Agent Audit MVP Source Review (2026-05-12)

**Disposition:** KB-only coverage / no maintainer escalation.

Reviewed upstream `npm/node-semver` at `v7.8.0` / commit `efa4be6096c1f9b77d9d27d6132f6220c43b4e31`, focusing on the parser-complexity and ReDoS history represented by `GHSA-c2qf-rxjj-qqgw` and `GHSA-x6fg-f45m-jf5q`.

Evidence from this pass:

- `SECURITY.md` now points vulnerability reports to `opensource-security@github.com` or the GitHub HackerOne program, and explicitly asks researchers not to use public issues / PRs for security reports.
- `classes/range.js` normalizes range whitespace up front with `range.trim().replace(/\s+/g, ' ')` before applying the historical range-normalization regexes.
- `classes/semver.js` rejects version strings longer than `MAX_LENGTH` (`256`) before matching version regexes.
- `internal/re.js` builds both exported regexes and safer internal regexes; internal consumers use `safeRe`, and `makeSafeRegex()` bounds formerly greedy `\s`, `\d`, and identifier-character repetitions.
- `test/integration/whitespace.js` includes a 500,000-character whitespace regression case for range parsing and a large-zero invalid-input case for the 2022-style ReDoS surface.
- `npm test` completed successfully on the cloned upstream repo, including test coverage and lint/template checks.
- A small local timing probe over long whitespace, long numeric, many-`||`, and caret-spacing cases did not surface an obvious incomplete-fix candidate; the slowest intentionally invalid 500k-zero comparator case threw after roughly 755ms locally, while the whitespace regression path completed in a few milliseconds.
- `npm audit --omit=dev` reported zero production dependency vulnerabilities for the package install used in this review.
- Independent comparison review reached the same disposition and noted one compatibility caveat: semver still exports legacy raw `re` / `src` regexes for userland compatibility, while internal parser paths use `safeRe`. That exported surface is not evidence that `new Range()` remains vulnerable, but downstream users should avoid applying raw exported regexes to untrusted large strings without their own input caps.

No upstream issue, PR, or private disclosure was opened because this pass did not produce a minimal failing repro or maintainer-verifiable security defect.

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-c2qf-rxjj-qqgw / CVE-2022-25883 | High | Regular expression denial of service (ReDoS) in semver range processing; GitHub Advisory data maps the affected modern release lines to `>= 7.0.0, < 7.5.2`, `>= 6.0.0, < 6.3.1`, and `>= 2.0.0-alpha, < 5.7.2`. | 7.5.2 / 6.3.1 / 5.7.2 | https://github.com/advisories/GHSA-c2qf-rxjj-qqgw |
| GHSA-x6fg-f45m-jf5q / CVE-2015-8855 | High | Earlier ReDoS issue in semver's regex handling; public GHSA records mark versions `>= 1.0.4, < 4.3.2` as affected. | 4.3.2 | https://github.com/advisories/GHSA-x6fg-f45m-jf5q |

## Security Posture Notes

- Critical infrastructure package for dependency resolution and version gating across the JavaScript ecosystem.
- Current upstream disclosure posture is clearer than the earlier KB metadata suggested: GitHub-managed `SECURITY.md` directs vulnerability reports to `opensource-security@github.com` or the GitHub HackerOne program and discourages public security issues / PRs.
- The current `v7.8.0` source review found the ReDoS hardening concentrated in three places: early version-length rejection, whitespace normalization before range regex processing, and internally bounded `safeRe` regexes.
- Downstream compatibility caveat: semver still exports legacy raw regexes (`re` / `src`) for userland consumption; applications should prefer package APIs or apply explicit input caps before using those exported regexes on untrusted large strings.
- Public advisory history spans **at least two distinct parser-complexity failure modes** rather than one repeated bug: CVE-2015-8855 affected older releases before 4.3.2, while CVE-2022-25883 affected modern range parsing across the 5.x / 6.x / 7.x lines.
- The public remediation trail for the 2022 issue is unusually traceable: the GitHub Advisory references upstream PR `#564` and its fix commit, while GitHub release metadata for `v7.5.2`, `v6.3.1`, and `v5.7.2` all publicly note the same "better handling of whitespace" bug-fix theme tied to the backport set.
- That release trail matters operationally because it shows maintainers shipped the ReDoS hardening across three active lines rather than only on the newest major branch.
- Current npm metadata shows `semver` remains one of the highest-leverage parser dependencies in the ecosystem (`~632,658,124` downloads in the last week of this review pass; latest release `7.7.4`), so even parser-only denial-of-service issues have unusually broad downstream relevance.
- No newer published GHSA advisories were identified in this review pass beyond the 2015 and 2022 ReDoS records above.

## Dependencies of Note

- Commonly embedded in package managers, build tooling, and release automation.

## Open Questions

- Are there additional pathological range expressions not covered by the published 5.7.2 / 6.3.1 / 7.5.2 fixes? **Partially checked 2026-05-12:** no obvious current `v7.8.0` incomplete-fix candidate found in a focused source/test/timing pass, but broader fuzzing remains useful.
- Can the targeted timing probe be promoted into a reusable parser-complexity harness for semver-like packages?
- Which package managers or build tools still bundle pre-fix semver versions across the 4.x, 5.x, 6.x, or early 7.x lines?
- Can we systematically catalog the highest-risk user-controlled semver parsing entry points across popular tooling?

## Related Pages

- [[npm/index]]
- [[npm/lodash]]
- [[npm/minimist]]

---
*Last updated: 2026-05-12 | Sources: 13 (GitHub Advisory Database / GHSA, OSV.dev, public CVE records, npm registry metadata, npm downloads API, upstream PR / fix-commit history, GitHub release metadata for v5.7.2 / v6.3.1 / v7.5.2, upstream `SECURITY.md`, current `v7.8.0` source at `efa4be6`, upstream test suite, local pathological-input timing probe, and `npm audit --omit=dev`)*
