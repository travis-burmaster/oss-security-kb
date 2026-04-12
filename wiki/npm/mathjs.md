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

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-jvff-x2qm-6286 | High | Improperly controlled modification of dynamically determined object attributes (prototype / object-attribute pollution class) in `mathjs`; fixed in 15.2.0. | 15.2.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-jvff-x2qm-6286) |

## Security Posture Notes

- Maintenance status: actively maintained; 15.2.0 release notes explicitly mention two security vulnerabilities involving arbitrary JavaScript execution via the expression parser.
- Known sensitive surfaces: expression parsing, dynamic object-property access, configuration helpers, and any feature that evaluates user-controlled expressions.
- Disclosure maturity: GitHub advisory workflow is in place, but no standalone disclosure-policy URL was identified in this pass.
- Notes: the advisory tracked here is specifically the published object-attribute modification issue fixed in 15.2.0; the same release notes also mention another security fix, so follow-up review should separate those issues cleanly.
- Notes: no public CVE ID appeared in the gathered evidence for GHSA-jvff-x2qm-6286 at review time; GitHub Advisory Database and OSV both used the GHSA only.

## Dependencies of Note

- None flagged yet from this package-advisory pass.

## Open Questions

- What is the exact exploit boundary for the published attribute-modification issue: parser-only, config-only, or broader object-assignment utilities?
- Which of the two security fixes called out in the 15.2.0 history corresponds to this GHSA, and does the second have its own published advisory record yet?
- Should a deeper future page revision split expression-parser risks from general object-pollution hardening work noted elsewhere in `HISTORY.md`?

## Related Pages

- [[npm/index]]

---
*Last updated: 2026-04-12 | Sources: 6 (GitHub Advisory Database, OSV.dev, upstream HISTORY.md, fix PR, fix commit, npm registry / release metadata)*
