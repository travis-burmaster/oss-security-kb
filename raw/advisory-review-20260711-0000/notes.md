# Advisory Review — 2026-07-11

Pass type: public-information-only advisory mapping  
Ecosystems targeted: Maven, Homebrew, .NET/NuGet  
OSV.dev API: blocked (HTTP 403) — not consulted  
Homebrew API (formulae.brew.sh): blocked (HTTP 403) — not consulted  
Maven Central stats API: blocked (HTTP 403) — not consulted  
NuGet registration API: accessible (no per-package download counts exposed)

## Packages Researched

### maven/com.h2database/h2

**Primary sources consulted:**
- github/advisory-database via mcp__github__search_code query: `h2database OR "com.h2database" repo:github/advisory-database path:advisories extension:json`
- WebFetch of individual GHSA JSON files:
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/01/GHSA-h376-j262-vhq6/GHSA-h376-j262-vhq6.json — CVE-2021-42392 Critical CVSS 9.8 (H2 Console JNDI RCE)
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/01/GHSA-45hx-wfhj-473x/GHSA-45hx-wfhj-473x.json — CVE-2022-23221 Critical CVSS 9.8 (JDBC URL RCE)
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/12/GHSA-7rpj-hg47-cx62/GHSA-7rpj-hg47-cx62.json — CVE-2021-23463 High CVSS 7.6 (XXE in JdbcSQLXML)
  - https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/11/GHSA-22wj-vf5f-wrvj/GHSA-22wj-vf5f-wrvj.json — CVE-2022-45868 High CVSS 7.8 local (plaintext -webAdminPassword)
- Additional search: `"com.h2database" "h2" repo:github/advisory-database path:advisories extension:json CVE-2022` — confirmed 4 advisories total, no additional records found
- Maven Central metadata XML (blocked HTTP 403) — version and stats not obtained
- Download count: unknown (API blocked)
- GHSA advisory count: 4 confirmed reviewed advisories in github/advisory-database

### homebrew/curl

**Primary sources consulted:**
- Existing wiki page: wiki/linux/curl.md (last updated 2026-06-15) — provides the 6 upstream CVE records with curl.se advisory links
- formulae.brew.sh/api/formula/curl.json — blocked HTTP 403; version and analytics not obtained
- github/advisory-database search for curl/curl advisories (2025, 2026) — returned results mostly about tools using curl CLI, not libcurl CVEs; no new distinct libcurl GHSA-reviewed advisories found beyond the 6 in linux/curl
- curl.se/docs/vuln.html — blocked HTTP 403
- Homebrew formula behavior: cross-reference against prior passes for git and wget formulae, which confirmed Homebrew formula tracks upstream releases directly without custom patches

**CVE data sourced from linux/curl (cross-reference):**
- CVE-2023-38545: https://curl.se/docs/CVE-2023-38545.html
- CVE-2023-38546: https://curl.se/docs/CVE-2023-38546.html
- CVE-2024-2004: https://curl.se/docs/CVE-2024-2004.html
- CVE-2024-7264: https://curl.se/docs/CVE-2024-7264.html
- CVE-2024-8096: https://curl.se/docs/CVE-2024-8096.html (OCSP stapling — OpenSSL backend not affected)
- CVE-2025-0167: https://curl.se/docs/CVE-2025-0167.html

### dotnet/YamlDotNet

**Primary sources consulted:**
- github/advisory-database via mcp__github__search_code query: `YamlDotNet repo:github/advisory-database path:advisories extension:json` — 1 result
- WebFetch of GHSA JSON: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2018/10/GHSA-rpch-cqj9-h65r/GHSA-rpch-cqj9-h65r.json — CVE-2018-1000210 High CVSS 9.0 (insecure deserialization)
- NuGet registration API: https://api.nuget.org/v3/registration5-gz-semver2/yamldotnet/index.json — accessible; confirmed latest stable 18.1.0, last commit June 26, 2026; per-package download count not available in response
- GHSA advisory count: 1 confirmed reviewed advisory in github/advisory-database

### Index correction: dotnet/RestSharp

**Status:** wiki/dotnet/RestSharp.md existed (created 2026-07-03) but was absent from wiki/index.md. Confirmed by checking:
- Glob: wiki/dotnet/*.md → RestSharp.md present in filesystem
- wiki/dotnet/index.md → RestSharp entry present
- wiki/index.md → RestSharp entry missing (only 6 .NET entries listed)
- Correction applied: added RestSharp entry to wiki/index.md .NET section, updated count 6→8 (.NET; includes YamlDotNet added this pass)

## Confidence Assessment

| Advisory | Confidence | Basis |
|----------|-----------|-------|
| GHSA-h376-j262-vhq6 / CVE-2021-42392 | High | Full GHSA JSON fetched, details verified |
| GHSA-45hx-wfhj-473x / CVE-2022-23221 | High | Full GHSA JSON fetched, details verified |
| GHSA-7rpj-hg47-cx62 / CVE-2021-23463 | High | Full GHSA JSON fetched, details verified |
| GHSA-22wj-vf5f-wrvj / CVE-2022-45868 | High | Full GHSA JSON fetched, details verified |
| CVE-2023-38545 through CVE-2025-0167 (curl) | High | Cross-referenced from linux/curl page (sourced from curl.se advisory trail) |
| GHSA-rpch-cqj9-h65r / CVE-2018-1000210 | High | Full GHSA JSON fetched, details verified |
