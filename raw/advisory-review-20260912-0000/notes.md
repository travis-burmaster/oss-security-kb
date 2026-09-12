# Advisory Review Pass — 2026-09-12

## Targets

1. `rust/atty` — terminal-detection utility crate (crates.io)
2. `go/golang.org-x-image` — Go extended stdlib image codec module

## Sources Consulted

### rust/atty

- crates.io API: `https://crates.io/api/v1/crates/atty`
  - Total downloads: 349,083,168
  - Weekly downloads: ~30,505,185
  - Latest version: 0.2.14
- RUSTSEC-2021-0145: `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/atty/RUSTSEC-2021-0145.md`
  - ID: RUSTSEC-2021-0145 / GHSA-g98v-hv3f-hcfr
  - Issue: Unaligned pointer dereference on Windows (HANDLE reinterpret cast); formal UB, low practical risk
  - Fix: None (unmaintained)
  - Reference: https://github.com/softprops/atty/issues/50, PR #51
- RUSTSEC-2024-0375: `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/atty/RUSTSEC-2024-0375.md`
  - ID: RUSTSEC-2024-0375
  - Type: Informational (unmaintained)
  - Published: 2024-09-25
  - Recommended migration: std::io::IsTerminal (Rust ≥ 1.70.0) or `is-terminal` crate
- Upstream repository: https://github.com/softprops/atty
  - Last release: 0.2.14 (~2019); maintainer declared unmaintained in atty/issues/57

### go/golang.org-x-image

- Module: https://pkg.go.dev/golang.org/x/image — latest v0.46.0 as of 2026-09-12
- Repository: https://github.com/golang/image
- Security disclosure: https://go.dev/security
- GitHub advisory database search: `golang.org/x/image repo:github/advisory-database` — 6 results
- Advisories fetched via WebFetch on raw.githubusercontent.com:
  1. GHSA-qgc7-mgm3-q253 / CVE-2022-41727: TIFF DecodeConfig memory exhaustion → fixed 0.5.0 (Feb 2023)
  2. GHSA-j3p8-6mrq-6g7h / CVE-2023-29407: TIFF zero-height tile CPU exhaustion → fixed 0.10.0 (Aug 2023)
  3. GHSA-x92r-3vfx-4cv3 / CVE-2023-29408: TIFF compressed tile size unlimited → fixed 0.10.0 (Aug 2023)
  4. GHSA-9phm-fm57-rhg8 / CVE-2024-24792: palette-color image panic DoS → fixed 0.18.0 (Jun 2024)
  5. GHSA-44p7-9xx4-hf2g / CVE-2026-33809: TIFF 4GiB OOM allocation → fixed 0.38.0 (Mar 2026)
  6. GHSA-q675-qj96-32m9 / CVE-2026-46599: PackBits decompression DoS → fixed 0.41.0 (Jul 2026)
- All 6 GHSA records are github-reviewed advisories.

## Tools Used

- `mcp__github__search_code` — advisory database search
- `WebFetch` — raw advisory content, crates.io API, pkg.go.dev
- `mcp__github__list_commits` — main branch SHA for PR creation

## Notes

- OSV.dev API blocked (HTTP 403) as documented in CLAUDE.md; fallbacks used throughout.
- flate2 (rust) and spf13/cobra (go) investigated first; neither had entries in rustsec/advisory-db or github/advisory-database — dropped in favor of atty and golang.org/x/image which had confirmed advisories.
- The cobra search returned 5 results but none were for github.com/spf13/cobra itself.
