# tough-cookie (npm)

**Registry:** npm
**Weekly Downloads:** ~92,055,831 (2026-04-11 to 2026-04-17)
**Repository:** https://github.com/salesforce/tough-cookie
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-18 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream issue / commit / release references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for tough-cookie's published package security history, centered on two older cookie-parsing ReDoS fixes and the newer prototype-pollution fix in `4.1.3`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-26136 / GHSA-72xf-g2v4-qvf3 | Moderate | Public advisory records describe a prototype-pollution issue in the cookie memory-store path; the upstream fix changed object creation in `memstore.js` to `Object.create(null)` and the `v4.1.3` release was explicitly tagged as a security fix. | 4.1.3 | https://github.com/advisories/GHSA-72xf-g2v4-qvf3 |
| CVE-2017-15010 / GHSA-g7q5-pjjr-gqvp | Moderate | Crafted cookie input could trigger regular-expression denial of service until the parser hardening shipped in `2.3.3`; the linked fix commit says it constrains spaces before `=` to sidestep the ReDoS from issue `#92`. | 2.3.3 | https://github.com/advisories/GHSA-g7q5-pjjr-gqvp |
| CVE-2016-1000232 / GHSA-qhv9-728r-6jqg | Moderate | Long strings of semicolons could trigger excessive parsing work and denial of service before `2.3.0`; upstream fix commits explicitly describe reducing parse time for that input shape. | 2.3.0 | https://github.com/advisories/GHSA-qhv9-728r-6jqg |

## Security Posture Notes

- `tough-cookie` has a **small but real published advisory history**: two parser-complexity issues on older lines, followed years later by a separate prototype-pollution fix in the memory-store path.
- The advisory trail lines up cleanly with upstream public references. OSV, GitHub Advisory Database, CVE aliases, issue links, fix commits, and the `v4.1.3` release note all point at the same three package-level records.
- Two of the three published issues are **denial-of-service-oriented parser bugs**, which is consistent with the package's role as a cookie parsing and storage layer sitting on untrusted header content.
- The 2023 fix matters beyond historical curiosity because the package remains heavily deployed (~92.1M weekly downloads in this review window), often transitively through older HTTP-client stacks and scraping / automation tooling.
- Public evidence gathered here supports a practical floor of **`4.1.3+` for the full currently published advisory set**. Older `2.x` deployments can partially reduce risk at `2.3.3`, but they do not cover the later prototype-pollution fix.

## Recommendations for Developers

1. **Upgrade to `4.1.3` or newer**; the latest release at review time is `6.0.1`.
2. **Check transitive dependency trees** because `tough-cookie` often arrives indirectly via HTTP-client libraries rather than a direct top-level dependency.
3. **Treat cookie parsing as attacker-adjacent input handling**, especially in crawlers, proxies, API clients, or test rigs that accept or replay cookie material from untrusted sources.
4. **Do not assume a partial `2.3.x` upgrade is enough** if you still need coverage for the later prototype-pollution issue.

## Dependencies of Note

- Commonly used as a cookie-jar foundation under higher-level HTTP clients and scraping / automation tooling.
- Security-relevant behavior lives in both cookie parsing and cookie storage representations, so downstream wrappers that expose or serialize jar state deserve attention too.

## Open Questions

- Are there good public maintainer or downstream writeups that explain realistic exploitation boundaries for the `4.1.3` prototype-pollution fix in more detail than the advisory and commit trail gathered here?
- Which still-maintained HTTP-client packages most often pin `tough-cookie` below `4.1.3` in practice?
- Should a future KB pass cross-map `tough-cookie` advisories against popular Node.js scraping stacks and session-management helpers that vendor or wrap cookie jars?

## Related Pages

- [[npm/axios]]
- [[npm/follow-redirects]]
- [[npm/node-fetch]]
- [[npm/cookie]]
- [[npm/index]]

---
*Last updated: 2026-04-18 | Sources: 8 (OSV.dev package query for npm/tough-cookie, OSV vulnerability records for the three GHSA IDs listed above, GitHub Advisory Database entries for the same GHSA IDs, public CVE / NVD records, upstream issue references, upstream fix commits, the upstream `v4.1.3` release note, npm registry metadata, npm downloads API)*