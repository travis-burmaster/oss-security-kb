# axios (npm)

**Registry:** npm
**Weekly Downloads:** ~97,700,000 (2026-04-05 to 2026-04-11)
**Repository:** https://github.com/axios/axios
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-12 | OpenClaw recurring review | public advisory refresh | public-source curation (OSV.dev, GitHub Advisory Database, public maintainer postmortem, npm registry metadata) | 12 published records mapped, including 1 malicious publish record and a broader SSRF / DoS / CSRF / ReDoS history | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-42xw-2xvc-qx8m / CVE-2019-10742 | High | Axios had a denial-of-service issue in older releases. | 0.18.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-42xw-2xvc-qx8m) |
| GHSA-4w2v-q235-vp99 / CVE-2020-28168 | High | Server-side request forgery in older request handling. | 0.21.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-4w2v-q235-vp99) |
| GHSA-cph5-m8f7-6c5x / CVE-2021-3749 | Moderate | Inefficient regular-expression handling could enable ReDoS. | 0.21.2 | [GitHub Advisory Database](https://github.com/advisories/GHSA-cph5-m8f7-6c5x) |
| GHSA-wf5p-g6vw-rhxx / CVE-2023-45857 | Moderate | Cross-site request forgery behavior in affected 1.x releases. | 1.6.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-wf5p-g6vw-rhxx) |
| GHSA-8hc4-vh64-cxmj / CVE-2024-39338 | High | SSRF in affected 1.x releases. | 1.7.4 | [GitHub Advisory Database](https://github.com/advisories/GHSA-8hc4-vh64-cxmj) |
| GHSA-jr5f-v2jv-69x6 / CVE-2025-27152 | High | Absolute URLs could bypass `baseURL` expectations, leading to SSRF and credential leakage in affected call patterns. | 1.8.2 | [GitHub Advisory Database](https://github.com/advisories/GHSA-jr5f-v2jv-69x6) |
| GHSA-4hjh-wcwx-xvwj / CVE-2025-58754 | Moderate | Lack of a data-size check could enable denial of service. | 1.12.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-4hjh-wcwx-xvwj) |
| GHSA-3p68-rc4w-qgx5 / CVE-2025-62718 | High | `NO_PROXY` hostname normalization mistakes could let loopback / internal destinations be sent through a configured proxy unexpectedly, undermining SSRF defenses. | 1.15.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-3p68-rc4w-qgx5) |
| GHSA-qj83-cq47-w5f8 / CVE-2026-39865 | High | HTTP/2 session cleanup state corruption vulnerability. | 1.13.2 | [GitHub Advisory Database](https://github.com/advisories/GHSA-qj83-cq47-w5f8) |
| GHSA-fvcv-3m26-pcqx / CVE-2026-40175 | Critical | Header-injection behavior in affected versions could be used in a cloud-metadata exfiltration chain when combined with prototype pollution elsewhere in the stack. | 1.15.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-fvcv-3m26-pcqx) |
| GHSA-43fc-jf86-j433 / CVE-2026-25639 | Moderate | A `__proto__` key in `mergeConfig` could trigger denial of service in affected 1.x releases. | 1.13.5 | [GitHub Advisory Database](https://github.com/advisories/GHSA-43fc-jf86-j433) |
| GHSA-fw8c-xr5c-95f9 / MAL-2026-2307 | Critical | Malicious npm publishes of `axios` 1.14.1 and 0.30.4 injected `plain-crypto-js@4.2.1`, with public postmortem material saying the versions were live for about 3 hours before removal. GitHub's malware advisory warns any machine that installed or ran them should be treated as fully compromised. | No patched version for the malicious builds; avoid 1.14.1 and 0.30.4, treat 1.14.0 / 0.30.3 as known-clean rollback targets, and prefer current clean releases such as 1.15.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-fw8c-xr5c-95f9) |

## Security Posture Notes

- Axios has a substantial public advisory history spanning classic library flaws and one major supply-chain incident: SSRF, proxy / URL-handling mistakes, denial of service, ReDoS, CSRF-style request handling issues, HTTP/2 state corruption, and the March 2026 malicious publish event.
- The public record shows SSRF-adjacent behavior recurring across multiple years: older SSRF in 0.x, absolute-URL / `baseURL` credential leakage in 1.8.2, and later `NO_PROXY` normalization mistakes fixed in 1.15.0. That makes outbound-request policy and URL construction the package's clearest long-term risk theme.
- The March 2026 malicious publish stands apart from normal code defects. Public maintainer postmortem material says compromised versions `1.14.1` and `0.30.4` injected `plain-crypto-js@4.2.1`, were available for about 3 hours, and should be treated as host-compromise events rather than ordinary vulnerable versions.
- Public remediation guidance around the malicious publish is unusually strong: GitHub's advisory says affected machines should be considered fully compromised and secrets should be rotated from a different machine; the maintainer postmortem additionally points defenders at `sfrclak.com` and `142.11.206.73` as indicators mentioned during response.
- Axios's blast radius is unusually large because the package remains one of npm's most widely downloaded HTTP clients (~97.7M weekly downloads in this pass), so even narrowly scoped request-handling flaws can have broad downstream impact.
- npm registry metadata in this review showed `latest=1.15.0`, which clears the currently published advisory set captured here.

## Dependencies of Note

- `plain-crypto-js@4.2.1` was the malicious dependency injected into the compromised 2026 npm publishes.
- Because multiple public advisories center on URL parsing, proxy handling, headers, and config merge behavior, downstream applications should also treat adjacent config-merging and prototype-pollution gadgets in their own stacks as part of the practical exposure picture.

## Open Questions

- Has axios published a formal SECURITY.md or disclosure workflow since the March 2026 compromise, beyond the public postmortem issue?
- Which of axios's newer request-routing and proxy-hardening changes were driven by independent bug reports versus follow-on fixes after earlier SSRF findings?
- Should a future KB pass separate traditional code vulnerabilities from supply-chain incidents into different subsections for high-volume packages like axios?

## Related Pages

- [[npm/index]]
- [[npm/express]]
- [[python/requests]]
- [[python/urllib3]]

---
*Last updated: 2026-04-12 | Sources: 7 (OSV.dev package query for npm/axios, GitHub Advisory Database entries for the published GHSA/CVE set, axios maintainer postmortem issue on the March 2026 compromise, npm registry metadata, npm downloads API)*
