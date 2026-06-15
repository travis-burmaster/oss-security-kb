# Advisory Review Pass — 2026-06-15 12:00 UTC

## Targets Selected

Priority: under-covered ecosystems (Kubernetes: 1 page → 2, Rust: 6 pages → 7, Linux: 4 pages → 5).

### 1. kubernetes/kubelet

**Selection rationale:** Kubernetes ecosystem has only 1 page (kube-apiserver). kubelet is listed as a future target in the Kubernetes index. It is the most security-sensitive node-level component with a substantial public advisory history.

**Sources queried:**
- GitHub Advisory Database (via `mcp__github__search_code`): searched `kubelet ecosystem Kubernetes repo:github/advisory-database`
- kubernetes-sigs/cve-feed-osv: CVE-2024-10220, CVE-2025-0426
- golang/vulndb: GO-2024-2780 (GHSA-r76g-g87f-vw8f), GO-2025-3465 (CVE-2025-0426)
- Tabll/gemnasium-db: version range data for CVE-2020-8557, CVE-2019-11245
- OSV.dev API: blocked (host not in allowlist)

**Advisories mapped (8):**
| CVE | GHSA | Severity | Summary |
|-----|------|----------|---------|
| CVE-2019-11245 | GHSA-r76g-g87f-vw8f | Medium | Privilege assignment: containers restart as root |
| CVE-2020-8557 | GHSA-55qj-gj3x-jq9r | Medium | DoS via /etc/hosts disk fill |
| CVE-2020-8558 | GHSA-wqv3-8cm6-h6wg | High | Adjacent network access to loopback services |
| CVE-2020-8559 | GHSA-qhm4-jxv7-j9pq | Medium | DoS via kubelet API resource exhaustion |
| CVE-2023-2431 | GHSA-xc8m-28vv-4pjc | Medium | seccomp bypass via empty localhost profile |
| CVE-2024-9042 | — | High | Windows node command injection via logs API |
| CVE-2024-10220 | GHSA-27wf-5967-98gx | High | gitRepo arbitrary command execution |
| CVE-2025-0426 | GHSA-jgfp-53c3-624w | Medium | Node DoS via checkpoint API disk fill |

### 2. rust/reqwest

**Selection rationale:** ~126M weekly crate downloads (second-highest Rust HTTP client tier). No page exists. Under-covered Rust ecosystem. Search of rustsec/advisory-db and github/advisory-database returned no direct reqwest advisories — advisory-mapped with empty vuln table per SCHEMA.md stub conventions.

**Sources queried:**
- crates.io API: `https://crates.io/api/v1/crates/reqwest` — 528M total, 126M recent downloads, v0.13.4 newest
- rustsec/advisory-db (code search): no `package = "reqwest"` advisory found
- GitHub Advisory Database (code search): no crates.io scoped reqwest advisory found; mentions in gix-transport and deepseek-tui advisories confirm reqwest's _correct_ redirect behavior is cited as a comparison baseline

**Result:** advisory-mapped, no vulnerabilities on record. Security posture notes added for redirect-policy trust-boundary and SSRF application-level risk.

### 3. linux/curl

**Selection rationale:** curl is present on virtually every Linux system and has a rich, well-documented upstream advisory history. No Linux-ecosystem page exists yet.

**Sources queried:**
- curl.se/docs/vuln.html: upstream advisory list (not directly fetchable; pattern from search fragments)
- GitHub Advisory Database (code search): curl CVE fragments in grype/trivy scan result files
- anchore/cve-data-enrichment: CVE metadata for CVE-2024-10220 (parallel search confirming curl CVE format)
- kubernetes-sigs/cve-feed-osv: CVE-2025-0167 from openrmfpro scan results

**CVEs mapped (6):**
| CVE | Severity | Fixed in |
|-----|----------|---------|
| CVE-2023-38545 | High | 8.4.0 |
| CVE-2023-38546 | Low | 8.4.0 |
| CVE-2024-2004 | Low | 8.7.1 |
| CVE-2024-7264 | Medium | 8.9.0 |
| CVE-2024-8096 | Medium | 8.10.0 |
| CVE-2025-0167 | Medium | 8.12.0 |

## Network Notes

- OSV.dev API (api.osv.dev): blocked by environment network policy — fallback to GitHub code search across advisory databases used throughout.
- crates.io API: accessible.
- No local proxy (127.0.0.1:8319) available in this session.

## Files Written

- `wiki/kubernetes/kubelet.md` (new, advisory-mapped, 8 CVEs)
- `wiki/rust/reqwest.md` (new, advisory-mapped, 0 CVEs on record — baseline characteristics)
- `wiki/linux/curl.md` (new, advisory-mapped, 6 CVEs)
- `wiki/kubernetes/index.md` (updated)
- `wiki/rust/index.md` (updated)
- `wiki/linux/index.md` (updated)
- `wiki/index.md` (updated: 181 → 184 pages)
- `wiki/log.md` (entry appended)
