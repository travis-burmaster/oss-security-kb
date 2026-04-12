# urllib3 (python)

**Registry:** PyPI
**Weekly Downloads:** unknown (as of 2026-04-12)
**Repository:** https://github.com/urllib3/urllib3
**Security Contact:** https://tidelift.com/security
**Disclosure Policy:** https://github.com/urllib3/urllib3/blob/main/.github/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-12 | OpenClaw recurring review | api-surface | manual | 16 publicly disclosed package vulnerabilities curated from OSV, GHSA, CVE, upstream changelog, and release history | https://osv.dev/list?ecosystem=PyPI&q=urllib3 |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-21441 / GHSA-38jv-5279-wg99 | High | When using the streaming API with `preload_content=False`, redirect handling could decompress redirect-response bodies before read limits applied, enabling decompression-bomb style resource exhaustion from untrusted servers. | 2.6.3 | https://github.com/urllib3/urllib3/security/advisories/GHSA-38jv-5279-wg99 |
| CVE-2025-66418 / GHSA-gm62-xv2j-4w53 | High | urllib3 allowed an unbounded `Content-Encoding` decompression chain, enabling excessive CPU / memory consumption on attacker-controlled responses. | 2.6.0 | https://github.com/urllib3/urllib3/security/advisories/GHSA-gm62-xv2j-4w53 |
| CVE-2025-66471 / GHSA-2xpw-w6gg-jr37 | High | The streaming API could fully decode highly compressed data in one operation, defeating chunk-size expectations and causing client-side resource exhaustion. | 2.6.0 | https://github.com/urllib3/urllib3/security/advisories/GHSA-2xpw-w6gg-jr37 |
| CVE-2025-50181 / GHSA-pq67-6m6q-mj2v | Moderate | Redirect disabling configured via `PoolManager(retries=...)` was ignored, which can undermine SSRF or redirect-control assumptions. | 2.5.0 | https://github.com/urllib3/urllib3/security/advisories/GHSA-pq67-6m6q-mj2v |
| CVE-2025-50182 / GHSA-48p4-8xcf-vxj5 | Moderate | In Pyodide / browser / Node.js runtimes, urllib3 could not actually enforce its documented redirect controls because the underlying runtime owns redirect behavior. | 2.5.0 | https://github.com/urllib3/urllib3/security/advisories/GHSA-48p4-8xcf-vxj5 |
| CVE-2024-37891 / GHSA-34jh-p97f-mpxf | Moderate | `Proxy-Authorization` was not stripped on cross-origin redirects when users set that header outside urllib3's proxy helpers. | 1.26.19 / 2.2.2 | https://github.com/urllib3/urllib3/security/advisories/GHSA-34jh-p97f-mpxf |
| CVE-2023-45803 / GHSA-g4mx-q9vg-27p4 | Moderate | After a 303 redirect changed a request to `GET`, urllib3 could retain the original request body, creating low-likelihood but real data-leak exposure when a trusted origin or redirect target becomes hostile. | 1.26.18 / 2.0.7 | https://github.com/urllib3/urllib3/security/advisories/GHSA-g4mx-q9vg-27p4 |
| CVE-2023-43804 / GHSA-v845-jxx5-vc9f | High | `Cookie` headers were not stripped on cross-origin redirects, risking credential leakage when redirects were followed automatically. | 1.26.17 / 2.0.6 | https://github.com/urllib3/urllib3/security/advisories/GHSA-v845-jxx5-vc9f |
| CVE-2021-33503 / GHSA-q2q7-5pp4-w6pg | High | The URL authority parser could hit catastrophic backtracking on URLs containing many `@` characters, enabling denial of service. | 1.26.5 | https://github.com/urllib3/urllib3/security/advisories/GHSA-q2q7-5pp4-w6pg |
| CVE-2021-28363 / GHSA-5phf-pp7p-vc2r | Moderate | HTTPS-over-HTTPS proxy connections using the default `SSLContext` failed to verify the proxy certificate hostname. | 1.26.4 | https://github.com/urllib3/urllib3/security/advisories/GHSA-5phf-pp7p-vc2r |
| CVE-2020-26137 / GHSA-wqvq-5m8c-6g24 | Moderate | CRLF injection was possible if an attacker controlled the HTTP method string. | 1.25.9 | https://github.com/advisories/GHSA-wqvq-5m8c-6g24 |
| CVE-2020-7212 / GHSA-hmv2-79q8-fv6g | High | `_encode_invalid_chars()` could consume excessive CPU on crafted URLs because percent-encoding normalization work scaled poorly. | 1.25.8 | https://github.com/advisories/GHSA-hmv2-79q8-fv6g |
| CVE-2019-11236 / GHSA-r64q-w8jr-g9qp | Moderate | CRLF injection was possible when attacker-controlled request parameters were passed through vulnerable request paths. | 1.24.3 | https://github.com/advisories/GHSA-r64q-w8jr-g9qp |
| CVE-2019-11324 / GHSA-mh33-7rrq-662w | High | Certain certificate-validation configurations combining custom CA inputs and system certificates could accept TLS connections that should fail verification. | 1.24.2 | https://github.com/advisories/GHSA-mh33-7rrq-662w |
| CVE-2018-25091 / GHSA-gwvm-45gx-3cf8 | Moderate | The first cross-origin redirect fix for `Authorization` leakage was incomplete because header stripping was case-sensitive. | 1.24.2 | https://github.com/advisories/GHSA-gwvm-45gx-3cf8 |
| CVE-2018-20060 / GHSA-www2-v7xj-xrc6 | Critical | urllib3 did not strip `Authorization` on cross-origin redirects, risking credential leakage to unintended hosts or cleartext transport. | 1.23 | https://github.com/advisories/GHSA-www2-v7xj-xrc6 |
| CVE-2016-9015 / GHSA-v4w5-p2hg-8fh6 | Moderate | In a narrow PyOpenSSL + OpenSSL 1.1.0 configuration, urllib3 1.17-1.18 could fail to validate TLS certificates correctly. | 1.18.1 | https://github.com/advisories/GHSA-v4w5-p2hg-8fh6 |

