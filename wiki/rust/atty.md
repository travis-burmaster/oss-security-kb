# atty (Rust)

**Registry:** crates.io
**Weekly Downloads:** ~30.1M (as of 2026-09-24); 353M+ all-time
**Repository:** https://github.com/softprops/atty
**Security Contact:** none listed (unmaintained; maintainer unreachable)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2021-0145 / GHSA-g98v-hv3f-hcfr | Informational (unsound) | Potentially unaligned read on Windows: `atty` dereferences a raw `HANDLE` pointer cast to `*mut BOOL` (Windows `GetConsoleMode`), which may be unaligned. Practical exploitation is low because Windows `HeapAlloc` guarantees alignment in practice, but the cast is undefined behavior under Rust's memory model. No patched version was ever released; the maintainer became unreachable while a fix PR was open. | No patched version; migrate to `std::io::IsTerminal` (stable Rust ≥ 1.70.0) or the `is-terminal` crate | [RUSTSEC-2021-0145](https://rustsec.org/advisories/RUSTSEC-2021-0145.html) |

## Security Posture Notes

`atty` answers one question: is a given file descriptor (stdin/stdout/stderr) connected to a terminal/TTY? Despite this narrow API surface, it was a transitive dependency of many high-profile Rust CLI tools — including `clap` ≤ 3.x, `indicatif`, `env_logger`, `cargo` toolchain components, and dozens of popular binaries — making it one of the most widely pulled crates in the ecosystem (353M+ total downloads).

The RUSTSEC-2021-0145 advisory was filed on 2021-07-04 and classified **informational / unsound**: the code invokes undefined behavior in Rust's safety model even though the practical probability of an exploitable misaligned read on modern Windows allocators is low. The crate is **unmaintained** — the maintainer is unreachable, the last release (0.2.14) predates the advisory, and no patch exists. The advisory will remain open indefinitely since no fix can land without a new maintainer.

**`cargo audit` / `cargo deny` impact:** Any crate that carries `atty` as a transitive dependency will trigger an advisory warning in `cargo audit` output. This is a high-volume finding in security audit reports for Rust CLI projects. Teams encountering it should migrate their own direct `atty` usage and pin or replace transitive dependencies.

**Recommended migration:**
- Direct users: replace `atty::is(atty::Stream::Stdout)` with `std::io::stdout().is_terminal()` (requires Rust ≥ 1.70.0 and `use std::io::IsTerminal`)
- Teams on older Rust toolchains: use the `is-terminal` crate as a drop-in replacement
- `clap` 4.x already replaced `atty` internally; upgrading from `clap` 3.x removes one atty dependency path

## Dependencies of Note

None flagged (`atty` has no crates.io dependencies of its own).

## Open Questions

- Which Rust CLI tools in active use still carry `atty` as a transitive dependency as of 2026?
- Is any maintainer in the Rust ecosystem considering adopting and patching `atty`, or is the migration to `is-terminal` considered complete?

## Related Pages

- [[rust/index]]

---
*Last updated: 2026-09-24 | Sources: 1*
