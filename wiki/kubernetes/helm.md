# Helm (Kubernetes)

**Registry:** k8s / CNCF (Go module: `helm.sh/helm/v3`, `helm.sh/helm/v4`)
**Weekly Downloads:** not tracked per-package (CLI tool distributed via Homebrew, Chocolatey, Snapcraft, direct binary)
**Repository:** https://github.com/helm/helm
**Security Contact:** cncf-helm-security@lists.cncf.io
**Disclosure Policy:** https://github.com/helm/helm/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-1010275 / GHSA-x6r5-vxfg-gq3v | Critical (CVSS 9.8) | Helm 2 Tiller: improper TLS certificate validation allows unauthorized remote client connections | 2.7.2 | [GHSA-x6r5-vxfg-gq3v](https://github.com/advisories/GHSA-x6r5-vxfg-gq3v) |
| CVE-2019-18658 / GHSA-p5pc-m4q7-7qm9 | Critical (CVSS 9.8) | Helm 2: malicious chart uses symlinks to gain unauthorized file access or cause DoS during chart loading or packaging | 2.15.2 | [GHSA-p5pc-m4q7-7qm9](https://github.com/advisories/GHSA-p5pc-m4q7-7qm9) |
| CVE-2019-1000008 / GHSA-xrxm-mvqm-r553 | Moderate | Helm 2: path traversal in chart archive extraction via `helm fetch --untar` (zip-slip style) allows write outside target directory | 2.12.2 | [GHSA-xrxm-mvqm-r553](https://github.com/advisories/GHSA-xrxm-mvqm-r553) |
| CVE-2020-7919 / GHSA-cjjc-xp8v-855w | High (CVSS 7.5) | Malformed X.509 certificate triggers `golang.org/x/crypto` panic, enabling remote denial of service | 2.16.8 / 3.1.0 | [GHSA-cjjc-xp8v-855w](https://github.com/advisories/GHSA-cjjc-xp8v-855w) |
| CVE-2020-11013 / GHSA-q8q8-93cv-v6h8 | High | `lookup` template function contacts live Kubernetes cluster during `helm template` runs, leaking sensitive cluster data to untrusted chart authors | 3.1.3 / 3.2.0 | [GHSA-q8q8-93cv-v6h8](https://github.com/advisories/GHSA-q8q8-93cv-v6h8) |
| CVE-2020-4053 / GHSA-qq3j-xp49-j73f | Low | Plugin installation via tar archive over HTTP allows directory traversal (zip-slip), enabling writes outside intended plugin directory | 3.2.4 | [GHSA-qq3j-xp49-j73f](https://github.com/advisories/GHSA-qq3j-xp49-j73f) |
| CVE-2020-15185 / GHSA-jm56-5h66-w453 | Low | Duplicate chart entries in repository `index.yaml` allow last-entry-wins injection of malicious charts during non-SSL attacks | 3.3.2 / 2.16.11 | [GHSA-jm56-5h66-w453](https://github.com/advisories/GHSA-jm56-5h66-w453) |
| CVE-2020-15184 / GHSA-9vp5-m38w-j776 | Low | Unsanitized `alias` field in `Chart.yaml` dependency allows newline or path character injection | 3.3.2 / 2.16.11 | [GHSA-9vp5-m38w-j776](https://github.com/advisories/GHSA-9vp5-m38w-j776) |
| CVE-2020-15186 / GHSA-m54r-vrmv-hw33 | Low | Plugin names lack sanitization, allowing special characters to duplicate plugin names or corrupt help output | 3.3.2 / 2.16.11 | [GHSA-m54r-vrmv-hw33](https://github.com/advisories/GHSA-m54r-vrmv-hw33) |
| CVE-2020-15187 / GHSA-c52f-pq47-2r9j | Low | Duplicate entries in `plugin.yaml` allow attacker with repository write access to override plugin installation hooks via last-wins behavior | 3.3.2 / 2.16.11 | [GHSA-c52f-pq47-2r9j](https://github.com/advisories/GHSA-c52f-pq47-2r9j) |
| CVE-2021-21303 / GHSA-c38g-469g-cmgx | Moderate | Malformed SemVer version strings in chart metadata bypass validation and enable terminal escape code injection to manipulate operator output | 3.5.2 | [GHSA-c38g-469g-cmgx](https://github.com/advisories/GHSA-c38g-469g-cmgx) |
| CVE-2021-32690 / GHSA-7jr6-prv4-5wf5 / GHSA-56hp-xqp3-w2jf | Moderate | Repository credentials inadvertently forwarded to alternate domains referenced in chart index files; fixed by restricting credentials to origin domain unless `--pass-credentials` is explicitly set | 3.6.1 | [GHSA-7jr6-prv4-5wf5](https://github.com/advisories/GHSA-7jr6-prv4-5wf5) |
| CVE-2022-36055 / GHSA-7hfp-qfw3-5jxh | Moderate (CVSS 6.5) | `strvals` package (Helm SDK) causes out-of-memory panic when parsing certain untrusted input strings | 3.9.4 | [GHSA-7hfp-qfw3-5jxh](https://github.com/advisories/GHSA-7hfp-qfw3-5jxh) |
| CVE-2022-23524 / GHSA-6rx9-889q-vv2r | Moderate (CVSS 5.3) | `strvals` parser stack overflow via malicious strings passed via `--set` flags, causing unrecoverable panic | 3.10.3 | [GHSA-6rx9-889q-vv2r](https://github.com/advisories/GHSA-6rx9-889q-vv2r) |
| CVE-2022-23525 / GHSA-53c4-hhmh-vw5q | Moderate (CVSS 5.3) | Malformed repository `index.yaml` file triggers memory violation and panic in Helm's repository package | 3.10.3 | [GHSA-53c4-hhmh-vw5q](https://github.com/advisories/GHSA-53c4-hhmh-vw5q) |
| CVE-2022-23526 / GHSA-67fx-wx78-jx33 | Moderate (CVSS 5.3) | Malicious JSON schema file in chart causes segmentation fault / panic in `chartutil` package | 3.10.3 | [GHSA-67fx-wx78-jx33](https://github.com/advisories/GHSA-67fx-wx78-jx33) |
| CVE-2023-25165 / GHSA-pwcw-6f5g-gxf8 | Moderate (CVSS 4.3) | `getHostByName` template function performs DNS lookups that can leak sensitive chart data to external DNS resolvers | 3.11.1 | [GHSA-pwcw-6f5g-gxf8](https://github.com/advisories/GHSA-pwcw-6f5g-gxf8) |
| CVE-2024-25620 / GHSA-v53g-5gjp-272r | Moderate (CVSS 6.4) | Relative path components in chart names bypass validation and allow chart to be written outside intended directory | 3.14.1 | [GHSA-v53g-5gjp-272r](https://github.com/advisories/GHSA-v53g-5gjp-272r) |
| CVE-2024-26147 / GHSA-r53h-jv2g-vpx6 | High (CVSS 7.5) | Missing required metadata in index or plugin YAML files triggers panic that crashes all Helm client commands | 3.14.2 | [GHSA-r53h-jv2g-vpx6](https://github.com/advisories/GHSA-r53h-jv2g-vpx6) |
| CVE-2025-32386 / GHSA-4hfp-h4cw-hj8p | Moderate | Zip/tar bomb in malicious chart archive decompresses to enormous size, exhausting available memory and crashing Helm | 3.17.3 | [GHSA-4hfp-h4cw-hj8p](https://github.com/advisories/GHSA-4hfp-h4cw-hj8p) |
| CVE-2025-32387 / GHSA-5xqw-8hwv-wg92 | Moderate (CVSS 7.5) | Deeply nested `$ref` chain in chart JSON Schema triggers recursive parsing that exhausts stack memory | 3.17.3 | [GHSA-5xqw-8hwv-wg92](https://github.com/advisories/GHSA-5xqw-8hwv-wg92) |
| CVE-2025-53547 / GHSA-557j-xg8c-q2mm | High (CVSS 7.3) | Malicious `Chart.yaml` symlinks `Chart.lock` to an executable file (e.g., a shell script), enabling unintended code execution during `helm dependency update` | 3.17.4 / 3.18.4 | [GHSA-557j-xg8c-q2mm](https://github.com/advisories/GHSA-557j-xg8c-q2mm) |
| CVE-2025-55198 / GHSA-f9f8-9pmf-xv68 | Moderate (CVSS 7.5) | Malformed YAML in `Chart.yaml` (null maintainers, invalid import-values) or empty entries in `index.yaml` cause Helm to panic and crash | 3.18.5 | [GHSA-f9f8-9pmf-xv68](https://github.com/advisories/GHSA-f9f8-9pmf-xv68) |
| CVE-2025-55199 / GHSA-9h84-qmv7-982p | Moderate (CVSS 7.5) | JSON Schema `$ref` pointing to a system path (e.g., `/dev/zero`) causes Helm to consume all available memory and OOM-crash | 3.18.5 | [GHSA-9h84-qmv7-982p](https://github.com/advisories/GHSA-9h84-qmv7-982p) |
| CVE-2026-35206 / GHSA-hr2v-4r36-88hr | Moderate | `helm pull --untar` writes files into current working directory rather than a named subdirectory, risking overwrite of existing files | 3.20.2 / 4.1.4 | [GHSA-hr2v-4r36-88hr](https://github.com/advisories/GHSA-hr2v-4r36-88hr) |
| CVE-2026-35205 / GHSA-q5jf-9vfq-h4h7 | High | Helm v4 fails to enforce signature/provenance verification for plugins lacking provenance files, enabling unsigned plugin installation | 4.1.4 | [GHSA-q5jf-9vfq-h4h7](https://github.com/advisories/GHSA-q5jf-9vfq-h4h7) |
| CVE-2026-35204 / GHSA-vmx8-mqv2-9gmg | High (CVSS 9.9) | Crafted Helm v4 plugin exploits path traversal to write plugin contents to arbitrary filesystem locations, enabling potential system compromise | 4.1.4 | [GHSA-vmx8-mqv2-9gmg](https://github.com/advisories/GHSA-vmx8-mqv2-9gmg) |

**Withdrawn advisory:** GHSA-jw44-4f3j-q396 / CVE-2019-25210 — `--dry-run` exposing secret values in plaintext was initially filed as a vulnerability but subsequently withdrawn; the behavior was intentional and documented.

## Security Posture Notes

Helm is a CNCF-graduated project and the de facto package manager for Kubernetes. It has a well-documented security disclosure process via cncf-helm-security@lists.cncf.io and publishes advisories through both GitHub Security Advisories and the Helm repository.

Advisory history spans three distinct eras:

**Helm 2 / Tiller era (2019–2020):** The Helm 2 architecture used a server-side component (Tiller) running with cluster-admin privileges inside Kubernetes. Multiple high-severity advisories targeted Tiller's TLS validation (GHSA-x6r5-vxfg-gq3v, CVSS 9.8) and symlink/archive extraction flaws (GHSA-p5pc-m4q7-7qm9, GHSA-xrxm-mvqm-r553). Helm 2 was fully deprecated and reached end-of-life on November 13, 2020. All Helm 2 deployment should be considered unsupported.

**Helm 3 core (2020–2024):** Helm 3 removed Tiller but introduced new attack surfaces around template functions (`lookup` leaking cluster data, `getHostByName` DNS leakage), plugin handling (zip-slip, name injection, hook override), repository index manipulation (duplicate-entry injection), and the `strvals` input parser (multiple OOM/stack-overflow DoS vectors). The 3.3.2, 3.10.3, 3.14.1, and 3.14.2 releases each addressed clusters of related issues.

**Helm v3/v4 JSON Schema and input parsing (2025–2026):** Recent advisories center on malicious chart inputs that exhaust resources: decompression bombs (GHSA-4hfp-h4cw-hj8p), nested `$ref` stack exhaustion (GHSA-5xqw-8hwv-wg92, GHSA-9h84-qmv7-982p), malformed YAML panics (GHSA-f9f8-9pmf-xv68), and an unusual symlink-to-executable code execution path via `Chart.yaml` (GHSA-557j-xg8c-q2mm). Helm v4 (2025–2026) introduced a new plugin signing model but shipped with a critical path-traversal flaw (GHSA-vmx8-mqv2-9gmg, CVSS 9.9) and a signature-verification bypass (GHSA-q5jf-9vfq-h4h7) fixed in 4.1.4.

Latest stable versions: v3.21.2 (2026-06-20) and v4.1.4. Users should stay current given the active advisory cadence.

## Dependencies of Note

- `golang.org/x/crypto` — CVE-2020-7919 (GHSA-cjjc-xp8v-855w) affected Helm via a dependency-level X.509 parsing flaw.
- Helm v3 depends on `k8s.io/client-go` for cluster API access; the `lookup` template function exposes the full Kubernetes API surface to chart templates.

## Open Questions

- Are there additional advisories for `helm.sh/helm/v4` beyond the 2026-04 cluster? v4 was recently released and the advisory surface is still developing.
- What is the threat model for Helm chart repositories hosted in public registries (e.g., Artifact Hub)? Several advisories exploit malicious repository content.
- Has a formal security audit of Helm 3/4 core been published by a third party?

## Related Pages

- [[kubernetes/containerd]]
- [[kubernetes/kube-apiserver]]
- [[kubernetes/index]]

---
*Last updated: 2026-06-23 | Sources: 27 GHSA advisories (github/advisory-database)*
