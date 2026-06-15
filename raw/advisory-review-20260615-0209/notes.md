# Advisory Review Pass — 2026-06-15 02:09 UTC

## Targets

- rust/openssl (crates.io) — Rust bindings for OpenSSL (sfackler/rust-openssl)
- dotnet/Microsoft.IdentityModel.JsonWebTokens (NuGet) — Microsoft JWT library
- linux/openssh — OpenSSH server/client (upstream advisory mapping)

## Sources Used

### rust/openssl
- RustSec advisory database at rustsec/advisory-db (github.com code search + raw.githubusercontent.com):
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl/RUSTSEC-2016-0001.md
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl/RUSTSEC-2018-0010.md
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl/RUSTSEC-2023-0022.md
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl/RUSTSEC-2023-0023.md
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl/RUSTSEC-2023-0024.md
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl/RUSTSEC-2023-0044.md
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl/RUSTSEC-2023-0072.md
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl/RUSTSEC-2024-0357.md
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl/RUSTSEC-2025-0004.md
  - https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl/RUSTSEC-2025-0022.md
- sfackler/rust-openssl repository (upstream fix PRs/issues referenced by advisories):
  - https://github.com/sfackler/rust-openssl/releases/tag/v0.9.0 (RUSTSEC-2016-0001)
  - https://github.com/sfackler/rust-openssl/pull/942 (RUSTSEC-2018-0010)
  - https://github.com/sfackler/rust-openssl/pull/1854 (RUSTSEC-2023-0022/0023/0024)
  - https://github.com/sfackler/rust-openssl/issues/1965 (RUSTSEC-2023-0044)
  - https://github.com/sfackler/rust-openssl/issues/2096 (RUSTSEC-2023-0072)
  - https://github.com/sfackler/rust-openssl/pull/2266 (RUSTSEC-2024-0357)
  - https://github.com/sfackler/rust-openssl/security/advisories/GHSA-rpmj-rpgj-qmpm (RUSTSEC-2025-0004)
  - https://github.com/sfackler/rust-openssl/pull/2390 (RUSTSEC-2025-0022)
- Network access to crates.io API and osv.dev was blocked by environment policy.
  Weekly downloads marked "unknown" per SCHEMA conventions.

### dotnet/Microsoft.IdentityModel.JsonWebTokens
- github/advisory-database (GitHub MCP code search):
  - advisories/github-reviewed/2024/01/GHSA-59j7-ghrg-fj52/GHSA-59j7-ghrg-fj52.json
  - advisories/github-reviewed/2024/01/GHSA-8g9c-28fc-mcx2/GHSA-8g9c-28fc-mcx2.json (duplicate of above)
- NuGet partial metadata via api.nuget.org: 133 published versions confirmed for Microsoft.IdentityModel.Tokens;
  JsonWebTokens package confirmed in advisory ecosystem field.
- osv.dev API blocked; NuGet download count unavailable.

### linux/openssh
- github/advisory-database (GitHub MCP code search):
  - advisories/unreviewed/2023/07/GHSA-px36-p9hv-7h2v/GHSA-px36-p9hv-7h2v.json (CVE-2023-38408)
  - advisories/unreviewed/2024/07/GHSA-2x8c-95vh-gfv4/GHSA-2x8c-95vh-gfv4.json (CVE-2024-6387, regreSSHion)
  - advisories/unreviewed/2023/12/GHSA-44xq-r8h3-q4q6/GHSA-44xq-r8h3-q4q6.json (PKCS#11 dest constraint bypass)
  - advisories/unreviewed/2023/12/GHSA-45x7-px36-x8w8/GHSA-45x7-px36-x8w8.json (CVE-2023-48795, Terrapin)
  - advisories/unreviewed/2025/02/GHSA-jrwv-mv4h-7rrq/GHSA-jrwv-mv4h-7rrq.json (CVE-2025-26465)
- openssh-portable upstream repo referenced via advisory URLs
- osv.dev and nvd.nist.gov APIs blocked.

## Methodology notes
- OSV.dev API (api.osv.dev) blocked by environment network policy.
- NVD (nvd.nist.gov) blocked by environment network policy.
- rustsec.org blocked by environment network policy.
- GitHub GHSA advisory pages (github.com/advisories/*) returned 404 via WebFetch (likely auth required for rendered pages).
- raw.githubusercontent.com accessible — used for full RustSec advisory content.
- GitHub code search (mcp__github__search_code) accessible and used as primary discovery mechanism.
- All advisory content verified against source documents; no findings invented.
