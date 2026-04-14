# ws (npm)

**Registry:** npm
**Weekly Downloads:** ~184,200,000 (2026-04-07 to 2026-04-13)
**Repository:** https://github.com/websockets/ws
**Security Contact:** security@3rd-Eden.com
**Disclosure Policy:** https://github.com/websockets/ws/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-14 | OpenClaw recurring review | public advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database, upstream SECURITY.md, public release notes) | 5 published records mapped; input-parsing and header-handling surfaces dominate the public history | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-2mhh-w6q8-5hxw / CVE-2016-10518 | Low | Ping / pong payload handling could disclose uninitialized memory and trigger unintended buffer allocation behavior in older releases. | 1.0.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-2mhh-w6q8-5hxw) |
| GHSA-6663-c963-2gqg / CVE-2016-10542 | High | Excessively large WebSocket messages could cause denial of service in older releases. | 1.1.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-6663-c963-2gqg) |
| GHSA-5v72-xg48-5rpm | Moderate | A crafted `Sec-WebSocket-Extensions` header using `Object.prototype` property names could crash a `ws` server. | 1.1.5 / 3.3.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-5v72-xg48-5rpm) |
| GHSA-6fc8-4gx4-v693 / CVE-2021-32640 | Moderate | A specially crafted `Sec-Websocket-Protocol` header could trigger regex-based denial of service during protocol parsing. | 5.2.3 / 6.2.2 / 7.4.6 | [GitHub Advisory Database](https://github.com/advisories/GHSA-6fc8-4gx4-v693) |
| GHSA-3h5v-q93c-6h6q / CVE-2024-37890 | Moderate | Requests with many HTTP headers beyond `server.maxHeadersCount` could crash a `ws` server during upgrade handling. | 5.2.4 / 6.2.3 / 7.5.10 / 8.17.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-3h5v-q93c-6h6q) |

## Security Posture Notes

- `ws` has an unusually explicit public disclosure workflow for a high-volume npm package: upstream `SECURITY.md` lists `security@3rd-Eden.com`, promises acknowledgement within 24 hours, and says confirmed bugs will be published via GitHub Security Advisories.
- The public advisory history is dominated by denial-of-service risk rather than memory corruption or code execution. Four of the five mapped records are DoS issues; one is a low-severity information-disclosure bug from older ping / pong handling.
- The recurring sensitive surface is parsing of untrusted handshake inputs: `Sec-WebSocket-Extensions`, `Sec-Websocket-Protocol`, raw header-count handling during HTTP upgrade, and oversized message handling.
- Public maintainer release notes document practical mitigations for some affected deployments before patching: reducing maximum HTTP header size or adjusting `server.maxHeadersCount` for the 2024 header-count crash, and constraining header size for the 2021 protocol-header ReDoS.
- npm download data in this review (~184.2M weekly downloads) makes `ws` a high-blast-radius package even when published flaws are “only” availability or information-disclosure bugs.
- npm registry metadata in this pass showed `latest=8.20.0`, which is newer than the most recent mapped fix release (`8.17.1`).

## Dependencies of Note

- `ws` is frequently embedded beneath higher-level WebSocket frameworks, dev servers, proxies, and real-time application stacks, so older vulnerable majors can linger transitively even when applications do not depend on it directly.
- Attack preconditions in the public record generally require attacker control over handshake headers or message sizes reaching a live `ws` endpoint.

## Open Questions

- Has the project ever published a formal third-party security audit, or is its public security record driven entirely by advisory-by-advisory disclosures?
- Which popular downstream frameworks or toolchains still pin older `ws` majors affected by the 2021 and 2024 advisories?
- Would a future KB pass benefit from mapping which server defaults in common Node runtimes meaningfully reduce exposure to the header-size and header-count denial-of-service issues?

## Related Pages

- [[npm/index]]
- [[npm/express]]
- [[npm/debug]]
- [[npm/path-to-regexp]]

---
*Last updated: 2026-04-14 | Sources: 6 (OSV.dev package query for npm/ws, GitHub Advisory Database entries, upstream SECURITY.md, public GitHub release notes, npm registry metadata, npm downloads API)*
