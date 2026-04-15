# minimist (npm)

**Registry:** npm
**Weekly Downloads:** ~118,243,616 (last week, fetched 2026-04-14)
**Repository:** https://github.com/minimistjs/minimist
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-refreshed

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-14 | OpenClaw recurring review | package advisory refresh | public-source curation (GitHub Advisory Database, OSV.dev, public CVE records, npm registry metadata, upstream PR history) | Refreshed published advisory coverage, current package metadata, and the public maintainer follow-up trail around the incomplete-fix lineage. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-7598 / GHSA-vh95-rmgr-6w4m | Medium | Prototype pollution via unsanitized argument parsing; public GHSA text includes `--__proto__.y=Polluted` as a representative payload and notes exploitability when attackers control argv-like input passed into `minimist`. | 1.2.3 / 0.2.1 | https://github.com/advisories/GHSA-vh95-rmgr-6w4m |
| CVE-2021-44906 / GHSA-xvch-5gv4-984h | Critical | Incomplete fix for the earlier prototype pollution issue; public advisory coverage says `constructor.prototype` payloads in `setKey()` still remained reachable before 1.2.6 / 0.2.4. | 1.2.6 / 0.2.4 | https://github.com/advisories/GHSA-xvch-5gv4-984h |

## Security Posture Notes

- Tiny package, huge blast radius because it sits in CLI parsing paths throughout the npm ecosystem.
- Public advisory history still consists of **two published prototype-pollution advisories**, but the record is unusually instructive because it includes a clear incomplete-fix chain: CVE-2020-7598 covered the earlier `__proto__`-style pollution path, and CVE-2021-44906 documents that `constructor.prototype` paths in `setKey()` still remained reachable until 1.2.6 / 0.2.4.
- The GitHub Advisory Database now gives precise affected-version ranges for both trains: `< 0.2.1` and `>= 1.0.0, < 1.2.3` for the 2020 bug, then `< 0.2.4` and `>= 1.0.0, < 1.2.6` for the incomplete-fix follow-up.
- The public maintainer trail is worth preserving for readers: PR `#24` ("Robustness: rework isConstructorOrProto") was merged in February 2023 specifically to realign the legacy backport logic with the main branch after questions about the earlier 0.2.x fix path.
- Current npm metadata shows `minimist` remains extremely widely consumed (`~118,243,616` downloads in the last week of this review pass; latest release `1.2.8`), so even old parser bugs still matter for transitive dependency hygiene.
- No additional published GHSA advisories were identified for `minimist` in this review pass beyond the two prototype-pollution records above.

## Dependencies of Note

- Often appears as a transitive dependency in CLIs and build tools.
- Especially important to track transitively because downstream consumers may not realize they are inheriting vulnerable parser behavior from tiny utility dependencies.

## Open Questions

- Which currently popular packages still pin vulnerable minimist versions transitively, especially on the older `0.2.x` branch?
- Has anyone published a modern full-source audit after the `1.2.6` / `0.2.4` follow-up fixes landed?
- Are there parser edge cases beyond the published `__proto__` and `constructor.prototype` CVE lineage worth cataloging?
- Which downstream exploit chains turn this parser flaw into practical command execution, config corruption, or environment tampering?

## Related Pages

- [[npm/index]]
- [[npm/lodash]]
- [[npm/semver]]

---
*Last updated: 2026-04-14 | Sources: 8 (GitHub Advisory Database / GHSA, OSV.dev, public CVE records, npm registry metadata, npm downloads API, and public maintainer PR history including minimistjs/minimist#24)*
