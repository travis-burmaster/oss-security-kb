# io.netty:netty-codec-http (Maven)

**Registry:** Maven Central  
**Weekly Downloads:** unknown  
**Repository:** https://github.com/netty/netty  
**Security Contact:** Netty GitHub Security Advisories / project security policy  
**Disclosure Policy:** https://github.com/netty/netty/security/policy  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-12 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation from OSV.dev package query, GitHub Advisory Database aliases surfaced by OSV, public CVE/NVD links surfaced by OSV, Netty GitHub advisories referenced by OSV, Maven Central metadata, and local proxy-assisted drafting | Added initial Maven package page for 15 package-scoped public OSV records. The public history is dominated by HTTP request-smuggling / parser-differential issues, with additional response-splitting, CRLF injection, decompression/resource-exhaustion, and local temporary-file disclosure records. The May 2026 advisory cluster fixes multiple HTTP codec issues in `4.1.133.Final` / `4.2.13.Final`. | https://osv.dev/list?ecosystem=Maven&q=io.netty%3Anetty-codec-http |

## Known Vulnerabilities

| CVE / Issue | Description | Fixed in | Source |
|-------------|-------------|----------|--------|
| CVE-2019-20444 / GHSA-cqqj-4p63-rrmm | HTTP Request Smuggling in Netty | 4.1.44 | https://osv.dev/vulnerability/GHSA-cqqj-4p63-rrmm |
| CVE-2021-21290 / GHSA-5mcr-gq6c-3hq2 | Local Information Disclosure Vulnerability in Netty on Unix-Like systems | 4.1.59.Final | https://osv.dev/vulnerability/GHSA-5mcr-gq6c-3hq2 |
| CVE-2021-43797 / GHSA-wx5j-54mm-rqqq | HTTP request smuggling in netty | 4.1.71.Final | https://osv.dev/vulnerability/GHSA-wx5j-54mm-rqqq |
| CVE-2022-24823 / GHSA-269q-hmxg-m83q | Local Information Disclosure Vulnerability in io.netty:netty-codec-http | 4.1.77.Final | https://osv.dev/vulnerability/GHSA-269q-hmxg-m83q |
| CVE-2022-41915 / GHSA-hh82-3pmq-7frp | Netty vulnerable to HTTP Response splitting from assigning header value iterator | 4.1.86.Final | https://osv.dev/vulnerability/GHSA-hh82-3pmq-7frp |
| CVE-2024-29025 / GHSA-5jpm-x58v-624v | Netty's HttpPostRequestDecoder can OOM | 4.1.108.Final | https://osv.dev/vulnerability/GHSA-5jpm-x58v-624v |
| CVE-2025-58056 / GHSA-fghv-69vj-qj49 | Netty vulnerable to request smuggling due to incorrect parsing of chunk extensions | 4.1.125.Final, 4.2.5.Final | https://osv.dev/vulnerability/GHSA-fghv-69vj-qj49 |
| CVE-2026-33870 / GHSA-pwqr-wmgm-9rr8 | Netty: HTTP Request Smuggling via Chunked Extension Quoted-String Parsing | 4.1.132.Final, 4.2.10.Final | https://osv.dev/vulnerability/GHSA-pwqr-wmgm-9rr8 |
| CVE-2026-41417 / GHSA-v8h7-rr48-vmmv | Netty: Start-Line Injection in DefaultHttpRequest.setUri() Allows HTTP Request Smuggling and RTSP Request Injection | 4.1.133.Final, 4.2.13.Final | https://osv.dev/vulnerability/GHSA-v8h7-rr48-vmmv |
| CVE-2025-67735 / GHSA-84h7-rjj3-6jx4 | Netty has a CRLF Injection vulnerability in io.netty.handler.codec.http.HttpRequestEncoder | 4.1.129.Final, 4.2.8.Final | https://osv.dev/vulnerability/GHSA-84h7-rjj3-6jx4 |
| CVE-2026-42580 / GHSA-m4cv-j2px-7723 | Netty vulnerable to HTTP Request Smuggling due to incorrect chunk size parsing | 4.1.133.Final, 4.2.13.Final | https://osv.dev/vulnerability/GHSA-m4cv-j2px-7723 |
| CVE-2026-42581 / GHSA-xxqh-mfjm-7mv9 | Netty HTTP/1.0 TE+CL Coexistence Bypasses Smuggling Sanitization | 4.1.133.Final, 4.2.13.Final | https://osv.dev/vulnerability/GHSA-xxqh-mfjm-7mv9 |
| CVE-2026-42584 / GHSA-57rv-r2g8-2cj3 | Netty has HttpClientCodec response desynchronization | 4.1.133.Final, 4.2.13.Final | https://osv.dev/vulnerability/GHSA-57rv-r2g8-2cj3 |
| CVE-2026-42585 / GHSA-38f8-5428-x5cv | Netty vulnerable to HTTP Request Smuggling due to malformed Transfer-Encoding | 4.1.133.Final, 4.2.13.Final | https://osv.dev/vulnerability/GHSA-38f8-5428-x5cv |
| CVE-2026-42587 / GHSA-f6hv-jmp6-3vwv | Netty: HttpContentDecompressor maxAllocation bypass when Content-Encoding set to br/zstd/snappy leads to decompression bomb DoS | 4.1.133.Final, 4.2.13.Final | https://osv.dev/vulnerability/GHSA-f6hv-jmp6-3vwv |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=io.netty%3Anetty-codec-http*

