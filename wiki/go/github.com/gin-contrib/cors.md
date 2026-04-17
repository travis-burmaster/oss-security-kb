# github.com/gin-contrib/cors (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-04-17)
**Repository:** https://github.com/gin-contrib/cors
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-17 | OpenClaw recurring review | package advisory history | public-source curation (OSV.dev, GitHub Advisory Database / public GHSA page, Go vuln record, upstream README, upstream PR / commit / release metadata) | Added a new advisory-mapped page for the standalone Gin CORS middleware module after confirming that the wildcard-origin parsing flaw tracked as `CVE-2019-25211` belongs cleanly to `github.com/gin-contrib/cors`, not just to core Gin. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-25211 / GHSA-869c-j7wc-8jqv / GO-2024-2955 | critical | The middleware's wildcard-origin parsing accepted unintended suffix matches before `1.6.0`, so patterns such as `https://example.com/*` could match origins like `https://example.community/*`, and `http://localhost/*` could match `http://localhost.example.com/*`. This matters when applications relied on `AllowWildcard` and expected stricter origin boundaries. | 1.6.0 | https://github.com/advisories/GHSA-869c-j7wc-8jqv |

*Full CVE history: https://osv.dev/list?ecosystem=Go&q=github.com/gin-contrib/cors*

## Security Posture Notes

- Public advisory history for this module is currently small but non-empty: the OSV package query for `github.com/gin-contrib/cors` returned the wildcard-origin flaw as both a GitHub-reviewed advisory and a Go vuln record, which is enough to justify a dedicated package page without overstating broader issue volume.
- The published flaw is configuration-dependent rather than universal. It becomes relevant when applications enabled wildcard origin matching and relied on trailing-wildcard patterns for trust decisions; conservative or explicit allowlists reduce the exposure.
- The upstream README reinforces that origin handling is security-sensitive: it documents `AllowOrigins`, `AllowWildcard`, and custom validation hooks, and it warns that permissive origin settings can have credential and browser-behavior consequences.
- Upstream fix evidence is clean and traceable: the public advisory references the fix PRs, the specific remediation commit `27b723a473efd80d5a498fa9f5933c80204c850d`, the `v1.5.0...v1.6.0` compare view, and the `v1.6.0` release page.
- Consumers should treat this package as an independent middleware trust boundary even when the broader application framework is Gin. Shared organization ownership does not mean shared versioning or identical advisory scope.

## Dependencies of Note

- This module is often pulled into services that already depend on `github.com/gin-gonic/gin`, so framework review alone can miss middleware-specific security history.
- Reverse proxies, browser credential use, and application-specific origin policies materially shape real-world impact.
- Projects that replace built-in matching with `AllowOriginFunc` or `AllowOriginWithContextFunc` bypass the vulnerable wildcard parser but assume responsibility for their own matching correctness.

## Open Questions

- Are there good public maintainer-authored hardening notes or issue discussions beyond PR `#106` that explain recommended safe origin-pattern design in more operational detail?
- Should future Go pages separate core-framework, first-party middleware, and third-party middleware more explicitly so shared-ecosystem advisories are easier to normalize?
- Is there any public evidence of downstream packages still pinning pre-`1.6.0` `gin-contrib/cors` versions in commonly reused starter stacks or templates?

## Related Pages

- [[go/github.com/gin-gonic/gin]]
- [[go/index]]

---
*Last updated: 2026-04-17 | Sources: 8 (OSV package query, GitHub Advisory Database / public GHSA page, Go vuln record, upstream README, two upstream PR references, upstream fix commit, upstream release / compare metadata)*
