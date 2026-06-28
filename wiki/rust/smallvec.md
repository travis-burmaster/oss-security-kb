# smallvec (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~15.4M/week estimated (as of 2026-06-28)
**Repository:** https://github.com/servo/rust-smallvec
**Security Contact:** GitHub Security Advisories — https://github.com/servo/rust-smallvec/security
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2018-0003 / CVE-2018-20991 / GHSA-rxr4-x558-x7hw | Critical (CVSS 9.8) | Double-free in `SmallVec::insert_many` when the supplied iterator's `next()` panics during unwinding; vector left in inconsistent state causing the same value to be dropped twice | ≥ 0.6.3 | [RUSTSEC-2018-0003](https://rustsec.org/advisories/RUSTSEC-2018-0003.html) |
| RUSTSEC-2018-0018 / CVE-2018-25023 | Informational (unsound) | Use of `mem::uninitialized()` for generic type `T` violates Rust safety invariants when `T` is a reference type (references must be non-null); replaced by `MaybeUninit` in the fix | ≥ 0.6.13 | [RUSTSEC-2018-0018](https://rustsec.org/advisories/RUSTSEC-2018-0018.html) |
| RUSTSEC-2019-0009 / CVE-2019-15551 / GHSA-mm7v-vpv8-xfc3 | Critical (CVSS 9.8) | Double-free and use-after-free in `SmallVec::grow()` when growth value equals current capacity, triggering premature deallocation followed by a second free on drop | ≥ 0.6.10 | [RUSTSEC-2019-0009](https://rustsec.org/advisories/RUSTSEC-2019-0009.html) |
| RUSTSEC-2019-0012 / CVE-2019-15554 / GHSA-69gw-hgj3-45m7 | Critical (CVSS 9.8) | Memory corruption in `SmallVec::grow()` when called on a spilled SmallVec with a requested capacity lower than the current capacity; could allow code execution via attacker-controlled grow argument | ≥ 0.6.10 | [RUSTSEC-2019-0012](https://rustsec.org/advisories/RUSTSEC-2019-0012.html) |
| RUSTSEC-2021-0003 / CVE-2021-25900 / GHSA-43w2-9j62-hq99 | Critical (CVSS 9.8) | Buffer overflow in `SmallVec::insert_many` when the iterator's `size_hint` lower bound underestimates the actual element count; method allocates a buffer smaller than needed and writes past its boundary, corrupting heap memory | ≥ 0.6.14, ≥ 1.6.1 | [RUSTSEC-2021-0003](https://rustsec.org/advisories/RUSTSEC-2021-0003.html) |

## Security Posture Notes

`smallvec` implements a "small vector" optimization that stores up to N elements on the stack before spilling to heap allocation, avoiding unnecessary allocation for small collections. The crate is maintained by the Servo project (`servo/rust-smallvec`) and is widely used as a transitive dependency — Mozilla Firefox, the Rust compiler, and many CNCF-adjacent crates depend on it. Current latest stable: 1.15.2.

All five advisories are historical (2018–2021) and fully resolved in the current 1.x release line. Any version ≥ 1.6.1 addresses all known advisories. The two 2019 advisories (RUSTSEC-2019-0009 and RUSTSEC-2019-0012) cover distinct capacity-arithmetic conditions in `grow()`, both fixed simultaneously in 0.6.10. The critical 2021 advisory (RUSTSEC-2021-0003) affects both the 0.6.x legacy branch (fixed in 0.6.14) and the 1.x branch (fixed in 1.6.1).

The advisory pattern — four Critical (CVSS 9.8) memory-safety issues plus one unsoundness informational — reflects the difficulty of writing correct `unsafe` Rust around capacity arithmetic and iterator interaction. The 2018-0018 unsoundness fix mirrors a broader ecosystem migration from `mem::uninitialized()` to `MaybeUninit`, which became stable in Rust 1.36.0 (2019).

## Dependencies of Note

None flagged — `smallvec` has minimal transitive dependencies by design.

## Open Questions

- Are there any security implications of the `union` feature flag that enables `Copy`-type inline storage via a Rust union rather than `ManuallyDrop<[T; N]>`?
- Has any fuzzing been published targeting capacity-arithmetic paths in modern 1.x versions (e.g. via cargo-fuzz)?

## Related Pages

- [[rust/index]]

---
*Last updated: 2026-06-28 | Sources: 5*
