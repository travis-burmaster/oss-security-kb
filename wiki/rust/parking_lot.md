# parking_lot (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~23.5M/week est. (211M/90 days as of 2026-09-15)
**Repository:** https://github.com/Amanieu/parking_lot
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-35910 / GHSA-ppj3-7jw3-8vc4 (lock_api) | Moderate (CVSS 3.1 AV:L) | Data race via MappedMutexGuard unsoundness: MappedMutexGuard incorrectly implemented Send, allowing it to be moved across thread boundaries when the guarded type is not Send — enabling data races in otherwise safe Rust code. | lock_api 0.4.2 / parking_lot 0.11.2 | [GHSA-ppj3-7jw3-8vc4](https://github.com/advisories/GHSA-ppj3-7jw3-8vc4) |
| CVE-2020-35911 / GHSA-vh4p-6j7g-f4j9 (lock_api) | Moderate (CVSS 3.1 AV:L) | Data race via MappedRwLockReadGuard unsoundness: same incorrect Send bound on MappedRwLockReadGuard; non-Send type can be moved across thread boundaries through a remapped read guard. | lock_api 0.4.2 / parking_lot 0.11.2 | [GHSA-vh4p-6j7g-f4j9](https://github.com/advisories/GHSA-vh4p-6j7g-f4j9) |
| CVE-2020-35912 / GHSA-5wg8-7c9q-794v (lock_api) | Moderate (CVSS 7.1 AV:L) | Data race via MappedRwLockWriteGuard unsoundness: incorrect Send/Sync trait bounds on write guard enable cross-thread moves and concurrent access where exclusive access is required. | lock_api 0.4.2 / parking_lot 0.11.2 | [GHSA-5wg8-7c9q-794v](https://github.com/advisories/GHSA-5wg8-7c9q-794v) |
| CVE-2020-35913 / GHSA-hj9h-wrgg-hgmx (lock_api) | Moderate (CVSS 3.1 AV:L) | Data race via RwLockReadGuard unsoundness: Sync was incorrectly implemented for RwLockReadGuard, enabling shared references to non-Sync types to be observed concurrently from multiple threads. | lock_api 0.4.2 / parking_lot 0.11.2 | [GHSA-hj9h-wrgg-hgmx](https://github.com/advisories/GHSA-hj9h-wrgg-hgmx) |
| CVE-2020-35914 / GHSA-gmv4-vmx3-x9f3 (lock_api) | Moderate (CVSS 3.1 AV:L) | Data race via RwLockWriteGuard unsoundness: incorrect Sync implementation on write guards allows multiple threads to observe the same guarded value simultaneously, violating exclusive-access guarantees. | lock_api 0.4.2 / parking_lot 0.11.2 | [GHSA-gmv4-vmx3-x9f3](https://github.com/advisories/GHSA-gmv4-vmx3-x9f3) |

*All five CVEs are catalogued together as RUSTSEC-2020-0070 in the RustSec advisory database under the `lock_api` crate. The `lock_api` crate (v0.4.14, ~984M total crates.io downloads) is a sub-crate of the parking_lot workspace; users of `parking_lot` ≤ 0.11.1 that depend on `lock_api` < 0.4.2 are transitively affected.*

## Security Posture Notes

parking_lot provides compact, efficient alternatives to `std::sync` primitives (Mutex, RwLock, Condvar, Once, etc.) and is one of the most widely used synchronization crates in the Rust ecosystem (~1B+ total crates.io downloads for parking_lot; ~984M for lock_api). It underpins Tokio's internal synchronization, Rayon thread pools, Diesel connection pools, and many other high-usage libraries.

The five CVEs (CVE-2020-35910–35914) all stem from the same root cause in `lock_api` < 0.4.2: the `Mapped*Guard` types (produced by `MutexGuard::map` / `RwLockReadGuard::map` / `RwLockWriteGuard::map`) and the `RwLock*Guard` types had incorrect `Send` and/or `Sync` trait implementations that the compiler could not catch. In safe Rust code, a user could:

- Move a `MappedMutexGuard<T>` across a thread boundary even when `T: !Send`
- Share a `RwLockReadGuard<T>` across threads even when `T: !Sync`

The fix (lock_api 0.4.2, parking_lot 0.11.2, January 2021) adjusts the Send/Sync bounds on all affected Mapped guard types and removes the erroneous Sync implementation from RwLock guards.

**Impact scope:** local only (AV:L). The unsoundness requires a thread-spawning context already accessible to the attacker; exploiting it leads to undefined behavior (data races), which in practice causes crashes or stale data rather than code execution. No remote attack vector.

Current parking_lot: 0.12.5 (2024-03-25). Current lock_api: 0.4.14. Both unaffected by all five CVEs.

No active security contact or SECURITY.md exists in the parking_lot repository; security issues should be reported via GitHub Issues or private GitHub security advisory disclosure.

## Dependencies of Note

- `lock_api` — the directly affected sub-crate; separately versioned; has own crates.io entry
- `parking_lot_core` — internal scheduler (futex / event pairs); part of the workspace; no known direct advisories

## Open Questions

- Does parking_lot_core have any soundness issues not yet captured in public advisories?
- Are there any downstream crates that expose MappedGuard types without re-adding correct bounds (e.g., custom async wrappers)?

## Related Pages

- [[rust/crossbeam]]
- [[rust/dashmap]]
- [[rust/index]]

---
*Last updated: 2026-09-15 | Sources: RUSTSEC-2020-0070 (rustsec/advisory-db), 5 GHSA advisories (github/advisory-database), crates.io API*
