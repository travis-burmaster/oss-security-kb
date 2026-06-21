# chrono (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~125,700,595 (as of 2026-06-21)
**Repository:** https://github.com/chronotope/chrono
**Security Contact:** https://github.com/chronotope/chrono/security/advisories
**Disclosure Policy:** https://github.com/chronotope/chrono/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-21 | OSS Security KB | advisory-db lookup | automated | 1 public advisory mapped (code-execution / memory-corruption) | [rustsec/advisory-db](https://github.com/rustsec/advisory-db/tree/main/crates/chrono) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-26235 / RUSTSEC-2020-0159 | Medium — potential code-execution / memory-corruption | On Unix-like systems, `chrono`'s `oldtime` feature depends on `time` 0.1.x, which calls `localtime_r`. Because `std::env::set_var` and `localtime_r` are both non-reentrant / non-thread-safe, concurrent invocations from separate threads can cause a use-after-free, producing a segmentation fault or undefined behaviour. Any binary that (a) uses `chrono`'s date-from-local APIs and (b) modifies environment variables from another thread is in scope. The `oldtime` feature was disabled by default in 0.4.20, removing `time` 0.1.x from the default dependency graph. Explicit re-enabling of `oldtime` on older versions retains the exposure. | 0.4.20 | [RUSTSEC-2020-0159](https://rustsec.org/advisories/RUSTSEC-2020-0159.html) |

*OSV live record: https://osv.dev/list?ecosystem=crates.io&q=chrono*

## Security Posture Notes

`chrono` is the dominant date-and-time library for Rust, with ~635M total downloads and ~125.7M recent downloads. Current version 0.4.45 (released 2026-06-04) is well past the 0.4.20 fix boundary.

The 0.4.20 release disabled the `oldtime` feature by default, removing the `time` 0.1.x dependency from the default build. Users who explicitly opt in to the `oldtime` feature or who are pinned to a version older than 0.4.20 remain exposed to the segfault path.

The `time` crate published a companion advisory RUSTSEC-2020-0071 for the same `localtime_r` unsoundness in its own bindings. `chrono` 0.4.x uses `time` 0.3.x in the default configuration, where the unsafe binding is absent.

No remote-code-execution, remote denial-of-service, or integrity advisory has been published against `chrono` at the package level beyond RUSTSEC-2020-0159.

## Dependencies of Note

- `time` (0.1.x, via the `oldtime` feature) — source of the `localtime_r` unsoundness; present only when the `oldtime` feature is explicitly enabled in chrono ≥ 0.4.20.
- `iana-time-zone` — IANA timezone data provider; no published advisory at time of this pass.

## Open Questions

- Search rustsec/advisory-db for any new chrono-specific advisories filed after 0.4.20 (timezone boundary handling, platform-specific unsoundness, or DST edge cases).
- Confirm whether `time` 0.3.x (used in the default build) carries any unresolved unsoundness advisories that propagate through `chrono`.

## Related Pages

- [[rust/index]]

---
*Last updated: 2026-06-21 | Sources: 2 (rustsec/advisory-db, crates.io API)*
