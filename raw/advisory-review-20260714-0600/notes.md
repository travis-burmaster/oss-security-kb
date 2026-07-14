# Advisory Review Notes — 2026-07-14

## Targets

- rust/quinn (and quinn-proto) — Rust QUIC implementation
- dotnet/Microsoft.Data.SqlClient — .NET SQL Server driver
- homebrew/imagemagick — Homebrew ImageMagick formula

## Sources Consulted

### rust/quinn + quinn-proto
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/quinn/RUSTSEC-2021-0035.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/quinn-proto/RUSTSEC-2023-0063.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/quinn-proto/RUSTSEC-2024-0373.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/quinn-proto/RUSTSEC-2026-0037.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/quinn-proto/RUSTSEC-2026-0185.md
- https://crates.io/api/v1/crates/quinn (download stats: 225,390,513 total; 73,428,483 recent)
- https://crates.io/api/v1/crates/quinn-proto (download stats: 230,947,993 total; 75,192,634 recent)
- mcp__github__search_code: `quinn repo:rustsec/advisory-db path:crates` (5 results returned)

### dotnet/Microsoft.Data.SqlClient
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/11/GHSA-8g2p-5pqh-5jmc/GHSA-8g2p-5pqh-5jmc.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-98g6-xh36-x2p7/GHSA-98g6-xh36-x2p7.json
- https://api.nuget.org/v3-flatcontainer/microsoft.data.sqlclient/index.json (102+ versions listed, latest stable 7.0.2)
- mcp__github__search_code: `Microsoft.Data.SqlClient repo:github/advisory-database path:advisories` (2 GitHub-reviewed results)

### homebrew/imagemagick
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-24cp-26gx-3pp4/GHSA-24cp-26gx-3pp4.json (CVE-2016-3714 / ImageTragick)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2023/02/GHSA-g5qh-f5rv-grcp/GHSA-g5qh-f5rv-grcp.json (CVE-2022-44268)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2023/05/GHSA-cm6m-2vvh-cxc6/GHSA-cm6m-2vvh-cxc6.json (CVE-2023-34151)
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/07/GHSA-84mh-5fq7-7fx5/GHSA-84mh-5fq7-7fx5.json (CVE-2026-61857)
- Upstream ImageMagick advisory GHSA-qh5g-q395-cx4j (XMP UAF, June 2026): confirmed via reference in GHSA-84mh-5fq7-7fx5
- mcp__github__search_code: `imagemagick repo:github/advisory-database path:advisories` (698 total results)
- mcp__github__search_code: `CVE-2023-34151 ImageMagick repo:github/advisory-database path:advisories` → GHSA-cm6m-2vvh-cxc6
- mcp__github__search_code: `CVE-2022-44268 repo:github/advisory-database path:advisories` → GHSA-g5qh-f5rv-grcp
- formulae.brew.sh/api/formula/imagemagick.json — BLOCKED (HTTP 403, network policy)

## Blocked Sources
- api.osv.dev (HTTP 403 — network policy; advisory content sourced from rustsec/advisory-db and github/advisory-database instead)
- formulae.brew.sh (HTTP 403 — network policy; Homebrew formula stats unavailable)

## Findings Summary

- rust/quinn: 5 advisories confirmed across quinn and quinn-proto crates (RUSTSEC-2021-0035, RUSTSEC-2023-0063, RUSTSEC-2024-0373, RUSTSEC-2026-0037, RUSTSEC-2026-0185). Latest advisory RUSTSEC-2026-0185 (OOM) disclosed 2026-06-22; fixed in quinn-proto ≥ 0.11.15.
- dotnet/Microsoft.Data.SqlClient: 2 GitHub-reviewed advisories confirmed (GHSA-8g2p-5pqh-5jmc CVE-2022-41064 Moderate, GHSA-98g6-xh36-x2p7 CVE-2024-0056 High). Current stable 7.0.2 unaffected.
- homebrew/imagemagick: 4 representative advisories documented from 698+ total CVE record set. Focus on RCE (ImageTragick / CISA KEV), info disclosure (PNG file read), recurring integer overflow class, and most recent (2026 XMP UAF).
