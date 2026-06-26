# hashicorp/go-getter (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-06-26); 1,235 known importers on pkg.go.dev
**Repository:** https://github.com/hashicorp/go-getter
**Security Contact:** security@hashicorp.com
**Disclosure Policy:** https://discuss.hashicorp.com/c/security-announcements/23 (HashiCorp HCSEC advisories)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-26 | OSS Security KB | GHSA database lookup | automated | 10 public advisory rows mapped (GHSA-27rq through GHSA-92mm) | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-29810 / GHSA-27rq-4943-qcwp | High (CVSS 7.1, local) | SSH private keys logged in base64 as URL query parameters when a git download fails; keys visible in Fleet/Rancher UI and pod logs for misconfigured URLs. CWE-532. | ≥ 1.5.11 | [GHSA-27rq-4943-qcwp](https://github.com/advisories/GHSA-27rq-4943-qcwp) |
| CVE-2022-26945 / GHSA-x24g-9w7v-vprh | Critical (CVSS 9.8) | Command injection: maliciously crafted URLs enable OS command execution. All v1 before 1.6.1 and all v2 before 2.1.0 affected. CWE-77. | ≥ 1.6.1 (v1) / ≥ 2.1.0 (v2) | [GHSA-x24g-9w7v-vprh](https://github.com/advisories/GHSA-x24g-9w7v-vprh) |
| CVE-2022-30321 / GHSA-fcgg-rvwg-jv58 | High (CVSS 7.4) | Protocol switching, endless redirect, and configuration bypass via abuse of custom HTTP response headers (e.g. X-Terraform-Get), enabling SSRF and download redirection to attacker-controlled destinations. | ≥ 1.6.1 (v1) / ≥ 2.1.0 (v2) | [GHSA-fcgg-rvwg-jv58](https://github.com/advisories/GHSA-fcgg-rvwg-jv58) |
| CVE-2022-30322 / GHSA-cjr4-fv6c-f3mv | High (CVSS 7.5) | Unsafe downloads: path traversal, symlink processing, and command injection flaws allow arbitrary host access during file downloads. | ≥ 1.6.1 (v1) / ≥ 2.1.0 (v2) | [GHSA-cjr4-fv6c-f3mv](https://github.com/advisories/GHSA-cjr4-fv6c-f3mv) |
| CVE-2022-30323 / GHSA-28r2-q6m8-9hpx | High (CVSS 7.5) | Asymmetric resource exhaustion: processing malicious HTTP responses causes disproportionate CPU/memory consumption on the client, enabling denial of service. | ≥ 1.6.1 (v1) / ≥ 2.1.0 (v2) | [GHSA-28r2-q6m8-9hpx](https://github.com/advisories/GHSA-28r2-q6m8-9hpx) |
| CVE-2023-0475 / GHSA-jpxj-2jvg-6jv9 | Moderate (CVSS 7.1, local) | Decompression bomb (CWE-409): processing specially crafted compressed archives exhausts disk and memory, enabling denial of service. | ≥ 1.7.0 (v1) / ≥ 2.2.0 (v2) | [GHSA-jpxj-2jvg-6jv9](https://github.com/advisories/GHSA-jpxj-2jvg-6jv9) |
| CVE-2024-3817 / GHSA-q64h-39hv-4cf7 | Critical (CVSS 9.8) | Git argument injection: when fetching repos without an explicit ref, go-getter constructs git commands with unsanitized URL components, enabling remote code execution. CWE-88. Affected 1.5.9–1.7.3. | ≥ 1.7.4 | [GHSA-q64h-39hv-4cf7](https://github.com/advisories/GHSA-q64h-39hv-4cf7) |
| CVE-2024-6257 / GHSA-xfhp-jf8p-mh5w | High (CVSS 7.9) | Git configuration code execution: go-getter can be coerced into running git update on a maliciously modified `.git/config` after cloning, allowing arbitrary code execution via injected git hooks. CWE-77. | ≥ 1.7.5 | [GHSA-xfhp-jf8p-mh5w](https://github.com/advisories/GHSA-xfhp-jf8p-mh5w) |
| CVE-2025-8959 / GHSA-wjrx-6529-hcj3 | High (CVSS 9.1) | Symlink attack in subdirectory download: symlinks inside compressed archives can escape the destination directory boundary, enabling arbitrary file read outside the intended extraction path. CWE-59. | ≥ 1.7.9 | [GHSA-wjrx-6529-hcj3](https://github.com/advisories/GHSA-wjrx-6529-hcj3) |
| CVE-2026-4660 / GHSA-92mm-2pjq-r785 | High (CVSS 7.5) | Arbitrary file read via git operations: go-getter v1 ≤ 1.8.5 allows reading of arbitrary local filesystem files when processing maliciously crafted URLs during git clone/fetch. CWE-200. v2 module unaffected. | ≥ 1.8.6 (v1 only) | [GHSA-92mm-2pjq-r785](https://github.com/advisories/GHSA-92mm-2pjq-r785) |

*OSV live record: https://osv.dev/list?ecosystem=Go&q=github.com%2Fhashicorp%2Fgo-getter*

## Security Posture Notes

`github.com/hashicorp/go-getter` is HashiCorp's file-download library for Go, used as a core dependency in Terraform (module/provider downloading), Nomad (artifact stanza), OpenTofu, Consul, and other HashiCorp tooling. It supports downloading from HTTP(S), Git, Mercurial, S3, GCS, and local filesystems, and implements archive extraction and checksum verification. With 1,235 known importers on pkg.go.dev and transitive exposure through Terraform's enormous install base, the blast radius of any go-getter vulnerability spans the infrastructure-as-code ecosystem broadly.

**Security cluster (May 2022 — 1.6.1 / 2.1.0):** CVE-2022-26945, CVE-2022-30321, CVE-2022-30322, and CVE-2022-30323 were coordinated disclosures fixing four distinct attack surfaces (command injection, HTTP header abuse, path traversal/symlink, and resource exhaustion) in a single release cluster. HashiCorp simultaneously released fixes in both the v1 and v2 module lines and disclosed through their HCSEC advisory process. CVE-2022-29810 (SSH credential logging) was a separate, earlier disclosure fixed in 1.5.11.

**Git-specific attack cluster (2024–2026):** Three advisories target go-getter's git integration specifically: CVE-2024-3817 (argument injection via unsanitized refs), CVE-2024-6257 (post-clone git config code execution), and CVE-2026-4660 (arbitrary file read via crafted git URLs). Each required a distinct fix: 1.7.4 for argument injection, 1.7.5 for config execution, and 1.8.6 for the 2026 file-read issue (v2 not affected). The 2026 advisory was first disclosed publicly through OpenTofu's security advisory (GHSA-q7j3-v8qv-22vq) before the go-getter maintainers published GHSA-92mm-2pjq-r785.

**Current safe versions:** v1 ≥ 1.8.6, v2 ≥ 2.2.0. The v2 module (`github.com/hashicorp/go-getter/v2`) was not affected by CVE-2026-4660. Callers on v1 must upgrade to 1.8.6 for the full fix set.

**Disclosure posture:** HashiCorp maintains a dedicated security announcement forum and a responsible-disclosure policy at https://www.hashicorp.com/security. HCSEC advisory numbers reference internal triage. CVEs are assigned through NVD/MITRE.

## Dependencies of Note

None flagged at the module level. The security risk of go-getter arises from its own protocol-handling and subprocess-execution logic, not from transitive dependencies.

## Open Questions

- Determine whether v2 will receive continued security maintenance or if HashiCorp considers it EOL.
- Monitor for future git-integration advisories given the recurring pattern in CVE-2024-3817 / CVE-2024-6257 / CVE-2026-4660.
- Confirm weekly download counts via pkg.go.dev or the Go module proxy once public telemetry is available.

## Related Pages

- [[go/github.com/golang-jwt/jwt]]
- [[go/index]]

---
*Last updated: 2026-06-26 | Sources: 3 (github/advisory-database, pkg.go.dev, discuss.hashicorp.com)*
