# Advisory Review — 2026-06-26 06:00 UTC

## Targets

### 1. github.com/hashicorp/go-getter (Go)
### 2. github.com/go-jose/go-jose (Go)

## Sources Consulted

### go-getter
- https://pkg.go.dev/github.com/hashicorp/go-getter — import count (1,235), current version v1.8.6
- https://github.com/github/advisory-database — mcp__github__search_code for "hashicorp/go-getter"
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/04/GHSA-27rq-4943-qcwp/GHSA-27rq-4943-qcwp.json — CVE-2022-29810 (SSH credential logging)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-x24g-9w7v-vprh/GHSA-x24g-9w7v-vprh.json — CVE-2022-26945 (command injection, Critical 9.8)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-fcgg-rvwg-jv58/GHSA-fcgg-rvwg-jv58.json — CVE-2022-30321 (protocol switching)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-cjr4-fv6c-f3mv/GHSA-cjr4-fv6c-f3mv.json — CVE-2022-30322 (path traversal/symlink)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-28r2-q6m8-9hpx/GHSA-28r2-q6m8-9hpx.json — CVE-2022-30323 (resource exhaustion)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/02/GHSA-jpxj-2jvg-6jv9/GHSA-jpxj-2jvg-6jv9.json — CVE-2023-0475 (decompression bomb)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/04/GHSA-q64h-39hv-4cf7/GHSA-q64h-39hv-4cf7.json — CVE-2024-3817 (git argument injection, Critical 9.8)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/06/GHSA-xfhp-jf8p-mh5w/GHSA-xfhp-jf8p-mh5w.json — CVE-2024-6257 (git config code execution)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/08/GHSA-wjrx-6529-hcj3/GHSA-wjrx-6529-hcj3.json — CVE-2025-8959 (symlink file read)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/04/GHSA-92mm-2pjq-r785/GHSA-92mm-2pjq-r785.json — CVE-2026-4660 (arbitrary file read via git)
- https://discuss.hashicorp.com/c/security-announcements/23 — HashiCorp HCSEC advisory forum (disclosure policy reference)

### go-jose
- https://pkg.go.dev/github.com/go-jose/go-jose/v4 — import count (601), current version v4.1.4
- https://github.com/github/advisory-database — mcp__github__search_code for "go-jose"
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/06/GHSA-86r9-39j9-99wp/GHSA-86r9-39j9-99wp.json — CVE-2016-9121 (ECDH-ES invalid curve)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/06/GHSA-3fx4-7f69-5mmg/GHSA-3fx4-7f69-5mmg.json — CVE-2016-9123 (CBC-HMAC integer overflow)
- https://github.com/advisories/GHSA-77gc-fj98-665h — signature validation bypass (no CVE)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/11/GHSA-2c7c-3mj9-8fqh/GHSA-2c7c-3mj9-8fqh.json — PBES2 billion-hashes DoS
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/03/GHSA-c5q2-7r4c-mv6g/GHSA-c5q2-7r4c-mv6g.json — CVE-2024-28180 (decompression bomb)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/02/GHSA-c6gw-w398-hv78/GHSA-c6gw-w398-hv78.json — CVE-2025-27144 (parsing DoS)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/04/GHSA-78h2-9frx-2jm8/GHSA-78h2-9frx-2jm8.json — CVE-2026-34986 (key-wrapping panic)
- https://go.dev/security/policy — Go vulnerability database disclosure policy

## Notes

- OSV.dev API (api.osv.dev) returned HTTP 403 as expected; all advisory data sourced from github/advisory-database.
- GHSA-wm2r-rp98-8pmh (Rancher/Fleet SSH credential exposure via go-getter) noted but omitted from go-getter's vuln table as it is a downstream Rancher advisory, not a direct go-getter package advisory.
- GHSA-77gc-fj98-665h has no CVE alias; included as Moderate based on advisory classification.
- `gopkg.in/square/go-jose.v2` (archived) will not receive patches for CVE-2024-28180; noted in go-jose posture section.
- go-getter v2 module was unaffected by CVE-2026-4660 (GHSA-92mm-2pjq-r785).
