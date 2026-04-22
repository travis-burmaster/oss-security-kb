# github.com/gorilla/websocket (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-04-22)
**Repository:** https://github.com/gorilla/websocket
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-22 | OpenClaw recurring review | package advisory normalization | public-source curation (OSV package query, Go vuln record, GitHub Advisory Database, public CVE record, upstream fix PR / commit, upstream release metadata, repository metadata, local proxy draft assist) | Added a new advisory-mapped page after confirming that the two OSV package results for `github.com/gorilla/websocket` collapse to one underlying public issue: the integer-overflow / read-limit bypass denial-of-service flaw fixed in `v1.4.1`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-27813 / GHSA-3xh2-74w9-5vxm / GHSA-jf24-p9p9-4rjh / GO-2020-0019 | High | Integer overflow in websocket frame-length / remaining-byte handling could let malicious peers bypass read-limit expectations and drive excessive memory use or denial of service. Public OSV results expose this as both a GitHub-reviewed advisory record and a Go vuln record, but they alias the same underlying issue. | 1.4.1 | https://github.com/advisories/GHSA-3xh2-74w9-5vxm |

*Full CVE history: https://osv.dev/list?ecosystem=Go&q=github.com/gorilla/websocket*

## Security Posture Notes

- The current public package-level advisory history is small but non-empty: the OSV package query returns two records, but both normalize to the same underlying vulnerability (`CVE-2020-27813`) rather than to two distinct flaws.
- The published bug sits on a core trust boundary for this package: parsing attacker-controlled websocket frames while enforcing read limits and message-size accounting.
- Public maintainer advisory text is unusually clear here: it explicitly says malicious frames could trigger integer overflow, bypass read limits, and potentially drive excessive memory use or out-of-memory conditions, and it points users to `v1.4.1` as the fix floor.
- The public fix chain is easy to trace through upstream evidence: PR `#537` ("Read Limit Fix") merged on 2019-08-25, release `v1.4.1` was published the same day, and the linked fix commit is `5b740c29263eb386f33f265561c8262522f19d37`.
- Repository metadata in this pass showed the project was still publicly maintained (`pushed_at` 2025-03-19) with newer releases available through `v1.5.3`, so this is not a dead-package warning story.
- No root `SECURITY.md` or `.github/SECURITY.md` was confirmed in the gathered public repository contents, so the package currently lacks a clearly published disclosure path in the standard GitHub locations reviewed here.

## Dependencies of Note

- Because `gorilla/websocket` is a foundational Go websocket implementation, many downstream services inherit its frame-parsing and message-size enforcement behavior transitively through wrappers or direct use.
- Reverse proxies, HTTP upgrade handling, and application-level read-limit settings shape practical exposure even though the published flaw is in the library's own frame-handling logic.
- Adjacent Gorilla packages such as `gorilla/mux` should be tracked separately; shared organization ownership does not imply shared advisory history.

## Open Questions

- Are there public maintainer notes or issue threads explaining why the fix landed in August 2019 while the GitHub advisory publication happened in May 2021, beyond the visible PR / release chronology?
- Does the project publish a disclosure workflow anywhere outside the standard root and `.github/` `SECURITY.md` locations checked in this pass?
- Are there public fuzzing, differential-testing, or parser-hardening writeups for `gorilla/websocket`, given that websocket frame parsing is such a security-sensitive surface?

## Related Pages

- [[go/github.com/gorilla/mux]]
- [[go/github.com/gin-gonic/gin]]
- [[go/index]]

---
*Last updated: 2026-04-22 | Sources: 9 (OSV package query for Go/github.com/gorilla/websocket, normalized OSV vulnerability records for GHSA-3xh2-74w9-5vxm and GO-2020-0019, GitHub Advisory Database entry / public GHSA advisory, public NVD CVE record, upstream fix PR #537, upstream fix commit 5b740c2, upstream release metadata for v1.4.1 and later releases, public repository metadata, local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid)*
