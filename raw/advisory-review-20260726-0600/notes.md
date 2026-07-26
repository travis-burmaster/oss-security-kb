# Advisory Review Evidence — 2026-07-26

**Pass date:** 2026-07-26  
**Targets:** kubernetes/argo-cd (new), rust/curve25519-dalek (new)  
**Ecosystem focus:** Kubernetes (Argo CD), Rust/crates.io (curve25519-dalek)

---

## Environment constraints

- OSV.dev API (api.osv.dev): HTTP 403 blocked — not used
- crates.io API (api.crates.io): getaddrinfo ENOTFOUND — download stats unavailable for curve25519-dalek
- formulae.brew.sh API: HTTP 403 blocked (not needed this pass)
- GitHub MCP tools: available and used for advisory search
- WebFetch (raw.githubusercontent.com): available and used

---

## kubernetes/argo-cd

### Target selection rationale
- Listed as "Future Target" in `wiki/kubernetes/index.md`
- CNCF Graduated project with well-known advisory history
- Kubernetes ecosystem is under-covered relative to npm/python

### Advisory discovery

**Primary method:** `mcp__github__search_code` with query `argo-cd repo:github/advisory-database path:advisories/github-reviewed`
- Result: 56 total GHSA advisories
- Page 1 (30 paths) + Page 2 (26 paths) retrieved

**Individual advisory files fetched via WebFetch (raw.githubusercontent.com):**

| GHSA ID | CVE | Severity | Notes |
|---------|-----|----------|---------|
| GHSA-xj7v-c82w-92q2 | CVE-2018-21034 | Moderate | Sensitive API info exposure |
| GHSA-vj54-cjrx-x696 | CVE-2020-11576 | Moderate | User enumeration |
| GHSA-qq5v-f4c3-395c | CVE-2021-23347 | Moderate | XSS via SSO CLI |
| GHSA-63qx-x74g-jcr7 | CVE-2022-24348 | High | Helm symlink path traversal |
| GHSA-2f5v-8r3f-8pww | CVE-2022-24768 | Critical 9.9 | Privilege escalation to admin |
| GHSA-6gcg-hp2x-q54h | CVE-2022-24904 | Moderate | Repo-server symlink |
| GHSA-xmg8-99r8-jc2j | CVE-2022-24905 | Moderate | Login screen spoofing |
| GHSA-r642-gv9p-2wjj | CVE-2022-29165 | Critical 9.8 | JWT blind trust auth bypass |
| GHSA-2m7h-86qq-fp4v | CVE-2022-31034 | High 8.6 | Insecure PRNG for PKCE/OAuth |
| GHSA-h4w9-6x78-8vrj | CVE-2022-31035 | Critical 8.7 | XSS via deployment link annotations |
| GHSA-q4w5-4gq2-98vm | CVE-2022-31036 | Moderate | Repo-server symlink YAML |
| GHSA-pmjg-52h9-72qv | CVE-2022-31102 | Low | XSS in /auth/callback |
| GHSA-7943-82jg-wmw5 | CVE-2022-31105 | High 8.6 | OIDC TLS cert skip |
| GHSA-2q5c-qw9c-fmvq | CVE-2022-41354 | Moderate | App name enumeration |
| GHSA-q9hr-j4rf-8fjc | CVE-2023-22482 | Critical 8.6 | JWT audience bypass |
| GHSA-6p4m-hw2h-6gmw | CVE-2023-22736 | High 7.5 | Namespace isolation bypass |
| GHSA-3jfq-742w-xg8j | CVE-2023-23947 | Critical 9.1 | Cluster secret RBAC bypass |
| GHSA-mv6w-j4xc-qpfw | CVE-2023-25163 | Moderate | Credential leak in errors/logs |
| GHSA-c8xw-vjgf-94hr | CVE-2023-40025 | High | Web terminal session not expiring |
| GHSA-fwr2-64vr-xv9m | CVE-2023-40029 | Critical 8.7 | Cluster creds via annotation |
| GHSA-g687-f2gx-6wm8 | CVE-2023-40584 | Moderate | repo-server tar DoS |
| GHSA-x32m-mvfj-52xv | CVE-2024-21652 | Critical 9.8 | Brute-force bypass via crash |
| GHSA-2vgg-9h6w-m454 | CVE-2024-21662 | Moderate | Brute-force bypass via cache overflow |
| GHSA-92mw-q256-5vwg | CVE-2024-22424 | High 8.8 | CSRF via content-type bypass |
| GHSA-3cqf-953p-h5cp | CVE-2024-36106 | Moderate | Cluster name enumeration |
| GHSA-87p9-x75h-p4j2 | CVE-2024-37152 | Moderate | Unauthenticated /api/v1/settings |
| GHSA-47g2-qmh2-749v | CVE-2025-23216 | Moderate | Secrets in patch error messages |
| GHSA-wp4p-9pxh-cgx2 | CVE-2025-59537 | High 9.0 | Gogs webhook nil-ptr DoS |
| GHSA-3v3m-wc6v-x4x3 | CVE-2026-42880 | Critical 9.1 | ServerSideDiff unmasked secrets |
| GHSA-rg3g-4rw9-gqrp | CVE-2026-45737 | Moderate | ServerSideDiff annotation bypass |
| GHSA-h98r-wv3h-fr38 | CVE-2026-45738 | High 7.1 | Stored XSS dev→admin escalation |

