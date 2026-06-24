# rand (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~23,700,000 (as of 2026-06-24)
**Repository:** https://github.com/rust-random/rand
**Security Contact:** https://github.com/rust-random/rand/security/advisories
**Disclosure Policy:** https://github.com/rust-random/rand/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-24 | OSS Security KB | advisory-db lookup | automated | 1 public advisory mapped (unsoundness / undefined behavior) | [rustsec/advisory-db](https://github.com/rustsec/advisory-db/tree/main/crates/rand), [github/advisory-database](https://github.com/advisories/GHSA-cq8v-f236-94qc) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2026-0097 / GHSA-cq8v-f236-94qc | Low (informational: unsound) | Unsoundness in `rand::rng()` / `rand::thread_rng()` when the `log` and `thread_rng` features are both enabled and a custom logger calls back into `rand::rng()` during the periodic reseed (every 64 KiB of output). The unsafe casting path creates aliased mutable references, violating Stacked Borrows rules and producing undefined behavior in optimized builds. Affected: 0.7.0–0.8.5, 0.9.0–0.9.2, 0.10.0. | 0.10.1 / 0.9.3 / 0.8.6 | [RUSTSEC-2026-0097](https://rustsec.org/advisories/RUSTSEC-2026-0097.html) / [GHSA-cq8v-f236-94qc](https://github.com/advisories/GHSA-cq8v-f236-94qc) |

*OSV live record: https://osv.dev/list?ecosystem=crates.io&q=rand*

## Security Posture Notes

`rand` is the de facto standard random-number-generation library for Rust (~1.3B total crates.io downloads, ~23.7M/week as of 2026-06-24). Current version is 0.10.1. The crate is maintained by the rust-random organization; security disclosures go through GitHub Security Advisories.

RUSTSEC-2026-0097 (published 2026-04-09) is an informational unsoundness advisory: the vulnerability only triggers under a specific combination of feature flags (`log` + `thread_rng`) combined with a custom logger implementation that re-enters `rand::rng()` during reseeding. In practice, this combination is uncommon; most production deployments that do not implement custom loggers invoking rand inside logging callbacks are not affected. The undefined behavior arises from aliased `&mut ThreadRng` references created through unsafe casting in the reseeding path, which violates the Stacked Borrows model and may cause incorrect behavior in optimized (`--release`) builds.

The fix is available in all maintained minor lines (0.8.6, 0.9.3, 0.10.1). Given that 0.10.1 is the current stable release, users should upgrade and run `cargo update -p rand`.

No remote-attack-surface advisories (DoS, RCE, bias, predictability) have been published against `rand` at the package level in the advisory databases searched. The crate's design uses OS-level entropy sources (via `getrandom`) and periodic reseeding, providing a strong forward-secrecy baseline.

## Dependencies of Note

- `rand_core` — foundational trait and RNG primitives; no direct package-scoped RustSec advisory confirmed at time of this pass.
- `getrandom` — OS entropy source; has its own advisory history around WASM target unsoundness (RUSTSEC-2020-0[..]) — verify separately.
- `rand_chacha` — default ChaCha RNG backend; no published advisory at time of this pass.

## Open Questions

- Search rustsec/advisory-db for advisories against `rand_core`, `rand_chacha`, and `getrandom` that propagate through `rand` via its dependency graph.
- Assess whether any randomness-bias or predictability advisories exist for older 0.4.x–0.6.x versions of `rand` that remain in transitive dependency graphs of long-lived codebases.
- Monitor for follow-on advisories in the 0.11.x development line as the API stabilizes.

## Related Pages

- [[rust/ring]]
- [[rust/rustls]]
- [[rust/openssl]]
- [[rust/index]]

---
*Last updated: 2026-06-24 | Sources: 3 (rustsec/advisory-db, github/advisory-database, crates.io API)*
