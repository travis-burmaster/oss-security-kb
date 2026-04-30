# undici (npm)

**Registry:** npm
**Weekly Downloads:** ~80,083,000 (2026-04-09 to 2026-04-15)
**Repository:** https://github.com/nodejs/undici
**Security Contact:** https://github.com/nodejs/undici/security
**Disclosure Policy:** https://github.com/nodejs/undici/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-16 | OpenClaw recurring review | package advisory curation | public-source curation (OSV.dev, GitHub Advisory Database / public GHSA pages, public CVE aliases, upstream SECURITY.md, npm registry metadata, npm downloads API, local proxy draft assist) | 22 published records mapped; recurring themes were redirect credential leakage, CRLF / request-smuggling style header handling, parser-driven DoS, and newer WebSocket / decompression bugs across maintained major lines | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-1525 / GHSA-2mjp-6q6p-2qxm | Moderate | Duplicate case-variant `Content-Length` headers could reach the wire together, enabling malformed-request handling and request / response smuggling risk in some intermediary-backed deployments. | 6.24.0, 7.24.0 | https://github.com/nodejs/undici/security/advisories/GHSA-2mjp-6q6p-2qxm |
| CVE-2024-24758 / GHSA-3787-6prv-h9w3 | Low | `fetch()` did not clear `Proxy-Authorization` on cross-origin redirects, so sensitive proxy credentials could leak to an unintended destination. | 5.28.3, 6.6.1 | https://github.com/nodejs/undici/security/advisories/GHSA-3787-6prv-h9w3 |
| CVE-2022-31150 / GHSA-3cvr-822r-rqcc | Moderate | Older releases accepted CRLF injection in request headers, allowing header-splicing style abuse when untrusted input reached header construction. | 5.8.0 | https://github.com/nodejs/undici/security/advisories/GHSA-3cvr-822r-rqcc |
| CVE-2024-38372 / GHSA-3g92-w8c5-73pq | Low | Public advisory records describe a data leak when applications called `response.arrayBuffer()` on attacker-influenced responses. | 6.19.2 | https://github.com/nodejs/undici/security/advisories/GHSA-3g92-w8c5-73pq |
| CVE-2026-1527 / GHSA-4992-7rv2-5pvq | Moderate | The `upgrade` option could be abused for CRLF injection, extending the package's long-running header-validation risk pattern. | 6.24.0, 7.24.0 | https://github.com/nodejs/undici/security/advisories/GHSA-4992-7rv2-5pvq |
| CVE-2023-23936 / GHSA-5r9g-qh6m-jxff | Moderate | The public advisory set records CRLF injection through the `Host` / authority handling path until `5.19.1`. | 5.19.1 | https://github.com/nodejs/undici/security/advisories/GHSA-5r9g-qh6m-jxff |
| CVE-2022-35949 / GHSA-8qr4-xgw6-wmr3 | Moderate | `undici.request()` could be turned into SSRF when callers passed an absolute URL through `pathname`, breaking the expected authority boundary. | 5.8.2 | https://github.com/nodejs/undici/security/advisories/GHSA-8qr4-xgw6-wmr3 |
| CVE-2024-24750 / GHSA-9f24-jqhm-jfcw | Moderate | `fetch(url)` could leak memory under attacker-influenced input, creating a denial-of-service path for long-running clients. | 6.6.1 | https://github.com/nodejs/undici/security/advisories/GHSA-9f24-jqhm-jfcw |
| CVE-2024-30261 / GHSA-9qxr-qj54-h672 | Low | `fetch()` integrity handling was too lax when an algorithm was specified with an invalid hash value, so integrity enforcement could fail open in some cases. | 5.28.4, 6.11.1 | https://github.com/nodejs/undici/security/advisories/GHSA-9qxr-qj54-h672 |
| CVE-2025-22150 / GHSA-c76h-2ccp-4975 | Moderate | Insufficient randomness in boundary generation weakened multipart request unpredictability until fixes landed across 5.x, 6.x, and 7.x. | 5.28.5, 6.21.1, 7.2.3 | https://github.com/nodejs/undici/security/advisories/GHSA-c76h-2ccp-4975 |
| CVE-2025-47279 / GHSA-cxrh-j4jr-qwg3 | Low | Malformed certificate data could trigger a denial of service during TLS handling. | 5.29.0, 6.21.2, 7.5.0 | https://github.com/nodejs/undici/security/advisories/GHSA-cxrh-j4jr-qwg3 |
| CVE-2026-1528 / GHSA-f269-vfmq-vjvj | High | A malicious WebSocket frame length could overflow parsing logic and crash the client. | 6.24.0, 7.24.0 | https://github.com/nodejs/undici/security/advisories/GHSA-f269-vfmq-vjvj |
| CVE-2022-35948 / GHSA-f772-66g8-q5h3 | Moderate | Older releases were vulnerable to CRLF injection through `Content-Type`, again showing how sensitive undici's low-level header-construction surface can be. | 5.8.2 | https://github.com/nodejs/undici/security/advisories/GHSA-f772-66g8-q5h3 |
| CVE-2026-22036 / GHSA-g9mf-h72j-4rw9 | Moderate | Public records describe an unbounded decompression chain in HTTP response handling that could drive resource exhaustion through crafted `Content-Encoding` behavior. | 6.23.0, 7.18.2 | https://github.com/nodejs/undici/security/advisories/GHSA-g9mf-h72j-4rw9 |
| CVE-2024-30260 / GHSA-m4v8-wqvr-p9f7 | Low | The non-`fetch()` APIs (`dispatch`, `request`, `stream`, `pipeline`) also failed to clear `Proxy-Authorization` across cross-origin redirects until coordinated fixes landed. | 5.28.4, 6.11.1 | https://github.com/nodejs/undici/security/advisories/GHSA-m4v8-wqvr-p9f7 |
| CVE-2022-32210 / GHSA-pgw7-wx7w-2w33 | High | `ProxyAgent` allowed a man-in-the-middle condition in affected proxy-mediated deployments. | 5.5.1 | https://github.com/nodejs/undici/security/advisories/GHSA-pgw7-wx7w-2w33 |
| CVE-2026-2581 / GHSA-phc3-fgpg-7m6h | Moderate | `DeduplicationHandler` response buffering could grow without bound, enabling memory-consumption denial of service. | 7.24.0 | https://github.com/nodejs/undici/security/advisories/GHSA-phc3-fgpg-7m6h |
| CVE-2022-31151 / GHSA-q768-x9m6-m9qp | Low | Older releases failed to clear `cookie` headers on cross-host / cross-origin redirects, exposing session material to the wrong destination. | 5.8.0 | https://github.com/nodejs/undici/security/advisories/GHSA-q768-x9m6-m9qp |
| CVE-2023-24807 / GHSA-r6ch-mqf9-qc9w | High | Header parsing contained a regular-expression denial-of-service path until `5.19.1`. | 5.19.1 | https://github.com/nodejs/undici/security/advisories/GHSA-r6ch-mqf9-qc9w |
| CVE-2026-2229 / GHSA-v9p9-hfj2-hcw8 | High | Invalid `server_max_window_bits` values could trigger an unhandled exception in the WebSocket client. | 6.24.0, 7.24.0 | https://github.com/nodejs/undici/security/advisories/GHSA-v9p9-hfj2-hcw8 |
| CVE-2026-1526 / GHSA-vrm6-8vpv-qv8q | High | WebSocket `permessage-deflate` decompression could consume unbounded memory when fed malicious compressed input. | 6.24.0, 7.24.0 | https://github.com/nodejs/undici/security/advisories/GHSA-vrm6-8vpv-qv8q |
| CVE-2023-45143 / GHSA-wqq4-5wpv-mx2g | Low | `fetch()` failed to clear `cookie` headers on cross-origin redirects until `5.26.2`, reinforcing the package's repeated redirect-boundary mistakes. | 5.26.2 | https://github.com/nodejs/undici/security/advisories/GHSA-wqq4-5wpv-mx2g |

