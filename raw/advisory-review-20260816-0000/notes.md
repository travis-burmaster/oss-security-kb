# Advisory Review — 2026-08-16

## Targets

- `rust/hickory-dns` (hickory-dns / trust-dns ecosystem, Rust/crates.io)
- `homebrew/gnupg` (GnuPG OpenPGP implementation, Homebrew)

---

## hickory-dns / trust-dns

### Discovery

- `mcp__github__search_code` query: `hickory repo:rustsec/advisory-db path:crates` → 7 results
- `mcp__github__search_code` query: `trust-dns repo:rustsec/advisory-db path:crates` → 4 results

### Advisories Fetched (WebFetch raw.githubusercontent.com)

| Advisory | URL |
|----------|-----|
| RUSTSEC-2018-0007 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/trust-dns-proto/RUSTSEC-2018-0007.md |
| RUSTSEC-2020-0001 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/trust-dns-server/RUSTSEC-2020-0001.md |
| RUSTSEC-2023-0041 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/trust-dns-server/RUSTSEC-2023-0041.md |
| RUSTSEC-2025-0006 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/hickory-proto/RUSTSEC-2025-0006.md |
| RUSTSEC-2025-0017 (informational) | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/trust-dns-proto/RUSTSEC-2025-0017.md |
| RUSTSEC-2025-0013 (unrelated: `resolve` crate unmaintained) | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/resolve/RUSTSEC-2025-0013.md |
| RUSTSEC-2026-0106 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/hickory-recursor/RUSTSEC-2026-0106.md |
| RUSTSEC-2026-0118 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/hickory-proto/RUSTSEC-2026-0118.md |
| RUSTSEC-2026-0119 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/hickory-proto/RUSTSEC-2026-0119.md |
| RUSTSEC-2026-0120 | https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/hickory-net/RUSTSEC-2026-0120.md |

RUSTSEC-2025-0013 excluded (unrelated `resolve` crate, not hickory-dns). RUSTSEC-2025-0017 excluded from vulnerability table (informational: unmaintained notice).

### Download Stats (crates.io API)

- `hickory-proto`: ~19.5M recent weekly downloads; ~70M total; max_version 0.26.1
- `hickory-resolver`: ~18.8M recent weekly downloads; ~68M total; max_version 0.26.1
- `hickory-client`: ~324K recent weekly downloads; ~1.6M total; max_version 0.26.0-alpha.1
- `hickory-dns` (meta-crate): ~2K recent weekly downloads; ~25K total; max_version 0.26.1
- `trust-dns-resolver` (legacy): ~2.8M recent weekly downloads; ~55.7M total

---

## homebrew/gnupg

### Discovery

- `mcp__github__search_code` queries against `github/advisory-database` using CVE IDs
- Homebrew formula version confirmed: https://raw.githubusercontent.com/Homebrew/homebrew-core/master/Formula/g/gnupg.rb → 2.5.21
- formulae.brew.sh API: blocked (HTTP connection error)

### CVEs Confirmed

| CVE | GHSA | URL |
|-----|------|-----|
| CVE-2019-14855 | GHSA-cpvm-f36g-55vg | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-cpvm-f36g-55vg/GHSA-cpvm-f36g-55vg.json |
| CVE-2022-34903 | GHSA-356p-pg27-x2cf | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/07/GHSA-356p-pg27-x2cf/GHSA-356p-pg27-x2cf.json |
| CVE-2025-68972 | GHSA-w789-3q45-984r | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2025/12/GHSA-w789-3q45-984r/GHSA-w789-3q45-984r.json |
| CVE-2025-68973 | GHSA-pj23-86ww-f72p | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2025/12/GHSA-pj23-86ww-f72p/GHSA-pj23-86ww-f72p.json |

All four GHSAs are "unreviewed" (NVD-imported, not github-reviewed). Severity from GHSA database_specific.severity field; descriptions verified against references.

### Additional References

- GnuPG announcement 2.2.18: https://lists.gnupg.org/pipermail/gnupg-announce/2019q4/000442.html
- RWC 2020 SHA-1 slides (Leurent): https://rwc.iacr.org/2020/slides/Leurent.pdf
- dev.gnupg.org/T4755 (CVE-2019-14855): https://dev.gnupg.org/T4755
- dev.gnupg.org/T6027 (CVE-2022-34903): https://dev.gnupg.org/T6027
- gpg.fail/formfeed (CVE-2025-68972): https://gpg.fail/formfeed
- gpg.fail/memcpy (CVE-2025-68973): https://gpg.fail/memcpy
- CCC 2025 talk: https://media.ccc.de/v/39c3-to-sign-or-not-to-sign-practical-vulnerabilities-i
- GitHub commit fixing CVE-2025-68973 in 2.2.x: https://github.com/gpg/gnupg/compare/gnupg-2.2.50...gnupg-2.2.51
- NVD: blocked. Severity scores taken from GHSA database_specific fields.
