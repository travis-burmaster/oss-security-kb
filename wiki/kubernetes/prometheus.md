# Prometheus (Kubernetes / monitoring)

**Registry:** Docker Hub (`prom/prometheus`), Helm (`prometheus-community/prometheus`)
**Weekly Downloads:** unknown (container image + binary; GitHub stars: ~57,000+)
**Repository:** https://github.com/prometheus/prometheus
**Security Contact:** https://github.com/prometheus/prometheus/security/advisories
**Disclosure Policy:** https://github.com/prometheus/.github/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-09-17 | oss-security-kb nightly | advisory-review 2022–2026 | advisory-mapping (GHSA) | 5 confirmed GHSA advisories (1 withdrawn excluded) | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-4v48-4q5m-8vx4 | High (CVSS 8.8) | Basic authentication bypass via bcrypt cache poisoning — an attacker with access to the hashed password file can forge requests by exploiting a hash-computation cache that stores results keyed only on the input, not the stored hash; allows authentication with a different password that produces a cached hit | 2.37.4 / 2.40.4 | [GHSA-4v48-4q5m-8vx4](https://github.com/advisories/GHSA-4v48-4q5m-8vx4) |
| CVE-2026-42154 | High (CVSS 7.5) | Remote read `/api/v1/read` endpoint does not validate the snappy-encoded body before allocating memory — unauthenticated DoS via compact payloads that trigger unbounded heap allocation; no size check before decompression | 3.11.3 / 3.5.3 LTS | [GHSA-8rm2-7qqf-34qm](https://github.com/advisories/GHSA-8rm2-7qqf-34qm) |
| CVE-2026-42151 | High | Azure AD OAuth `client_secret` exposed in plaintext via `/-/config` API — the configuration field uses plain `string` type instead of a protected secret type, exposing credentials to anyone with read access to the config endpoint | 3.11.3 / 3.5.3 LTS | [GHSA-wg65-39gg-5wfj](https://github.com/advisories/GHSA-wg65-39gg-5wfj) |
| CVE-2026-40179 | Moderate (CVSS 5.4) | Stored XSS in new web UI — metric names and label values injected into `innerHTML` without escaping in chart tooltip rendering; exploitable via a compromised scrape target that returns malicious metric names or label values | 3.5.2 LTS / 3.11.2 | [GHSA-vffh-x6r8-xx99](https://github.com/advisories/GHSA-vffh-x6r8-xx99) |
| CVE-2026-44903 | Moderate (CVSS 5.4) | Stored XSS in old UI (`--enable-feature=old-ui`) — histogram heatmap renders `le` label values in HTML axis tick marks without sanitization; exploitable via a scrape target injecting JavaScript in label values | see GHSA | [GHSA-fw8g-cg8f-9j28](https://github.com/advisories/GHSA-fw8g-cg8f-9j28) |

*Note: GHSA-3m87-5598-2v4f (CVE-2019-3826 — Cross-Site Scripting in Console pages) is withdrawn and excluded from the table above.*

## Security Posture Notes

Prometheus is CNCF-graduated and deployed in the majority of production Kubernetes clusters, typically via the `kube-prometheus-stack` Helm chart. The advisory history through 2026 shows two primary risk areas: API/endpoint exposure (the `/api/v1/read` memory-exhaustion DoS and the `/-/config` credential leak are the highest-severity) and XSS in the built-in web UI (two stored-XSS findings, both requiring a compromised or malicious scrape target to inject payloads via metric names or label values).

The bcrypt cache-poisoning authentication bypass (GHSA-4v48-4q5m-8vx4) is operationally significant: Prometheus's built-in basic-auth is often used as a lightweight access control layer; operators relying on it should verify they are running ≥ 2.37.4 or ≥ 2.40.4.

The `/-/config` API credential exposure (CVE-2026-42151) affects deployments using Azure AD OAuth. The `/-/config` and `/-/flags` endpoints are accessible to any user with read access to the Prometheus UI; Prometheus should not be internet-exposed without a reverse proxy enforcing authentication.

Long-term support (LTS) branches (currently 3.5.x LTS) receive security backports for approximately 12 months.

## Dependencies of Note

- **prometheus/client_golang** — Go instrumentation library used by nearly all Go services that expose Prometheus metrics; see [[go/github.com/prometheus/client_golang]] for its own advisory (promhttp cardinality DoS)
- **Alertmanager** — companion CNCF component receiving alerts from Prometheus; has its own GHSA advisory history not covered in this page
- **kube-prometheus-stack** — community Helm chart bundling Prometheus + Grafana + Alertmanager + exporters; chart-level version lag can leave components unpatched despite upstream fixes

## Open Questions

- Prometheus 2.x (non-LTS) reached end of support in 2025; operators on 2.x should migrate to 3.x or the 3.5.x LTS branch.
- Grafana, which commonly fronts Prometheus, has its own substantial GHSA advisory history not reviewed in this pass.
- The `--enable-feature=old-ui` flag is deprecated; CVE-2026-44903 provides additional motivation to ensure it is not enabled in production.

## Related Pages

- [[go/github.com/prometheus/client_golang]] — Prometheus Go instrumentation library
- [[kubernetes/kube-apiserver]] — Kubernetes API server metrics endpoint commonly scraped by Prometheus
- [[kubernetes/cert-manager]] — frequently deployed alongside kube-prometheus-stack