## Security Posture Notes

- `netty-codec-http` is a foundational HTTP/1.x codec used by Netty-based servers, clients, proxies, gateways, and higher-level frameworks. Parser behavior can become security-critical when Netty peers disagree with front-end proxies, back-end servers, or upstream/downstream HTTP components.
- The advisory pattern is concentrated in HTTP request smuggling and message-boundary parsing: malformed `Transfer-Encoding`, incorrect chunk-size or chunk-extension handling, `TE` plus `Content-Length` coexistence, URI/start-line injection, and client-side response desynchronization all appear in the public record.
- Recent public fixes are clustered. OSV records for the May 2026 GHSA set list fixes in `4.1.133.Final` and `4.2.13.Final` for several independent HTTP codec issues, while `CVE-2026-33870` was fixed earlier in `4.1.132.Final` / `4.2.10.Final`.
- Resource-exhaustion records include `HttpPostRequestDecoder` out-of-memory behavior and a `HttpContentDecompressor` `maxAllocation` bypass for compressed content encodings. These matter most for applications that accept attacker-controlled HTTP bodies or compressed responses.
- Maven Central metadata saved in this pass listed `5.0.0.Alpha2` as the latest / release version. For production patch guidance, use the maintained stable line in deployment (`4.1.x` or `4.2.x`) and the fixed versions in the relevant advisory rather than treating the alpha line as a routine upgrade target.

## Dependencies of Note

- Netty is often consumed transitively through Java networking stacks, RPC frameworks, reactive web frameworks, and cloud SDKs. Review the resolved dependency tree, because applications may not declare `io.netty:netty-codec-http` directly.
- Protocol-boundary exposure depends on where Netty is used: an internet-facing Netty HTTP server, reverse proxy, gateway, HTTP client, or service mesh sidecar has a different risk profile than an internal-only component.
- Coordinate with adjacent Netty artifacts such as `netty-codec-http2`, `netty-handler`, and framework-managed Netty BOMs when patching, so codec, handler, and transport versions remain compatible.

## Open Questions

- Should the KB add companion pages for `io.netty:netty-codec-http2`, `io.netty:netty-handler`, and Netty BOM usage to distinguish HTTP/1.x parser issues from HTTP/2 and TLS/handler advisories?
- Which high-usage frameworks pin affected Netty versions after the May 2026 fix cluster, and do their release notes clearly surface the Netty security dependency upgrade?
- Should future generated appendices normalize all Netty advisories across artifacts, since some CVEs affect multiple Maven coordinates?

## Related Pages

- [[maven/index]]
- [[maven/org.springframework/spring-webflux]]
- [[maven/org.springframework/spring-webmvc]]
- [[maven/org.apache.tomcat.embed/tomcat-embed-core]]
- [[go/golang.org-x-net]]

---
*Last updated: 2026-05-12 | Sources: 5 (OSV package query and individual vulnerability records, GitHub Advisory Database public aliases surfaced by OSV, public CVE/NVD links surfaced by OSV, Netty GitHub advisories referenced by OSV, Maven Central metadata, local proxy synthesis used as drafting aid only)*
