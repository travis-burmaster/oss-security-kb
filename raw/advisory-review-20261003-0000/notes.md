# Advisory Review Pass — 2026-10-03 00:00 UTC

## Pass Summary
- Target: kubernetes/prometheus (new advisory-mapped page)
- Secondary: master index kubernetes section correction (10 stale → 14 correct)
- OSV.dev: blocked (HTTP 403) — bypassed per CLAUDE.md fallback procedure

## Sources Consulted

### mcp__github__search_code — github/advisory-database
Query: `repo:github/advisory-database "prometheus/prometheus" GHSA path:advisories`
Total results: 6 advisories (5 valid + 1 withdrawn)

Results:
- GHSA-4v48-4q5m-8vx4 (2022-12)
- GHSA-vffh-x6r8-xx99 (2026-04)
- GHSA-fw8g-cg8f-9j28 (2026-05)
- GHSA-8rm2-7qqf-34qm (2026-05)
- GHSA-wg65-39gg-5wfj (2026-05)
- GHSA-3m87-5598-2v4f (2023-12, WITHDRAWN)

### Advisory JSON fetched via WebFetch (raw.githubusercontent.com)

1. GHSA-4v48-4q5m-8vx4
   URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/12/GHSA-4v48-4q5m-8vx4/GHSA-4v48-4q5m-8vx4.json
   Severity: High CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H (7.2)
   CVE: none assigned
   Summary: Basic auth bypass via bcrypt hash cache poisoning in exporter-toolkit
   Affected: github.com/prometheus/prometheus 2.24.1–2.40.3
   Fixed: 2.37.4 (LTS) / 2.40.4
   Published: 2022-12-05

2. GHSA-vffh-x6r8-xx99
   URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/04/GHSA-vffh-x6r8-xx99/GHSA-vffh-x6r8-xx99.json
   CVE: CVE-2026-40179
   Severity: Moderate CVSS 5.4
   Summary: Stored XSS in web UI tooltip rendering and metrics explorer (innerHTML injection)
   Affected: github.com/prometheus/prometheus 3.0.0–3.11.1
   Fixed: 3.5.2 LTS / 3.11.2
   Published: 2026-04-13

3. GHSA-fw8g-cg8f-9j28
   URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/05/GHSA-fw8g-cg8f-9j28/GHSA-fw8g-cg8f-9j28.json
   CVE: CVE-2026-44903
   Severity: Moderate CVSS 5.4
   Summary: Stored XSS in legacy UI histogram heatmap via unescaped le label values
   Affected: github.com/prometheus/prometheus (old-ui feature flag)
   Fixed: 3.11.3 / 3.5.3 LTS
   Published: 2026-05-05

4. GHSA-8rm2-7qqf-34qm
   URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/05/GHSA-8rm2-7qqf-34qm/GHSA-8rm2-7qqf-34qm.json
   CVE: CVE-2026-42154
   Severity: High CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H (7.5)
   Summary: Pre-auth remote read OOM via unvalidated snappy decompression declared length
   Affected: github.com/prometheus/prometheus remote read endpoint
   Fixed: 3.11.3 / 3.5.3 LTS
   Published: 2026-05-05

5. GHSA-wg65-39gg-5wfj
   URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/05/GHSA-wg65-39gg-5wfj/GHSA-wg65-39gg-5wfj.json
   CVE: CVE-2026-42151
   Severity: High CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N (7.5)
   Summary: Azure AD remote write ClientSecret exposed unredacted via /-/config endpoint
   Affected: github.com/prometheus/prometheus Azure AD remote write configs
   Fixed: 3.11.3 / 3.5.3 LTS
   Published: 2026-05-05

6. GHSA-3m87-5598-2v4f
   URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/12/GHSA-3m87-5598-2v4f/GHSA-3m87-5598-2v4f.json
   CVE: CVE-2019-3826
   Status: WITHDRAWN 2023-12-18 — advisory determined inapplicable to the Go package
   Action: Excluded from vulnerability table; noted in page

### GitHub Repository Metadata
Tool: mcp__github__search_repositories
Repo: prometheus/prometheus
Stars: 66,345 | Forks: 10,885
Updated: 2026-10-03
Latest release (via WebFetch api.github.com): v3.15.0 (2026-09-25)

### Master Index Correction
Tool: Bash ls /home/user/oss-security-kb/wiki/kubernetes/
Actual pages (13, excluding index.md):
  argo-cd.md, cert-manager.md, cilium.md, containerd.md, coredns.md,
  flux2.md, helm.md, ingress-nginx.md, kube-apiserver.md,
  kube-controller-manager.md, kube-proxy.md, kubelet.md, runc.md

Master index previously stated 10 with 4 phantoms (etcd, open-policy-agent, falco, trivy)
and 7 missing real pages (coredns, containerd, kube-controller-manager, kube-proxy,
kubelet, runc, cilium) plus 2 wrong-name entries (kubernetes→kube-apiserver, flux→flux2).
All corrected; prometheus added as 14th page.

## Files Changed
- wiki/kubernetes/prometheus.md (new)
- wiki/kubernetes/index.md (prometheus entry added)
- wiki/index.md (kubernetes section corrected 10→14; total 305→309)
- wiki/log.md (entry prepended)
- raw/advisory-review-20261003-0000/notes.md (this file, new)
