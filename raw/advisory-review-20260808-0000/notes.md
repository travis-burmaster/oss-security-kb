# Advisory Review Notes — 2026-08-08

**Pass type:** advisory-mapping  
**Targets:** linux/apache2 (new), rust/rocket (new)  
**OSV.dev:** blocked (HTTP 403) — using fallback sources throughout

---

## linux/apache2

### Sources consulted
- `mcp__github__search_code` query: `apache httpd repo:github/advisory-database path:advisories` — 371 results
- `mcp__github__search_code` query: `apache httpd CVE-2021-41773 repo:github/advisory-database` — 2 results
- `mcp__github__search_code` query: `apache httpd CVE-2021-42013 repo:github/advisory-database` — 1 result (GHSA-m24x-wx9p-jqmh)
- `mcp__github__search_code` query: `apache httpd CVE-2021-40438 repo:github/advisory-database` — 1 result (GHSA-rwxq-58vm-3v2j)
- `mcp__github__search_code` query: `apache httpd CVE-2024-38474 repo:github/advisory-database` — 1 result (GHSA-x6g9-g4wf-qrf7)
- WebFetch: `https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-29h7-gr57-5f8r/GHSA-29h7-gr57-5f8r.json` — CVE-2021-41773 path traversal
- WebFetch: `https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-m24x-wx9p-jqmh/GHSA-m24x-wx9p-jqmh.json` — CVE-2021-42013 incomplete fix
- WebFetch: `https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-rwxq-58vm-3v2j/GHSA-rwxq-58vm-3v2j.json` — CVE-2021-40438 SSRF
- WebFetch: `https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2024/07/GHSA-x6g9-g4wf-qrf7/GHSA-x6g9-g4wf-qrf7.json` — CVE-2024-38474 mod_rewrite
- WebFetch: `https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-9mgw-4qp5-wrrj/GHSA-9mgw-4qp5-wrrj.json` — CVE-2017-3167 auth bypass
- NVD references used as primary sources for CVE-2019-0211, CVE-2022-22720, CVE-2022-36760, CVE-2023-25690, CVE-2024-38475, CVE-2024-38476
- httpd.apache.org blocked by egress proxy; NVD used as authoritative fallback for version-range data

### Confirmed GHSA IDs (directly fetched)
- GHSA-9mgw-4qp5-wrrj → CVE-2017-3167 (Critical: auth bypass via ap_get_basic_auth_pw)
- GHSA-29h7-gr57-5f8r → CVE-2021-41773 (High: path traversal in 2.4.49)
- GHSA-m24x-wx9p-jqmh → CVE-2021-42013 (Critical: incomplete fix, RCE)
- GHSA-rwxq-58vm-3v2j → CVE-2021-40438 (Critical: SSRF via mod_proxy, CISA KEV)
- GHSA-x6g9-g4wf-qrf7 → CVE-2024-38474 (Critical: mod_rewrite substitution encoding)

### Advisories cited via NVD (not fetched from GHSA directly)
- CVE-2019-0211 — local privilege escalation via MPM scoreboard
- CVE-2022-22720 — HTTP request smuggling (inbound connection handling)
- CVE-2022-36760 — mod_proxy_ajp HTTP request smuggling
- CVE-2023-25690 — mod_proxy HTTP request smuggling via RewriteRule/ProxyPassMatch
- CVE-2024-38475 — mod_rewrite improper output escaping
- CVE-2024-38476 — backend response header SSRF/info disclosure

### Notes
- All 371 github/advisory-database results include many mod_dav_svn (Subversion) advisories that apply to the Subversion package, not to core httpd; filtered to core httpd CVEs only.
- GHSA records in the `unreviewed` path all have `"affected": []`; version ranges sourced from NVD prose.
- httpd.apache.org/security/vulnerabilities_24.html was blocked by egress proxy; NVD data is equivalent.

---

## rust/rocket

### Sources consulted
- `mcp__github__search_code` query: `rocket repo:rustsec/advisory-db path:crates` — 2 results
- WebFetch: `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/rocket/RUSTSEC-2021-0044.md`
- WebFetch: `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/rocket/RUSTSEC-2020-0028.md`
- WebFetch: `https://crates.io/api/v1/crates/rocket` — download stats

### Confirmed advisories
- RUSTSEC-2020-0028 — LocalRequest::clone multiple mutable references (0.4.0–0.4.4, fixed 0.4.5)
- RUSTSEC-2021-0044 — use-after-free in uri::Formatter (< 0.4.7, fixed 0.4.7)

### Download stats (2026-08-08)
- All-time downloads: 12,489,085
- Recent downloads: 1,230,773
- max_version: 0.5.1

---

## Index changes
- wiki/linux/index.md: added apache2 entry
- wiki/rust/index.md: added rocket entry
- wiki/index.md: Linux 13→14, Rust 31→32, total 248→250
- wiki/log.md: prepended 2026-08-08 entry
