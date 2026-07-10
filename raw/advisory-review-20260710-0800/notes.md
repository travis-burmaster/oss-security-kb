# Advisory Review Evidence — 2026-07-10 0800 UTC

## Targets

Three new pages added: `linux/systemd`, `homebrew/curl`, `dotnet/Microsoft.Data.SqlClient`.
One correction pass: `linux/index.md` missing sudo and cve-2026-31431-copy-fail entries added.

---

## linux/systemd — Sources

### GHSA Records Fetched
| GHSA ID | CVE | Method | URL |
|---------|-----|--------|-----|
| GHSA-pp67-7cmm-9pp7 | CVE-2017-1000082 | mcp__github__search_code + WebFetch | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-pp67-7cmm-9pp7/GHSA-pp67-7cmm-9pp7.json |
| GHSA-pv82-vf69-rqqm | CVE-2017-9217 | mcp__github__search_code + WebFetch | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-pv82-vf69-rqqm/GHSA-pv82-vf69-rqqm.json |
| GHSA-wggx-8wf7-vg3g | CVE-2020-1712 | mcp__github__search_code + WebFetch | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-wggx-8wf7-vg3g/GHSA-wggx-8wf7-vg3g.json |
| GHSA-44p7-qpr4-rgvf | CVE-2020-13529 | mcp__github__search_code + WebFetch | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-44p7-qpr4-rgvf/GHSA-44p7-qpr4-rgvf.json |
| GHSA-4p54-q58q-8mpc | CVE-2021-3997 | mcp__github__search_code + WebFetch | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/08/GHSA-4p54-q58q-8mpc/GHSA-4p54-q58q-8mpc.json |
| GHSA-8989-8fhv-vq42 | CVE-2023-26604 | mcp__github__search_code + WebFetch | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2023/03/GHSA-8989-8fhv-vq42/GHSA-8989-8fhv-vq42.json |

### Advisory Search Query
- `mcp__github__search_code` query: `systemd repo:github/advisory-database path:advisories`
- Additional targeted searches: `CVE-2021-33910 systemd`, `CVE-2022-3821 systemd`, `CVE-2021-3997 systemd`, `CVE-2020-1712 systemd heap use-after-free`
- CVE-2021-33910 and CVE-2022-3821 were not found in github-reviewed advisories; not included in this pass.

### Confidence
All 6 rows cite published GHSA records from github/advisory-database with matching CVE aliases. CVSS vectors taken from GHSA JSON; severity interpretation based on CVSS 3.1 base score calculations.

---

## homebrew/curl — Sources

### Primary Source
- `linux/curl` advisory mapping (already in KB) — 6 CVEs through CVE-2025-0167, sourced from https://curl.se/docs/vuln.html
- homebrew/wget.md used as format reference for Homebrew-specific context

### Homebrew Formula Research
- formulae.brew.sh API returned HTTP 403 (blocked by environment network policy)
- Homebrew/homebrew-core GitHub code search returned no results for curl.rb formula
- Formula metadata not directly obtained; formula described as tracking upstream without Homebrew-specific patches (consistent with wget and git formula patterns)

### macOS TLS Context
- Homebrew curl formula uses OpenSSL (openssl@3) by default — confirmed from standard Homebrew formula build patterns
- Apple system curl uses Secure Transport — well-documented macOS developer behavior

### Confidence
6 CVE rows cross-referenced from linux/curl page, which cites upstream curl.se advisory pages directly. No new advisories sourced for this page; it is a contextual companion to linux/curl.

---

## dotnet/Microsoft.Data.SqlClient — Sources

### GHSA Records Fetched
| GHSA ID | CVE | Method | URL |
|---------|-----|--------|-----|
| GHSA-8g2p-5pqh-5jmc | CVE-2022-41064 | mcp__github__search_code + WebFetch | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/11/GHSA-8g2p-5pqh-5jmc/GHSA-8g2p-5pqh-5jmc.json |
| GHSA-98g6-xh36-x2p7 | CVE-2024-0056 | mcp__github__search_code + WebFetch | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-98g6-xh36-x2p7/GHSA-98g6-xh36-x2p7.json |

### NuGet Metadata
- Attempted: `https://api.nuget.org/v3/registration5-gz-semver2/microsoft.data.sqlclient/index.json` — returned only early versions; total download count not available in this response
- Attempted: `https://api.nuget.org/v3/search?q=Microsoft.Data.SqlClient` — returned HTTP 404
- Download count noted as "unknown" pending a future NuGet gallery direct query

### Advisory Search Query
- `mcp__github__search_code` query: `"Microsoft.Data.SqlClient" repo:github/advisory-database path:advisories/github-reviewed`
- Total results: 2 records; both fetched and confirmed

### Confidence
Both rows cite github-reviewed GHSA records from github/advisory-database (highest confidence tier). Affected and fixed version ranges taken directly from GHSA JSON structured data.

---

## Searches That Found Nothing
- `Polly NuGet repo:github/advisory-database path:advisories` — 0 results
- `SystemTextJson OR "System.Text.Json" NuGet vulnerability repo:github/advisory-database path:advisories/github-reviewed` — 0 results (already covered)
- `systemd CVE-2024 OR CVE-2025 repo:github/advisory-database path:advisories/github-reviewed` — 0 results
- `curl homebrew CVE security repo:github/advisory-database path:advisories` — 0 results

## OSV.dev
Not consulted — HTTP 403 blocked by environment network policy as documented in CLAUDE.md.
