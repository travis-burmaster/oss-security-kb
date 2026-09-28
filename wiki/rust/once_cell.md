# once_cell (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~286.5M (as of 2026-09-28)
**Repository:** https://github.com/matklad/once_cell
**Security Contact:** https://github.com/matklad/once_cell/issues (no dedicated security contact)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2019-0017 / CVE-2019-16141 / GHSA-7j44-fv4x-79g9 | High (CVSS 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | `Lazy<T>::deref` / `Lazy<T>::force` undefined behavior on panic: if the initialization function panics on the first dereference, subsequent dereferences execute `std::hint::unreachable_unchecked`, which is instant UB; can cause arbitrary memory corruption or program termination. Configurations with `panic = "abort"` are unaffected since a panic prevents further execution. | >= 1.0.1 | [RUSTSEC-2019-0017](https://rustsec.org/advisories/RUSTSEC-2019-0017.html) |

## Security Posture Notes

`once_cell` provides single-assignment cell and lazy-value primitives: `OnceCell<T>`, `OnceLock<T>`, `Lazy<T>`, and `LazyLock<T>` (sync and unsync variants). It is one of the most widely depended-upon utility crates in the Rust ecosystem, with 1B+ total downloads.

- **Advisory status:** RUSTSEC-2019-0017 is the sole advisory on record. It was discovered and patched in September 2019 (fixed 1.0.1); the current stable version is **1.21.4** (released March 2026). All modern users of `once_cell` are unaffected.
- **Stabilization note:** The Rust standard library stabilized equivalent types in Rust 1.70.0 (June 2023): `std::sync::OnceLock<T>` and `std::cell::OnceCell<T>`. `std::sync::LazyLock<T>` was stabilized in Rust 1.80.0 (July 2024). For new code, std types are preferred; `once_cell` remains widely used as a compatibility layer for older MSRV targets and for the additional `unsync::Lazy<T>` variant.
- **Transitive exposure:** `once_cell` is a transitive dependency of a significant fraction of the Rust ecosystem (cargo, rustc internals, many popular crates). The historical advisory is well past the affected version range and poses no practical risk to projects on current releases.

## Dependencies of Note

None flagged. `once_cell` itself has no Cargo dependencies.

## Open Questions

- Verify whether any crates.io security advisories are pending for the std migration path (e.g., projects pinned to older once_cell releases with UB-affected versions).

## Related Pages

- [[rust/lazy_static]] — older alternative for lazy statics (if a page exists in future passes)
- [[rust/index]]

---
*Last updated: 2026-09-28 | Sources: 1 (rustsec/advisory-db via raw.githubusercontent.com, crates.io API)*
