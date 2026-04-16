# undici (npm)

**Registry:** npm
**Weekly Downloads:** ~71,600,000 (2026-03-17 to 2026-04-16, derived from last-month npm downloads)
**Repository:** https://github.com/nodejs/undici
**Security Contact:** Node.js security process
**Disclosure Policy:** https://github.com/nodejs/node/blob/HEAD/SECURITY.md
**Current Status:** advisory mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-16 | OpenClaw recurring review | package advisory curation | public-source curation (OSV.dev, GitHub Advisory Database, public CVE records, upstream SECURITY.md, npm registry metadata) | 22 published records mapped; recurring redirect-boundary leakage, CRLF injection, and newer WebSocket / resource-exhaustion clusters confirmed | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-pgw7-wx7w-2w33 / CVE-2022-32210 | High | `ProxyAgent` could route nominally HTTPS traffic without properly verifying the remote server certificate, enabling man-in-the-middle risk on proxied connections. | 5.5.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-pgw7-wx7w-2w33) |
| GHSA-3cvr-822r-rqcc / CVE-2022-31150 | Moderate | Older releases allowed CRLF injection through request headers, `path`, and `method` when applications passed unsanitized input. | 5.8.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-3cvr-822r-rqcc) |
| GHSA-q768-x9m6-m9qp / CVE-2022-31151 | Low | Cross-origin redirects in older releases did not clear `Cookie` headers, creating a credential-leakage risk when redirects were enabled. | 5.8.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-q768-x9m6-m9qp) |
| GHSA-8qr4-xgw6-wmr3 / CVE-2022-35949 | Moderate | `undici.request()` could treat an absolute URL supplied via `pathname` / `path` as a new destination, enabling SSRF when applications assumed the origin could not change. | 5.8.2 | [GitHub Advisory Database](https://github.com/advisories/GHSA-8qr4-xgw6-wmr3) |
| GHSA-f772-66g8-q5h3 / CVE-2022-35948 | Moderate | CRLF injection via `content-type` allowed request splitting if untrusted input flowed into that header. Public records describe a 5.8.1 patch path, while OSV's affected range treats `5.8.2` as the first unaffected release. | 5.8.2 (see note) | [GitHub Advisory Database](https://github.com/advisories/GHSA-f772-66g8-q5h3) |
| GHSA-r6ch-mqf9-qc9w / CVE-2023-24807 | High | `Headers.set()` and `Headers.append()` used a regex normalization path vulnerable to ReDoS with attacker-controlled header values. | 5.19.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-r6ch-mqf9-qc9w) |
| GHSA-5r9g-qh6m-jxff / CVE-2023-23936 | Moderate | The `Host` header was another CRLF injection surface in older releases, showing the bug class extended beyond the first 2022 header fixes. | 5.19.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-5r9g-qh6m-jxff) |
| GHSA-wqq4-5wpv-mx2g / CVE-2023-45143 | Low | `fetch()` cross-origin redirects did not clear `Cookie` headers; this is a follow-on redirect credential-leakage issue distinct from the earlier lower-level redirect bug. | 5.26.2 | [GitHub Advisory Database](https://github.com/advisories/GHSA-wqq4-5wpv-mx2g) |
| GHSA-3787-6prv-h9w3 / CVE-2024-24758 | Low | `fetch()` cross-origin redirects cleared `Authorization` but not `Proxy-Authorization`, leaking proxy credentials until fixes landed on both the 5.x and 6.x lines. | 5.28.3 / 6.6.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-3787-6prv-h9w3) |
| GHSA-9f24-jqhm-jfcw / CVE-2024-24750 | Moderate | `fetch(url)` could leak memory when the response body was not consumed or was consumed very slowly, creating a resource-exhaustion / leak condition. | 6.6.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-9f24-jqhm-jfcw) |
| GHSA-m4v8-wqvr-p9f7 / CVE-2024-30260 | Low | `Proxy-Authorization` leakage also affected `request`, `dispatch`, `stream`, and `pipeline`, showing the redirect-boundary problem crossed multiple API surfaces. | 5.28.4 / 6.11.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-m4v8-wqvr-p9f7) |
| GHSA-9qxr-qj54-h672 / CVE-2024-30261 | Low | The `fetch()` `integrity` option could accept tampered content when the algorithm was specified but the hash value was malformed. | 5.28.4 / 6.11.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-9qxr-qj54-h672) |
| GHSA-3g92-w8c5-73pq / CVE-2024-38372 | Low | Under some network and process conditions, `response.arrayBuffer()` could include process-memory data in the returned buffer. | 6.19.2 | [GitHub Advisory Database](https://github.com/advisories/GHSA-3g92-w8c5-73pq) |
| GHSA-c76h-2ccp-4975 / CVE-2025-22150 | Moderate | Multipart `fetch()` boundaries were generated with `Math.random()`, a predictability problem relevant when attackers could observe enough generated values and influence multipart traffic. | 5.28.5 / 6.21.1 / 7.2.3 | [GitHub Advisory Database](https://github.com/advisories/GHSA-c76h-2ccp-4975) |
| GHSA-cxrh-j4jr-qwg3 / CVE-2025-47279 | Low | Repeated requests to a server with invalid certificate data could create a memory leak / DoS pattern in webhook-like retry loops. | 5.29.0 / 6.21.2 / 7.5.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-cxrh-j4jr-qwg3) |
| GHSA-g9mf-h72j-4rw9 / CVE-2026-22036 | Moderate | `fetch()` and the decompress interceptor accepted unbounded `Content-Encoding` chains, allowing resource exhaustion through extremely long decompression sequences. | 6.23.0 / 7.18.2 | [GitHub Advisory Database](https://github.com/advisories/GHSA-g9mf-h72j-4rw9) |
| GHSA-2mjp-6q6p-2qxm / CVE-2026-1525 | Moderate | Case-variant duplicate `Content-Length` headers could be emitted on the wire, enabling malformed requests and potential request-smuggling conditions in split-parser deployments. | 6.24.0 / 7.24.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-2mjp-6q6p-2qxm) |
| GHSA-4992-7rv2-5pvq / CVE-2026-1527 | Moderate | The `upgrade` option accepted CRLF sequences, reopening HTTP header injection / smuggling risk on a newer API surface. | 6.24.0 / 7.24.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-4992-7rv2-5pvq) |
| GHSA-f269-vfmq-vjvj / CVE-2026-1528 | High | A malicious WebSocket peer could send a 64-bit length that overflowed parser math and crashed the client process. | 6.24.0 / 7.24.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-f269-vfmq-vjvj) |
| GHSA-v9p9-hfj2-hcw8 / CVE-2026-2229 | High | Invalid `server_max_window_bits` handling in the WebSocket client could trigger an uncaught exception and immediate process termination. | 6.24.0 / 7.24.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-v9p9-hfj2-hcw8) |
| GHSA-vrm6-8vpv-qv8q / CVE-2026-1526 | High | WebSocket `permessage-deflate` decompression could expand a small compressed payload into extremely large memory consumption, causing DoS. | 6.24.0 / 7.24.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-vrm6-8vpv-qv8q) |
| GHSA-phc3-fgpg-7m6h / CVE-2026-2581 | Moderate | `interceptors.deduplicate()` could buffer large or long-lived upstream responses in memory for downstream consumers, creating a DoS risk under concurrent identical requests. | 7.24.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-phc3-fgpg-7m6h) |

