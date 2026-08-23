# Advisory Review Evidence — 2026-08-23 07:30 UTC

## Targets
- `kubernetes/cert-manager` (new page)
- `rust/diesel` (new page)

## URLs Consulted

### cert-manager
- https://github.com/advisories/GHSA-r4pg-vg54-wxx4 (CVE-2024-12401, reviewed)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/11/GHSA-r4pg-vg54-wxx4/GHSA-r4pg-vg54-wxx4.json
- https://github.com/advisories/GHSA-gx3x-vq4p-mhhv (CVE-2026-25518, reviewed)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/02/GHSA-gx3x-vq4p-mhhv/GHSA-gx3x-vq4p-mhhv.json
- https://github.com/advisories/GHSA-ghw8-3xqw-hhcj (CVE-2024-12401 duplicate, withdrawn)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/12/GHSA-ghw8-3xqw-hhcj/GHSA-ghw8-3xqw-hhcj.json
- https://github.com/advisories/GHSA-9cfq-668r-pxhc (CVE-2024-36537, unreviewed)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2024/07/GHSA-9cfq-668r-pxhc/GHSA-9cfq-668r-pxhc.json
- https://github.com/advisories/GHSA-35w7-q98m-gqgx (CVE-2026-10840, unreviewed, OpenShift Pipelines — NOT a direct cert-manager advisory)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/06/GHSA-35w7-q98m-gqgx/GHSA-35w7-q98m-gqgx.json
- https://github.com/advisories/GHSA-9gcg-w975-3rjh (CVE-2026-39350, reviewed, istio.io/istio — NOT cert-manager)
- https://cert-manager.io/docs/contributing/security/
- mcp__github__search_code: `cert-manager repo:github/advisory-database path:advisories`

### diesel
- https://github.com/advisories/GHSA-j8q9-5rp9-4mv9 (CVE-2021-28305 / RUSTSEC-2021-0037, reviewed)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-j8q9-5rp9-4mv9/GHSA-j8q9-5rp9-4mv9.json
- https://github.com/advisories/GHSA-wq9x-qwcq-mmgf (RUSTSEC-2024-0365, reviewed)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/08/GHSA-wq9x-qwcq-mmgf/GHSA-wq9x-qwcq-mmgf.json
- https://github.com/advisories/GHSA-h5x4-m2qf-r4f2 (reviewed)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/05/GHSA-h5x4-m2qf-r4f2/GHSA-h5x4-m2qf-r4f2.json
- https://github.com/advisories/GHSA-m9p2-fxp5-v3fp (RUSTSEC-2026-0136, reviewed)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/05/GHSA-m9p2-fxp5-v3fp/GHSA-m9p2-fxp5-v3fp.json
- https://github.com/advisories/GHSA-q8x8-jrhj-fh9p (RUSTSEC-2026-0137, reviewed)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/05/GHSA-q8x8-jrhj-fh9p/GHSA-q8x8-jrhj-fh9p.json
- https://github.com/advisories/GHSA-ggxf-9f6j-w742 (reviewed)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/07/GHSA-ggxf-9f6j-w742/GHSA-ggxf-9f6j-w742.json
- https://github.com/advisories/GHSA-ff9q-rm55-q7qr (diesel-async, NOT diesel core)
- https://github.com/advisories/GHSA-3jvj-v6w2-h948 (lemmy_api_commons, NOT diesel)
- https://crates.io/api/v1/crates/diesel (download stats)
- mcp__github__search_code: `diesel repo:github/advisory-database path:advisories`

## Notes
- GHSA-ghw8-3xqw-hhcj: withdrawn duplicate of GHSA-r4pg-vg54-wxx4; excluded from cert-manager vuln table
- GHSA-9gcg-w975-3rjh: maps to istio.io/istio (regex injection in AuthorizationPolicy), not cert-manager; excluded
- GHSA-35w7-q98m-gqgx: OpenShift Pipelines operator CRD RBAC misconfiguration that affects cert-manager CRDs indirectly; not a direct cert-manager advisory; excluded
- GHSA-ff9q-rm55-q7qr: affects diesel-async (sibling crate), not diesel core; excluded from diesel page
- GHSA-3jvj-v6w2-h948: affects lemmy_api_commons (Lemmy social platform), not diesel; false positive from keyword search
- OSV.dev API: HTTP 403 (blocked by network policy); all advisories sourced from github/advisory-database via WebFetch
