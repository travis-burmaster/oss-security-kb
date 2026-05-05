# aiohttp (python)

**Registry:** PyPI
**Weekly Downloads:** ~122,619,877 (last week, as of 2026-05-05; PyPIStats)
**Repository:** https://github.com/aio-libs/aiohttp
**Security Contact:** GitHub Security Advisories / aio-libs issue tracker (dedicated SECURITY.md not located in this pass)
**Disclosure Policy:** none located in this pass
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-05 | OpenClaw recurring review | package advisory history | public-source advisory mapping using OSV package query, GHSA records, public CVE/NVD aliases, upstream changelog, PyPI metadata, and PyPIStats | 33 unique public package advisories curated across HTTP parser / smuggling, static-file exposure, redirect credential leakage, multipart / header injection, and denial-of-service surfaces | https://osv.dev/list?ecosystem=PyPI&q=aiohttp |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-27mf-ghqm-j3j8 / CVE-2024-52303 | CVSS 3.1 | Middleware-enabled handling of non-allowed methods could leak memory, creating a denial-of-service path. | 3.10.11 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-27mf-ghqm-j3j8 |
| GHSA-2vrm-gr82-f7m5 / CVE-2026-34514 | CVSS 4.0 | Multipart part Content-Type header construction allowed CRLF injection. | 3.13.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-2vrm-gr82-f7m5 |
| GHSA-3wq7-rqq7-wx6j / CVE-2026-34517 | CVSS 4.0 | Non-file multipart field size enforcement happened too late, allowing memory exhaustion. | 3.13.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-3wq7-rqq7-wx6j |
| GHSA-45c4-8wx5-qw6w / CVE-2023-37276 / PYSEC-2023-120 | CVSS 3.1 | The llhttp-backed server parser accepted request forms that could enable HTTP request smuggling. | 3.8.5 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-45c4-8wx5-qw6w |
| GHSA-54jq-c3m8-4m76 / CVE-2025-69226 | CVSS 4.0 | Static-file handling could leak internal path components through brute-forceable responses. | 3.13.3 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-54jq-c3m8-4m76 |
| GHSA-5h86-8mv2-jq9f / CVE-2024-23334 / PYSEC-2024-24 | CVSS 3.1 | Static resource handling could expose files through directory traversal when `follow_symlinks` was used. | 3.9.2 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-5h86-8mv2-jq9f |
| GHSA-5m98-qgg9-wh84 / CVE-2024-30251 | CVSS 3.1 | Malformed POST parsing could trigger denial of service. | 3.9.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-5m98-qgg9-wh84 |
| GHSA-63hf-3vf5-4wqf / CVE-2026-34520 | CVSS 3.1 | The C parser accepted null bytes / control characters in response header values, enabling header-injection or bypass behavior. | 3.13.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-63hf-3vf5-4wqf |
| GHSA-69f9-5gxw-wvc2 / CVE-2025-69224 | CVSS 4.0 | Unicode header-value processing could create parsing discrepancies at protocol boundaries. | 3.13.3 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-69f9-5gxw-wvc2 |
| GHSA-6jhg-hg63-jvvf / CVE-2025-69228 | CVSS 4.0 | Large payload handling could exhaust resources and deny service. | 3.13.3 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-6jhg-hg63-jvvf |
| GHSA-6mq8-rvhq-8wgg / CVE-2025-69223 | CVSS 3.1 | HTTP parser `auto_decompress` behavior could be abused as a zip-bomb resource-exhaustion path. | 3.13.3 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-6mq8-rvhq-8wgg |
| GHSA-7gpw-8wmc-pm8g / CVE-2024-27306 | CVSS 3.1 | Static-file index pages could render cross-site scripting content. | 3.9.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-7gpw-8wmc-pm8g |
| GHSA-8495-4g3g-x7pr / CVE-2024-52304 | CVSS 4.0 | Incorrect chunk-extension parsing could enable HTTP request smuggling. | 3.10.11 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-8495-4g3g-x7pr |
| GHSA-8qpw-xqxj-h4r2 / CVE-2024-23829 / PYSEC-2024-26 | CVSS 3.1 | The Python HTTP parser remained overly lenient about separators, preserving parsing inconsistency risk. | 3.9.2 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-8qpw-xqxj-h4r2 |
| GHSA-9548-qrrj-x5pj / CVE-2025-53643 | CVSS 4.0 | Chunked trailer-section parsing could enable HTTP request/response smuggling. | 3.12.14 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-9548-qrrj-x5pj |
| GHSA-966j-vmvw-g2g9 / CVE-2026-34518 | CVSS 4.0 | Client redirects could leak Cookie and Proxy-Authorization headers across origins. | 3.13.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-966j-vmvw-g2g9 |
| GHSA-c427-h43c-vf67 / CVE-2026-34525 | CVSS 4.0 | Duplicate Host headers were accepted, creating routing / authority ambiguity. | 3.13.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-c427-h43c-vf67 |
| GHSA-fh55-r93g-j68g / CVE-2025-69230 | CVSS 4.0 | Cookie parsing could create a warning storm and resource exhaustion. | 3.13.3 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-fh55-r93g-j68g |
| GHSA-g84x-mcqj-x9qq / CVE-2025-69229 | CVSS 4.0 | Chunked message handling could be abused for denial of service. | 3.13.3 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-g84x-mcqj-x9qq |
| GHSA-gfw2-4jvh-wgfg / CVE-2023-47627 / PYSEC-2023-246 | CVSS 3.1 | The Python HTTP parser accepted invalid input in ways that could create request-smuggling / protocol-integrity issues. | 3.8.6 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-gfw2-4jvh-wgfg |
| GHSA-hcc4-c3v8-rx92 / CVE-2026-34513 | CVSS 4.0 | TCPConnector DNS cache growth was unbounded, enabling denial of service. | 3.13.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-hcc4-c3v8-rx92 |
| GHSA-jj3x-wxrx-4x23 / CVE-2025-69227 | CVSS 4.0 | Running with asserts bypassed could expose denial-of-service behavior. | 3.13.3 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-jj3x-wxrx-4x23 |
| GHSA-jwhx-xcg6-8xhj / CVE-2024-42367 | CVSS 3.1 | Compressed files served through symlinks were not protected from traversal exposure. | 3.10.2 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-jwhx-xcg6-8xhj |
| GHSA-m5qp-6w8w-w647 / CVE-2026-34516 | CVSS 3.1 | Multipart header limits could be bypassed, enabling denial of service. | 3.13.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-m5qp-6w8w-w647 |
| GHSA-mqqc-3gqh-h2x8 / CVE-2025-69225 | CVSS 4.0 | Regexes for ASCII protocol elements could match Unicode characters, causing parser discrepancies. | 3.13.3 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-mqqc-3gqh-h2x8 |
| GHSA-mwh4-6h8g-pg8w / CVE-2026-34519 | CVSS 4.0 | A carriage return in the reason phrase could cause HTTP response splitting. | 3.13.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-mwh4-6h8g-pg8w |
| GHSA-p998-jp59-783m / CVE-2026-34515 | CVSS 4.0 | On Windows, static resource handling could allow UNC SSRF, NTLMv2 credential exposure, or local file reads. | 3.13.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-p998-jp59-783m |
| GHSA-pjjw-qhg8-p2p9 | Unknown | Bundled / pinned llhttp dependency exposure carried request-smuggling risk until dependency refresh. | 3.8.6 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-pjjw-qhg8-p2p9 |
| GHSA-q3qx-c6g2-7pw2 / CVE-2023-49081 / PYSEC-2023-250 | CVSS 3.1 | ClientSession allowed CRLF injection through the HTTP version value. | 3.9.0 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-q3qx-c6g2-7pw2 |
| GHSA-qvrw-v9rv-5rjx / CVE-2023-49082 / PYSEC-2023-251 | CVSS 3.1 | ClientSession allowed CRLF injection through the HTTP method value. | 3.9.0 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-qvrw-v9rv-5rjx |
| GHSA-v6wp-4m6f-gcjg / CVE-2021-21330 / PYSEC-2021-76 | CVSS 3.1 | `normalize_path_middleware` could redirect to attacker-controlled paths. | 3.7.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-v6wp-4m6f-gcjg |
| GHSA-w2fm-2cpv-w7v5 / CVE-2026-22815 | CVSS 4.0 | Trailer headers were unlimited, allowing uncapped memory usage. | 3.13.4 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-w2fm-2cpv-w7v5 |
| GHSA-xx9p-xxvh-7g8j / CVE-2023-47641 / PYSEC-2023-247 | CVSS 3.1 | C and Python parsers interpreted Content-Length / Transfer-Encoding combinations inconsistently. | 3.8.0 | https://github.com/aio-libs/aiohttp/security/advisories/GHSA-xx9p-xxvh-7g8j |

