# multer (npm)

**Registry:** npm
**Weekly Downloads:** ~14,109,455 (2026-04-11 to 2026-04-17)
**Repository:** https://github.com/expressjs/multer
**Security Contact:** GitHub Security Advisories
**Disclosure Policy:** https://github.com/expressjs/multer/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-18 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream release notes / changelog, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for multer's published package security history, centered on the 2025-2026 multipart-upload denial-of-service fix train from `2.0.0` through `2.1.1`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2025-47935 / GHSA-44fp-w29j-9vj5 | High | Improper stream-error handling could leave internal `busboy` streams unclosed, causing memory / file-descriptor leakage and denial of service over repeated failures. | 2.0.0 | https://github.com/advisories/GHSA-44fp-w29j-9vj5 |
| CVE-2025-47944 / GHSA-4pg4-qvpc-4q3h | High | Maliciously crafted multipart requests could trigger denial of service on the maintained pre-`2.0.0` line. | 2.0.0 | https://github.com/advisories/GHSA-4pg4-qvpc-4q3h |
| CVE-2025-48997 / GHSA-g5hg-p3ph-g8qg | High | Unhandled exceptions in multipart processing could crash the process and cause denial of service. | 2.0.1 | https://github.com/advisories/GHSA-g5hg-p3ph-g8qg |
| CVE-2025-7338 / GHSA-fjgf-rc76-4x9p | High | Malformed requests could still trigger an unhandled-exception denial of service after the earlier fixes, requiring a follow-on patch. | 2.0.2 | https://github.com/advisories/GHSA-fjgf-rc76-4x9p |
| CVE-2026-2359 / GHSA-v52c-386h-88mc | High | Public advisory records describe a resource-exhaustion denial-of-service condition fixed in the `2.1.0` release. | 2.1.0 | https://github.com/advisories/GHSA-v52c-386h-88mc |
| CVE-2026-3304 / GHSA-xf7r-hgr6-v32p | High | Incomplete cleanup during upload error handling could leave the process exposed to denial of service until the `2.1.0` fix. | 2.1.0 | https://github.com/advisories/GHSA-xf7r-hgr6-v32p |
| CVE-2026-3520 / GHSA-5528-5vmv-3xc2 | High | Uncontrolled recursion in upload handling could be triggered for denial of service until the `2.1.1` release. | 2.1.1 | https://github.com/advisories/GHSA-5528-5vmv-3xc2 |

## Security Posture Notes

- `multer` now has a **dense recent public advisory trail** rather than a long legacy history: seven published high-severity denial-of-service issues landed across the 2025-2026 review window gathered here.
- The advisories cluster around **multipart parser boundary handling, stream lifecycle cleanup, malformed-request handling, and resource exhaustion**, which makes sense given the package's role as an upload middleware layer sitting directly on attacker-controlled request bodies.
- Public release evidence lines up unusually cleanly with the advisory trail. Upstream's `v2.0.0`, `v2.0.1`, `v2.0.2`, `v2.1.0`, and `v2.1.1` release notes all explicitly call out the corresponding CVE / GHSA fixes, which makes the fix windows easy to map without speculation.
- The 2025 fixes show a notable **follow-on pattern**: `2.0.0` fixed two denial-of-service issues, then `2.0.1` and `2.0.2` each shipped more exception-handling hardening for nearby malformed-request paths. That pattern matters operationally because "already upgraded to 2.0.0" was not the end of the security story.
- Current npm metadata collected in this pass shows the package remains widely deployed (~14.1M downloads in the last week of this review), so older Express stacks pinned below `2.1.1` still deserve attention even though the fixes are public and available.
- Public evidence in this pass supports a straightforward baseline recommendation: **treat `2.1.1+` as the minimum currently reviewed release line** if you want coverage for the full published advisory set gathered here.

## Recommendations for Developers

1. **Upgrade to `2.1.1` or newer** to cover the full currently published advisory set reviewed in this pass.
2. **Treat file-upload middleware as a trust-boundary component**, not just glue code; malformed multipart bodies and abort/error paths are repeatedly where the public issues landed.
3. **Exercise unhappy-path upload tests** (abort, parser errors, malformed boundaries, oversized bodies, repeated invalid parts) instead of testing only successful uploads.
4. **Apply upstream request-size and timeout limits** at the reverse proxy and application layer, because every published issue in this pass is denial-of-service oriented.
5. **Review long-lived 1.x / `1.4.4-lts.1` deployments carefully**, since several published advisories explicitly name that maintained pre-2.0 range as affected.

## Dependencies of Note

- `multer` delegates multipart parsing to `busboy`, so stream and parser-boundary behavior in that integration path is security-relevant.
- The package is commonly used directly in Express applications, admin backends, and media / document upload flows where unauthenticated or semi-trusted users can reach the multipart parser.

## Open Questions

- Are there good maintainer-authored or third-party writeups that explain exploit preconditions for the 2026 `2.1.0` and `2.1.1` fixes beyond the advisory and release-note trail gathered here?
- Should a future KB pass map which popular Express starter kits, CMS integrations, or internal upload wrappers still pin `multer` below `2.1.1`?
- Are there public regression tests or issue threads that make the 2025 malformed-request / unhandled-exception chain easier to summarize package-by-package for downstream users?

## Related Pages

- [[npm/express]]
- [[npm/body-parser]]
- [[npm/qs]]
- [[npm/cookie]]
- [[npm/index]]

---
*Last updated: 2026-04-18 | Sources: 8 (OSV.dev package query for npm/multer, OSV vulnerability records for the seven GHSA IDs listed above, GitHub Advisory Database entries for the same GHSA IDs, public CVE records via advisory aliases, upstream GitHub security advisories, upstream release notes / changelog for v2.0.0-v2.1.1, npm registry metadata, npm downloads API)*