## Security Posture Notes

- `undici` now has a broad public advisory history rather than a single isolated bug class, but three themes recur strongly in the published record: redirect-boundary credential leakage, CRLF / header-injection surfaces, and resource-exhaustion bugs.
- Redirect handling is the clearest repeating pattern. Public advisories show separate fixes for `Cookie`, `Proxy-Authorization`, and multiple API surfaces (`fetch()` versus lower-level request/dispatch/stream/pipeline paths), which suggests consumers should be careful about assuming one redirect fix covered the whole package.
- The 2026 advisory cluster is especially concentrated around the WebSocket client and resource handling: parser crashes, permessage-deflate memory exhaustion, invalid compression parameter handling, duplicate `Content-Length` smuggling, and deduplication-buffering DoS all landed in a relatively short window.
- npm registry metadata gathered in this pass shows ongoing parallel maintenance across 6.x, 7.x, and 8.x, with very recent 6.25.0 / 7.25.0 / 8.1.0 publishes. That active maintenance matters because many advisories were backported across branches rather than fixed only in the newest major.
- Upstream `SECURITY.md` points reporters to the Node.js security process, which matches `undici`'s importance as the HTTP client foundation behind Node's modern fetch stack.
- The package's blast radius is materially larger than direct dependency counts suggest because `undici` is used directly by applications, indirectly by tooling, and operationally via Node.js integrations.

## Recommendations for Developers

1. **Prefer a branch at or above `6.24.0` / `7.24.0` / current 8.x** so the dense 2026 advisory cluster is covered.
2. **Treat redirects as a sensitive boundary** and avoid forwarding user-controlled redirect destinations or custom credential-like headers without explicit policy.
3. **Do not pass unsanitized input into low-level request fields** such as headers, `path`, `pathname`, `host`, or `upgrade`; multiple public advisories show that new injection surfaces kept surfacing over time.
4. **Review WebSocket usage separately from plain HTTP usage** because several of the newest and highest-severity records only affect the WebSocket client path.
5. **Be cautious with opt-in features** like deduplication interceptors, decompression, multipart generation, and proxy dispatchers; a meaningful share of the public advisory history lives in those advanced surfaces rather than the simplest request path.

## Dependencies of Note

- `undici` is both a direct npm dependency and part of the broader Node.js HTTP/fetch ecosystem, so the real operational exposure can exceed what a quick `package.json` scan suggests.
- Security fixes are frequently branch-specific; older pinned majors can stay exposed even when the package appears actively maintained overall.

## Open Questions

- Should the KB eventually add a shared pattern note connecting `undici`, `follow-redirects`, `requests`, and `urllib3` around repeated redirect-credential leakage classes?
- Which popular frameworks and tools still pin pre-`6.24.0` or pre-`7.24.0` lines, especially for WebSocket-heavy use cases?
- Is there a public upstream hardening note that more clearly distinguishes safe defaults versus opt-in risky surfaces such as deduplication interceptors and WebSocket compression?

## Related Pages

- [[npm/axios]]
- [[npm/follow-redirects]]
- [[python/requests]]
- [[python/urllib3]]
- [[npm/index]]

---
*Last updated: 2026-04-16 | Sources: 6 (OSV.dev package query for npm/undici, GitHub Advisory Database entries for the published GHSA/CVE set, public CVE records referenced through OSV/GHSA, upstream SECURITY.md, npm registry metadata, npm downloads API)*
