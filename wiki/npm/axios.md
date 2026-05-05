# axios (npm)

**Registry:** npm
**Weekly Downloads:** ~98,174,477 (last-week npm downloads API snapshot saved 2026-05-05)
**Repository:** https://github.com/axios/axios
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-05 | OpenClaw recurring review | public advisory refresh | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database links, public CVE aliases, npm registry/download metadata, local proxy synthesis used only as a drafting aid) | Refreshed axios to 25 public OSV/GHSA records, adding the May 2026 cluster around prototype-pollution gadgets, proxy bypasses, streamed size-limit bypasses, CRLF/null-byte injection, and form-data recursion DoS. | `raw/advisory-review-20260505-1439/` |
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
| GHSA-3p68-rc4w-qgx5 / CVE-2025-62718 | High | `NO_PROXY` hostname normalization mistakes could let `localhost.` (trailing dot) or IPv6 literals like `[::1]` skip NO_PROXY matching and go through the configured proxy unexpectedly, undermining SSRF defenses. | 1.15.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-3p68-rc4w-qgx5) |
| GHSA-qj83-cq47-w5f8 / CVE-2026-39865 | High | HTTP/2 session cleanup state corruption vulnerability. | 1.13.2 | [GitHub Advisory Database](https://github.com/advisories/GHSA-qj83-cq47-w5f8) |
| GHSA-fvcv-3m26-pcqx / CVE-2026-40175 | Critical | Axios did not sanitize CRLF (`\r\n`) in header values; when combined with prototype pollution elsewhere, polluted properties could be merged into headers and used for header injection / request smuggling chains (including cloud-metadata exfiltration scenarios). | 1.15.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-fvcv-3m26-pcqx) |
| GHSA-43fc-jf86-j433 / CVE-2026-25639 | Moderate | A `__proto__` key in `mergeConfig` could trigger denial of service in affected 1.x releases. | 1.13.5 | [GitHub Advisory Database](https://github.com/advisories/GHSA-43fc-jf86-j433) |
| GHSA-fw8c-xr5c-95f9 / MAL-2026-2307 | Critical | Malicious npm publishes of `axios` 1.14.1 and 0.30.4 injected `plain-crypto-js@4.2.1`, with public postmortem material saying the versions were live for about 3 hours before removal. GitHub's malware advisory warns any machine that installed or ran them should be treated as fully compromised. | No patched version for the malicious builds; avoid 1.14.1 and 0.30.4, treat 1.14.0 / 0.30.3 as known-clean rollback targets, and prefer current clean releases such as 1.16.0 | [GitHub Advisory Database](https://github.com/advisories/GHSA-fw8c-xr5c-95f9) |
| GHSA-pf86-5x62-jrwf / CVE-2026-42033 | High | Prototype-pollution read-side gadgets could affect response tampering, data exfiltration, and request hijacking paths in affected 1.x / 0.x releases. | 1.15.1 / 0.31.1 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-pf86-5x62-jrwf) |
| GHSA-5c9x-8gcm-mpgx / CVE-2026-42034 | Moderate | HTTP adapter streamed uploads could bypass `maxBodyLength` when `maxRedirects: 0`, weakening upload-size controls. | 1.15.1 / 0.31.1 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-5c9x-8gcm-mpgx) |
| GHSA-6chq-wfr3-2hj9 / CVE-2026-42035 | High | Prototype-pollution gadget path could lead to header injection in affected releases. | 1.15.1 / 0.31.1 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-6chq-wfr3-2hj9) |
| GHSA-vf2m-468p-8v99 / CVE-2026-42036 | Moderate | HTTP adapter streamed responses could bypass `maxContentLength`, weakening response-size controls. | 1.15.1 / 0.31.1 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-vf2m-468p-8v99) |
| GHSA-445q-vr5w-6q77 / CVE-2026-42037 | Moderate | Multipart/form-data streaming could allow CRLF injection through unsanitized `Blob.type` metadata. | 1.15.1 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-445q-vr5w-6q77) |
| GHSA-m7pr-hjqh-92cm / CVE-2026-42038 | Moderate | `no_proxy` matching could be bypassed with IP alias forms, creating an SSRF-relevant proxy-boundary issue. | 1.15.1 / 0.31.1 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-m7pr-hjqh-92cm) |
| GHSA-62hf-57xw-28j9 / CVE-2026-42039 | Moderate | Deeply nested request data passed to `toFormData` could trigger unbounded recursion and denial of service. | 1.15.1 / 0.31.1 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-62hf-57xw-28j9) |
| GHSA-xhjh-pmcv-23jw / CVE-2026-42040 | Low | Reverse-encoding behavior in `AxiosURLSearchParams` could produce a null-byte injection issue. | 1.15.1 / 0.31.1 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-xhjh-pmcv-23jw) |
| GHSA-w9j2-pvgh-6h63 / CVE-2026-42041 | Moderate | Prototype-pollution gadget in `validateStatus` merge behavior could affect status-based authentication or authorization checks. | 1.15.1 / 0.31.1 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-w9j2-pvgh-6h63) |
| GHSA-xx6v-rp6x-q39c / CVE-2026-42042 | Moderate | Prototype-pollution gadget in `withXSRFToken` boolean coercion could leak XSRF tokens cross-origin in affected call patterns. | 1.15.1 / 0.31.1 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-xx6v-rp6x-q39c) |
| GHSA-pmwg-cvhr-8vh7 / CVE-2026-42043 | High | Incomplete `NO_PROXY` fix for CVE-2025-62718 allowed bypass through RFC 1122 loopback subnet forms such as 127.0.0.0/8. | 1.15.1 / 0.31.1 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-pmwg-cvhr-8vh7) |
| GHSA-3w6x-2g7m-8v23 / CVE-2026-42044 | Moderate | Prototype-pollution gadget in `parseReviver` could enable invisible JSON response tampering. | 1.15.2 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-3w6x-2g7m-8v23) |
| GHSA-q8qp-cvcw-x6jj / CVE-2026-42264 | High | Prototype-pollution read-side gadgets in the HTTP adapter could allow credential injection and request hijacking. | 1.15.2 | [GitHub Advisory Database](https://github.com/axios/axios/security/advisories/GHSA-q8qp-cvcw-x6jj) |

## Security Posture Notes

- Axios has a substantial public advisory history spanning classic library flaws and one major supply-chain incident: SSRF, proxy / URL-handling mistakes, denial of service, ReDoS, CSRF-style request handling issues, HTTP/2 state corruption, prototype-pollution gadget chains, streamed size-limit bypasses, form-data / URL encoding injection, and the March 2026 malicious publish event.
- The public record shows SSRF-adjacent behavior recurring across multiple years: older SSRF in 0.x, absolute-URL / `baseURL` credential leakage in 1.8.2, `NO_PROXY` normalization mistakes fixed in 1.15.0, and the May 2026 follow-on IP-alias / loopback-subnet bypasses fixed in 1.15.1 / 0.31.1. That makes outbound-request policy and URL construction one of the package's clearest long-term risk themes.
- The March 2026 malicious publish stands apart from normal code defects. Public maintainer postmortem material says compromised versions `1.14.1` and `0.30.4` injected `plain-crypto-js@4.2.1`, were available for about 3 hours, and should be treated as host-compromise events rather than ordinary vulnerable versions.
- The May 2026 advisory cluster also shows that axios can become a gadget surface when applications have prototype pollution elsewhere: several records describe polluted properties influencing headers, credentials, XSRF-token behavior, JSON response parsing, or status validation.
- Public remediation guidance around the malicious publish is unusually strong: GitHub's advisory says affected machines should be considered fully compromised and secrets should be rotated from a different machine; the maintainer postmortem additionally points defenders at `sfrclak.com` and `142.11.206.73` as indicators mentioned during response.
- Axios's blast radius is unusually large because the package remains one of npm's most widely downloaded HTTP clients (~97.7M weekly downloads in this pass), so even narrowly scoped request-handling flaws can have broad downstream impact.
- npm registry metadata in this review showed `latest=1.16.0`, which is newer than the currently published fixed versions captured here.

## Dependencies of Note

- `plain-crypto-js@4.2.1` was the malicious dependency injected into the compromised 2026 npm publishes.
- Because multiple public advisories center on URL parsing, proxy handling, headers, config merge behavior, and prototype-pollution read-side gadgets, downstream applications should also treat adjacent config-merging and prototype-pollution bugs in their own stacks as part of the practical exposure picture.

## Open Questions

- Has axios published a formal SECURITY.md or disclosure workflow since the March 2026 compromise, beyond the public postmortem issue?
- Which of axios's newer request-routing and proxy-hardening changes were driven by independent bug reports versus follow-on fixes after earlier SSRF findings?
- Should a future KB pass split axios into thematic subsections (SSRF/proxy, prototype-pollution gadgets, size-limit/DoS, injection, supply-chain incident) so the table remains readable as public records continue to grow?

## Related Pages

- [[npm/index]]
- [[npm/express]]
- [[python/requests]]
- [[python/urllib3]]

---
*Last updated: 2026-05-05 | Sources: 7 (OSV.dev package query and vulnerability records for npm/axios, GitHub Advisory Database entries linked from OSV, public CVE/NVD aliases referenced by OSV/GHSA records, axios maintainer postmortem issue on the March 2026 compromise, npm registry metadata, npm downloads API, local Claude-compatible proxy synthesis saved under `raw/advisory-review-20260505-1439/` and used only as a drafting aid)*
