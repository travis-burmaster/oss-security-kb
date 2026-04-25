# basic-ftp (npm)

**Registry:** npm
**Weekly Downloads:** ~25,440,970 (2026-04-17 to 2026-04-23)
**Repository:** https://github.com/patrickjuchli/basic-ftp
**Security Contact:** GitHub Security Advisory (private reporting enabled)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-24 | OpenClaw recurring review | package advisory refresh | public-source curation (OSV.dev package query, GitHub Advisory Database / public GHSA page, npm registry metadata, npm downloads API, local Claude-compatible proxy used only as a drafting aid) | Refreshed the page after a new high-severity `Client.list()` unbounded-memory / DoS record (`GHSA-rp42-5vxx-qpwr`) surfaced with a `5.3.0` fix boundary. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| 2026-04-12 | [@travis-burmaster](https://github.com/travis-burmaster) | package advisory review | public-source curation (GitHub Advisory Database, OSV.dev, upstream changelog / release metadata, public CVE records) | 3 published package advisories mapped | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-5rq4-664w-9x2c / CVE-2026-27699 | Critical | Invalid file names in `downloadToDir` could create unsafe local paths; the published advisory history treats 5.2.0 as the security fix. | 5.2.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-5rq4-664w-9x2c) |
| GHSA-chqc-8p9q-pq6q / CVE-2026-39983 | High | Version 5.2.0 introduced an FTP command-injection bug via CRLF handling in path-bearing commands; upstream 5.2.1 release notes explicitly say control-character injection attempts using paths were rejected as the fix. | 5.2.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-chqc-8p9q-pq6q) |
| GHSA-6v7q-wjvx-w8wg | High | The 5.2.1 CRLF hardening was incomplete, allowing arbitrary FTP command execution via crafted credentials and `MKD` commands until 5.2.2 tightened control-character rejection again. | 5.2.2 | [GitHub Advisory Database](https://github.com/advisories/GHSA-6v7q-wjvx-w8wg) |
| GHSA-rp42-5vxx-qpwr | High | `Client.list()` buffered remote directory listings into an in-memory `StringWriter` without a size limit, so a malicious or compromised FTP server could send an extremely large or never-ending listing and drive unbounded memory consumption / denial of service until the `5.3.0` fix. | 5.3.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-rp42-5vxx-qpwr) |

## Security Posture Notes

- Maintenance status: actively maintained; upstream shipped 5.2.0, 5.2.1, and 5.2.2 in quick succession for the earlier path / command-handling fixes, and public OSV / GHSA data now adds a separate `5.3.0` denial-of-service fix.
- Known sensitive surfaces: FTP command construction, control-character handling in credentials and path-bearing commands, any API that maps remote server data into local filesystem operations, and **directory-listing flows that buffer server-controlled output into memory**.
- Disclosure maturity: published GitHub Security Advisories exist, but no standalone SECURITY.md / policy URL was identified in this review.
- Notes: the 5.2.x line shows a clear fix-regression-fix pattern — 5.2.0 fixed the path-traversal issue, 5.2.1 addressed CRLF injection via paths, and 5.2.2 hardened that CRLF protection again after the first fix proved incomplete.
- Notes: the newer `GHSA-rp42-5vxx-qpwr` record is a **different bug class** from the earlier injection flaws: it concerns unbounded buffering of server-controlled `LIST` responses in `Client.list()`, so even read-only directory enumeration can become an availability boundary when the FTP server is malicious or compromised.
- Notes: public release notes made the earlier 5.2.1 / 5.2.2 lineage easy to verify, while the 2026 DoS record is currently easiest to normalize through the published GHSA / OSV evidence and the `5.3.0` fix boundary it documents.
- Recommendation: users should prefer `>= 5.3.0` to clear the currently published path-traversal, command-injection, and directory-listing DoS issues gathered in this pass.

## Dependencies of Note

- None flagged yet from this package-advisory pass.

## Open Questions

- Has the project published a formal security policy outside GitHub's advisory flow?
- Are other FTP verbs or path-bearing APIs protected by the same control-character validation tightened in 5.2.1 and 5.2.2?
- Should future review cover FTPS certificate / PASV trust boundaries in more depth?

## Related Pages

- [[npm/index]]

---
*Last updated: 2026-04-24 | Sources: 9 (GitHub Advisory Database / public GHSA pages, OSV.dev package query and vulnerability records, public CVE records for CVE-2026-27699 and CVE-2026-39983, upstream GitHub release notes for v5.2.1 and v5.2.2, npm registry metadata, npm downloads API)*
