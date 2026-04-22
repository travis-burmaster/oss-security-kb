# loader-utils (npm)

**Registry:** npm
**Weekly Downloads:** ~55,048,614 (2026-04-14 to 2026-04-20)
**Repository:** https://github.com/webpack/loader-utils
**Security Contact:** webpack security policy via https://github.com/webpack/webpack/blob/main/SECURITY.md
**Disclosure Policy:** https://github.com/webpack/webpack/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-22 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public upstream issue / PR / commit references, npm registry metadata, npm downloads API, local Claude-compatible proxy used only as a drafting aid) | Added a new advisory-mapped page for `loader-utils` covering three currently published npm package advisories: two 2022 ReDoS records and one 2022 prototype-pollution record across the 1.x, 2.x, and 3.x lines. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-hhq3-ff78-jv3g / CVE-2022-37599 | High | Public GHSA / OSV records describe a regular-expression denial-of-service issue in `interpolateName.js`; crafted input could trigger excessive CPU consumption before the fixes landed across supported major lines. | 1.4.2, 2.0.4, 3.2.1 | https://github.com/advisories/GHSA-hhq3-ff78-jv3g |
| GHSA-3rfm-jhwj-7488 / CVE-2022-37603 | High | Public GHSA / OSV records describe a second ReDoS issue in `loader-utils`, specifically via the `url` variable handling path, with the same remediation points across the 1.x, 2.x, and 3.x lines. | 1.4.2, 2.0.4, 3.2.1 | https://github.com/advisories/GHSA-3rfm-jhwj-7488 |
| GHSA-76p3-8jx3-jpfq / CVE-2022-37601 | Critical | Public GHSA / OSV records describe prototype pollution in `parseQuery.js` via the `name` variable, affecting releases before `1.4.1` and `2.0.3`. | 1.4.1, 2.0.3 | https://github.com/advisories/GHSA-76p3-8jx3-jpfq |

## Security Posture Notes

- `loader-utils` carries a **compact but non-trivial public vulnerability history**: three currently published npm advisories, clustered in late 2022.
- The public upstream trail is unusually direct: issues `#211`, `#212`, and `#213` line up with the two ReDoS reports and the prototype-pollution report, while PR `#217` and multiple fix commits document remediation work in public.
- The ReDoS fixes were shipped across the active major lines, suggesting maintainers treated the package as shared infrastructure rather than only hardening the newest branch.
- npm registry metadata still shows a large transitive footprint (**~55.0M weekly downloads** in this review window), so even older utility-package flaws can have broad downstream impact.
- Unlike many small utility packages, the repository does publish a `SECURITY.md`, though it delegates reporting to the broader webpack security policy rather than a package-specific process.
- No additional package-scoped OSV records were surfaced for `loader-utils` in this pass beyond the three mapped advisories above.

## Recommendations for Developers

1. **Upgrade off vulnerable lines**: any use below `1.4.2`, below `2.0.4`, or below `3.2.1` leaves at least one published advisory unresolved.
2. **Check transitive dependencies and build tooling**, not just direct dependencies, because `loader-utils` commonly arrives through webpack-adjacent packages.
3. **Treat small parsing / interpolation helpers as real attack surface** when they process attacker-influenced filenames, query-like strings, or URL-shaped inputs.

## Dependencies of Note

- Commonly appears as a transitive helper in webpack-centered build pipelines and loader ecosystems rather than as an intentionally chosen application dependency.
- Utility packages with this install base can still matter operationally because vulnerable versions often linger in older frontend toolchains.

## Open Questions

- Which still-common webpack plugin or loader chains continue to pin `loader-utils` below the fixed versions?
- Did later upstream work add tests or guardrails specifically aimed at preventing future regex-complexity and prototype-pollution regressions?
- Should this page eventually cross-link to broader webpack ecosystem package pages to make transitive upgrade paths clearer?

## Related Pages

- [[npm/webpack-dev-server]]
- [[npm/qs]]
- [[npm/index]]

---
*Last updated: 2026-04-22 | Sources: 11 (OSV.dev package query, three OSV / GitHub Advisory Database vulnerability records for GHSA-hhq3-ff78-jv3g / GHSA-3rfm-jhwj-7488 / GHSA-76p3-8jx3-jpfq, public upstream issues webpack/loader-utils#211 #212 #213, public upstream PR webpack/loader-utils#217, public fix commits 17cbf8f / ac09944 / d2d752d, upstream SECURITY.md, npm registry / downloads metadata)*
