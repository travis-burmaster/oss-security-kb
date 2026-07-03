# crossbeam (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~7.9M/week est. (crossbeam-channel sub-crate, the highest-traffic component); crossbeam meta ~1.9M/week (as of 2026-07-03)
**Repository:** https://github.com/crossbeam-rs/crossbeam
**Security Contact:** GitHub security advisories (https://github.com/crossbeam-rs/crossbeam/security)
**Disclosure Policy:** GitHub security advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

The crossbeam workspace publishes multiple crates from a single monorepo (`crossbeam-rs/crossbeam`). Advisories span the meta-crate (`crossbeam`) and sub-crates (`crossbeam-channel`, `crossbeam-deque`, `crossbeam-utils`, `crossbeam-queue`). Each row notes the affected sub-crate.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2018-0009 / CVE-2018-20996 / GHSA-c3cw-c387-pj65 | Critical (CVSS:3.0 9.8) | `crossbeam` — double-free in `MsQueue` and `SegQueue`: elements popped from a queue still had their destructor run inside the epoch-based GC, causing double-free | crossbeam ≥ 0.4.1 | [RUSTSEC-2018-0009](https://rustsec.org/advisories/RUSTSEC-2018-0009) |
| RUSTSEC-2022-0029 / GHSA-rwf4-gx62-rqfw | High (memory-corruption; no CVSS assigned) | `crossbeam` — `MsQueue::push`/`pop` use atomic orderings that are too weak for the data structure, likely causing memory corruption under concurrent access | crossbeam ≥ 0.3.0 | [RUSTSEC-2022-0029](https://rustsec.org/advisories/RUSTSEC-2022-0029) |
| RUSTSEC-2022-0020 / GHSA-8gj8-hv75-gp94 | Informational / Unsound | `crossbeam` — `SegQueue` calls `mem::zeroed()` for user-supplied type `T`; unsound when `T` is a reference type (non-null invariant violated) | crossbeam ≥ 0.7.0 | [RUSTSEC-2022-0020](https://rustsec.org/advisories/RUSTSEC-2022-0020) |
| RUSTSEC-2020-0052 / CVE-2020-15254 / GHSA-m8h8-v6jh-c762 | High (memory-corruption) | `crossbeam-channel` — bounded channel undefined behavior: destructor reconstructs `Vec` from raw pointer assuming `Vec::from_iter` allocates exactly the element count, which is not guaranteed; deallocation with wrong capacity | crossbeam-channel ≥ 0.4.4 | [RUSTSEC-2020-0052](https://rustsec.org/advisories/RUSTSEC-2020-0052) |
| RUSTSEC-2022-0019 / GHSA-9g55-pg62-m8hh | Informational / Unsound | `crossbeam-channel` — channel calls `mem::zeroed()` for user-supplied type `T`; same root cause as RUSTSEC-2022-0020; fixed in same upstream PR #458 | crossbeam-channel ≥ 0.4.3 | [RUSTSEC-2022-0019](https://rustsec.org/advisories/RUSTSEC-2022-0019) |
| RUSTSEC-2021-0093 / CVE-2021-32810 / GHSA-pqqp-xmhj-wgcw | Critical (CVSS:3.1 9.8) | `crossbeam-deque` — data race in concurrent `Stealer::steal`, `steal_batch`, and `steal_batch_and_pop`: tasks can be dropped twice (double-free for heap-allocated tasks) while other tasks become permanently inaccessible; credited to @kmaork | crossbeam-deque ≥ 0.7.4 (< 0.8.0) or ≥ 0.8.1 | [RUSTSEC-2021-0093](https://rustsec.org/advisories/RUSTSEC-2021-0093) |
| RUSTSEC-2022-0041 / CVE-2022-23639 / GHSA-qc84-gqf4-9926 | Informational / Unsound | `crossbeam-utils` — `AtomicCell<{i,u}64>` assumes `{i,u}64` and `Atomic{I,U}64` have the same alignment on 32-bit targets; on affected targets (e.g. `i686-unknown-linux-gnu`, `i686-linux-android`) alignment of `{i,u}64` is smaller, causing unaligned memory accesses and data races; 64-bit targets unaffected | crossbeam-utils ≥ 0.8.7 (affected 0.8.x yanked) | [RUSTSEC-2022-0041](https://rustsec.org/advisories/RUSTSEC-2022-0041) |
| RUSTSEC-2022-0021 / GHSA-6888-wf7j-34jq | Informational / Unsound | `crossbeam-queue` — same `mem::zeroed()` soundness hole as RUSTSEC-2022-0019/0020; published 2022-05-10 in the same upstream batch fix (PR #458) | see advisory | [RUSTSEC-2022-0021](https://rustsec.org/advisories/RUSTSEC-2022-0021) |
| RUSTSEC-2025-0024 / CVE-2025-4574 / GHSA-pg9f-39pc-qf8g | High (memory-corruption) | `crossbeam-channel` — `Channel::drop` race in `discard_all_messages`: two code paths could both observe a non-null block pointer without one of them nulling it first, leading to double-free and memory corruption; regression introduced in 0.5.12 (all of 0.5.12–0.5.14 yanked) | crossbeam-channel ≥ 0.5.15 | [RUSTSEC-2025-0024](https://rustsec.org/advisories/RUSTSEC-2025-0024) |

## Security Posture Notes

The crossbeam workspace is maintained by the `crossbeam-rs` organization and is a transitive dependency of much of the Rust async and parallel-computation ecosystem. Notably, `crossbeam-deque` underpins tokio's work-stealing thread scheduler and `rayon`'s parallel iterator implementation; the RUSTSEC-2021-0093 data race was therefore latent in a very large fraction of Rust multi-threaded programs.

The two Critical advisories (RUSTSEC-2018-0009, RUSTSEC-2021-0093) represent genuine memory-safety failures under concurrent access, not merely theoretical soundness violations. Both were exploitable (double-free) with high-confidence reachability in programs using standard API calls.

The May 2022 batch of informational/unsound advisories (RUSTSEC-2022-0019, -0020, -0021) share a single root cause — `mem::zeroed()` used to initialize slot buffers for a generic type `T`. This is unsound for any `T` with a non-zero validity invariant (references, `NonNull`, etc.). The fix was switching uniformly to `MaybeUninit`. These were filed as informational rather than vulnerability-rated because exploitation requires a caller to provide a `T` with a validity invariant and observe the specific zeroed value, which is an unusual pattern in practice.

The 2025 double-free advisory (RUSTSEC-2025-0024) was introduced as a regression during a memory-leak fix in 0.5.12 and fixed promptly in 0.5.15; all three affected versions (0.5.12–0.5.14) were yanked from crates.io.

The project uses GitHub security advisories for disclosure. No separate SECURITY.md or bug-bounty program is documented.

## Dependencies of Note

- `crossbeam-deque` is used by `rayon` and `tokio` work-stealing schedulers; security fixes cascade into those ecosystems.
- `crossbeam-utils` `AtomicCell` is used across numerous crates as a safe atomic wrapper; the 32-bit alignment issue (RUSTSEC-2022-0041) was specific to platforms with native `Atomic{I,U}64` where `{i,u}64` has smaller alignment.

## Open Questions

- Confirm the exact patched version for `crossbeam-queue` RUSTSEC-2022-0021 (the advisory references upstream PR #458 but the specific crate version is not captured in the search result).
- Assess whether the archived `crossbeam-epoch` crate (the sub-crate whose bug triggered RUSTSEC-2018-0009) is still reachable through any active API in the current crossbeam meta-crate.

## Related Pages

- [[rust/tokio]]
- [[rust/index]]

---
*Last updated: 2026-07-03 | Sources: 9*
