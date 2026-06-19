# Advisory Review Pass — 2026-06-18 21:00 UTC

## Targets Selected

- **rust/base64** — crates.io, 250M weekly downloads (top-10 by total downloads), no existing KB page
- **go/go.etcd.io/etcd-v3** — critical Kubernetes backing-store component, under-covered Go ecosystem, no existing KB page

## Sources Consulted

| Source | URL / Location | Notes |
|--------|---------------|-------|
| crates.io API | https://crates.io/api/v1/crates?sort=downloads&per_page=25 | Used to identify top Rust crates missing from KB |
| crates.io API (base64) | https://crates.io/api/v1/crates/base64 | Download stats, latest version, repo URL |
| rustsec/advisory-db (GitHub code search) | `name = "base64" path:crates repo:rustsec/advisory-db` | Found RUSTSEC-2017-0004.md |
| rustsec advisory raw | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/base64/RUSTSEC-2017-0004.md | Full advisory details |
| github/advisory-database (code search) | `"go.etcd.io/etcd" repo:github/advisory-database path:advisories` | Returned 20 advisories (full list page 1) |
| GHSA-5gjm-fj42-x983 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-5gjm-fj42-x983/GHSA-5gjm-fj42-x983.json | CVE-2018-1098 CSRF |
| GHSA-h6xx-pmxh-3wgp | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/04/GHSA-h6xx-pmxh-3wgp/GHSA-h6xx-pmxh-3wgp.json | CVE-2018-16886 RBAC CN bypass |
| GHSA-p4g4-wgrh-qrg2 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/02/GHSA-p4g4-wgrh-qrg2/GHSA-p4g4-wgrh-qrg2.json | CVE-2020-15106 WAL large frame panic |
| GHSA-m332-53r6-2w93 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/10/GHSA-m332-53r6-2w93/GHSA-m332-53r6-2w93.json | CVE-2020-15112 WAL ReadAll panic |
| GHSA-4993-m7g5-r9hh | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/10/GHSA-4993-m7g5-r9hh/GHSA-4993-m7g5-r9hh.json | CVE-2020-15115 no min password length |
| GHSA-2xhq-gv6c-p224 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-2xhq-gv6c-p224/GHSA-2xhq-gv6c-p224.json | CVE-2020-15114 gateway self-loop DoS |
| GHSA-wr2v-9rpq-c35q | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-wr2v-9rpq-c35q/GHSA-wr2v-9rpq-c35q.json | CVE-2020-15136 gateway TLS DNS-only |
| GHSA-528j-9r78-wffx | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/10/GHSA-528j-9r78-wffx/GHSA-528j-9r78-wffx.json | credentials in WAL |
| GHSA-9gp7-6833-wv89 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/10/GHSA-9gp7-6833-wv89/GHSA-9gp7-6833-wv89.json | service discovery negative size panic |
| GHSA-h8g9-6gvh-5mrc | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/10/GHSA-h8g9-6gvh-5mrc/GHSA-h8g9-6gvh-5mrc.json | gateway TOCTOU |
| GHSA-5x4g-q5rc-36jp | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/02/GHSA-5x4g-q5rc-36jp/GHSA-5x4g-q5rc-36jp.json | insecure TLS ciphers |
| GHSA-vjg6-93fv-qv64 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/02/GHSA-vjg6-93fv-qv64/GHSA-vjg6-93fv-qv64.json | CN auth logging |
| GHSA-pm3m-32r3-7mfh | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/02/GHSA-pm3m-32r3-7mfh/GHSA-pm3m-32r3-7mfh.json | negative compaction retention |
| GHSA-j86v-2vjr-fg8f | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/02/GHSA-j86v-2vjr-fg8f/GHSA-j86v-2vjr-fg8f.json | gateway TLS TCP-only check |
| GHSA-gmph-wf7j-9gcm | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/04/GHSA-gmph-wf7j-9gcm/GHSA-gmph-wf7j-9gcm.json | CVE-2021-28235 debug endpoint RCE |
| GHSA-rfx7-8w68-q57q | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-rfx7-8w68-q57q/GHSA-rfx7-8w68-q57q.json | CVE-2026-33343 nested txn RBAC bypass |
| GHSA-q8m4-xhhv-38mg | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-q8m4-xhhv-38mg/GHSA-q8m4-xhhv-38mg.json | CVE-2026-33413 gRPC API auth bypass |
| GHSA-x35m-3gp4-4fh5 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/05/GHSA-x35m-3gp4-4fh5/GHSA-x35m-3gp4-4fh5.json | CVE-2026-44283 PrevKv/lease txn bypass |
| pkg.go.dev | https://pkg.go.dev/go.etcd.io/etcd/v3 | Latest version (3.6.12), active vuln flags |
| etcd security policy | https://github.com/etcd-io/etcd/blob/main/security/security-release-process.md | security@etcd.io, PSC structure |

## Environment Notes

- OSV.dev API returned HTTP 403 (blocked by network policy) — advisory content sourced from raw GitHub files instead
- rustsec/advisory-db and github/advisory-database not accessible via `get_file_contents` MCP tool (restricted to travis-burmaster/oss-security-kb only); accessed via WebFetch to raw.githubusercontent.com and mcp search_code
- `gh` CLI not installed in this environment; PR creation via MCP GitHub tools or local git proxy

## Pages Written

- `wiki/rust/base64.md` — 1 vulnerability row (RUSTSEC-2017-0004)
- `wiki/go/go.etcd.io/etcd-v3.md` — 18 vulnerability rows
