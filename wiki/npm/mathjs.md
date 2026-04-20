# mathjs (npm)

**Registry:** npm
**Weekly Downloads:** ~2,500,000 (as of 2026-04-12)
**Repository:** https://github.com/josdejong/mathjs
**Security Contact:** GitHub Security Advisory (private reporting enabled)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-12 | [@travis-burmaster](https://github.com/travis-burmaster) | package advisory review | public-source curation (GitHub Advisory Database, OSV, upstream history, fix PR / commit, npm metadata) | 1 published package advisory mapped | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| 2026-04-20 | OpenClaw recurring review | published advisory reconciliation | public-source curation (OSV.dev, public CVE records, upstream HISTORY.md, GitHub Security Advisories, fix PR / commit references) | Reconciled the page against the full OSV package record and added four previously missing public advisories from the `3.17.0`, `7.5.1`, and `15.2.0` security fixes. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-pv8x-p9hq-j328 / CVE-2017-1001003 | Critical | Arbitrary code execution via crafted typed-function names in older releases; upstream `3.17.0` changelog explicitly calls out this security fix. | 3.17.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-pv8x-p9hq-j328) |
| GHSA-vx5c-87qx-cv6c / CVE-2017-1001002 | High | Forbidden properties such as `constructor` could be replaced using Unicode characters during object creation, with upstream warning this could allow arbitrary code execution. | 3.17.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-vx5c-87qx-cv6c) |
| GHSA-x2fc-mxcx-w4mf / CVE-2020-7743 | High | Prototype pollution in `math.config`; upstream `7.5.1` release notes explicitly describe it as an object-pollution vulnerability fix. | 7.5.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-x2fc-mxcx-w4mf) |
| GHSA-jvff-x2qm-6286 | High | Improperly controlled modification of dynamically determined object attributes (prototype / object-attribute pollution class) in `mathjs`; one of two public 15.2.0 expression-parser security fixes. | 15.2.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-jvff-x2qm-6286) |
| GHSA-29qv-4j9f-fjw5 / CVE-2026-40897 | High | Unsafe object property setter in the expression parser; public advisory and upstream `15.2.0` history align on a second arbitrary-JavaScript-execution-class fix in the same release. | 15.2.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-29qv-4j9f-fjw5) |

## Security Posture Notes

- Maintenance status: actively maintained; public history now shows a longer vulnerability trail than this page originally captured, spanning 2017 arbitrary-code-execution fixes, a 2020 `math.config` prototype-pollution fix, and two separate 15.2.0 expression-parser advisories.
- Known sensitive surfaces: expression parsing, dynamic object-property access, configuration helpers, and any feature that evaluates user-controlled expressions.
- The 2017 and 2026 records both center on **code-generation / object-property boundaries** rather than classic parser DoS, which makes `mathjs` especially sensitive when applications evaluate user-controlled expressions or expose customization hooks.
- Disclosure maturity: GitHub advisory workflow is in place, but no standalone disclosure-policy URL was identified in this pass.
- Public evidence now cleanly supports treating **15.2.0** as the minimum version that covers the currently published 2026 expression-parser advisory pair, while **7.5.1** and **3.17.0** remain important historical security landmarks for older pinned deployments.
- No public evidence gathered in this pass justified claims beyond the published OSV / GHSA / CVE set listed here.

## Dependencies of Note

- None flagged yet from this package-advisory pass.

## Open Questions

- What is the exact exploit boundary for the two `15.2.0` expression-parser advisories in real applications: parser-only, config-only, or broader object-assignment utilities?
- Are there maintainer-authored public notes that map the two `15.2.0` GHSAs more explicitly to individual code paths beyond the shared PR / release note trail?
- Should a deeper future page revision split expression-parser risks from general object-pollution hardening work noted elsewhere in `HISTORY.md`?

## Related Pages

- [[npm/index]]

---
*Last updated: 2026-04-20 | Sources: 8 (GitHub Advisory Database, OSV.dev package query and vulnerability records, public CVE / NVD records, upstream HISTORY.md, upstream fix PR / commit references, npm registry / release metadata)*
