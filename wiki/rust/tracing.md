# tracing (Rust/crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~14.1M/week est. (~183.4M per 90 days as of 2026-09-07)
**Repository:** https://github.com/tokio-rs/tracing
**Security Contact:** https://github.com/tokio-rs/tracing/security/advisories
**Disclosure Policy:** GitHub Security Advisories (https://github.com/tokio-rs/tracing/security/advisories)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2023-0078 / GHSA-8f24-6m29-wm2r | Unsound (memory-corruption) | Stack use-after-free in `Instrumented::into_inner`: the method creates raw pointers to struct fields on the stack, then calls `std::mem::forget(self)` — which may allow LLVM to reuse that stack slot — and subsequently reads through those now-potentially-freed pointers. Per the Rust reference, pointers into memory passed to `mem::forget` do not carry validity guarantees. Affected versions (0.1.38, 0.1.39) have been yanked from crates.io. | ≥ 0.1.40 | [RustSec](https://rustsec.org/advisories/RUSTSEC-2023-0078.html) |

## Security Posture Notes

`tracing` is the dominant structured instrumentation and logging framework for async Rust, maintained by the Tokio project (tokio-rs org). It is a foundational dependency across the Rust async ecosystem — tokio, axum, hyper, tonic, and the Rust cloud-native toolchain all rely on it directly or transitively.

RUSTSEC-2023-0078 is classified as an **unsoundness** rather than an exploitable memory-safety bug in typical production use. No miscompilation was observed in Rust 1.73.0 at the time of disclosure, but the pattern constitutes undefined behavior per the Rust reference, and future LLVM optimizations or different architectures could make the use-after-free manifest. The fix in 0.1.40 (released 2023-10-19) replaces `std::mem::forget` with `std::mem::ManuallyDrop`, which preserves the stack layout while suppressing the destructor call. The affected versions (0.1.38, 0.1.39) were yanked from crates.io on disclosure day.

Ecosystem note: `tracing`'s download statistics place it among the most-downloaded crates on crates.io (~825M all-time downloads, current stable 0.1.44 released 2026-08-06). The large transitive footprint means the 0.1.38/0.1.39 issue affected a significant slice of the async Rust ecosystem, though the practical exploitation surface is limited to code paths that call `Instrumented::into_inner` in a configuration where LLVM stack reuse occurs.

The PR that introduced the bug was merged for 0.1.38 and was fixed in the same review thread: https://github.com/tokio-rs/tracing/pull/2765.

## Dependencies of Note

- `tracing-core` — defines the core `Subscriber` / `Dispatch` traits and the global dispatcher; same tokio-rs org; no separate published advisories confirmed in this pass.
- `tracing-subscriber` — composable `Subscriber` implementations (FmtLayer, EnvFilter, Registry); no direct published advisories confirmed in this pass.
- `pin-project` / `pin-project-lite` — used internally for async pinning; `pin-project` 0.4.x had its own unsoundness advisory (RUSTSEC-2020-0011); the `tracing` crate's transitive exposure should be checked against current `pin-project-lite` version.

## Open Questions

- Companion crates `tracing-subscriber`, `tracing-opentelemetry`, `tracing-flame`, and `tracing-forest` were not reviewed in this pass; their advisory histories should be checked.
- Verify that the current `pin-project-lite` version used by `tracing` is not affected by any outstanding unsoundness advisories.

## Related Pages

- [[rust/tokio]]
- [[rust/axum]]
- [[rust/hyper]]
- [[rust/index]]

---
*Last updated: 2026-09-07 | Sources: 1*
