# fastify (npm)

**Registry:** npm
**Weekly Downloads:** ~6,681,120 (2026-04-14 to 2026-04-20)
**Repository:** https://github.com/fastify/fastify
**Security Contact:** GitHub Security Advisories / Fastify Security Team
**Disclosure Policy:** https://github.com/fastify/fastify/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-21 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream release notes, npm registry metadata, npm downloads API, upstream SECURITY.md) | Added a new advisory-mapped baseline page for `fastify`'s published package security history, with especially strong recurring evidence around Content-Type parsing / validation-boundary flaws plus a smaller set of proxy-trust and memory-exhaustion issues. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-33806 / GHSA-247c-9743-5963 | High | Leading whitespace in the `Content-Type` header could bypass body schema validation on affected 5.x versions. Upstream `v5.8.5` was explicitly published as a security release for this issue. | 5.8.5 | https://github.com/advisories/GHSA-247c-9743-5963 |
| CVE-2026-3635 / GHSA-444r-cwp2-x5xf | Moderate | `request.protocol` and `request.host` were spoofable through `X-Forwarded-Proto` / `X-Forwarded-Host` from untrusted connections, creating a proxy-trust boundary problem in code that treats those values as authoritative. Upstream `v5.8.3` was explicitly published as the security release for this issue. | 5.8.3 | https://github.com/advisories/GHSA-444r-cwp2-x5xf |
| CVE-2026-3419 / GHSA-573f-x89g-hqp9 | Moderate | A missing end anchor in `subtypeNameReg` allowed malformed `Content-Type` values to pass validation on affected 5.x versions. | 5.8.1 | https://github.com/advisories/GHSA-573f-x89g-hqp9 |
| CVE-2026-25224 / GHSA-mrq3-vjjr-p77c | Low | `sendWebStream` could allocate memory without an effective bound when handling a malicious stream, allowing denial of service through memory pressure. | 5.7.3 | https://github.com/advisories/GHSA-mrq3-vjjr-p77c |
| CVE-2026-25223 / GHSA-jx2c-rxcm-jvmq | High | A horizontal tab in the `Content-Type` header could bypass body validation logic on vulnerable versions. | 5.7.2 | https://github.com/advisories/GHSA-jx2c-rxcm-jvmq |
| CVE-2025-32442 / GHSA-mg2h-6x62-wpwc | High | Invalid `Content-Type` parsing could let requests reach handlers without the expected body validation. Public OSV data shows a primary 5.x fix in `5.3.2` plus a narrowly affected `4.29.0` follow-on fixed in `4.29.1`. | 5.3.2, 4.29.1 | https://github.com/advisories/GHSA-mg2h-6x62-wpwc |
| CVE-2022-39288 / GHSA-455w-c45v-86rg | High | Malicious `Content-Type` input could trigger denial of service on affected 4.x versions. | 4.8.1 | https://github.com/advisories/GHSA-455w-c45v-86rg |
| CVE-2022-41919 / GHSA-3fjj-p79j-c9hh | Moderate | Incorrect `Content-Type` parsing could create a CSRF-relevant validation mismatch on affected 3.x and 4.x releases. | 4.10.2, 3.29.4 | https://github.com/advisories/GHSA-3fjj-p79j-c9hh |
| CVE-2020-8192 / GHSA-xw5p-hw6r-2j98 | Moderate | A crafted JSON payload could trigger denial of service on vulnerable pre-`2.15.1` versions. | 2.15.1 | https://github.com/advisories/GHSA-xw5p-hw6r-2j98 |
| CVE-2018-3711 / GHSA-mq6c-fh97-4gwv | High | Large JSON payload handling in early releases could cause denial of service through excessive memory consumption. | 0.38.0 | https://github.com/advisories/GHSA-mq6c-fh97-4gwv |

## Security Posture Notes

- `fastify` has a **real and still-active package advisory history**: the public package query used in this pass returned 10 published records spanning 2018 through 2026.
- The clearest recurring theme is **Content-Type parsing and validation-boundary behavior**. A majority of the currently published records are about malformed header parsing, validation bypass, or closely related request-classification problems.
- The release history makes that pattern unusually visible in public. Upstream `v5.7.2` release notes explicitly say parsing of the `Content-Type` header was tightened to a strict RFC 9110 parser, yet additional parsing / validation-bypass issues were still disclosed afterward and fixed in `5.8.1` and `5.8.5`.
- The package also has a smaller but important second theme around **availability and trust boundaries**: older JSON payload denial-of-service issues, the 2026 `sendWebStream` memory-allocation problem, and the 2026 forwarded-header spoofing issue affecting `request.host` / `request.protocol` from untrusted connections.
- Upstream `SECURITY.md` is more informative than many package policies. It explicitly states Fastify's threat model, treats all network input as untrusted, and calls out some non-vulnerability categories such as application code bugs, configuration mistakes, and content-type parser / schema mismatches caused by custom parser configuration.
- Current npm metadata in this pass showed `latest=5.8.5`, and the newest public fix point reviewed here is also `5.8.5`, so **current latest covers the full currently published advisory set gathered in this pass**.

## Recommendations for Developers

1. **Upgrade to `5.8.5` or newer** on the maintained major line if you want coverage for the currently published Fastify package advisories reviewed here.
2. **Treat `Content-Type` handling as a security boundary**, not just a compatibility detail. The public record shows repeated validation-bypass and denial-of-service issues in this area across multiple major lines.
3. **Be conservative with proxy trust settings and any code that relies on `request.host` or `request.protocol`**, especially when requests can arrive from untrusted or partially trusted intermediaries.
4. **Apply practical body-size and stream-handling limits** even on fixed versions; several public issues in this package's history are availability-related rather than classic code-execution bugs.
5. **Read the upstream threat model before filing or triaging Fastify issues internally**, because maintainers explicitly separate framework vulnerabilities from application-level schemas, handler logic, and configuration mistakes.

## Dependencies of Note

- Commonly used as a performance-oriented web framework foundation, so package-level flaws can propagate into API servers, SSR deployments, microservices, and plugin-heavy internal platforms.
- The most security-relevant boundary in the public record is Fastify core request parsing, not a single third-party dependency chain.
- Proxy deployments deserve extra scrutiny because the published 2026 `X-Forwarded-*` spoofing issue shows that application trust in derived request metadata can become security-relevant quickly.

## Open Questions

- Are there maintainer writeups or issue discussions that better explain how the 2025-2026 `Content-Type` fixes relate to one another at the parser-design level, beyond the advisory summaries and release notes?
- Should the KB eventually add a small framework-comparison cluster for request-parsing / trust-boundary issues across Fastify, Express, Flask, and Gin?
- Which still-common downstream templates or starter kits pin Fastify below `5.8.5` in long-lived branches?

## Related Pages

- [[npm/express]]
- [[python/flask]]
- [[go/github.com/gin-gonic/gin]]
- [[npm/index]]

---
*Last updated: 2026-04-21 | Sources: 9 (OSV.dev package query for npm/fastify, 10 OSV / GHSA vulnerability records, GitHub Advisory Database / upstream GitHub security advisories, public CVE records, upstream release notes for v5.7.2, v5.8.3, and v5.8.5, upstream SECURITY.md, npm registry metadata, npm downloads API)*
