# Advisory Review 2026-07-08 — Source Evidence

**Pass date:** 2026-07-08
**Targets:** bytes (crates.io), bash (Linux), wget (Homebrew)
**Index corrections:** crossbeam (crates.io), glibc (Linux) added to master index

## Sources Consulted

### bytes (crates.io) — RUSTSEC-2026-0007 / CVE-2026-25541 / GHSA-434x-w66g-qw3r

- RustSec advisory: https://rustsec.org/advisories/RUSTSEC-2026-0007.html
- GHSA record: https://github.com/advisories/GHSA-434x-w66g-qw3r
- GitHub tokio-rs/bytes security advisories: https://github.com/tokio-rs/bytes/security/advisories
- crates.io downloads: https://crates.io/crates/bytes (fetched 2026-07-08; ~836M all-time, ~14.5M/week est.)
- GitHub advisory-database: searched via mcp__github__search_code repo:github/advisory-database GHSA-434x-w66g-qw3r
- RustSec advisory-db: searched via mcp__github__search_code repo:rustsec/advisory-db bytes

### bash (Linux) — ShellShock cluster + CVE-2022-3715

- GHSA-6hfc-grwp-2p9c (CVE-2014-6271): https://github.com/advisories/GHSA-6hfc-grwp-2p9c
- GHSA-f7j6-xrjp-vffg (CVE-2014-7169): https://github.com/advisories/GHSA-f7j6-xrjp-vffg
- GHSA-55cc-h8m2-x3mp (CVE-2014-6277): https://github.com/advisories/GHSA-55cc-h8m2-x3mp
- GHSA-6493-28fj-f93w (CVE-2014-6278): https://github.com/advisories/GHSA-6493-28fj-f93w
- GHSA-cr4j-fv7c-759c (CVE-2022-3715): https://github.com/advisories/GHSA-cr4j-fv7c-759c
- GNU bash upstream repository: https://git.savannah.gnu.org/cgit/bash.git
- CISA KEV catalog (ShellShock): https://www.cisa.gov/known-exploited-vulnerabilities-catalog

### wget (Homebrew) — CVE-2024-38428 + CVE-2016-4971

- GHSA-2j66-vp53-phjj (CVE-2024-38428): https://github.com/advisories/GHSA-2j66-vp53-phjj
- GHSA-5w8p-rj9f-xvj7 (CVE-2016-4971): https://github.com/advisories/GHSA-5w8p-rj9f-xvj7
- GNU wget upstream repository: https://git.savannah.gnu.org/cgit/wget.git
- Upstream commit ed0c7c7 (CVE-2024-38428 fix): referenced in GHSA advisory

### Index corrections — crossbeam and glibc

- wiki/rust/crossbeam.md: pre-existing page (9 advisories, last updated 2026-07-03); absent from wiki/index.md Rust section
- wiki/linux/glibc.md: pre-existing page (6 advisories, last updated 2026-07-03); absent from wiki/index.md Linux section
- Discovered via Glob scan of wiki/rust/*.md and wiki/linux/*.md vs master index

## Blocked Sources

- OSV.dev API (https://api.osv.dev): HTTP 403, blocked by environment network policy
- Homebrew formulae.brew.sh analytics API: HTTP 403
- raw.githubusercontent.com: intermittent HTTP 429 (rate limited); worked around via mcp__github__search_code
