# Advisory Review Pass — 2026-09-11

## Session context

- Date: 2026-09-11
- Targets: kubernetes/kube-controller-manager, go/github.com/lestrrat-go/jwx
- OSV.dev: blocked (HTTP 403) — all advisory content sourced from github/advisory-database via mcp__github__search_code + WebFetch on raw.githubusercontent.com

## Target 1: kubernetes/kube-controller-manager

**Selection rationale:** Kubernetes section at 12 pages (smallest section alongside Homebrew); kube-controller-manager is a critical control-plane component with its own distinct advisory history separate from kube-apiserver and kubelet.

**Search queries:**
- `mcp__github__search_code: kube-controller-manager repo:github/advisory-database` → 4 results
- `mcp__github__search_code: kube-controller-manager CVE kubernetes repo:github/advisory-database path:advisories` → same 4 results (confirmed complete)

**Advisories fetched (all 4 GHSA records):**
1. GHSA-x6mj-w4jf-jmgw — CVE-2020-8555 — Moderate SSRF via in-tree storage volume provisioners
   - URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-x6mj-w4jf-jmgw/GHSA-x6mj-w4jf-jmgw.json
2. GHSA-5x96-j797-5qqw — CVE-2020-8566 — Moderate Ceph RBD credential logging
   - URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/04/GHSA-5x96-j797-5qqw/GHSA-5x96-j797-5qqw.json
3. GHSA-h7wq-jj8r-qm7p — CVE-2024-0793 — High HPA null pointer deref DoS
   - URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/11/GHSA-h7wq-jj8r-qm7p/GHSA-h7wq-jj8r-qm7p.json
4. GHSA-r6j8-c6r2-37rr — CVE-2025-13281 — Moderate half-blind SSRF via Portworx StorageClass
   - URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/12/GHSA-r6j8-c6r2-37rr/GHSA-r6j8-c6r2-37rr.json

**Additional context:**
- Kubernetes security policy: https://kubernetes.io/docs/reference/issues-security/security/
- NVD references verified via advisory content
- pkg.go.dev: k8s.io/kubernetes module; advisories tracked at module level
- Current Kubernetes stable: 1.34.x (1.34.2 patches CVE-2025-13281)

## Target 2: go/github.com/lestrrat-go/jwx

**Selection rationale:** Go JOSE/JWT library not yet in wiki; searched for advisories first to confirm real security history before committing.

**Search queries:**
- `mcp__github__search_code: lestrrat-go/jwx repo:github/advisory-database` → 4 results
- `mcp__github__search_code: gorm.io/gorm repo:github/advisory-database` → 0 results (rejected as alternative target)
- `mcp__github__search_code: spf13/cobra repo:github/advisory-database` → 0 results (rejected)

**Advisories fetched (all 4 GHSA records):**
1. GHSA-rm8v-mxj3-5rmq — no CVE — Moderate AES-CBC JWE padding oracle
   - URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/06/GHSA-rm8v-mxj3-5rmq/GHSA-rm8v-mxj3-5rmq.json
2. GHSA-7f9x-gw85-8grf — CVE-2023-49290 — Moderate PBES2 p2c iteration DoS
   - URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/12/GHSA-7f9x-gw85-8grf/GHSA-7f9x-gw85-8grf.json
3. GHSA-pvcr-v8j8-j5q3 — CVE-2024-21664 — Moderate JWS nil pointer deref DoS
   - URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-pvcr-v8j8-j5q3/GHSA-pvcr-v8j8-j5q3.json
4. GHSA-hj3v-m684-v259 — CVE-2024-28122 — Moderate JWE decompression bomb
   - URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/03/GHSA-hj3v-m684-v259/GHSA-hj3v-m684-v259.json

**Additional context:**
- pkg.go.dev: https://pkg.go.dev/github.com/lestrrat-go/jwx/v4 — current stable v4.5.0 (Sep 8, 2026); v2 deprecated
- pkg.go.dev: https://pkg.go.dev/github.com/lestrrat-go/jwx/v2 — deprecated, no longer maintained
- GitHub repository: https://github.com/lestrrat-go/jwx
- v4 requires Go ≥ 1.26
- No v3 or v4 GHSA advisories found in this pass

## Pages created

- `wiki/kubernetes/kube-controller-manager.md` — advisory-mapped, 4 advisories
- `wiki/go/github.com/lestrrat-go/jwx.md` — advisory-mapped, 4 advisories

## Index updates

- Kubernetes: 12 → 13 pages
- Go: 33 → 34 pages
- Master index: 288 → 290 pages
