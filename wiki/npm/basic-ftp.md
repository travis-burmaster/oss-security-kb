# basic-ftp (npm)

**Registry:** npm
**Weekly Downloads:** ~24,000,000 (as of 2026-04-12)
**Repository:** https://github.com/patrickjuchli/basic-ftp
**Security Contact:** GitHub Security Advisory (private reporting enabled)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-12 | [@travis-burmaster](https://github.com/travis-burmaster) | package advisory review | public-source curation (GitHub Advisory Database, OSV, upstream changelog, release metadata) | 2 published package advisories mapped | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-6v7q-wjvx-w8wg | High | Incomplete CRLF injection protection allowed arbitrary FTP command execution via crafted credentials and `MKD` commands. | 5.2.2 | [GitHub Advisory Database](https://github.com/advisories/GHSA-6v7q-wjvx-w8wg) |
| GHSA-5rq4-664w-9x2c / CVE-2026-27699 | High | Invalid file names in `downloadToDir` could create unsafe local paths; upstream changelog treats 5.2.0 as the security fix. | 5.2.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-5rq4-664w-9x2c) |

## Security Posture Notes

- Maintenance status: actively maintained; upstream shipped 5.2.0, 5.2.1, and 5.2.2 in quick succession with explicit security fixes noted in the changelog.
- Known sensitive surfaces: FTP command construction, path handling during uploads/downloads, and any API that maps remote server data into local filesystem operations.
- Disclosure maturity: published GitHub Security Advisories exist, but no standalone SECURITY.md / policy URL was identified in this review.
- Notes: the 5.2.2 changelog explicitly says it "Improve[s] control character rejection" and links to GHSA-6v7q-wjvx-w8wg, which makes the fix lineage unusually clear.
- Notes: no public CVE ID appeared in the gathered evidence for GHSA-6v7q-wjvx-w8wg at review time; OSV and GitHub both listed the GHSA identifier only.

## Dependencies of Note

- None flagged yet from this package-advisory pass.

## Open Questions

- Has the project published a formal security policy outside GitHub's advisory flow?
- Are other command-bearing FTP verbs protected by the same control-character validation added in 5.2.2?
- Should future review cover FTPS certificate / PASV trust boundaries in more depth?

## Related Pages

- [[npm/index]]

---
*Last updated: 2026-04-12 | Sources: 6 (GitHub Advisory Database, OSV.dev, upstream changelog, GitHub releases, npm registry, CVE reference for CVE-2026-27699)*
