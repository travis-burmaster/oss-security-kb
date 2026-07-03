# Advisory Review Notes — 2026-07-03 0600 UTC

## Targets

- `rust/crossbeam` (crates.io) — crossbeam concurrency workspace
- `linux/glibc` (Linux distro) — GNU C Library
- `dotnet/RestSharp` (NuGet) — lightweight HTTP client

## Method

- OSV.dev API: HTTP 403 (blocked by network policy); not used.
- RustSec advisories: fetched via `raw.githubusercontent.com/rustsec/advisory-db/main/crates/<crate>/<ID>.md` and confirmed via `mcp__github__search_code` in `repo:rustsec/advisory-db`.
- GHSA records: fetched via `raw.githubusercontent.com/github/advisory-database/main/advisories/.../<GHSA-id>/<GHSA-id>.json` and confirmed via `mcp__github__search_code` in `repo:github/advisory-database`.
- Registry metadata: crates.io API (`https://crates.io/api/v1/crates/<name>`), NuGet gallery web page.

---

## crossbeam

### Sources consulted

| Advisory | Source URL |
|----------|-----------|
| RUSTSEC-2018-0009 / CVE-2018-20996 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/crossbeam/RUSTSEC-2018-0009.md |
| RUSTSEC-2022-0029 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/crossbeam/RUSTSEC-2022-0029.md |
| RUSTSEC-2022-0020 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/crossbeam/RUSTSEC-2022-0020.md |
| RUSTSEC-2020-0052 / CVE-2020-15254 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/crossbeam-channel/RUSTSEC-2020-0052.md |
| RUSTSEC-2022-0019 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/crossbeam-channel/RUSTSEC-2022-0019.md |
| RUSTSEC-2025-0024 / CVE-2025-4574 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/crossbeam-channel/RUSTSEC-2025-0024.md |
| RUSTSEC-2021-0093 / CVE-2021-32810 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/crossbeam-deque/RUSTSEC-2021-0093.md |
| RUSTSEC-2022-0041 / CVE-2022-23639 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/crossbeam-utils/RUSTSEC-2022-0041.md |
| RUSTSEC-2022-0021 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/crossbeam-queue/RUSTSEC-2022-0021.md (confirmed via search snippet; full fetch not performed — sibling of RUSTSEC-2022-0019/0020) |
| crates.io metadata | https://crates.io/api/v1/crates/crossbeam and https://crates.io/api/v1/crates/crossbeam-channel |

### Key facts

- crossbeam: 115,642,476 total downloads; 24,739,981 recent (90d); current version 0.8.4 (2024-01-08)
- crossbeam-channel: 493,578,334 total downloads; 102,017,121 recent (90d); current version 0.5.15 (2025-04-08)
- Two advisories have full CVSS: RUSTSEC-2018-0009 (9.8 CVSS:3.0) and RUSTSEC-2021-0093 (9.8 CVSS:3.1)
- RUSTSEC-2025-0024 carries TROVE-2025-013 alias (new namespace)
- All 0.5.12–0.5.14 crossbeam-channel versions were yanked from crates.io

---

## glibc

### Sources consulted

| Advisory | Source URL |
|----------|-----------|
| CVE-2015-0235 GHOST | https://github.com/advisories/GHSA-jwcp-p679-fcr4 |
| CVE-2015-7547 | https://github.com/advisories/GHSA-5xr7-h7cp-w9pc |
| CVE-2021-3326 | https://github.com/advisories/GHSA-w279-vhxx-7qx8 |
| CVE-2021-33574 | https://github.com/advisories/GHSA-rx5m-j84j-22pg |
| CVE-2023-4911 Looney Tunables | https://github.com/advisories/GHSA-m77w-6vjw-wh2f |
| CVE-2025-0577 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/02/GHSA-7qhw-4fcq-2g37/GHSA-7qhw-4fcq-2g37.json |
| glibc version | https://sourceware.org/glibc/ |

### Key facts

- Current upstream stable: glibc 2.43 (released 2026-01-23)
- CVE-2023-4911 (Looney Tunables) is in CISA KEV (confirmed exploitation)
- CVE-2021-33574 NVD severity (9.8) is disputed by Amazon Linux, Ubuntu, Red Hat who rate it Low/Medium
- No central download stats — distributed through OS package managers

---

## RestSharp

### Sources consulted

| Advisory | Source URL |
|----------|-----------|
| GHSA-9pq7-rcxv-47vq / CVE-2021-27293 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/07/GHSA-9pq7-rcxv-47vq/GHSA-9pq7-rcxv-47vq.json |
| GHSA-4rr6-2v9v-wcpc / CVE-2024-45302 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/08/GHSA-4rr6-2v9v-wcpc/GHSA-4rr6-2v9v-wcpc.json |
| NuGet metadata | https://www.nuget.org/packages/RestSharp |

### Key facts

- Total NuGet downloads: 561,700,000+; current version 114.0.0
- GHSA-4rr6-2v9v-wcpc affects range: 107.0.0-preview.1 to < 112.0.0 (entire v107–v111 series)
- GHSA-9pq7-rcxv-47vq affects range: all versions < 106.11.8-alpha.0.13 (fixed in 106.x series)
- GitHub advisory database contains exactly 2 reviewed advisories for this package
