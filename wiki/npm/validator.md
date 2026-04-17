# validator (npm)

**Registry:** npm
**Weekly Downloads:** ~42,000,000 (last week, fetched 2026-04-17)
**Repository:** https://github.com/validatorjs/validator.js
**Security Contact:** GitHub Security Advisory
**Disclosure Policy:** https://github.com/validatorjs/validator.js/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-17 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream changelog / README, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for validator's published security history, including the legacy XSS-filter lineage plus newer `isURL`, `isLength`, and regex-complexity fixes. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2013-7451 / GHSA-qpjp-7rp2-9c3f | Moderate | Legacy `xss()` filter bypass via nested tags. | 1.1.0 | https://osv.dev/vulnerability/GHSA-qpjp-7rp2-9c3f |
| CVE-2013-7452 / GHSA-rh6c-q938-3r9q | Moderate | Legacy `xss()` filter bypass via crafted `javascript:` URIs. | 1.1.0 | https://osv.dev/vulnerability/GHSA-rh6c-q938-3r9q |
| CVE-2013-7453 / GHSA-552w-rqg8-gxxm | Moderate | Legacy `xss()` filter bypass via UI-redressing-style payloads. | 1.1.0 | https://osv.dev/vulnerability/GHSA-552w-rqg8-gxxm |
| CVE-2013-7454 / GHSA-q4qq-fm7q-cwp5 | Moderate | Multiple legacy blacklist-filter bypasses in `xss()`, including nested-tag and incomplete `javascript:` filtering cases. | 1.1.0 | https://osv.dev/vulnerability/GHSA-q4qq-fm7q-cwp5 |
| CVE-2014-9772 / GHSA-79mx-88w7-8f7q | Moderate | Legacy `xss()` filter bypass via hex-encoded characters inside attributes / URLs. | 2.0.0 | https://osv.dev/vulnerability/GHSA-79mx-88w7-8f7q |
| CVE-2014-8882 / GHSA-f5w6-r7rg-mcgq | High | Regular-expression denial of service in `isURL()`. | 3.22.1 | https://osv.dev/vulnerability/GHSA-f5w6-r7rg-mcgq |
| CVE-2021-3765 / GHSA-qgmg-gppg-76g5 and GHSA-xx4c-jj58-r7x6 | Moderate | Inefficient regular-expression complexity / ReDoS issues remediated in the 13.7.0 hardening release; public records cover both broad package impact and a narrower `trim` / `rtrim` sanitizer variant. | 13.7.0 | https://osv.dev/vulnerability/GHSA-qgmg-gppg-76g5 |
| CVE-2025-56200 / GHSA-9965-vmph-33xx | Moderate | `isURL()` protocol parsing treated `://` as a delimiter while browsers key on `:`, enabling URL-validation bypasses with downstream XSS or open-redirect impact in applications that trusted the validator result. | 13.15.20 | https://osv.dev/vulnerability/GHSA-9965-vmph-33xx |
| CVE-2025-12758 / GHSA-vghf-hv5q-vc2g | High | `isLength()` mishandled Unicode variation selectors (`U+FE0F`, `U+FE0E`), letting overlong inputs pass validation and potentially causing downstream truncation, buffer pressure, or policy bypass. | 13.15.22 | https://osv.dev/vulnerability/GHSA-vghf-hv5q-vc2g |

## Security Posture Notes

- `validator` has a **long public security history**, but it falls into two fairly different eras: an older blacklist-based `xss()` filtering era with repeated bypasses, and a newer validator/sanitizer era where the published issues are more about parser / regex complexity and boundary mismatches in helper functions like `isURL()` and `isLength()`.
- The upstream README now explicitly says **XSS sanitization was removed from the library**, which is an important interpretation aid for the early 2013-2014 CVEs: those records are real and historically relevant, but they track a feature that modern users should not treat as a supported HTML / script sanitization defense.
- Public changelog evidence shows active maintenance on the recent security fixes: `13.15.20` explicitly says `isURL: improve protocol detection. Resolves CVE-2025-56200`, and `13.15.22` ships the `isLength` Unicode-variation-selector fix that lines up with `CVE-2025-12758`.
- The 2021 `13.7.0` hardening release is a meaningful watershed because public advisories tie it to regex-complexity fixes affecting string-trimming behavior and broader inefficient-regex concerns.
- Operationally, the main risk with `validator` is **over-trusting convenience validators as security boundaries**. Functions like `isURL()` and `isLength()` are useful guards, but published advisories show they can still disagree with browser, Unicode, or runtime behavior in edge cases.
- Current public evidence from this pass points to `13.15.22+` as the minimum release line that covers the known published advisory set reviewed here.

## Dependencies of Note

- Frequently used directly in Express / Koa / NestJS validation pipelines and form-processing code rather than as a deeply hidden transitive dependency.
- Risk increases when applications use `isURL()` results to authorize redirects, embeds, or outbound requests, or use `isLength()` as a hard boundary before storage or downstream parsing.

## Open Questions

- Should future KB passes split the legacy `xss()` advisory cluster into a short appendix, since those records all relate to a removed feature rather than the current core validation posture?
- Are there good maintainer or researcher writeups explaining practical exploit preconditions for `CVE-2025-56200` beyond the advisory / issue / PR trail?
- Which high-download downstream packages still pin vulnerable pre-`13.15.22` validator ranges in long-lived enterprise support branches?

## Related Pages

- [[npm/express]]
- [[npm/qs]]
- [[npm/minimist]]
- [[npm/index]]

---
*Last updated: 2026-04-17 | Sources: 7 (OSV.dev, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream changelog, upstream README, npm registry metadata, npm downloads API)*
