# zerocopy (Rust/crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~17M/week est. (as of 2026-08-10; derived from ~218M recent-90-day downloads per crates.io API)
**Repository:** https://github.com/google/zerocopy
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2023-0074 | Moderate (no CVE) | **Ref methods unsoundness via cell::Ref / cell::RefMut** — `Ref::into_ref`, `into_mut`, `into_slice`, and `into_slice_mut` are unsound when the buffer type parameter `B` is `cell::Ref<'_, T>` or `cell::RefMut<'_, T>`; a safe caller can trigger undefined behaviour. Narrow usage pattern: mainstream consumers using `Ref<&[u8], T>` or `Ref<&mut [u8], T>` are unaffected. No CVE assigned. Disclosed 2023-12-14. | 0.2.9 / 0.3.2 / 0.4.1 / 0.5.2 / 0.6.6 / 0.7.31 | [GHSA-3mv5-343c-w2qg](https://github.com/advisories/GHSA-3mv5-343c-w2qg) · [RUSTSEC-2023-0074](https://rustsec.org/advisories/RUSTSEC-2023-0074.html) |

## Security Posture Notes

- `zerocopy` is a Google-maintained crate developed for the Fuchsia OS kernel; it also powers Chromium, Android, TensorFlow, and a large body of network-protocol and parsing libraries on crates.io. Its purpose is to provide safe, zero-cost abstractions over unsafe pointer operations and memory layout transformations.
- RUSTSEC-2023-0074 affects a narrow pattern (`Ref<cell::Ref<...>, T>` or `Ref<cell::RefMut<...>, T>` as the buffer type). Consumers using slice references or `Vec`-backed buffers are not affected. The maintainers simultaneously patched all actively maintained major lines (0.2 through 0.7) in December 2023.
- 0.8.x and 0.9.x (alpha) lines are not listed as affected by RUSTSEC-2023-0074; no additional advisories found in rustsec/advisory-db or github/advisory-database for those lines as of this pass.
- The crate has no formal SECURITY.md disclosure policy; vulnerability reports are made via GitHub issues or the RustSec advisory process.
- ~792M total crates.io downloads as of 2026-08-10; widely embedded as an indirect dependency via Android, Fuchsia, and network-stack crates.

## Dependencies of Note

None flagged.

## Open Questions

- Are there soundness issues in the 0.8.x or 0.9.x lines (released after the 0.7.31 fix)?
- Does the zerocopy project intend to adopt a formal security disclosure policy or SECURITY.md?
- Should downstream consumers using the 0.6.x or earlier series be flagged for upgrade (given 0.7.31+ breaks the affected API)?

## Related Pages

- [[rust/bytes]]
- [[rust/serde]]
- [[rust/index]]

---
*Last updated: 2026-08-10 | Sources: 2 (GHSA-3mv5-343c-w2qg, GHSA-rjhf-4mh8-9xjq via github/advisory-database; RUSTSEC-2023-0074 via rustsec/advisory-db; crates.io API for download stats)*
