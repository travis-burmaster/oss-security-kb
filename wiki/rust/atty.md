# atty (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~30.5M (as of 2026-09-12)
**Repository:** https://github.com/softprops/atty
**Security Contact:** none listed (unmaintained; maintainer unreachable since ~2020)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-09-12 | oss-security-kb nightly pass | api-surface | automated | 2 advisories confirmed | [RUSTSEC-2021-0145](https://rustsec.org/advisories/RUSTSEC-2021-0145.html), [RUSTSEC-2024-0375](https://rustsec.org/advisories/RUSTSEC-2024-0375.html) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2021-0145 / GHSA-g98v-hv3f-hcfr | Unsound (Moderate) | `atty::is_tty()` on Windows reinterprets a raw `HANDLE` value (a raw pointer) as a `HANDLE` type via potentially unaligned pointer dereference in the FFI boundary. The Windows system allocator's alignment guarantees make observable miscompilation unlikely in practice, but the operation is formally undefined behavior. Pull request fixing the issue was submitted to the maintainer but never merged. **No patched version released.** | None (unmaintained; no fix planned) | [RUSTSEC-2021-0145](https://rustsec.org/advisories/RUSTSEC-2021-0145.html) |
| RUSTSEC-2024-0375 | Informational | Crate declared officially unmaintained by the maintainer. All versions affected. Maintainer-recommended migration: `std::io::IsTerminal` (stable Rust ≥ 1.70.0). | None; migrate away | [RUSTSEC-2024-0375](https://rustsec.org/advisories/RUSTSEC-2024-0375.html) |

*OSV link: https://osv.dev/list?ecosystem=crates.io&q=atty*

## Security Posture Notes

`atty` is a minimal Rust crate for detecting whether a file descriptor is connected to a TTY/terminal. It reached 0.2.14 in 2019 and has not had a release since. The `softprops` maintainer became unreachable; a community pull request fixing the Windows unsoundness (#51) has been open and unmerged for years.

Despite being functionally frozen, `atty` receives approximately **30.5 million downloads per week** as of September 2026. The downloads are almost entirely transitive: `clap` 3.x, `indicatif`, `tracing-subscriber`, `env_logger`, and dozens of other high-download crates depend on `atty` directly.

**Migration:** The functionality is now part of the Rust standard library as `std::io::IsTerminal`, stable since Rust 1.70.0 (May 2023). The `is-terminal` crate provides the same API for codebases targeting Rust < 1.70. Downstreams (clap 4.x, indicatif ≥ 0.17.6, etc.) have already migrated; older pinned major versions may still pull `atty` transitively.

The Windows unsoundness (RUSTSEC-2021-0145) has no practical exploit vector outside of highly contrived scenarios due to allocator alignment guarantees, but it contributes to the `cargo audit` / `cargo deny` advisory noise in any project that transitively depends on `atty`. The correct response is to upgrade to clap 4.x and other upstreams that have migrated away.

## Dependencies of Note

- `libc` (Unix TTY detection via `isatty(3)`)
- `winapi` (Windows HANDLE-based detection — source of the unsoundness)

## Open Questions

- Confirm whether all top-10 transitive dependents have fully migrated away from `atty` (clap 4, indicatif 0.17.6+, tracing-subscriber 0.3.18+).
- Watch for any MSRV-sensitive projects still locked on clap 3.x that cannot upgrade without a Rust version bump.

## Related Pages

- [[rust/index]]

---
*Last updated: 2026-09-12 | Sources: 2 (RUSTSEC-2021-0145, RUSTSEC-2024-0375)*