*Full CVE history: https://osv.dev/list?ecosystem=PyPI&q=urllib3*

## Security Posture Notes

- urllib3 has one of the clearer public vulnerability histories among Python infrastructure packages because it sits directly on redirect handling, header forwarding, URL parsing, proxy/TLS configuration, and streaming/decompression boundaries.
- The advisory record clusters around three recurring bug families: **redirect credential leakage**, **TLS / certificate-validation edge cases**, and **resource-consumption bugs in URL parsing or decompression paths**.
- Upstream changelog entries line up cleanly with the advisory history: 1.23 introduced default `Authorization` stripping on redirects; 1.24.2 fixed the case-sensitive follow-up and CA-store handling; 1.26.17 / 1.26.18 / 1.26.19 and 2.0.6 / 2.0.7 / 2.2.2 extended redirect stripping to `Cookie`, request bodies on 303-to-GET transitions, and `Proxy-Authorization`; 2.6.0 and 2.6.3 hardened the streaming/decompression path against decompression bombs.
- The repository security policy is mature and explicit: reports go through Tidelift, public GitHub issues are discouraged for undisclosed vulnerabilities, and only the active 2.x line receives security fixes. That matters when evaluating whether 1.x fix versions are historical anchors versus currently supported upgrade targets.
- Several redirect-related advisories are low-likelihood in ordinary deployments, but urllib3 is so widely embedded that seemingly narrow header-handling bugs can still have large downstream blast radius when higher-level clients assume automatic redirect safety.

## Dependencies of Note

- [[python/requests]] is the most important adjacent page because Requests relies on urllib3 and inherits parts of its redirect, connection-management, and proxy behavior.
- Python's `ssl` / `SSLContext` behavior and optional PyOpenSSL integration remain relevant operational dependencies for interpreting older TLS-validation advisories.
- Browser / Node.js Pyodide runtimes matter for modern urllib3 because some redirect-control semantics are constrained by the host runtime rather than by urllib3 alone.

## Open Questions

- Which urllib3 hardening guidance from the official docs can be cited cleanly in a future evidence-backed hardening section without drifting into unsourced best practices?
- Should the KB split future coverage between package vulnerabilities and higher-level client inheritance (for example Requests / botocore) so redirect and proxy bugs are not double-counted or overstated?
- Are there public maintainer-authored postmortems or audit writeups beyond the advisory pages that would better explain the 2025-2026 decompression-bomb fixes and their practical exploit conditions?

## Related Pages

- [[python/requests]]
- [[python/index]]

---
*Last updated: 2026-04-12 | Sources: 5 (OSV package query, GitHub Advisory Database / GHSA pages, CVE aliases via OSV, upstream CHANGES.rst, repository SECURITY.md)*
