# golang.org/x/net (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-05-09)
**Repository:** https://go.googlesource.com/net
**Security Contact:** https://go.dev/security/policy
**Disclosure Policy:** https://go.dev/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-09 | OpenClaw recurring review | api-surface | manual | 10 representative public vulnerabilities curated from OSV, GitHub Advisory Database, Go issue tracker / announce posts, and CVE aliases | https://osv.dev/list?ecosystem=Go&q=golang.org/x/net |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-27664 / GHSA-69cg-p879-7622 / GO-2022-0969 | Unknown | HTTP/2 server connections in `net/http` and `x/net/http2` could hang after shutdown/error handling, creating denial-of-service risk. | Go 1.18.6, Go 1.19.1, `x/net` pseudo-version `0.0.0-20220906165146-f3363e06e74c` | https://osv.dev/vulnerability/GO-2022-0969 |
| CVE-2022-41717 / GHSA-xrjj-mj9h-534m / GO-2022-1144 | Unknown | HTTP/2 header handling could allow excessive memory growth in `net/http` and `x/net/http2`. | Go 1.18.9, Go 1.19.4, `x/net` 0.4.0 | https://osv.dev/vulnerability/GO-2022-1144 |
| CVE-2022-41721 / GHSA-fxg5-wq6x-vr4w / GO-2023-1495 | Unknown | `x/net/http2/h2c` request-body handling with `MaxBytesHandler` could enable request-smuggling behavior. | `x/net` pseudo-version `0.1.1-0.20221104162952-702349b0e862` | https://github.com/advisories/GHSA-fxg5-wq6x-vr4w |
| CVE-2022-41723 / GHSA-vvpx-j8f3-3w6h / GO-2023-1571 | Unknown | Crafted HTTP/2 streams could trigger excessive CPU consumption in `net/http` and `x/net/http2`. | Go 1.19.6, Go 1.20.1, `x/net` 0.7.0 | https://osv.dev/vulnerability/GO-2023-1571 |
| CVE-2023-3978 / GHSA-2wrh-6pvc-2jm9 / GO-2023-1988 | Unknown | `x/net/html` could render text nodes outside the HTML namespace without proper escaping, creating XSS risk in affected render paths. | `x/net` 0.13.0 | https://github.com/advisories/GHSA-2wrh-6pvc-2jm9 |
| CVE-2023-39325 / GHSA-4374-p667-p6c8 / GO-2023-2102 | Unknown | HTTP/2 Rapid Reset patterns could force excessive work in `net/http` and `x/net/http2`. | Go 1.20.10, Go 1.21.3, `x/net` 0.17.0 | https://osv.dev/vulnerability/GO-2023-2102 |
| CVE-2023-45288 / GHSA-4v7x-pqxf-cx7m / GO-2024-2687 | Unknown | HTTP/2 CONTINUATION-frame handling could continue processing excessive header data before closing connections, enabling CPU/memory exhaustion. | Go 1.21.9, Go 1.22.2, `x/net` 0.23.0 | https://github.com/advisories/GHSA-4v7x-pqxf-cx7m |
| CVE-2024-45338 / GHSA-w32m-9786-jp63 / GO-2024-3333 | Unknown | `x/net/html` case-insensitive content parsing could become non-linear on crafted input. | `x/net` 0.33.0 | https://osv.dev/vulnerability/GO-2024-3333 |
| CVE-2025-22870 / GHSA-qxp5-gwg8-xv66 / GO-2025-3503 | Unknown | Proxy bypass was possible when IPv6 zone identifiers were handled in URLs used by HTTP proxy logic. | Go 1.23.7, Go 1.24.1, `x/net` 0.36.0 | https://github.com/advisories/GHSA-qxp5-gwg8-xv66 |
| CVE-2025-22872 / GHSA-vvgc-356p-c3xw / GO-2025-3595 | Unknown | `x/net/html` output generation had an input-neutralization flaw that could result in web-page generation / XSS exposure. | `x/net` 0.38.0 | https://github.com/advisories/GHSA-vvgc-356p-c3xw |

*Full public advisory history: https://osv.dev/list?ecosystem=Go&q=golang.org/x/net*

## Security Posture Notes

- `golang.org/x/net` is a foundational Go module rather than a single narrow library: its security history spans HTTP/2 transport behavior, h2c upgrade/request handling, HTML parsing/rendering, proxy semantics, and IDNA/text-adjacent web boundaries.
- The densest recurring class in public advisories is HTTP/2 resource exhaustion. Several records were fixed both in Go toolchain releases and in `x/net`, so consumers should check both the Go version and the module version when assessing exposure.
- The HTML-related advisories are a separate class: they matter most for applications that render, transform, or serialize attacker-influenced HTML trees.
- The 2025 IPv6 zone-ID proxy-bypass issue is trust-boundary sensitive: package users should treat proxy routing and URL normalization as security controls rather than convenience behavior.

## Dependencies of Note

- `net/http` and `x/net/http2` are tightly coupled for several historical advisories; downstream services often need both a Go runtime update and a module update.
- Frameworks and reverse proxies built on Go HTTP/2 should be reviewed for how quickly they pick up Go release-train fixes after public advisories.
- HTML sanitizers or renderers that compose with `x/net/html` need their own page-level review before attributing sanitization guarantees to this package alone.

## Open Questions

- Should this page eventually split HTTP/2 transport advisories from HTML parser/renderer advisories if both histories continue to grow?
- Are there public maintainer release notes that map every advisory to a specific `x/net` tag, or should this page continue using OSV fixed-version ranges as the canonical source?
- Which high-usage Go frameworks pin or vendor vulnerable `x/net` versions long enough to deserve downstream tracking pages?

## Related Pages

- [[go/golang.org-x-crypto]]
- [[go/google.golang.org/grpc]]
- [[go/index]]

---
*Last updated: 2026-05-09 | Sources: 6 (OSV package query, GitHub Advisory Database aliases, Go issue tracker, Go announce posts, Go change lists, public CVE aliases)*
