# ws (npm)

**Registry:** npm
**Weekly Downloads:** ~184,200,000 (2026-04-07 to 2026-04-13)
**Repository:** https://github.com/websockets/ws
**Security Contact:** security@3rd-Eden.com
**Disclosure Policy:** https://github.com/websockets/ws/security/policy
**Current Status:** advisory mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-14 | OpenClaw recurring review | package advisory curation | public-source curation (OSV.dev, GitHub Advisory Database, public repository security advisories, upstream release notes, npm registry metadata) | 5 published records mapped; repeated header-parser and resource-exhaustion history confirmed | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-2mhh-w6q8-5hxw / CVE-2016-10518 | Low | A non-Buffer argument to `client.ping()` could cause allocation of a non-zeroed buffer and remote memory disclosure in older releases. | 1.0.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-2mhh-w6q8-5hxw), [1.0.1 release](https://github.com/websockets/ws/releases/tag/1.0.1) |
| GHSA-6663-c963-2gqg / CVE-2016-10542 | High | Older releases did not appropriately limit large incoming websocket payloads, enabling denial of service; public mitigation guidance also points to the `maxPayload` option. | 1.1.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-6663-c963-2gqg) |
| GHSA-5v72-xg48-5rpm | High | A crafted `Sec-WebSocket-Extensions` header using `Object.prototype` property names could crash the server during extension parsing. | 1.1.5 and 3.3.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-5v72-xg48-5rpm), [3.3.1 release](https://github.com/websockets/ws/releases/tag/3.3.1) |
| GHSA-6fc8-4gx4-v693 / CVE-2021-32640 | Moderate | A crafted `Sec-Websocket-Protocol` header could trigger regex-based denial of service; the fix was backported across the 5.x, 6.x, and 7.x lines. | 5.2.3 / 6.2.2 / 7.4.6 | [GitHub Advisory Database](https://github.com/advisories/GHSA-6fc8-4gx4-v693), [7.4.6 release](https://github.com/websockets/ws/releases/tag/7.4.6) |
| GHSA-3h5v-q93c-6h6q / CVE-2024-37890 | High | A request with enough HTTP headers to exceed `server.maxHeadersCount` could crash a `ws` server; the fix was backported across maintained major lines. | 5.2.4 / 6.2.3 / 7.5.10 / 8.17.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-3h5v-q93c-6h6q), [8.17.1 release](https://github.com/websockets/ws/releases/tag/8.17.1) |

## Security Posture Notes

- `ws` has a long public security history, but the pattern is fairly consistent: network-triggerable denial of service and parser-boundary bugs in HTTP upgrade headers or websocket payload handling, rather than a sprawling mix of unrelated vulnerability classes.
- The upstream security-policy page publicly lists a disclosure address and also records a concise timeline of four security events: the 2016 buffer disclosure, the 2017 `Sec-WebSocket-Extensions` DoS, the 2021 `Sec-Websocket-Protocol` ReDoS, and the 2024 header-count crash. That makes the project's public response trail unusually easy to verify.
- Public release and advisory material shows active backporting discipline across older major lines. Both the 2021 ReDoS and 2024 header-count DoS were fixed on several supported branches instead of only in the latest major release.
- The package's operational blast radius is high: npm download data in this review was ~184.2M per week, putting even "just DoS" bugs in a high-impact ecosystem position because `ws` is frequently pulled in transitively by developer tooling and server frameworks.
- npm registry metadata in this pass showed `latest=8.20.0`, which is above all currently published fixed versions captured here.

## Recommendations for Developers

1. **Run a patched line** — at minimum `5.2.4`, `6.2.3`, `7.5.10`, or `8.17.1`, and preferably the current clean latest on your active branch.
2. **Set `maxPayload` explicitly** for production servers so payload-size handling is not left entirely to defaults.
3. **Use Node.js header limits defensively** (`server.maxHeadersCount`, `maxHeaderSize`, and/or `--max-http-header-size`) because multiple public `ws` advisories center on upgrade-header parsing pressure.
4. **Check transitive consumers**, not just direct dependencies — `ws` often arrives through build tooling, test tooling, and higher-level websocket stacks.
5. **Watch upstream security advisories and release notes** if you are pinned to an older major line, since the project has historically shipped targeted backports for security fixes.

## Dependencies of Note

- `ws` is often deployed directly in network-facing services and also transitively through build/dev tooling, which means lagging indirect upgrades can keep old vulnerable major lines alive in practice.
- The package ships optional native performance addons in some environments, but the public vulnerability set gathered in this pass centered on JavaScript parser and resource-handling behavior rather than native-code memory-safety bugs.

## Open Questions

- Has the project published any newer hardening guidance around safe default `maxPayload` sizing for internet-facing deployments beyond the advisory-level workaround text?
- Which large downstream projects still pin the older 5.x–7.x lines, keeping the backport branches operationally important?
- Should the KB eventually add a separate note for high-blast-radius transitive packages like `ws` that are frequently present even when developers never depend on them directly?

## Related Pages

- [[npm/debug]]
- [[npm/express]]
- [[npm/path-to-regexp]]
- [[npm/index]]

---
*Last updated: 2026-04-14 | Sources: 7 (OSV.dev package query for npm/ws, GitHub Advisory Database entries for the published GHSA/CVE set, upstream repository security-policy page, GitHub release notes for 1.0.1 / 3.3.1 / 7.4.6 / 8.17.1, npm registry metadata, npm downloads API)*
