# Tornado (python)

**Registry:** PyPI
**Weekly Downloads:** ~28,076,659 (last week, as of 2026-05-10; PyPIStats)
**Repository:** https://github.com/tornadoweb/tornado
**Security Contact:** GitHub Security Advisories / Tornado security policy
**Disclosure Policy:** https://github.com/tornadoweb/tornado/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-10 | OpenClaw recurring review | package advisory history | public-source advisory mapping using OSV package queries, GitHub Advisory Database / GitHub Security Advisories surfaced through OSV, public CVE/NVD aliases, upstream release/security-policy pages, PyPI metadata, and PyPIStats | 14 public OSV records reviewed; representative history curated across HTTP request smuggling, cookie and multipart denial of service, CRLF / cookie-attribute injection, open redirect, and legacy XSRF-token side-channel behavior | https://osv.dev/list?ecosystem=PyPI&q=tornado |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-f7fv-v9rh-prvc / CVE-2012-2374 / PYSEC-2012-5 | High | `RequestHandler.set_header` allowed CRLF injection / HTTP response splitting via crafted input. | 2.2.1 | https://nvd.nist.gov/vuln/detail/CVE-2012-2374 |
| GHSA-8vpw-mgpf-mpvv / CVE-2014-9720 / PYSEC-2020-213 | High | XSRF token handling could expose a fixed token to BREACH-style side-channel attacks when responses were compressed. | 3.2.2 | https://nvd.nist.gov/vuln/detail/CVE-2014-9720 |
| GHSA-hj3f-6gcp-jg8j / CVE-2023-28370 / PYSEC-2023-75 | Moderate | Open redirect in Tornado could allow crafted URLs to redirect users to attacker-controlled sites. | 6.3.2 | https://github.com/advisories/GHSA-hj3f-6gcp-jg8j |
| GHSA-qppv-j76h-2rpx | Moderate | HTTP parser accepted non-standard characters in `Content-Length` and chunk lengths, creating request-smuggling risk behind parsers with different behavior. | 6.3.3 | https://github.com/tornadoweb/tornado/security/advisories/GHSA-qppv-j76h-2rpx |
| GHSA-753j-mpmx-qq6g | Moderate | Duplicate `Transfer-Encoding: chunked` handling could create request-smuggling risk in some reverse-proxy deployments. | 6.4.1 | https://github.com/tornadoweb/tornado/security/advisories/GHSA-753j-mpmx-qq6g |
| GHSA-w235-7p84-xx57 | Moderate | `CurlAsyncHTTPClient` request-header handling allowed CRLF injection in outgoing headers. | 6.4.1 | https://github.com/tornadoweb/tornado/security/advisories/GHSA-w235-7p84-xx57 |
| GHSA-8w49-h785-mj3c / CVE-2024-52804 | High | HTTP cookie parsing could have quadratic complexity, blocking the event loop and causing denial of service. | 6.4.2 | https://github.com/tornadoweb/tornado/security/advisories/GHSA-8w49-h785-mj3c |
| GHSA-7cx3-6m66-7c5m / CVE-2025-47287 | High | Malformed multipart form data could trigger excessive synchronous warning logging, enabling denial of service. | 6.5 | https://github.com/tornadoweb/tornado/security/advisories/GHSA-7cx3-6m66-7c5m |
| GHSA-qjxf-f2mg-c6mc / CVE-2026-31958 | High | Multipart form parsing lacked a specific part-count limit beyond total body size, allowing synchronous parsing resource exhaustion. | 6.5.5 | https://github.com/advisories/GHSA-qjxf-f2mg-c6mc |
| GHSA-78cv-mqj4-43f7 | Moderate | Incomplete validation of cookie `domain`, `path`, and `samesite` attributes could allow cookie-attribute injection. | 6.5.5 | https://github.com/tornadoweb/tornado/security/advisories/GHSA-78cv-mqj4-43f7 |
| GHSA-fqwm-6jpj-5wxc / CVE-2026-35536 | Moderate | Parallel public advisory for cookie-attribute injection via `RequestHandler.set_cookie` arguments. | 6.5.5 | https://github.com/advisories/GHSA-fqwm-6jpj-5wxc |

*Representative advisory history only; full package query: https://osv.dev/list?ecosystem=PyPI&q=tornado*

## Security Posture Notes

- Tornado combines web framework, HTTP client/server, and asynchronous networking surfaces, so its package-level advisory history spans both inbound request parsing and outbound client/header behavior.
- The most important recurring class in the public record is HTTP boundary interpretation: request-smuggling advisories depend on parser differences between Tornado and front-end proxies, while CRLF records affect response or client-request header construction.
- Denial-of-service issues concentrate around synchronous work in the event loop: cookie parsing, multipart parsing, and warning/logging behavior can affect all requests served by the same process.
- Cookie handling appears in multiple independent roles: parsing untrusted request cookies, generating `Set-Cookie` attributes, and older XSRF-token behavior.
- The 2026 cookie-attribute records appear closely related in public sources; keep them linked rather than treating them as separate bug classes unless upstream advisory text differentiates them further.
- Downstream distributions may backport fixes under older version numbers, so distro package users should map vendor package versions to vendor security advisories before relying on upstream semver alone.

## Dependencies of Note

- Reverse-proxy deployments should treat Tornado's HTTP parser behavior as a trust boundary and verify normalization of `Transfer-Encoding`, `Content-Length`, and chunk framing at the edge.
- Applications accepting large or attacker-controlled multipart uploads should review Tornado's current multipart limits and event-loop impact.
- Code that passes user-controlled data to response headers, client headers, redirects, or cookie attributes deserves focused review even when the framework version is current.

## Open Questions

- Should the KB split Tornado client-side issues (`CurlAsyncHTTPClient`, redirects, outbound headers) from server-side request parser issues once component-level pages are supported?
- Are major downstream frameworks or services embedding Tornado in reverse-proxy-sensitive positions where parser-differential advisories should be cross-linked?
- Should duplicate / parallel 2026 cookie-attribute records be normalized into one canonical row if GitHub Advisory Database and CVE metadata converge?

## Related Pages

- [[python/aiohttp]]
- [[python/twisted]]
- [[python/django]]
- [[python/requests]]
- [[python/index]]

---
*Last updated: 2026-05-10 | Sources: 6 (OSV package query, GitHub Advisory Database / GHSA pages, public CVE/NVD aliases, upstream security policy / releases, PyPI metadata, PyPIStats downloads)*
