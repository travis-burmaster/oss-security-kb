# github.com/gin-gonic/gin (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-04-12)
**Repository:** https://github.com/gin-gonic/gin
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-12 | OpenClaw recurring review | package advisory history | manual | 4 clean public module vulnerabilities curated from OSV, GHSA, CVE, Go vuln entries, and upstream release / PR history; 1 additional OSV/GHSA package mapping was left out of the core table because the public references point primarily to `gin-contrib/cors` rather than core Gin itself | https://osv.dev/list?ecosystem=Go&q=github.com/gin-gonic/gin |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-36567 / GHSA-6vm3-jj99-7229 / GO-2020-0001 | High | Gin's default logger allowed unsanitized input, enabling remote log-line injection in applications that exposed attacker-controlled data to default logging paths. | 1.6.0 | https://github.com/advisories/GHSA-6vm3-jj99-7229 |
| CVE-2020-28483 / GHSA-h395-qcrw-5vmq / GO-2021-0052 | High | Applications using `ClientIP()` could mis-handle `X-Forwarded-For`, letting clients spoof source IP information when Gin was exposed directly or trusted-proxy settings were too permissive. | 1.7.7 | https://github.com/advisories/GHSA-h395-qcrw-5vmq |
| CVE-2023-26125 / GHSA-3vp4-m3rf-835h | Medium | Specially crafted `X-Forwarded-Prefix` input could lead to improper input validation and downstream cache-poisoning risk depending on deployment and application logic. | 1.9.0 | https://github.com/advisories/GHSA-3vp4-m3rf-835h |
| CVE-2023-29401 / GHSA-2c4m-59x9-fr2g / GO-2023-1737 | Medium | `Context.FileAttachment` did not properly sanitize the filename parameter, allowing crafted values to alter `Content-Disposition` behavior and serve attachments under unexpected names. | 1.9.1 | https://github.com/advisories/GHSA-2c4m-59x9-fr2g |

*Full CVE history: https://osv.dev/list?ecosystem=Go&q=github.com/gin-gonic/gin*

## Security Posture Notes

- Gin sits on multiple trust boundaries at once: request routing, proxy-header interpretation, attachment/header generation, and default logging. Its advisory history reflects exactly those edges.
- The clearest recurring public bug class is boundary confusion around HTTP metadata: `X-Forwarded-For`, `X-Forwarded-Prefix`, and `Content-Disposition` handling all produced security-relevant behavior when applications trusted framework defaults or attacker-controlled header values.
- Upstream release notes provide useful fix anchors: v1.6.0 includes the log-injection mitigation, v1.7.7 explicitly calls out the `X-Forwarded-For` / `CVE-2020-28483` fix, v1.9.0 references the `X-Forwarded-Prefix` security work, and v1.9.1 includes the `FileAttachment` escaping fix.
- Exploitability varies sharply by deployment pattern. Several advisories become much more meaningful when apps are internet-facing, rely on proxy-derived client identity, or pass untrusted values into file-download helpers.
- One additional OSV / GHSA record (`GHSA-869c-j7wc-8jqv` / `CVE-2019-25211`) currently maps to the Gin package name but the cited public references point primarily to `gin-contrib/cors`. This pass did not treat it as a clean core-Gin vulnerability claim.

## Dependencies of Note

- `gin-contrib/cors` now has its own KB page and should be reviewed separately when applications use Gin's first-party CORS middleware; `CVE-2019-25211` maps cleanly to that module's wildcard-origin parsing logic rather than to core Gin alone.
- Reverse proxies, load balancers, and ingress layers materially affect the real-world impact of the forwarded-header and client-IP issues on this page.
- Go's standard `net/http` stack and transitive HTTP/2 components remain adjacent risk surfaces even when the published flaw is recorded against Gin.

## Open Questions

- Should this page eventually separate core-framework bugs from middleware-adjacent advisories even more explicitly so shared-ecosystem package boundaries stay easier to audit?
- Are there public maintainer-authored hardening notes on trusted proxies, header sanitization, or safe file-download patterns worth citing in a later pass?
- Are there other first-party Gin ecosystem modules with enough public advisory history to deserve companion pages?

## Related Pages

- [[go/github.com/gin-contrib/cors]]
- [[go/index]]

---
*Last updated: 2026-04-17 | Sources: 10 (OSV package query, four GHSA advisory pages, three public Go / upstream release references, two upstream issue / PR threads)*