## Security Posture Notes

- Public evidence shows a broad but coherent vulnerability pattern rather than random one-offs. The biggest recurring themes are **redirect-boundary credential handling**, **header / request-construction validation**, and **resource-exhaustion bugs** in parser, buffering, decompression, and WebSocket code.
- That pattern fits undici's role: it sits very close to the HTTP wire format, proxy handling, and the Node.js `fetch()` compatibility layer, so small implementation mistakes can become protocol-boundary security bugs.
- The package is high-blast-radius infrastructure. Weekly npm downloads in this pass were ~80.1M, and undici also matters beyond direct npm installs because it underpins modern Node.js HTTP client behavior and is closely associated with the platform's `fetch()` stack.
- The advisory trail shows active maintenance across multiple major lines instead of "fix only latest" behavior. Several 2024-2026 records list coordinated fixes for both 5.x/6.x or 6.x/7.x, which is a good signal for downstream users pinned below latest.
- Upstream publishes a `SECURITY.md` and uses GitHub Security Advisories, which gives the package a cleaner public disclosure path than many similarly critical npm transport libraries.
- npm registry metadata gathered in this pass showed `latest=8.1.0`, which is newer than every fixed version in the currently published OSV set captured here.

## Recommendations for Developers

1. **Run 8.1.0 or newer where possible.** That version sits above every fixed release line surfaced in this review.
2. **Treat upgrades as security-sensitive even when the changelog sounds protocol-specific.** For undici, many bugs live in low-level redirect, header, proxy, decompression, and WebSocket behavior that application owners may not realize they depend on.
3. **Be especially careful with user-controlled headers, redirect targets, proxy configuration, and upgrade / WebSocket paths.** Those are the most visibly repeated bug classes in the public advisory set.
4. **Check Node.js runtime exposure, not just direct package.json usage.** Undici is often present indirectly through frameworks, tooling, or platform integrations.
5. **Prioritize memory / resource guards at the application layer** for response buffering, decompression, and WebSocket traffic, because several newer advisories were denial-of-service issues rather than classic input-validation bugs.

## Dependencies of Note

- `undici` is not just another HTTP client dependency; it is part of the modern Node.js transport stack and has a wider ecosystem footprint than direct npm install counts alone suggest.
- Its position near `fetch()`, proxies, HTTP upgrade flows, and WebSockets means downstream risk depends heavily on how wrappers and runtimes expose those features.

## Open Questions

- Which Node.js release lines bundled vulnerable undici snapshots long enough to matter for users who never declared `undici` directly?
- Should the KB eventually track undici separately as both an npm package and a Node runtime component, given the overlap but non-identical upgrade paths?
- Are there additional public maintainer notes or release-post explanations that would sharpen the chronology of the 2026 WebSocket and decompression bug cluster?

## Related Pages

- [[npm/follow-redirects]]
- [[npm/axios]]
- [[python/requests]]
- [[python/urllib3]]
- [[npm/ws]]
- [[npm/index]]

---
*Last updated: 2026-04-16 | Sources: 7 (OSV.dev package query for npm/undici, GitHub Advisory Database / public GHSA pages for 22 published records, public CVE aliases surfaced through OSV, upstream SECURITY.md, npm registry metadata, npm downloads API, local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid)*
