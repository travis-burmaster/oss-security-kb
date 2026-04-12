# next-intl (npm)

**Registry:** npm
**Weekly Downloads:** ~2,400,000 (as of 2026-04-12)
**Repository:** https://github.com/amannn/next-intl
**Security Contact:** GitHub Security Advisory (private reporting enabled)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-12 | [@travis-burmaster](https://github.com/travis-burmaster) | package advisory review | public-source curation (GitHub Advisory Database, OSV, upstream changelog, fix PR / commit, release metadata) | 1 published package advisory mapped | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-8f24-v5vv-gm5j | Moderate | Open redirect vulnerability in middleware pathname handling. Public advisory and upstream 4.9.1 changelog both point to improved pathname validation as the fix. | 4.9.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-8f24-v5vv-gm5j) |

## Security Posture Notes

- Maintenance status: actively maintained; 4.9.1 shipped the same day as the advisory and fix PR.
- Known sensitive surfaces: locale / pathname routing middleware, redirect handling, and any application code that trusts user-controlled path segments during localization flows.
- Disclosure maturity: package uses GitHub's security advisory workflow, but no separate disclosure-policy URL was identified in the review bundle.
- Notes: upstream changelog for 4.9.1 says "Improve middleware pathname validation" and references issue / PR #2304, matching the advisory's remediation path.
- Notes: no public CVE ID appeared in the gathered evidence for this issue at review time; GitHub Advisory Database and OSV both carried the GHSA only.

## Dependencies of Note

- None flagged yet from this package-advisory pass.

## Open Questions

- Does the project maintain a standalone SECURITY.md or out-of-band disclosure route not surfaced in the public evidence bundle?
- Which `next-intl` middleware integration patterns are most likely to convert an open redirect bug into credential-phishing or OAuth callback abuse downstream?
- Are there older pathname / locale-routing edge cases worth reviewing beyond the single published advisory?

## Related Pages

- [[npm/index]]

---
*Last updated: 2026-04-12 | Sources: 6 (GitHub Advisory Database, OSV.dev, upstream changelog, fix PR, fix commit, GitHub release metadata / npm registry)*
