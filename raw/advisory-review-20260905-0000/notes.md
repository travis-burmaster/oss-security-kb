# Advisory Review Notes — 2026-09-05

## Session metadata
Date: 2026-09-05 | Ecosystem targets: Kubernetes | OSV.dev: blocked (HTTP 403)

## Sources consulted
- github/advisory-database (via mcp__github__search_code + WebFetch on raw.githubusercontent.com)
- api.github.com/repos/cilium/cilium (repo metadata, stars, latest release)
- api.github.com/repos/fluxcd/flux2 (repo metadata, stars, latest release)
- pkg.go.dev/github.com/cilium/cilium (module info)

## Search queries
- `cilium repo:github/advisory-database language:json` → 49 total results
- `fluxcd repo:github/advisory-database language:json` → 11 total results
- `spf13/cobra repo:github/advisory-database language:json` → 0 results (ruled out as target)

## Target selection
1. **kubernetes/cilium** — CNCF-graduated eBPF CNI network layer; 49 GHSA advisories; 25,071 GitHub stars; not previously covered
2. **kubernetes/flux2** — CNCF-graduated GitOps delivery platform; 11 GHSA advisories (10 reviewed); 8,383 GitHub stars; not previously covered

## Advisories fetched for kubernetes/cilium (github/advisory-database)
All URLs below are raw.githubusercontent.com paths into github/advisory-database main branch:

- GHSA-2h44-x2wx-49f4 (CVE-2023-30851, Moderate): HTTP policy bypass
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/05/GHSA-2h44-x2wx-49f4/GHSA-2h44-x2wx-49f4.json
- GHSA-gj2r-phwg-6rww (CVE-2023-39347, Moderate CVSS 6.1): pod-label policy bypass
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/09/GHSA-gj2r-phwg-6rww/GHSA-gj2r-phwg-6rww.json
- GHSA-x989-52fc-4vr4 (CVE-2024-25631, Moderate CVSS 6.1): WireGuard+external-kvstore unencrypted traffic
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/02/GHSA-x989-52fc-4vr4/GHSA-x989-52fc-4vr4.json
- GHSA-wh78-7948-358j (CVE-2024-37307, High): bugtool credential leak
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/06/GHSA-wh78-7948-358j/GHSA-wh78-7948-358j.json
- GHSA-qcm3-7879-xcww (CVE-2024-42487, Moderate CVSS 5.3): Gateway API route match precedence
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/08/GHSA-qcm3-7879-xcww/GHSA-qcm3-7879-xcww.json
- GHSA-xg58-75qf-9r67 (CVE-2024-52529, Moderate CVSS 5.3): L7 wildcard-port policy bypass
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/11/GHSA-xg58-75qf-9r67/GHSA-xg58-75qf-9r67.json

### Excluded from cilium vuln table (noted as context only):
- GHSA-xhgw-qwwf-pg32 (CVE-2026-10722, Low): integer overflow in `github.com/cilium/ebpf` — separate package; noted in Dependencies
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/06/GHSA-xhgw-qwwf-pg32/GHSA-xhgw-qwwf-pg32.json
- GHSA-57hq-w56x-2gq6 (CVE-2025-22021): Linux kernel netfilter — unreviewed; kernel advisory, not a cilium package issue; noted as dependency context
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2025/04/GHSA-57hq-w56x-2gq6/GHSA-57hq-w56x-2gq6.json

Note: 49 total GHSA search results for "cilium"; 6 direct cilium package advisories mapped here; remaining ~43 not examined in this pass.

## Advisories fetched for kubernetes/flux2 (github/advisory-database)
- GHSA-35rf-v2jv-gfg7 (CVE-2021-41254, High CVSS 8.8): kustomize-controller privilege escalation
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/11/GHSA-35rf-v2jv-gfg7/GHSA-35rf-v2jv-gfg7.json
- GHSA-vvmq-fwmg-2gjc (CVE-2022-24817, Critical CVSS 9.9): kubeconfig exec-injection ACE
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-vvmq-fwmg-2gjc/GHSA-vvmq-fwmg-2gjc.json
- GHSA-7pwf-jg34-hxwp (CVE-2022-24878, High CVSS 7.5): kustomization infinite-loop DoS
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-7pwf-jg34-hxwp/GHSA-7pwf-jg34-hxwp.json
- GHSA-xwf3-6rgv-939r (CVE-2022-36035, High CVSS 7.6): CLI path traversal
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/09/GHSA-xwf3-6rgv-939r/GHSA-xwf3-6rgv-939r.json
- GHSA-p2g7-xwvr-rrw3 (CVE-2022-36049, High CVSS 7.1): Helm SDK memory DoS in helm-controller
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/09/GHSA-p2g7-xwvr-rrw3/GHSA-p2g7-xwvr-rrw3.json
- GHSA-f4p5-x4vc-mh4v (CVE-2022-39272, Moderate): invalid Duration reconciliation DoS
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/10/GHSA-f4p5-x4vc-mh4v/GHSA-f4p5-x4vc-mh4v.json
- GHSA-v554-xwgw-hc3w (CVE-2024-31216, Moderate): Azure SAS token credential leak in logs
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/05/GHSA-v554-xwgw-hc3w/GHSA-v554-xwgw-hc3w.json
- GHSA-4xh5-jcj2-ch8q (CVE-2026-23990, Moderate): Flux Operator Web UI impersonation bypass
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/01/GHSA-4xh5-jcj2-ch8q/GHSA-4xh5-jcj2-ch8q.json
- GHSA-h9cx-xjg6-5v2w (CVE-2026-40109, Low CVSS 4.2): notification-controller GCR OIDC email-claim bypass
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/04/GHSA-h9cx-xjg6-5v2w/GHSA-h9cx-xjg6-5v2w.json
- GHSA-jjrm-hr5f-673x (CVE-2026-47680, Moderate): source-controller Bucket+sparse-checkout path traversal
  https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/06/GHSA-jjrm-hr5f-673x/GHSA-jjrm-hr5f-673x.json

## Registry/metadata notes
- cilium/cilium: 25,071 GitHub stars, v1.20.1 latest, Apache-2.0, CNCF-graduated
- fluxcd/flux2: 8,383 GitHub stars, v2.9.5 latest (2026-08-31), Apache-2.0, CNCF-graduated
- Neither package has meaningful "download" counts in the traditional registry sense (both are deployed operators, not imported Go libraries)

## Index updates
- wiki/kubernetes/index.md: 10 → 12 pages (added cilium, flux2)
- wiki/index.md: Kubernetes (10) → Kubernetes (12); total 280 → 282 pages; date 2026-09-03 → 2026-09-05
