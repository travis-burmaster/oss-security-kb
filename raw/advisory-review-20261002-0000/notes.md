# Advisory Review Notes — 2026-10-02

## Pass summary

- OSV.dev API: blocked (HTTP 403, per known environment policy). Not used.
- Primary sources: rustsec/advisory-db (via mcp__github__search_code + WebFetch raw.githubusercontent.com), github/advisory-database (same), crates.io API, NuGet registration API, GitHub repository metadata.

## Targets selected

1. **MailKit / MimeKit** (dotnet, NEW) — .NET email client library. Selected because .NET ecosystem was under-covered (16 pages) and MailKit is one of the most popular .NET email libraries with a known advisory history.
2. **Rust/serde** (rust, STUB UPGRADE) — serde serialization framework. Currently a baseline stub. Selected to document the third independent advisory pass confirming clean status and to upgrade the page to advisory-mapped.

---

## Target 1: MailKit / MimeKit (NuGet)

### URLs consulted

- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-g7hc-96xr-gvvx/GHSA-g7hc-96xr-gvvx.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/04/GHSA-9j88-vvj5-vhgr/GHSA-9j88-vvj5-vhgr.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/07/GHSA-gmc6-fwg3-75m5/GHSA-gmc6-fwg3-75m5.json
- https://api.nuget.org/v3/registration5-gz-semver2/mailkit/index.json (version metadata; no download counts)
- https://api.nuget.org/v3/registration5-gz-semver2/mimekit/index.json (version metadata; no download counts)
- https://raw.githubusercontent.com/jstedfast/MailKit/master/SECURITY.md
- GitHub API: api.github.com/repos/jstedfast/MailKit (returned 403; metadata sourced from rendered page)

### Search queries used

- mcp__github__search_code: `MailKit repo:github/advisory-database NuGet`
- mcp__github__search_code: `MimeKit repo:github/advisory-database NuGet`
- mcp__github__search_code: `"jstedfast/MailKit" repo:github/advisory-database`
- mcp__github__search_code: `MailKit filename:*.md repo:github/advisory-database path:advisories` (initial search)

### Advisories confirmed

| GHSA | CVE | Severity | Package | Fixed |
|------|-----|----------|---------|-------|
| GHSA-gmc6-fwg3-75m5 | — | High CVSS 7.5 | MimeKit (NuGet) ≥ 3.0.0 < 4.7.1 | MimeKit 4.7.1 |
| GHSA-g7hc-96xr-gvvx | CVE-2026-30227 | Moderate CVSS 4.0 | MimeKit + MailKit ≤ 4.15.0 | MimeKit/MailKit 4.15.1 |
| GHSA-9j88-vvj5-vhgr | CVE-2026-41319 | High CVSS 7.5 | MailKit all versions < 4.16.0 | MailKit 4.16.0 |

### Excluded advisories

- GHSA-rj4g-w683-5gq4, GHSA-28j2-6q62-7r48, GHSA-wqq2-m2pv-x493, GHSA-69c5-xxxm-r666, GHSA-3wf8-vwmj-p686 — all target the "EmailKit" WordPress plugin, not the MailKit .NET NuGet library; confirmed by reading raw JSON.

---

## Target 2: Rust/serde (stub upgrade)

### URLs consulted

- https://crates.io/api/v1/crates/serde (download stats, version info)
- https://crates.io/api/v1/crates/serde_json (download stats, version info)
- rustsec/advisory-db (via mcp__github__search_code)

### Search queries used

- mcp__github__search_code: `"crate = \"serde\"" repo:rustsec/advisory-db`
- mcp__github__search_code: `"crate = \"serde_json\"" repo:rustsec/advisory-db`
- mcp__github__search_code: `serde repo:rustsec/advisory-db` (broad; 15 results, all adjacent crates)

### Result

No RUSTSEC advisories found for `serde` or `serde_json` in three independent passes (2026-04-20, 2026-07-19, 2026-10-02). Page upgraded from baseline stub to advisory-mapped; download stats updated.

### Key stats (as of 2026-10-02)

- serde: v1.0.229, ~1.47B total downloads, ~335.4M recent 90-day (~26.1M/week est.)
- serde_json: v1.0.151, ~1.37B total downloads, ~336.8M recent 90-day (~26.2M/week est.)
