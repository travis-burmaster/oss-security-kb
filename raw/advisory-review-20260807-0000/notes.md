# Advisory Review Notes — 2026-08-07

## Pass metadata
- Scheduled run: ~00:00 UTC 2026-08-07
- OSV.dev: blocked (HTTP 403) — not used
- Sources: github/advisory-database (mcp__github__search_code + WebFetch on raw.githubusercontent.com), rustsec/advisory-db (mcp__github__search_code + WebFetch on raw.githubusercontent.com), crates.io API, pkg.go.dev
- git push (127.0.0.1:44641): blocked (HTTP 403) — all remote writes via mcp__github__push_files

## Targets selected
1. `github.com/go-git/go-git` (Go) — pure-Go Git implementation; not previously covered; ~4,979 pkg.go.dev importers; widely used in CI/CD automation
2. `nix` crate (Rust/crates.io, nix-rust/nix) — foundational POSIX bindings; not previously covered; ~12.1M/week downloads; high blast radius

**Rejected target:** `zip` crate (Rust) — searched `zip path:crates repo:rustsec/advisory-db`; found only `zip_next` (RUSTSEC-2023-0080, unmaintained), not the `zip` crate itself. No package-level RUSTSEC advisory for `zip` confirmed. Pivoted to `nix`.

## go-git research

### Search queries
- `mcp__github__search_code`: `go-git repo:github/advisory-database` — returned GHSA file hits for go-git/go-git
- `mcp__github__search_code`: `GHSA-449p-3h89-pw88 repo:github/advisory-database` — confirmed path in 2024/01/
- `mcp__github__search_code`: `GHSA-r9px-m959-cxf4 repo:github/advisory-database` — confirmed path in 2025/01/

### URLs fetched
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-449p-3h89-pw88/GHSA-449p-3h89-pw88.json`
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-mw99-9chc-xw7r/GHSA-mw99-9chc-xw7r.json`
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/01/GHSA-v725-9546-7q7m/GHSA-v725-9546-7q7m.json`
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/01/GHSA-r9px-m959-cxf4/GHSA-r9px-m959-cxf4.json`
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/07/GHSA-389r-gv7p-r3rp/GHSA-389r-gv7p-r3rp.json`
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/08/GHSA-w5pp-99ch-qj29/GHSA-w5pp-99ch-qj29.json`
- `https://pkg.go.dev/github.com/go-git/go-git/v5` — confirmed ~4,979 importers, v5.19.2 current

### Advisory mapping confidence
- All 6 advisories sourced from github-reviewed GHSA records (highest confidence tier)
- GHSA-449p-3h89-pw88 path: 2024/01/ (not 2023/12/ as initially guessed — corrected via search_code)
- GHSA-r9px-m959-cxf4 path: 2025/01/ (confirmed)
- CVE-2026-45022 / GHSA-389r-gv7p-r3rp: GHSA-assigned severity Moderate, CVSS score 4.0
- GHSA-w5pp-99ch-qj29: GHSA-assigned severity Moderate, CVSS score 7.5 (note: standard v3.1 mapping for 7.5 is High; Moderate label used as-sourced from GHSA)

## nix research

### Search queries
- `mcp__github__search_code`: `RUSTSEC-2021-0119 repo:rustsec/advisory-db` — found advisory TOML
- `mcp__github__search_code`: `nix getgrouplist repo:rustsec/advisory-db` — corroborating hit
- `mcp__github__search_code`: `nix-rust repo:github/advisory-database` — found GHSA cross-references

### URLs fetched
- `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/nix/RUSTSEC-2021-0119.toml` — primary source
- `https://crates.io/api/v1/crates/nix` — download stats: max_version 0.31.3, ~710M total, ~157.9M 90-day

### Advisory mapping confidence
- RUSTSEC-2021-0119 confirmed from rustsec/advisory-db TOML (highest confidence tier)
- GHSA-76w9-p8mg-j927 and GHSA-wgrg-5h56-jg27 are dual GHSA IDs cross-referenced in the advisory (both cover the same vulnerability)
- Platform exclusions (not macOS, not < 0.16.0) confirmed from advisory text and patched version ranges
- No additional RUSTSEC advisories found for `nix` crate beyond RUSTSEC-2021-0119
