# Advisory Review Pass — 2026-06-23 06:00 UTC

## Targets Selected

1. **kubernetes/helm** — CNCF-graduated Kubernetes package manager (helm.sh/helm/v3, helm.sh/helm/v4)
   - Rationale: Kubernetes ecosystem had only 4 pages; Helm is the dominant Kubernetes package manager with a rich and confirmed advisory history in github/advisory-database

2. **rust/serde_json** — de facto standard Rust JSON library (crates.io)
   - Rationale: Rust ecosystem had 12 pages; serde_json is the most-downloaded non-proc-macro crate on crates.io (1B+ downloads) with no existing KB page

## Sources Consulted

### Helm (kubernetes/helm)

**GitHub Advisory Database search:**
- Query: `repo:github/advisory-database "helm.sh/helm" path:advisories` → 29 total hits
- All 29 GHSA JSON files fetched via raw.githubusercontent.com

**Advisory files fetched (raw.githubusercontent.com):**
- GHSA-x6r5-vxfg-gq3v (CVE-2019-1010275 Tiller TLS validation, Critical)
- GHSA-p5pc-m4q7-7qm9 (CVE-2019-18658 Helm 2 symlink attack, Critical)
- GHSA-xrxm-mvqm-r553 (CVE-2019-1000008 path traversal, Moderate)
- GHSA-cjjc-xp8v-855w (CVE-2020-7919 X.509 panic DoS, High)
- GHSA-q8q8-93cv-v6h8 (CVE-2020-11013 lookup cluster data leakage, High)
- GHSA-qq3j-xp49-j73f (CVE-2020-4053 plugin zip-slip, Low)
- GHSA-jm56-5h66-w453 (CVE-2020-15185 duplicate index entries, Low)
- GHSA-9vp5-m38w-j776 (CVE-2020-15184 alias field injection, Low)
- GHSA-m54r-vrmv-hw33 (CVE-2020-15186 plugin name sanitization, Low)
- GHSA-c52f-pq47-2r9j (CVE-2020-15187 duplicate plugin.yaml hooks, Low)
- GHSA-c38g-469g-cmgx (CVE-2021-21303 SemVer terminal escape injection, Moderate)
- GHSA-7jr6-prv4-5wf5 (CVE-2021-32690 credential forwarding, Moderate)
- GHSA-56hp-xqp3-w2jf (CVE-2021-32690 duplicate record for same fix)
- GHSA-7hfp-qfw3-5jxh (CVE-2022-36055 strvals OOM, Moderate)
- GHSA-6rx9-889q-vv2r (CVE-2022-23524 strvals stack overflow, Moderate)
- GHSA-53c4-hhmh-vw5q (CVE-2022-23525 repo index memory violation, Moderate)
- GHSA-67fx-wx78-jx33 (CVE-2022-23526 JSON schema segfault, Moderate)
- GHSA-pwcw-6f5g-gxf8 (CVE-2023-25165 getHostByName DNS leakage, Moderate)
- GHSA-v53g-5gjp-272r (CVE-2024-25620 chart name path traversal, Moderate)
- GHSA-r53h-jv2g-vpx6 (CVE-2024-26147 metadata panic DoS, High)
- GHSA-jw44-4f3j-q396 (CVE-2019-25210 withdrawn — dry-run behavior intentional)
- GHSA-4hfp-h4cw-hj8p (CVE-2025-32386 decompression bomb, Moderate)
- GHSA-5xqw-8hwv-wg92 (CVE-2025-32387 $ref stack overflow, Moderate)
- GHSA-557j-xg8c-q2mm (CVE-2025-53547 Chart.yaml symlink code execution, High)
- GHSA-f9f8-9pmf-xv68 (CVE-2025-55198 malformed YAML panic, Moderate)
- GHSA-9h84-qmv7-982p (CVE-2025-55199 JSON Schema /dev/zero OOM, Moderate)
- GHSA-hr2v-4r36-88hr (CVE-2026-35206 pull --untar path escape, Moderate)
- GHSA-q5jf-9vfq-h4h7 (CVE-2026-35205 Helm v4 plugin signing bypass, High)
- GHSA-vmx8-mqv2-9gmg (CVE-2026-35204 Helm v4 plugin path traversal CVSS 9.9, High)

**pkg.go.dev:**
- https://pkg.go.dev/helm.sh/helm/v3 — latest v3.21.2 (2026-06-20)

**Upstream:**
- SECURITY.md: https://github.com/helm/helm/blob/main/SECURITY.md
- Security contact: cncf-helm-security@lists.cncf.io

**OSV:** API blocked (HTTP 403) — sourced from github/advisory-database directly.

### serde_json (rust/serde_json)

**crates.io API:**
- https://crates.io/api/v1/crates/serde_json
  - Total downloads: 1,001,041,240
  - Recent 90-day downloads: 207,149,044
  - Latest version: 1.0.150
  - License: MIT OR Apache-2.0
  - Maintainer: David Tolnay (dtolnay) / serde-rs organization

**RustSec advisory-db search:**
- Query: `repo:rustsec/advisory-db serde_json` → 3 hits, all references to serde_json in other crates' advisories (json, gix-attributes, json5); no advisory filed under `crates/serde_json/`
- Confirms: no direct package-scoped RustSec advisory for serde_json

**GitHub advisory-database search:**
- No serde_json-scoped GHSA records found in code search

**Upstream repository:**
- https://github.com/serde-rs/json
- No SECURITY.md or formal disclosure policy

## Decision Log

- Selected helm over argo-cd and kube-proxy because of confirmed rich advisory history (29 GHSAs) vs. needing further research for others.
- Selected serde_json as baseline stub to document the high-blast-radius package with no advisories rather than skipping it — this is useful for future consumers and follows SCHEMA.md guidance on baseline stubs.
- Withdrawn advisory GHSA-jw44-4f3j-q396 noted in posture section only, not in vulnerability table per METHODOLOGY.md (no active advisory).
- GHSA-56hp-xqp3-w2jf merged with GHSA-7jr6-prv4-5wf5 in the same table row since both cover CVE-2021-32690 and the same fix.
