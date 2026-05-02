# tar (npm)

**Registry:** npm
**Weekly Downloads:** ~65,379,500 (as of 2026-04-13)
**Repository:** https://github.com/isaacs/node-tar
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-13 | OpenClaw recurring review | package advisory history | manual | Curated 15 published advisories spanning 2015-2026 using OSV, GitHub advisory pages, CVE aliases, npm registry metadata, public fix references, and repo-policy checks; tar was the clearest substantive gap from this pass compared with `ws` and `handlebars`. | https://osv.dev/list?ecosystem=npm&q=tar |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2015-8860 / GHSA-gfjr-3jmm-4g9v | High | Early `tar` releases allowed symlink-based arbitrary file overwrite during extraction, establishing the package's long-running archive-path trust-boundary risk. | 2.0.0 | https://github.com/advisories/GHSA-gfjr-3jmm-4g9v |
| CVE-2018-20834 / GHSA-j44m-qm6p-hp7m | High | Another arbitrary file overwrite issue showed that extraction-path protections were still incomplete across supported lines. | 2.2.2 / 4.4.2 | https://github.com/advisories/GHSA-j44m-qm6p-hp7m |
| CVE-2021-32804 / GHSA-3jfq-g458-7qm9 | High | Absolute-path sanitization bypass allowed crafted archives to create or overwrite files outside the intended destination. | 3.2.2 / 4.4.14 / 5.0.6 / 6.1.1 | https://github.com/advisories/GHSA-3jfq-g458-7qm9 |
| CVE-2021-32803 / GHSA-r628-mhmh-qjhw, CVE-2021-37701 / GHSA-9r2w-394v-53qc, CVE-2021-37712 / GHSA-qq89-hq3f-393p, CVE-2021-37713 / GHSA-5955-9wpr-37jh | High | The 2021 advisory cluster documented repeated symlink-protection, directory-cache-poisoning, and Windows path-sanitization bypasses, with multiple follow-on fixes across 3.x-6.x branches. | 3.2.3 / 4.4.15-4.4.18 / 5.0.7-5.0.10 / 6.1.2-6.1.9 | https://github.com/advisories/GHSA-r628-mhmh-qjhw |
| CVE-2024-28863 / GHSA-f5x3-32g6-xq36 | Moderate | Denial of service while parsing a crafted tar file because folder-count validation was missing. | 6.2.1 | https://github.com/advisories/GHSA-f5x3-32g6-xq36 |
| CVE-2025-64118 / GHSA-29xp-372q-xqph | Moderate | A race condition could expose uninitialized memory during archive handling in the 7.x line. | 7.5.2 | https://github.com/advisories/GHSA-29xp-372q-xqph |
| CVE-2026-23745 / GHSA-8qq5-rm4j-mr97, CVE-2026-23950 / GHSA-r6q2-hw4h-h46w, CVE-2026-24842 / GHSA-34x7-hfp2-rc4v, CVE-2026-26960 / GHSA-83g3-92jg-28cx, CVE-2026-29786 / GHSA-qffp-2rhf-9h96, CVE-2026-31802 / GHSA-9ppj-qmqm-q256 | High | The 2026 `7.5.x` chain added more bypasses around symlink / hardlink traversal, symlink poisoning, drive-relative linkpaths, symlink-chain escapes, and macOS APFS Unicode-collision edge cases, showing another fix-then-bypass cycle in extraction safety logic. | 7.5.3 / 7.5.4 / 7.5.7 / 7.5.8 / 7.5.10 / 7.5.11 | https://github.com/advisories/GHSA-8qq5-rm4j-mr97 |

*Full CVE history: https://osv.dev/list?ecosystem=npm&q=tar*

## Security Posture Notes

- Public advisory history for `tar` is dominated by **archive extraction trust-boundary bugs**: symlink following, hardlink traversal, directory cache poisoning, absolute-path handling, Windows drive-relative behavior, and newer filesystem edge cases such as APFS Unicode normalization.
- The package shows a clear **fix-then-bypass pattern** in two major eras: the dense 2021 chain across older branches and the 2025-2026 `7.5.x` chain. That makes intermediate patch levels materially risky, not just obviously ancient versions.
- `tar` remains a very high-blast-radius dependency at roughly **65.4 million weekly npm downloads** in this review pass, so even locally triggered extraction bugs can cascade widely through developer tooling and CI pipelines.
- Public metadata in this pass did **not** show a repository-root `SECURITY.md`, so the package looks less explicit about disclosure process than some modern peers even though fixes are clearly being shipped.
- The current latest npm version (`7.5.13`) is beyond every publicly listed fixed version surfaced in this pass, which is good operationally, but the advisory cadence suggests downstream users should watch patch releases closely rather than waiting for major upgrades.
- Compared with other candidates reviewed in the same pass (`ws`, `handlebars`), `tar` was the cleanest page-addition target because the public package-level advisory trail is dense, well-linked, and strongly versioned through OSV / GHSA data.

## Dependencies of Note

- `tar` often lands transitively through Node.js packaging and build tooling, so SBOM and lockfile checks matter more than direct dependency declarations alone.
- Archive extraction paths interacting with symlinks, hardlinks, platform-specific path rules, or untrusted CI artifacts deserve extra scrutiny in downstream consumers.
- Windows and macOS-specific filesystem semantics are part of the real attack surface here, not just Unix path normalization.

## Open Questions

- Is there a public maintainer writeup that explains the supported-branch security backport policy for the newer `7.x` series as clearly as the advisory pages explain individual fixes?
- Which high-volume downstream packages still pin vulnerable pre-`7.5.11` lines transitively, especially in older CLI or build-tool chains?
- Are there public independent audits of `tar`'s extraction model, or is the current record still mostly advisory-by-advisory hardening?

## Related Pages

- [[npm/index]]
- [[npm/path-to-regexp]]
- [[npm/express]]

---
*Last updated: 2026-05-02 | Sources: 6 (OSV package query, GitHub Security Advisories, CVE / NVD aliases surfaced through OSV, npm registry metadata, npm downloads API, public fix references / repo security-policy check)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