**Not individually fetched (25 advisories):**
GHSA-6w87-g839-9wv7, GHSA-xcqr-9h24-vrgw, GHSA-h8jc-jmrf-9h8f (2021),
GHSA-h6h5-6fmq-rh28, GHSA-r9cr-hvjj-496v, GHSA-96jv-vj39-x4j6, GHSA-jhqp-vf4w-rpwq (2022),
GHSA-jwv5-8mqv-g387, GHSA-g623-jcgg-mhmm, GHSA-6v85-wr92-q4p7, GHSA-jhwx-mhww-rgc3,
GHSA-9m6p-x4h2-6frq, GHSA-2gvw-w6fj-7m3c, GHSA-9766-5277-j5hr (2024 Mar-May),
GHSA-jmvp-698c-4x3w, GHSA-v8wx-v5jq-qhhw (2024 Jul),
GHSA-gppm-hq3p-h4rp (2024 Nov),
GHSA-58fx-7v9q-3g56, GHSA-274v-mgcv-cm8j, GHSA-2hj5-g64g-fp6p (2025 Jan-May),
GHSA-gpx4-37g2-c8pv, GHSA-f9gq-prrc-hrhc, GHSA-786q-9hcg-v9ff, GHSA-g88p-r42r-ppp9 (2025 Sep)

**Current version:** v3.4.5 (released 2026-07-09) — fetched from github.com/argoproj/argo-cd/releases/latest via WebFetch

---

## rust/curve25519-dalek

### Advisory discovery

**Primary method:** `mcp__github__search_code` with query `curve25519-dalek repo:rustsec/advisory-db`
- Result: 1 advisory — RUSTSEC-2024-0344.md

**Advisory file fetched:**
- URL: `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/curve25519-dalek/RUSTSEC-2024-0344.md`
- Fields extracted: id, package, date, url, aliases (CVE-2024-58262, GHSA-x4gp-pqpj-f43q), categories, patched (>= 4.1.3)
- Fix reference: https://github.com/dalek-cryptography/curve25519-dalek/pull/659
- Researcher: Fraunhofer AISEC / TU Munich, DATA tool

**Download stats:** Not retrieved (api.crates.io returned getaddrinfo ENOTFOUND)

**GHSA record:** Attempted fetch of GHSA-x4gp-pqpj-f43q.json — returned HTTP 404 (path not at expected location); advisory data sourced from rustsec file which includes the GHSA alias and CVE alias.

---

## Counts verification

| File | Before | After |
|------|--------|-------|
| wiki/index.md total pages | 236 | 238 |
| wiki/index.md Kubernetes count | 7 (8) | 8 |
| wiki/index.md Rust count | 26 | 27 |
| wiki/kubernetes/index.md entries | 7 | 8 |
| wiki/rust/index.md entries | 26 | 27 |
