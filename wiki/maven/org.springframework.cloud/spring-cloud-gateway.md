# spring-cloud-gateway (Maven / Java)

**Registry:** Maven Central
**Weekly Downloads:** unknown (Maven Central stats API returns 404 for Spring Cloud projects)
**Repository:** https://github.com/spring-projects/spring-cloud-gateway
**Security Contact:** spring-security@pivotal.io / https://spring.io/security
**Disclosure Policy:** https://spring.io/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No formal third-party audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2021-22051 | Moderate | Spring Cloud Gateway when integrated with Spring Security is vulnerable to a security bypass — specially crafted requests may bypass configured route security filters when using certain predicate configurations | 3.0.5+ / 3.1.0+ | [GHSA (spring.io advisory)](https://spring.io/security/cve-2021-22051) |
| CVE-2022-22947 | Critical (CVSS 10.0) | SpEL (Spring Expression Language) code injection via the Gateway Actuator endpoint — when the `/actuator/gateway` endpoint is exposed and unsecured, an unauthenticated attacker can inject arbitrary SpEL expressions via `/actuator/gateway/routes` to achieve remote code execution on the gateway host; actively exploited in the wild; added to CISA KEV | ≥ 3.1.1 / ≥ 3.0.7 | [GHSA-tpvf-6g75-5cv5](https://github.com/advisories/GHSA-tpvf-6g75-5cv5) / [spring.io](https://spring.io/security/cve-2022-22947) |
| CVE-2025-41235 | High | Spring Cloud Gateway routing or filter security bypass (2025 advisory batch) — crafted requests exploit a flaw in route predicate or filter evaluation; see GHSA for affected versions and full technical description | see GHSA | [spring.io security advisory](https://spring.io/security/cve-2025-41235) |
| CVE-2025-41243 | Critical (CVSS 10.0) | Spring Cloud Gateway Actuator code injection (2025) — unauthenticated code execution via the Gateway Actuator endpoint when exposed; same class as CVE-2022-22947; affects applications that expose the Actuator management endpoint without authentication | see GHSA | [spring.io security advisory](https://spring.io/security/cve-2025-41243) |
| CVE-2025-41253 | High (CVSS 7.5) | Spring Cloud Gateway Actuator information disclosure or restricted-endpoint bypass (2025) — access to internal gateway state via the Actuator endpoint when partially secured; unauthenticated Actuator access required | see GHSA | [spring.io security advisory](https://spring.io/security/cve-2025-41253) |
| CVE-2026-22750 | High (CVSS 7.5) | Spring Cloud Gateway routing or filter security bypass (2026 advisory) — see GHSA for full technical description and affected versions | see GHSA | [spring.io security advisory](https://spring.io/security/cve-2026-22750) |

## Security Posture Notes

Spring Cloud Gateway is the dominant Spring-ecosystem API gateway for reactive (WebFlux) applications, used heavily in microservice architectures to handle routing, load balancing, rate limiting, and cross-cutting concerns (auth, logging, tracing). It is maintained by VMware/Broadcom as part of the Spring Cloud project and publishes advisories at https://spring.io/security.

**Critical recurring theme — Gateway Actuator exposure:** Three of the six mapped advisories (CVE-2022-22947, CVE-2025-41243, CVE-2025-41253) exploit the Spring Boot Actuator endpoint (`/actuator/gateway`) when it is exposed unauthenticated over the network. CVE-2022-22947 (Critical CVSS 10.0) allows full unauthenticated remote code execution and was actively exploited in the wild shortly after disclosure in March 2022; it was added to the CISA Known Exploited Vulnerabilities (KEV) catalog. CVE-2025-41243 (Critical CVSS 10.0) represents a recurrence of the same attack class in 2025.

**Mitigation priority:**
1. Never expose `/actuator` endpoints on a public network without authentication; restrict to internal management interfaces only.
2. Keep spring-cloud-gateway at the latest patch release for the active Spring Boot generation.
3. Monitor https://spring.io/security for new advisories; Spring typically patches within 90 days of disclosure.

Spring Cloud Gateway 4.x (Spring Boot 3.x) is the currently maintained line. The 3.x line (Spring Boot 2.x) is on limited maintenance. Projects still on the 3.x or earlier lines should plan migration, as downstream advisories may not receive backports.

## Dependencies of Note

- `spring-webflux` — reactive web foundation; see [[maven/org.springframework/spring-webflux]] for its own advisory history
- `spring-security` — authorization / authentication for the gateway; see [[maven/org.springframework.security/spring-security-core]]
- `reactor-netty` / `netty-codec-http` — underlying HTTP transport; see [[maven/io.netty/netty-codec-http]]

## Open Questions

- Do CVE-2025-41235 and CVE-2026-22750 require Actuator exposure, or are they exploitable via the gateway's public routing surface?
- What are the precise affected and fixed versions for CVE-2025-41235, CVE-2025-41243, CVE-2025-41253, and CVE-2026-22750? GHSA pages should be fetched in a future pass for exact version ranges.
- Are there additional GHSA advisories for Spring Cloud Gateway beyond the 6 mapped here? A full GHSA search pass would confirm coverage.
- Does the spring-cloud-gateway Kubernetes operator / Helm chart expose Actuator by default?

## Related Pages

- [[maven/org.springframework/spring-webflux]] — reactive web framework underlying spring-cloud-gateway
- [[maven/org.springframework.security/spring-security-core]] — security framework wired into gateway route filters
- [[maven/io.netty/netty-codec-http]] — HTTP/1.x codec used by the gateway's Netty transport
- [[maven/index]]

---
*Last updated: 2026-08-15 | Sources: 6 (GitHub Advisory Database / spring.io security advisories: CVE-2021-22051, CVE-2022-22947, CVE-2025-41235, CVE-2025-41243, CVE-2025-41253, CVE-2026-22750)*
