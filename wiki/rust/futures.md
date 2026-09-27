# futures (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~13.7M/week est. (futures meta-crate, as of 2026-09-27)
**Repository:** https://github.com/rust-lang/futures-rs
**Security Contact:** https://github.com/rust-lang/futures-rs/security
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

Advisories are filed against individual sub-crates of the futures-rs workspace. The umbrella `futures` crate re-exports all of them; pinning any affected sub-crate version exposes callers.

| CVE / Issue | Severity | Crate | Description | Fixed in | Source |
|-------------|----------|-------|-------------|----------|--------|
| RUSTSEC-2020-0060 / CVE-2020-35906 / GHSA-r93v-9p5q-vhpf | High (code-execution, memory-corruption) | futures-task | **Missing `'static` bound on `waker()`** — callers can call `Waker::wake()` after the underlying data is freed, causing use-after-free / potential arbitrary code execution; affects 0.3.0–0.3.5 | futures-task ≥ 0.3.6 | [RUSTSEC-2020-0060](https://rustsec.org/advisories/RUSTSEC-2020-0060.html) |
| RUSTSEC-2020-0062 / CVE-2020-35908 / GHSA-5r9g-j7jj-hw6c | High (CVSS 3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | futures-util | **Unsound `Sync` on `FuturesUnordered`** — `Cell`-based interior mutability without synchronized access allows concurrent threads to see inconsistent head/length state, causing memory corruption; affects 0.3.0–0.3.1 | futures-util ≥ 0.3.2 | [RUSTSEC-2020-0062](https://rustsec.org/advisories/RUSTSEC-2020-0062.html) |
| RUSTSEC-2020-0061 / CVE-2020-35907 / GHSA-p9m5-3hj7-cp5r | High (CVSS 3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) | futures-task | **NULL pointer dereference in `noop_waker_ref`** — function used thread-local storage and returned a reference safely woken by another thread, causing segfault via `Waker::wake_by_ref()` cross-thread; affects 0.3.0–0.3.4 | futures-task ≥ 0.3.5 | [RUSTSEC-2020-0061](https://rustsec.org/advisories/RUSTSEC-2020-0061.html) |
| RUSTSEC-2020-0059 / CVE-2020-35905 / GHSA-rh4w-94hh-9943 | Medium (CVSS 3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:N/A:H) | futures-util | **Unsound `Send`/`Sync` on `MappedMutexGuard`** — `MutexGuard::map()` closure returning unrelated `U` only accounted for variance on `T`, allowing data race in safe code; affects 0.3.2–0.3.6 | futures-util ≥ 0.3.7 | [RUSTSEC-2020-0059](https://rustsec.org/advisories/RUSTSEC-2020-0059.html) |

**Related crate — futures-intrusive (separate author):**
RUSTSEC-2020-0072 / CVE-2020-35915 / GHSA-4hjg-cx88-g9f9: `GenericMutexGuard<T>` incorrectly implements `Sync` when `T: Send` but not `T: Sync`, enabling data races from safe code; fixed in futures-intrusive 0.4.0.

## Security Posture Notes

The `futures` crate is the foundational async-programming library for Rust, maintained under the rust-lang organization. It defines the `Future`, `Stream`, `Sink`, and `AsyncRead`/`AsyncWrite` traits and provides the combinators and executor tooling used across the entire Rust async ecosystem. The workspace sub-crates — `futures-core`, `futures-task`, `futures-util`, `futures-io`, `futures-channel`, `futures-sink`, `futures-executor` — each have their own crates.io entries; `futures` re-exports them all.

Download scale:
- `futures` (meta-crate): 810M+ total downloads, ~176M recent (90 days), est. ~13.7M/week
- `futures-task`: 942M+ total downloads, ~234M recent (90 days), est. ~18M/week

All four advisories above are from November–December 2020 and were discovered and patched during a coordinated review of the futures-rs 0.3.x workspace. They all share the `AV:L` (local) vector — they cannot be triggered remotely without attacker-controlled code running in the same process. The practical risk is callers pinned to old patch versions:
- Any `futures` < 0.3.6 carries the UAF advisory (RUSTSEC-2020-0060) — the most severe.
- `futures` 0.3.0–0.3.1 carries the memory corruption advisory (RUSTSEC-2020-0062).
- All four are caught by a standard `cargo audit` run against a current RustSec database.

The current stable release (0.3.34, published 2026-08-11) is unaffected by all listed advisories.

No security contact or disclosure policy is listed in the repository SECURITY.md. Security advisories are coordinated via GitHub security advisories on the rust-lang/futures-rs repository.

## Dependencies of Note

The futures-rs workspace has minimal external dependencies by design. No transitive dependencies with known advisories were flagged in this pass.

## Open Questions

- Does `futures-channel` or `futures-io` carry any unreported soundness issues from the same 2020 era?
- Is the `futures-intrusive` crate (RUSTSEC-2020-0072) in use via any widely deployed Rust services? (It is a separate ecosystem from rust-lang/futures-rs.)

## Related Pages

- [[rust/tokio]] — dominant async runtime; implements the `Future` interface from futures-rs
- [[rust/crossbeam]] — concurrent data structures; overlapping soundness/data-race advisory history
- [[rust/parking_lot]] — synchronization primitives; related incorrect `Send`/`Sync` history
- [[rust/index]]

---
*Last updated: 2026-09-27 | Sources: 5*
