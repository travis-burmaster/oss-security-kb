# moment (npm)

**Registry:** npm
**Weekly Downloads:** ~31,173,543 (2026-04-12 to 2026-04-18)
**Repository:** https://github.com/moment/moment
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/moment/moment/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-19 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / GitHub security advisories, public CVE records, upstream changelog, upstream issue / PR / commit references, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for Moment's published package security history, centered on two older ReDoS issues, the `moment.locale` path-traversal bug fixed in `2.29.2`, and the newer RFC2822 preprocessing ReDoS fixed in `2.29.4`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2016-4055 / GHSA-87vv-r9j6-g5qv | Moderate | Older Moment releases were vulnerable to regular-expression denial of service; OSV and GitHub Advisory Database track the public fix line at `2.11.2`. | 2.11.2 | https://github.com/advisories/GHSA-87vv-r9j6-g5qv |
| CVE-2017-18214 / GHSA-446m-mv8f-q348 | Moderate | A later ReDoS issue in date-string parsing was reported publicly in upstream issue `#4163`; OSV tracks the fix in `2.19.3`. | 2.19.3 | https://github.com/advisories/GHSA-446m-mv8f-q348 |
| CVE-2022-24785 / GHSA-8hfj-j24r-96c4 | High | `moment.locale` accepted crafted path input such as `dir/../../filename`, enabling path traversal in affected usage patterns. The upstream changelog for `2.29.2` explicitly says it addresses this security advisory. | 2.29.2 | https://github.com/advisories/GHSA-8hfj-j24r-96c4 |
| CVE-2022-31129 / GHSA-wc69-rhjr-hc9g | High | Inefficient regular expression complexity in RFC2822 preprocessing could trigger ReDoS. The upstream changelog for `2.29.4` explicitly calls out `Fix ReDoS in preprocessRFC2822 regex`. | 2.29.4 | https://github.com/advisories/GHSA-wc69-rhjr-hc9g |

## Security Posture Notes

- Moment has a **small but clear published package-advisory history** spanning two eras: older parser-complexity / ReDoS problems and newer 2022 fixes in locale loading and RFC2822 preprocessing.
- The public evidence lines up cleanly here. OSV, GitHub Advisory Database, CVE aliases, upstream issue / PR / commit links, and the maintained changelog all point at the same four package-level records.
- The `2.29.2` and `2.29.4` changelog entries are especially useful because they explicitly connect the release train to the published 2022 advisories instead of leaving the fix mapping ambiguous.
- Moment is no longer the shiny new date library, but it is still heavily deployed (~31.2M weekly downloads in this review window), so the remaining transitive footprint is large enough to matter operationally.
- The risk profile is mixed: some issues look like straightforward parser-complexity DoS concerns, while `CVE-2022-24785` is more usage-dependent because exploitability depends on applications exposing `moment.locale` with attacker-controlled input in a filesystem-relevant environment.
- Public evidence gathered in this pass supports **`2.29.4+` as the cleanest current floor** for the full published advisory set captured here.

## Recommendations for Developers

1. **Upgrade to `2.29.4` or newer**; earlier 2.x releases miss at least one of the 2022 security fixes.
2. **Audit any code paths that expose locale loading or dynamic locale selection** to attacker-controlled input.
3. **Treat date parsing as attacker-adjacent input handling** in APIs, importers, and log-processing paths where very large or malformed strings may arrive.
4. **Check transitive dependencies and legacy front-end bundles** because Moment often persists long after teams think they have standardized on newer date libraries.

## Dependencies of Note

- Often embedded deeply in older frontend bundles, dashboards, admin tools, SDKs, and server-side date formatting / parsing helpers.
- Security-sensitive use cases include untrusted date parsing and any environment that still permits dynamic locale loading from attacker-influenced input.

## Open Questions

- Are there good public downstream writeups that explain realistic exploit preconditions for `CVE-2022-24785` beyond the advisory summary and fix trail?
- Which still-maintained high-volume packages continue to pin Moment below `2.29.4` transitively?
- Should a future KB pass cross-link Moment with other long-lived parsing libraries whose main risk is legacy footprint rather than active feature churn?

## Related Pages

- [[npm/semver]]
- [[npm/qs]]
- [[npm/minimist]]
- [[npm/index]]

---
*Last updated: 2026-04-19 | Sources: 9 (OSV.dev package query for npm/moment, OSV vulnerability records for the four GHSA IDs listed above, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream changelog, upstream issue / PR / commit references, npm registry metadata, npm downloads API)*