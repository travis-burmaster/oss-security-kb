# Twisted (python)

**Registry:** PyPI
**Weekly Downloads:** ~2,774,235 (last week, as of 2026-05-09; PyPIStats)
**Repository:** https://github.com/twisted/twisted
**Security Contact:** GitHub Security Advisories / Twisted security policy
**Disclosure Policy:** https://github.com/twisted/twisted/blob/trunk/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-09 | OpenClaw recurring review | package advisory history | public-source advisory mapping using OSV package queries, GitHub Advisory Database / GitHub Security Advisories surfaced through OSV, public CVE/NVD aliases, upstream SECURITY.md and NEWS.rst, PyPI metadata, and PyPIStats | 27 public OSV records reviewed; representative history curated across HTTP request smuggling / parser ambiguity, HTTP pipelining response disordering, TLS validation, CRLF / header injection, redirect/header exposure, HTML injection, SSH / DNS / HTTP2 denial of service, and reverse-proxy forced-browsing behavior | https://osv.dev/list?ecosystem=PyPI&q=Twisted |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-32gv-6cf3-wcmq | Critical | HTTP/2 Ping, Reset, and Settings flood paths could consume resources and deny service. | 19.10.0 | https://github.com/twisted/twisted/security/advisories/GHSA-32gv-6cf3-wcmq |
| GHSA-3c45-wgjp-7v9r / CVE-2014-7143 / PYSEC-2019-212 | High | HTTP client handling did not respect the configured trust root, weakening TLS trust decisions. | 14.0.1 | https://nvd.nist.gov/vuln/detail/CVE-2014-7143 |
| GHSA-3gqj-cmxr-p4x2 / CVE-2016-1000111 / PYSEC-2020-214 | Moderate | Reverse-proxy resource publishing could allow forced browsing of otherwise protected resources. | 16.3.1 | https://nvd.nist.gov/vuln/detail/CVE-2016-1000111 |
| GHSA-65rm-h285-5cc5 / CVE-2019-12855 / PYSEC-2019-129 | Critical | TLS certificate validation / hostname-checking behavior could accept invalid certificates. | 19.7.0rc1 | https://nvd.nist.gov/vuln/detail/CVE-2019-12855 |
| GHSA-6cc5-2vg4-cc7m / CVE-2019-12387 / PYSEC-2019-128 | Moderate | HTTP client request construction allowed CRLF injection into request headers. | 19.2.1 | https://github.com/advisories/GHSA-6cc5-2vg4-cc7m |
| GHSA-8r99-h8j2-rw64 | Moderate | HTTP request parsing inconsistencies could enable request-smuggling / desynchronization behavior. | 20.3.0 | https://github.com/twisted/twisted/security/advisories/GHSA-8r99-h8j2-rw64 |
| GHSA-92x2-jw7w-xvvx / CVE-2022-21712 / PYSEC-2022-27 | High | Client redirects could expose cookies or headers to different origins. | 22.1.0 | https://github.com/twisted/twisted/security/advisories/GHSA-92x2-jw7w-xvvx |
| GHSA-c2jg-hw38-jrqq / CVE-2022-24801 / PYSEC-2022-195 | Critical | twisted.web interpreted malformed HTTP requests inconsistently, enabling request-smuggling risk. | 22.4.0 | https://github.com/twisted/twisted/security/advisories/GHSA-c2jg-hw38-jrqq |
| GHSA-c8m8-j448-xjx7 / CVE-2024-41671 | Moderate | HTTP pipelining could produce disordered responses, risking cross-request response mix-ups. | 24.7.0rc1 | https://github.com/twisted/twisted/security/advisories/GHSA-c8m8-j448-xjx7 |
| GHSA-cf56-g6w6-pqq2 / CVE-2024-41810 / PYSEC-2024-75 | Moderate | Redirect response bodies reflected unescaped input, creating HTML injection risk. | 24.7.0rc1 | https://github.com/twisted/twisted/security/advisories/GHSA-cf56-g6w6-pqq2 |
| GHSA-grgv-6hw6-v9g4 / CVE-2026-42304 | High | Crafted DNS compression pointer chains in twisted.names could trigger denial of service. | 26.4.0rc2 | https://github.com/twisted/twisted/security/advisories/GHSA-grgv-6hw6-v9g4 |
| GHSA-h96w-mmrf-2h6v / CVE-2020-10108 / PYSEC-2020-259 | Critical | Malformed HTTP requests could trigger improper input-validation behavior in Twisted. | 20.3.0 | https://nvd.nist.gov/vuln/detail/CVE-2020-10108 |
| GHSA-p5xh-vx83-mxcj / CVE-2020-10109 / PYSEC-2020-260 | Critical | HTTP request-smuggling issue in Twisted request parsing / framing behavior. | 20.3.0 | https://github.com/advisories/GHSA-p5xh-vx83-mxcj |
| GHSA-rv6r-3f5q-9rgx / CVE-2022-21716 / PYSEC-2022-160 | High | SSH handshake handling could be abused for denial of service. | 22.2.0 | https://github.com/twisted/twisted/security/advisories/GHSA-rv6r-3f5q-9rgx |
| GHSA-vg46-2rrj-3647 / CVE-2022-39348 | Moderate | NameVirtualHost host-header handling could allow host-header injection / routing confusion. | 22.10.0rc1 | https://github.com/twisted/twisted/security/advisories/GHSA-vg46-2rrj-3647 |
| GHSA-xc8x-vp79-p3wm / CVE-2023-46137 / PYSEC-2023-224 | Moderate | Earlier HTTP pipelining response-ordering flaw could send responses to the wrong request. | 23.10.0rc1 | https://github.com/twisted/twisted/security/advisories/GHSA-xc8x-vp79-p3wm |

