# Advisory Review — 2026-07-25

**Pass date:** 2026-07-25
**Targets:** rust/wasmtime (new page), rust/tar (new page)
**Ecosystem focus:** Rust / crates.io (under-covered relative to npm/Python)
**OSV.dev status:** HTTP 403 (blocked by network policy) — not used

## URLs Consulted

### wasmtime

- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2021-0110.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2022-0016.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2022-0076.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2022-0095.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2022-0096.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2022-0097.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2022-0099.md (duplicate of RUSTSEC-2022-0016; same CVE-2022-24791 / GHSA-gwc9-348x-qwv2; deduplicated)
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2022-0100.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2023-0090.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2023-0093.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2024-0439.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2025-0046.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2025-0118.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2026-0020.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2026-0085.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2026-0087.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2026-0088.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/wasmtime/RUSTSEC-2026-0089.md
- https://crates.io/api/v1/crates/wasmtime (max_version: 47.0.2; recent_downloads: 7,568,765; total: 29,431,673)
- mcp__github__search_code: repo:rustsec/advisory-db path:crates wasmtime (45 results, all wasmtime/* and sibling crate advisories)

### tar

- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/tar/RUSTSEC-2018-0002.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/tar/RUSTSEC-2021-0080.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/tar/RUSTSEC-2026-0067.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/tar/RUSTSEC-2026-0068.md
- https://crates.io/api/v1/crates/tar (max_version: 0.4.46; recent_downloads: 43,357,839; total: 196,600,951)
- mcp__github__search_code: repo:rustsec/advisory-db path:crates/tar (4 results, all mapped)

## Deduplication Notes

- RUSTSEC-2022-0016 and RUSTSEC-2022-0099 share the same CVE (CVE-2022-24791) and GHSA (GHSA-gwc9-348x-qwv2). They appear as two advisory-db entries with slightly different dates (2022-03-31 vs 2022-03-28) and identical patched ranges. Both reference the externref + epoch-interruption UAF. Mapped as a single row in the vulnerability table.

## Sibling Crates (out of scope, noted for future passes)

- `wasmtime-wasi`: RUSTSEC-2026-0182 / GHSA-3p27-qvp9-27qf (2026-06-15, guest-controlled panic via WASI preview2)
- `wasmtime-jit-debug`: RUSTSEC-2024-0442 (2024-07-06, unsoundness in JIT debug helper)

## Index Changes

- wiki/rust/index.md: 24 → 26 pages (added wasmtime, tar)
- wiki/index.md: 234 → 236 pages (Rust section 24 → 26)
- wiki/log.md: prepended 2026-07-25 entry
