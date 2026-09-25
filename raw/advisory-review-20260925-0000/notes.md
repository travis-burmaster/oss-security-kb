# Advisory Review Pass — 2026-09-25

## Session context

Pass date: 2026-09-25  
OSV.dev API: blocked (HTTP 403) — not used  
Advisory sources: github/advisory-database (mcp__github__search_code + WebFetch raw.githubusercontent.com), rustsec/advisory-db (WebFetch raw.githubusercontent.com), crates.io API, pkg.go.dev

## Targets selected

1. **Rust / crates.io: `git2`** (libgit2 Rust bindings, rust-lang org)
   - Selected because: 115.7M total downloads, widely used in cargo toolchain; 4 RUSTSEC advisories found
   
2. **Go: `gorm.io/gorm`** (dominant Go ORM)
   - Selected because: 86,926 pkg.go.dev importers, no prior KB page, confirmed published GHSA advisory

Also backfilled wiki/index.md which was behind by 4 entries (borsh, atty in Rust; undertow-core, hibernate-core in Maven) from the 2026-09-23 and 2026-09-24 passes.

## URLs consulted

### git2
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/git2/RUSTSEC-2023-0002.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/git2/RUSTSEC-2026-0008.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/git2/RUSTSEC-2026-0183.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/git2/RUSTSEC-2026-0184.md
- https://crates.io/api/v1/crates/git2 (download stats, latest version)
- mcp__github__search_code: repo:rustsec/advisory-db path:crates/git2 (found 4 advisories)

### gorm.io/gorm
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-r28r-5q2m-wh2x/GHSA-r28r-5q2m-wh2x.json
- https://pkg.go.dev/gorm.io/gorm (importer count, latest version)
- https://raw.githubusercontent.com/go-gorm/gorm/master/SECURITY.md (404 — no SECURITY.md)
- mcp__github__search_code: gorm.io/gorm repo:github/advisory-database (0 results — no v2 advisories)
- mcp__github__search_code: jinzhu/gorm repo:github/advisory-database (1 result: GHSA-r28r-5q2m-wh2x)

## Advisory details confirmed

### git2 — RUSTSEC-2023-0002 (withdrawn 2023-01-13)
- Issue: SSH host key validation callback always returns 0 (accepts all keys) → MitM
- Related: CVE-2022-46176 (assigned to Cargo, not git2 directly)
- Fixed: git2 0.16.0
- Note: Advisory withdrawn from rustsec DB one day after publication

### git2 — RUSTSEC-2026-0008 / GHSA-j39j-6gw9-jw6h (Feb 2026)
- Issue: Buf::new()/default() pass null ptr to slice::from_raw_parts → UB
- Fixed: 0.20.4
- Source: https://github.com/rust-lang/git2-rs/pull/1213

### git2 — RUSTSEC-2026-0183 (May 2026)
- Issue: Remote::list() null ptr to slice::from_raw_parts when no references → UB
- Fixed: 0.21.0
- Source: https://github.com/rust-lang/git2-rs/pull/1250

### git2 — RUSTSEC-2026-0184 (May 2026)
- Issue: Blame::blame_buffer() BlameHunk Signature from null ptr → UB
- Fixed: 0.21.0
- Source: https://github.com/rust-lang/git2-rs/pull/1254

### gorm.io/gorm — CVE-2019-15562 / GHSA-r28r-5q2m-wh2x
- Package in advisory: github.com/go-gorm/gorm (old v1 module path)
- Severity: Critical CVSS 9.8 (CWE-89 SQL injection)
- Description: Incomplete parentheses in query construction allow attacker-controlled SQL injection
- Fixed: 1.9.10
- No advisory found for gorm.io/gorm v2 module path (separate Go module)

## Index corrections in this pass

- wiki/index.md: corrected from 295 to 301 pages
  - Added borsh, atty to Rust section (missing from 2026-09-24 pass backfill)
  - Added undertow-core, hibernate-core to Maven section (missing since 2026-09-23/24)
  - Added git2 to Rust section (new)
  - Added gorm.io/gorm to Go section (new)
  - Updated counts: total 295→301, Rust (42)→(45), Maven (35)→(37), Go (35)→(36)
