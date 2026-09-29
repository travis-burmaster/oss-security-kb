# Advisory Review Evidence — 2026-09-29

## Pass Summary

- **Date**: 2026-09-29
- **Ecosystem target**: Go (github.com/containerd/containerd)
- **OSV.dev**: blocked (HTTP 403) — not used
- **Primary sources**: github/advisory-database (via mcp__github__search_code + GHSA JSON WebFetch)
- **Secondary work**: master index count correction (Go and Homebrew sections)

## New Page: go/github.com/containerd/containerd

### Advisory Database Search

Query used: `containerd GHSA advisories path:advisories repo:github/advisory-database`
Total GHSA results: 36 (as of 2026-09-29)

### Advisories Fetched and Verified

| GHSA ID | CVE | Severity | Summary | Fixed In | Fetch URL |
|---------|-----|----------|---------|----------|-----------|
| GHSA-pg57-6jwg-q645 | CVE-2026-53493 | Moderate | OCI image index DoS via nested/fanned descriptor graph | 1.7.36, 2.0.13, 2.2.9, 2.3.6, 2.4.1 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/09/GHSA-pg57-6jwg-q645/GHSA-pg57-6jwg-q645.json |
| GHSA-rgh6-rfwx-v388 | CVE-2026-53489 | High | CRI checkpoint restore symlink following → arbitrary host file read | 2.1.9, 2.2.5, 2.3.2 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/06/GHSA-rgh6-rfwx-v388/GHSA-rgh6-rfwx-v388.json |
| GHSA-xhf5-7wjv-pqxp | CVE-2026-53488 | High | CRI LABEL injection → binary:// logger host-root RCE during image pull | 1.7.33, 2.0.10, 2.1.9, 2.2.5, 2.3.2 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/06/GHSA-xhf5-7wjv-pqxp/GHSA-xhf5-7wjv-pqxp.json |
| GHSA-cm76-qm8v-3j95 | CVE-2025-47290 | High | TOCTOU during image pulls → arbitrary host FS modification (affects 2.1.0 only) | 2.1.1 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/05/GHSA-cm76-qm8v-3j95/GHSA-cm76-qm8v-3j95.json |

### Additional Search Results (not yet fetched / mapped)

From the GHSA search results: GHSA-mvff-h3cj-wj9c (2022-01), GHSA-742w-89gc-8m9c (2022-02), GHSA-fqw6-gf59-qr4w (2026-05), GHSA-cxfp-7pvr-95ff (2025-05), GHSA-c9cp-9c75-9v8c (2024-05), and ~26 more.

### Known Historical Advisories (to map in future pass)

- CVE-2020-15257 — Shim API Unix socket exposed to network namespace
- CVE-2021-41103 — Insufficient permissions on container root file system
- CVE-2021-32760 — Privileged container break-out via writable host file system
- CVE-2022-23648 — Volume mount path traversal enabling access outside container
- CVE-2023-25173 — Supplemental group permissions bypass

## Master Index Correction

### File Count Audit (directory listing)

- `wiki/go/**/*.md` (excluding index.md): 35 existing pages → 36 after containerd added
- `wiki/homebrew/*.md` (excluding index.md): 9 pages

### Old vs New Counts in wiki/index.md

| Ecosystem | Old Count | New Count | Δ |
|-----------|-----------|-----------|---|
| Go | 14 | 36 | +22 |
| Homebrew | 4 | 9 | +5 |
| Total header | 305 | 281 | −24 (phantom correction) |

The net decrease in the header (305 → 281) reflects the removal of phantom entries that were being counted in the header total but had no backing files in the repository. The real page count increased by the actual new files found in Go (+22 uncounted) and Homebrew (+5 uncounted), minus the phantom entries removed from Go master entries (sprig, helm, terraform = 3 phantoms that had been counted).

Real change: 35 previously uncounted Go pages + 5 previously uncounted Homebrew pages + 1 new containerd page = +41 real pages added to the index. However the header went from 305 → 281 because 305 was inflated by ~65 phantom/overcounted entries (exact origin unclear from log history; may have accumulated across multiple early passes).

## URLs Consulted

1. https://github.com/advisories?query=containerd (GHSA search)
2. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/09/GHSA-pg57-6jwg-q645/GHSA-pg57-6jwg-q645.json
3. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/08/GHSA-72x6-4j93-7w86/GHSA-72x6-4j93-7w86.json
4. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/06/GHSA-rgh6-rfwx-v388/GHSA-rgh6-rfwx-v388.json
5. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/06/GHSA-xhf5-7wjv-pqxp/GHSA-xhf5-7wjv-pqxp.json
6. https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/05/GHSA-cm76-qm8v-3j95/GHSA-cm76-qm8v-3j95.json
7. https://github.com/containerd/containerd/blob/main/SECURITY.md