*Full advisory history: https://osv.dev/list?ecosystem=PyPI&q=aiohttp*

## Security Posture Notes

- `aiohttp` is a high-volume async HTTP client/server framework with roughly 123M weekly PyPI downloads in this pass, so parser and static-file bugs have broad downstream relevance.
- The public advisory record clusters around HTTP parser ambiguity / request smuggling, CRLF and response-splitting injection, redirect credential leakage, static-file path exposure, multipart parsing limits, and resource-exhaustion issues.
- Recent fix trains are dense: `3.13.3` addressed a large 2025 cluster around parser/resource-handling issues, and `3.13.4` addressed a second cluster across multipart, DNS cache, header parsing, redirect leakage, duplicate Host handling, trailer limits, Windows static-resource behavior, and response splitting.
- Server deployments should treat aiohttp's C parser (`llhttp`) and Python parser fallback as separate trust-boundary surfaces because several public advisories involve parser discrepancies or dependency parser behavior.
- Client deployments should review redirect policies and credential-header forwarding, especially where `Cookie`, `Authorization`, or `Proxy-Authorization` headers may be present.
- Static-file serving should be considered sensitive configuration: symlink handling, Windows UNC behavior, directory indexes, and compressed-file variants all appear in the public advisory history.

## Dependencies of Note

- `llhttp` / parser dependency behavior is security-relevant for request-smuggling and parser-boundary advisories.
- Compression and multipart parsing paths are recurring resource-exhaustion surfaces.
- [[python/urllib3]] and [[python/requests]] are adjacent Python HTTP-stack pages, but aiohttp's async client/server advisory history should be tracked separately.

## Open Questions

- Is there a maintainer-published private disclosure policy outside GitHub Security Advisories that should be captured?
- Should a future pass split the dense 2025-2026 `3.13.x` fix train into a dedicated timeline with upstream changelog citations per release?
- Which downstream frameworks rely on aiohttp static-resource serving defaults or redirect handling in security-sensitive contexts?

## Related Pages

- [[python/requests]]
- [[python/urllib3]]
- [[python/index]]

---
*Last updated: 2026-05-05 | Sources: 6 (OSV package query, GitHub Advisory Database / GHSA pages, public CVE/NVD aliases, upstream CHANGES.rst, PyPI metadata, PyPIStats downloads)*
