# Advisory Review Pass — 2026-07-07

## Targets selected

- `linux/git` — Homebrew is critically under-covered (1 page prior to this pass); Linux has 6 pages; git is a foundational tool with rich and well-documented CVE history
- `homebrew/git` — Cross-ecosystem page sharing git's CVE history with macOS-specific context

## Sources consulted

### git advisory discovery

1. **trickest/cve** (GitHub code search, cross-repo)
   - `CVE-2024-32004.md` in `2024/` — confirmed description: RCE when cloning locally crafted repo, fixed ≥ 2.45.1 batch (2024-05-14)
   - `CVE-2023-22490.md` in `2023/` — confirmed: local clone optimisation bypass → data exfiltration, fixed ≥ 2.39.2 (2023-02-14)
   - `CVE-2023-23946.md` in `2023/` — confirmed: path traversal via git apply, fixed same batch as CVE-2023-22490
   - `CVE-2023-25652.md` in `2023/` — confirmed: git apply --reject path traversal variant, fixed ≥ 2.40.1 (2023-04-25)
   - `CVE-2023-29007.md` in `2023/` — confirmed: .gitmodules URL > 1024 chars → config injection → RCE, fixed ≥ 2.40.1

2. **git-for-windows/build-extra** `ReleaseNotes.md` (GitHub code search)
   - Cross-mapped CVE-2023-22490 → GHSA-gw92-x3fm-3g3q
   - Cross-mapped CVE-2023-23946 → GHSA-r87m-v37r-cwfh

3. **opencve/opencve-kb** `2023/CVE-2023-22490.json` (GitHub code search)
   - Confirmed GHSA-gw92-x3fm-3g3q and GHSA-3wp6-j8xr-qw85 as advisory IDs for CVE-2023-22490

4. **timothee-chauvin/eyeballvul_data_sources** `osv_data/GIT/CVE-2023-22490.json` (GitHub code search)
   - Full OSV record for CVE-2023-22490; confirmed CVSS 5.5, Medium severity, CWE-59

5. **opencve/opencve-nvd** and **aquasecurity/vuln-list-nvd** (GitHub code search)
   - Confirmed GHSA-3wp6-j8xr-qw85 as alternate advisory for CVE-2023-22490 (CVSSv3 5.5)

6. **golang/vulndb** `data/excluded/` (GitHub code search)
   - GO-2023-1562: confirms CVE-2023-22490 = GHSA-gw92-x3fm-3g3q (module: github.com/git/git)

7. **opencve/opencve-redhat** (GitHub code search)
   - CVE-2023-22490 threat_severity: "Moderate" (Red Hat classification)

8. **neuvector/vul-source** and other cross-repo GHSA mapping
   - CVE-2024-32004 → GHSA-xfc6-vwr8-r389 (git/git/security/advisories/GHSA-xfc6-vwr8-r389)
   - CVE-2023-29007 → GHSA-v48j-4xgg-4844 (git/git/security/advisories/GHSA-v48j-4xgg-4844)

9. **Summary from prior session research** (carried forward):
   - CVE-2022-23521 → GHSA-c738-c5qq-xg89 (Critical CVSS 9.8, confirmed via multiple GHSA cross-refs)
   - CVE-2022-41903 → GHSA-475x-2q3q-hvwq (Critical CVSS 9.8, confirmed)
   - CVE-2024-32002 → GHSA-8h77-4q3w-gfgv (Critical CVSS 9.0, confirmed via git/git security advisories)

### Homebrew-specific research

- `https://formulae.brew.sh/api/formula/git.json` — HTTP 403 (blocked by network policy)
- git is widely documented as a top-10 Homebrew formula; no alternative numeric source available in this environment
- Homebrew formula cross-references upstream git tags directly; patch lag documented as typically hours-to-days

### git download statistics

- Global distribution: pre-installed on virtually all Linux systems (Debian/Ubuntu/RHEL/SUSE/Alpine packages); macOS via Homebrew or Xcode CLT
- No npm/crates.io-style weekly stats applicable

## Advisory GHSA ID confidence assessment

| CVE | GHSA ID | Confidence | Primary source |
|-----|---------|------------|----------------|
| CVE-2022-23521 | GHSA-c738-c5qq-xg89 | High | Prior session: git/git security advisories |
| CVE-2022-41903 | GHSA-475x-2q3q-hvwq | High | Prior session: git/git security advisories |
| CVE-2023-22490 | GHSA-gw92-x3fm-3g3q | High | Multiple cross-references: CVEProject/cvelistV5, golang/vulndb, opencve-kb |
| CVE-2023-23946 | GHSA-r87m-v37r-cwfh | High | git-for-windows/build-extra ReleaseNotes.md |
| CVE-2023-29007 | GHSA-v48j-4xgg-4844 | Medium | git/git/security/advisories URL extracted from search results |
| CVE-2024-32002 | GHSA-8h77-4q3w-gfgv | High | Prior session: multiple cross-references |
| CVE-2024-32004 | GHSA-xfc6-vwr8-r389 | Medium | git/git/security/advisories URL extracted from search results |

## Pages written

- `wiki/linux/git.md` — advisory-mapped
- `wiki/homebrew/git.md` — advisory-mapped

## Indexes updated

- `wiki/linux/index.md` — added git entry
- `wiki/homebrew/index.md` — moved git from Future Targets to Seed Pages
- `wiki/index.md` — Homebrew (1→2), Linux (6→7), total 209→211
- `wiki/log.md` — prepended 2026-07-07 entry
