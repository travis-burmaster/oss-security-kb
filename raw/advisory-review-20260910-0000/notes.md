# Advisory Review Pass — 2026-09-10 00:00 UTC

## Targets

1. **dashmap** (Rust / crates.io)
   - Package: https://crates.io/crates/dashmap
   - Repository: https://github.com/xacrimon/dashmap

2. **github.com/redis/go-redis** (Go)
   - Package: https://pkg.go.dev/github.com/redis/go-redis/v9
   - Repository: https://github.com/redis/go-redis

## URLs Consulted

### RustSec Advisory Database
- mcp__github__search_code: repo:rustsec/advisory-db dashmap
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/dashmap/RUSTSEC-2022-0002.toml

### GitHub Advisory Database
- mcp__github__search_code: repo:github/advisory-database dashmap
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/06/GHSA-mpg5-fvwp-42m2/GHSA-mpg5-fvwp-42m2.json
- mcp__github__search_code: repo:github/advisory-database go-redis
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/03/GHSA-92cp-5422-2mw7/GHSA-92cp-5422-2mw7.json

### crates.io API
- https://crates.io/api/v1/crates/dashmap (download stats, latest version)

### pkg.go.dev
- https://pkg.go.dev/github.com/redis/go-redis/v9 (importer count)

## Advisory Summary

### dashmap — RUSTSEC-2022-0002 / GHSA-mpg5-fvwp-42m2
- Type: Unsoundness (use-after-free / segfault)
- Severity: High
- Affected: dashmap ≥ 5.0.0 (< 5.1.0); versions < 5.0.0 unaffected
- Fixed: 5.1.0
- Disclosed: January 2022 (GitHub issue #167, then RustSec)

### go-redis — CVE-2025-29923 / GHSA-92cp-5422-2mw7
- Type: Out-of-order responses (data integrity)
- Severity: Low (CVSS 3.1 AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N)
- Affected: go-redis v9.5.1 – v9.7.1
- Fixed: v9.5.5, v9.6.3, v9.7.3
- Disclosed: March 2025

## Candidates Evaluated but Not Added

- async-std RUSTSEC-2025-0052 — skipped: informational/unmaintained notice, not a security vulnerability
- golang.org/x/crypto — already covered in wiki
- gorm.io/gorm — no confirmed GHSA advisories found in this pass
