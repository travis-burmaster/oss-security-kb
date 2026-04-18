# morgan (npm)

**Registry:** npm
**Weekly Downloads:** ~9,992,230 (last week, fetched 2026-04-18)
**Repository:** https://github.com/expressjs/morgan
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-18 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, Node.js Security WG advisory record, HackerOne report metadata, upstream release history / changelog, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for morgan's published package security history, centered on the 2019 format-compilation code-injection issue fixed in `1.9.1`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-5413 / GHSA-gwg9-rgvj-4h5j | High | Code injection in format compilation before `1.9.1`; public advisory text says exposure exists when user input is allowed into the filter / format path or when combined with a separate prototype-pollution primitive. | 1.9.1 | https://github.com/advisories/GHSA-gwg9-rgvj-4h5j |

## Security Posture Notes

- `morgan` has a **small published package-advisory footprint** in this review pass: one clearly documented 2019 code-injection issue, rather than a long chain of repeated parser or protocol bugs.
- The public advisory trail is still strong and worth preserving because it comes from multiple independent records that agree on the fix window: GitHub Advisory Database, the CVE / NVD entry, npm advisory `736`, the Node.js Security WG record, and the linked HackerOne disclosure metadata.
- Upstream release history for `1.9.1` notes "Fix using special characters in format", which aligns with the advisory narrative that the dangerous surface lives in format compilation rather than in ordinary request logging by itself.
- Real-world exploitability is **context-dependent**. The advisory language matters here: most applications are only exposed if untrusted input can influence morgan's format string / filter behavior directly, or if another bug such as prototype pollution can steer that path indirectly.
- Current package metadata shows the package remains widely used (`~9,992,230` downloads in the last week of this review pass; latest release `1.10.1`), so older long-lived Express stacks pinned below `1.9.1` still matter operationally even though the advisory itself is not new.
- No additional package-scoped OSV advisories were identified for `morgan` in this review pass beyond `CVE-2019-5413`.

## Dependencies of Note

- Commonly used directly in Express applications and starter templates rather than as a deeply hidden transitive dependency.
- Risk increases when applications construct log formats dynamically from tenant, request, or config input.

## Open Questions

- Are there good public writeups showing realistic exploit chains for the advisory beyond the high-level HackerOne / GHSA descriptions?
- Which maintained Express starter kits or internal templates still pin pre-`1.9.1` morgan releases?
- Should the KB eventually cross-link this page more explicitly with packages where prototype-pollution bugs could help reach the vulnerable format-compilation path?

## Related Pages

- [[npm/express]]
- [[npm/debug]]
- [[npm/minimist]]
- [[npm/index]]

---
*Last updated: 2026-04-18 | Sources: 8 (OSV.dev, GitHub Advisory Database, public CVE / NVD records, Node.js Security WG advisory record, HackerOne report metadata, npm advisory metadata, upstream release history / changelog, npm registry metadata, npm downloads API)*
