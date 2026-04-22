# sanitize-html (npm)

**Registry:** npm
**Weekly Downloads:** ~8,023,948 (2026-04-15 to 2026-04-21)
**Repository:** https://github.com/apostrophecms/sanitize-html
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-22 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / public GitHub security advisories, public CVE records, upstream issue / PR / commit references, npm registry metadata, npm downloads API, local Claude-compatible proxy used only as a drafting aid) | Added a new advisory-mapped page for `sanitize-html`'s published package security history, covering nine public records across repeated XSS / sanitization-bypass, input-validation, ReDoS, and information-exposure fixes through `2.17.3`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-16017 / GHSA-wg96-3933-j2w5 | High | Cross-site scripting issue in older `sanitize-html` releases; OSV maps the affected range to versions before `1.2.3`, with public references pointing to upstream issue `#19` and PR `#20`. | 1.2.3 | https://github.com/advisories/GHSA-wg96-3933-j2w5 |
| CVE-2016-1000237 / GHSA-3j7m-hmh3-9jmp | Moderate | Cross-site scripting issue in older releases; the public reference set links upstream issue `#29` plus fix commit `762fbc7`, and OSV maps the affected range to versions before `1.4.3`. | 1.4.3 | https://github.com/advisories/GHSA-3j7m-hmh3-9jmp |
| CVE-2017-16016 / GHSA-xc6g-ggrc-qq4r | Moderate | Cross-site scripting issue tracked through upstream issue `#100`; OSV maps the affected range to versions before `1.11.4`. | 1.11.4 | https://github.com/advisories/GHSA-xc6g-ggrc-qq4r |
| CVE-2019-25225 / GHSA-qhxp-v273-g94h | Moderate | Incomprehensive sanitization leading to XSS; OSV maps the affected range to versions before the `2.0.0-beta` fix train, with the public trail pointing to upstream issue `#293`, PR `#156`, and commit `712cb68`. | 2.0.0-beta | https://github.com/advisories/GHSA-qhxp-v273-g94h |
| CVE-2021-26539 / GHSA-rjqq-98f6-6j3r | Moderate | Improper input validation issue in versions before `2.3.1`; public references include upstream PR `#458` and fix commit `bdf7836`. | 2.3.1 | https://github.com/advisories/GHSA-rjqq-98f6-6j3r |
| CVE-2021-26540 / GHSA-mjxr-4v3x-q3m4 | Moderate | Follow-on improper input validation issue in versions before `2.3.2`; public references include upstream PR `#460` and the `2.3.2` changelog anchor. | 2.3.2 | https://github.com/advisories/GHSA-mjxr-4v3x-q3m4 |
| CVE-2022-25887 / GHSA-cgfm-xwp7-2cvr | High | Regular-expression denial of service (ReDoS) in versions before `2.7.1`; public references include upstream PR `#557` and fix commit `b4682c1`. | 2.7.1 | https://github.com/advisories/GHSA-cgfm-xwp7-2cvr |
| CVE-2024-21501 / GHSA-rm97-x556-q36h | Moderate | Information-exposure issue in versions before `2.12.1`; public references include upstream PR `#650`, fix commit `c5dbdf7`, and a published proof-of-concept gist linked from OSV. | 2.12.1 | https://github.com/advisories/GHSA-rm97-x556-q36h |
| CVE-2026-40186 / GHSA-9mrh-v2v3-xpfm | Moderate | `allowedTags` bypass via entity-decoded text in `nonTextTags` elements; OSV maps the affected range narrowly to `2.17.2` before the `2.17.3` fix. | 2.17.3 | https://github.com/advisories/GHSA-9mrh-v2v3-xpfm |

## Security Posture Notes

- `sanitize-html` sits directly on a trust boundary: callers use it specifically to reduce XSS risk, so even moderate-severity bypasses matter more than they might in a non-sanitizer utility package.
- The public package record gathered in this pass is substantial but coherent: **nine published OSV / GHSA records** spanning early `1.x`, the `2.0.0-beta` transition, and the modern `2.x` line.
- Most of the published history clusters around **XSS / sanitization-bypass and input-validation failures**, which is consistent with the package's role and a signal that defaults and option interactions deserve scrutiny during upgrades.
- The package also has at least one clearly distinct **availability-oriented ReDoS issue** (`CVE-2022-25887`) and one **information-exposure** issue (`CVE-2024-21501`), so the public record is not limited to classic XSS framing.
- The 2021 pair (`CVE-2021-26539` fixed in `2.3.1` and `CVE-2021-26540` fixed in `2.3.2`) is worth preserving as a compact follow-on fix train rather than two unrelated isolated bugs.
- The newest record is especially actionable: OSV maps `CVE-2026-40186` to a narrow regression window affecting `2.17.2` and fixed in `2.17.3`, which suggests some recent consumers could be only one patch release away from current coverage.
- Current npm metadata in this pass showed **`latest=2.17.3`**, which clears all nine public advisory records gathered here.
- The upstream GitHub API returned **no formal Releases objects** during this pass, so version-history normalization relies mainly on npm publish timestamps, tags, and the issue / PR / commit links preserved through OSV and GHSA.
- Upstream repository identity is a little noisy in older references: some public links still point to the historical `punkave/sanitize-html` namespace while the maintained repository now lives at `apostrophecms/sanitize-html`.
- No upstream `SECURITY.md` was confirmed in this pass, so there is no clearly documented repository-level disclosure path to point readers at beyond public advisory / issue channels.
- Current npm download data still shows meaningful ecosystem reach (**~8.0M weekly downloads**), so even narrow sanitizer regressions can have a broad downstream blast radius.

## Recommendations for Developers

1. **Upgrade to `2.17.3` or newer**; current npm metadata in this pass showed `2.17.3` as the latest release and the first version that clears the full public advisory set gathered here.
2. **Review sanitizer configuration, not just package version** — the newest public issue explicitly involves `allowedTags` and `nonTextTags` behavior, so custom option sets deserve regression testing on upgrade.
3. **Treat `sanitize-html` as one layer of defense-in-depth rather than a sole XSS control**; pair it with contextual output encoding, framework-safe rendering patterns, and CSP where appropriate.
4. **Track advisories proactively in dependency tooling** because the package's public history shows repeated follow-on fixes and regressions rather than a one-time historical cluster.

## Dependencies of Note

- Commonly embedded in CMS workflows, rich-text / WYSIWYG pipelines, Markdown-to-HTML rendering flows, comment systems, and any server-side or client-side feature that accepts user-authored HTML.
- Security relevance is highest where applications allow custom sanitizer options or process attacker-controlled HTML repeatedly at scale.

## Open Questions

- Which still-popular CMS, editor, or content-processing stacks pin `sanitize-html` below `2.17.3`?
- Are there public maintainer notes that better explain the exact root-cause relationship between the 2021 pair and the 2026 `nonTextTags` / entity-decoding bypass?
- Should a future KB pass cluster `sanitize-html` with adjacent sanitization packages to compare recurring option-interaction failure modes across ecosystems?

## Related Pages

- [[npm/marked]]
- [[npm/markdown-it]]
- [[npm/handlebars]]
- [[npm/index]]

---
*Last updated: 2026-04-22 | Sources: 12 (OSV.dev package query for npm/sanitize-html, OSV vulnerability records for the nine published GHSA entries above, GitHub Advisory Database / public GitHub security advisories for the same records, public CVE / NVD records, upstream issues / PRs / fix commits linked from OSV and GHSA, npm registry metadata, npm downloads API, and GitHub repository metadata for apostrophecms/sanitize-html)*