*Representative advisory history only; full package query: https://osv.dev/list?ecosystem=PyPI&q=Twisted*

## Security Posture Notes

- Twisted is a long-running Python event-driven networking framework with broad protocol surfaces: HTTP client/server, HTTP/2, SSH, DNS, TLS, proxying, and web resource publishing all appear in the public advisory record.
- The densest recurring cluster is `twisted.web` HTTP parser / request-boundary behavior: public records include request smuggling, malformed request handling, host-header / virtual-host confusion, redirect/header exposure, and HTTP pipelining response-ordering issues.
- Client-side deployments should treat TLS verification, redirect handling, and credential/header forwarding as sensitive trust boundaries; several public advisories involve certificates, cookies, or injected headers.
- Server deployments should review HTTP proxy deployments, pipelining, request parsing, and resource-publishing configuration, especially where Twisted sits behind or in front of another HTTP parser.
- Denial-of-service exposure is protocol-specific rather than one generic bug class: public records cover HTTP/2 flood behavior, SSH handshake behavior, and `twisted.names` DNS compression-pointer handling.
- Twisted publishes a repository `SECURITY.md` and multiple GitHub Security Advisories; distro advisories may backport fixes under older version numbers, so downstream users should map package-manager versions to vendor patches before assuming vulnerability or safety from upstream semver alone.

## Dependencies of Note

- HTTP parser / HTTP/2 behavior is central for Twisted web deployments and reverse-proxy use.
- TLS certificate validation and redirect policy are important for client code using Twisted's HTTP stack.
- DNS and SSH protocol handlers have separate resource-exhaustion histories and should be tracked as distinct surfaces.

## Open Questions

- Should future passes split Twisted into protocol-specific subpages (`twisted.web`, `twisted.names`, Conch / SSH) once the KB supports component-level pages?
- Which widely used downstream frameworks or agents embed Twisted in exposed HTTP proxy or DNS roles and therefore need linkage from this page?
- Should the 27 OSV package records be normalized into a full chronological table, including duplicate PyPA/GHSA aliases, in a longer dedicated pass?

## Related Pages

- [[python/aiohttp]]
- [[python/requests]]
- [[python/urllib3]]
- [[python/index]]

---
*Last updated: 2026-05-09 | Sources: 6 (OSV package query, GitHub Advisory Database / GHSA pages, public CVE/NVD aliases, upstream SECURITY.md, upstream NEWS.rst, PyPI metadata / PyPIStats downloads)*
