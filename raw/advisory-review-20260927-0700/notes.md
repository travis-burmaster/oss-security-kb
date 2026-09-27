# Advisory Review — 2026-09-27 07:00 UTC

## Pass summary

Targets: rust/connectrpc (new), rust/futures (new)
Ecosystems: Rust / crates.io
Pages added: 2 (connectrpc, futures)
Advisories mapped: 5 (1 for connectrpc, 4 for futures-rs workspace)

## Tools used

- mcp__github__search_code (repo:rustsec/advisory-db) — enumerate advisory files per crate
- WebFetch on raw.githubusercontent.com/rustsec/advisory-db — retrieve advisory TOML/markdown
- WebFetch on crates.io/api/v1/crates/{name} — retrieve download stats and version metadata
- OSV.dev API blocked (HTTP 403) — not used

## URLs consulted

### connectrpc
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/connectrpc/RUSTSEC-2026-0304.md
- https://crates.io/api/v1/crates/connectrpc
- https://rustsec.org/advisories/RUSTSEC-2026-0304.html (primary source link)
- https://github.com/connectrpc/connect-rust/pull/313 (fix PR)

### futures / futures-rs workspace
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/futures-task/RUSTSEC-2020-0060.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/futures-task/RUSTSEC-2020-0061.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/futures-util/RUSTSEC-2020-0059.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/futures-util/RUSTSEC-2020-0062.md
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/futures-intrusive/RUSTSEC-2020-0072.md
- https://crates.io/api/v1/crates/futures
- https://crates.io/api/v1/crates/futures-task

## Advisory mapping decisions

### connectrpc
- RUSTSEC-2026-0304 confirmed against rustsec/advisory-db (file present at crates/connectrpc/).
- No CVE or GHSA assigned as of 2026-09-27; searched github/advisory-database — 0 results.
- Version range: affected 0.2.0–0.9.0; patched 0.8.2 and 0.9.1.
- Download stat: 4,149,119 recent (90d) from crates.io API → ~323K/week est.

### futures
- RUSTSEC-2020-0059/0060/0061/0062 confirmed against rustsec/advisory-db.
- All four advisory files present; CVE/GHSA aliases confirmed via advisory TOML.
- futures-intrusive RUSTSEC-2020-0072 included as a note (different crate/author).
- Download stat: futures total 810,012,465; recent 176,304,220 (90d) → ~13.7M/week est.
- futures-task total 941,622,431; recent 233,965,317 (90d) → ~18M/week est.
- Latest stable (futures 0.3.34, 2026-08-11): unaffected by all listed advisories.

## Candidates considered but not selected

- rust/clap: no direct advisories in rustsec/advisory-db (only incidental mentions in other crates).
- rust/thiserror: no direct advisories found.
- rust/once_cell: RUSTSEC-2019-0017 / CVE-2019-16141 (2019, undefined_behavior); may be worth a future pass.
- go/spf13/cobra: 0 GHSA results — no advisories found.
- rust/connectrpc: SELECTED.
- rust/futures: SELECTED.
