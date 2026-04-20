# postcss (npm)

**Registry:** npm
**Weekly Downloads:** ~207,008,540 (2026-04-13 to 2026-04-19)
**Repository:** https://github.com/postcss/postcss
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/postcss/postcss/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-20 | OpenClaw recurring review | package advisory normalization | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream release references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for PostCSS's currently published package-scoped advisory history. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-23368 / GHSA-hwj9-h5mp-3pm3 | Moderate | Regular-expression denial of service during source-map parsing; public records map fixes to both the `7.x` and `8.x` lines. | 7.0.36 / 8.2.10 | https://github.com/advisories/GHSA-hwj9-h5mp-3pm3 |
| CVE-2021-23382 / GHSA-566m-qj78-rww5 | Moderate | Another source-map parsing ReDoS in `getAnnotationURL()` / `loadAnnotation()` in `lib/previous-map.js`; public advisory data treats this as a separate fix train from the earlier 2021 record even though both bugs sit near the same feature surface. | 7.0.36 / 8.2.13 | https://github.com/advisories/GHSA-566m-qj78-rww5 |
| CVE-2023-44270 / GHSA-7fh5-64p2-3v2j | Moderate | Carriage-return parsing discrepancy could let attacker-controlled CSS content move from a comment context into active CSS nodes in PostCSS output; GitHub's advisory specifically frames the risk around linters and other tools parsing external untrusted CSS. | 8.4.31 | https://github.com/advisories/GHSA-7fh5-64p2-3v2j |

## Security Posture Notes

- PostCSS has a **small but non-trivial published package advisory history**: two 2021 ReDoS records in source-map parsing and one 2023 parser-integrity issue around carriage-return handling.
- The two 2021 advisories are related but not identical. Public records keep them separate, and the `8.x` fix boundaries differ (`8.2.10` vs `8.2.13`), so downstream users should treat them as distinct fixes rather than duplicate metadata.
- The 2023 issue is not just another availability bug. Public advisory text says it affects tools that parse **external untrusted CSS**, because content inside comments may later appear as active CSS nodes in PostCSS output.
- Current npm metadata in this pass shows extremely high deployment volume (~207.0M downloads in the review week), so even moderate-severity parser bugs have broad downstream relevance.
- Upstream publishes a GitHub security-advisory surface, but this review did not separately confirm a repository `SECURITY.md`; the disclosure entry above intentionally links only to the public advisory listing.

## Recommendations for Developers

1. **Upgrade to `8.4.31` or newer** if you want coverage for the full currently published package advisory set reviewed in this pass.
2. If you are pinned to older major lines, note that **`7.0.36` covers the two 2021 ReDoS fixes but not the later 2023 carriage-return parsing issue** as normalized in public advisory records.
3. Treat PostCSS as a **parser trust-boundary component** when ingesting attacker-controlled or third-party CSS, especially in linters, build services, SaaS analyzers, and any workflow that feeds PostCSS output into later security-relevant logic.
4. Regression-test source-map parsing and odd comment / line-ending cases if you maintain wrappers around PostCSS or expose CSS processing to untrusted users.

## Dependencies of Note

- PostCSS commonly sits underneath other CSS tooling rather than at the application edge, which means vulnerable versions often arrive transitively through build chains rather than direct runtime dependencies.
- Source-map handling and tokenizer behavior are the main historically exposed surfaces in the public package records reviewed here.

## Open Questions

- Do widely used PostCSS-adjacent packages in the KB deserve companion pages so transitive exposure is easier to trace from this core parser package?
- Are there maintainer-authored release notes or changelog entries worth normalizing in a future pass for the `8.2.10`, `8.2.13`, and `8.4.31` fix points beyond the advisory references collected here?
- Should a future ecosystem pass map which high-download frontend frameworks still transitively pin pre-fix PostCSS ranges?

## Related Pages

- [[npm/js-yaml]]
- [[npm/qs]]
- [[npm/index]]

---
*Last updated: 2026-04-20 | Sources: 7 (OSV.dev package query for npm/postcss, OSV vulnerability records for GHSA-hwj9-h5mp-3pm3 / GHSA-566m-qj78-rww5 / GHSA-7fh5-64p2-3v2j, GitHub Advisory Database entries for the same GHSA IDs, public CVE records via advisory aliases, upstream release references linked from the advisory records, npm registry metadata, npm downloads API)*
