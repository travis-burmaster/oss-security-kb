# prometheus (kubernetes)

**Registry:** k8s
**Weekly Downloads:** unknown (binary/Docker distribution; ~66,345 GitHub stars as of 2026-10-03)
**Repository:** https://github.com/prometheus/prometheus
**Security Contact:** https://github.com/prometheus/prometheus/security/advisories
**Disclosure Policy:** https://github.com/prometheus/prometheus/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-10-03 | OSS Security KB (automated pass) | GHSA advisory database search — `prometheus/prometheus` Go package | advisory-mapping | 5 confirmed advisories (1 withdrawn excluded) | raw/advisory-review-20261003-0000/notes.md |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-4v48-4q5m-8vx4 | High CVSS 7.2 | Basic auth bypass via bcrypt hash cache poisoning in exporter-toolkit — an attacker who obtains the stored hashed password can forge a request to poison the computation cache, making subsequent requests authenticate successfully without the real password | 2.37.4 (LTS) / 2.40.4 | [GHSA-4v48-4q5m-8vx4](https://github.com/advisories/GHSA-4v48-4q5m-8vx4) |
| CVE-2026-40179 / GHSA-vffh-x6r8-xx99 | Moderate CVSS 5.4 | Stored XSS in web UI tooltip rendering and metrics explorer — metric names containing HTML/JavaScript are injected into `innerHTML` without escaping in both the Mantine and legacy React interfaces; an attacker with write access to a scraped target, remote write endpoint, or OTLP receiver can inject metric names that execute arbitrary JavaScript in users' browsers | 3.5.2 (LTS) / 3.11.2 | [GHSA-vffh-x6r8-xx99](https://github.com/advisories/GHSA-vffh-x6r8-xx99) |
| CVE-2026-44903 / GHSA-fw8g-cg8f-9j28 | Moderate CVSS 5.4 | Stored XSS in legacy UI histogram heatmap — when `--enable-feature=old-ui` is set, `le` label values used as axis tick marks are not HTML-escaped; same injection surface as CVE-2026-40179 (compromised scrape target, remote write, OTLP receiver) | 3.11.3 / 3.5.3 (LTS) | [GHSA-fw8g-cg8f-9j28](https://github.com/advisories/GHSA-fw8g-cg8f-9j28) |
| CVE-2026-42154 / GHSA-8rm2-7qqf-34qm | High CVSS 7.5 AV:N/AC:L/PR:N | Pre-auth remote read OOM — the `/api/v1/read` endpoint does not validate the declared decompressed length in snappy-compressed payloads before allocating memory; an unauthenticated attacker can trigger multi-GiB heap allocations with small requests, crashing the process under concurrent load; workaround: restrict the remote read endpoint with a reverse proxy or firewall | 3.11.3 / 3.5.3 (LTS) | [GHSA-8rm2-7qqf-34qm](https://github.com/advisories/GHSA-8rm2-7qqf-34qm) |
| CVE-2026-42151 / GHSA-wg65-39gg-5wfj | High CVSS 7.5 AV:N/AC:L/PR:N/C:H | Azure AD remote write credential exposure — the `ClientSecret` field in Azure AD remote write configuration was typed as a plain string rather than a `Secret` type, causing credentials to be returned unredacted via the `/-/config` HTTP endpoint to any user who can reach it; workaround: switch to Managed Identity or Workload Identity authentication | 3.11.3 / 3.5.3 (LTS) | [GHSA-wg65-39gg-5wfj](https://github.com/advisories/GHSA-wg65-39gg-5wfj) |

*GHSA-3m87-5598-2v4f (CVE-2019-3826, originally described as stored DOM XSS < 2.7.1) was withdrawn 2023-12-18 — advisory determined inapplicable to the Go package.*

## Security Posture Notes

Prometheus is a CNCF-graduated open-source monitoring and alerting platform, universally deployed in Kubernetes clusters (typically via the `kube-prometheus-stack` Helm chart, which also installs Alertmanager, Grafana, and node-exporter). Written in Go; maintained by the Prometheus Authors under Apache-2.0 / MIT licensing. Latest stable: v3.15.0 (September 2026); current LTS line: v3.5.x.

Security disclosures go via GitHub private security advisories. CNCF security governance at https://github.com/cncf/sig-security. The project has a documented SECURITY.md and participates in coordinated disclosure.

**Advisory pattern:** Three primary vulnerability classes:

1. **Authentication and credential boundary failures** — GHSA-4v48-4q5m-8vx4 (2022: bcrypt hash cache poisoning enabling basic-auth bypass) and CVE-2026-42151 (2026: Azure AD ClientSecret exposed in config API) both reflect seams between Prometheus's integration with external auth systems and its internal credential handling. The `/-/config` endpoint is a recurring exposure point.

2. **Stored XSS via metric name injection** — CVE-2026-40179 and CVE-2026-44903 (May 2026 cluster) demonstrate that metric names flow from external sources (scrape targets, remote write) into web UI rendering without sanitization. This is an inherent threat model risk: any compromised scrape target can inject UI-visible strings.

3. **Pre-auth denial of service on data ingestion endpoints** — CVE-2026-42154 (remote read OOM) follows a common pattern where Prometheus's data-plane endpoints (remote write, remote read, OTLP) lack input length validation. The remote read endpoint is frequently exposed without authentication in internal deployments.

**Operator guidance:** The `/-/config`, `/api/v1/read`, and similar admin endpoints should be firewalled or protected with a reverse proxy + authentication layer even on internal-only deployments. Azure AD remote write users should upgrade to 3.5.3 LTS / 3.11.3 immediately.

## Dependencies of Note

- `github.com/prometheus/exporter-toolkit` — HTTP/TLS/basic-auth layer for the Prometheus binary; GHSA-4v48-4q5m-8vx4 originated here. Any Prometheus exporter embedding exporter-toolkit shares this attack surface.
- `golang.org/x/net` — foundational HTTP/2 and networking layer; see [[go/golang.org-x-net]] for HTTP/2 DoS history.
- `github.com/klauspost/compress` (snappy) — decompression library relevant to CVE-2026-42154 input length validation flaw.

## Open Questions

- The GHSA search returned 6 total results (5 valid + 1 withdrawn); earlier pre-GHSA CVEs (particularly pre-2022) may not be fully captured. A broader CVE database search against `prometheus/prometheus` should be conducted in a future pass.
- Client libraries (client_golang, client_python, client_java, client_ruby) maintain separate advisory histories — see [[go/github.com/prometheus/client_golang]].
- The remote read OOM (CVE-2026-42154) may affect Thanos, VictoriaMetrics, or Cortex when using Prometheus-compatible remote read; this should be checked in a future pass.
- Alertmanager (github.com/prometheus/alertmanager) has its own advisory history not captured here.

## Related Pages

- [[go/github.com/prometheus/client_golang]]
- [[kubernetes/index]]

---
*Last updated: 2026-10-03 | Sources: 5 GHSA advisories (github/advisory-database) + GitHub repository metadata*
