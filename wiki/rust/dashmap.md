# dashmap (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~6.2M/week est. (as of 2026-09-10)
**Repository:** https://github.com/xacrimon/dashmap
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
| RUSTSEC-2022-0002 / GHSA-mpg5-fvwp-42m2 | High | Reference returned by methods of `Ref`, `RefMut`, `RefMulti`, and `RefMutMulti` may outlive the `Ref` and escape the lock — use-after-free / segfault from references that live past the owning guard. Affects dashmap ≥ 5.0.0 only; versions < 5.0.0 are unaffected. | ≥ 5.1.0 | [RUSTSEC-2022-0002](https://rustsec.org/advisories/RUSTSEC-2022-0002), [GHSA-mpg5-fvwp-42m2](https://github.com/advisories/GHSA-mpg5-fvwp-42m2) |

## Security Posture Notes

dashmap is the dominant concurrent `HashMap` for Rust, providing fine-grained sharded locking over DashMap and DashSet collections. It is a transitive dependency of many high-download crates (tracing, metrics, bevy, etc.).

The single published advisory (RUSTSEC-2022-0002, January 2022) identified an unsoundness in the 5.0.0 refactor: the `Ref`/`RefMut`/`RefMulti`/`RefMutMulti` mapref types exposed references whose lifetimes were insufficiently bounded to the owning guard, allowing safe Rust callers to trigger use-after-free / segfault. The fix in 5.1.0 tightened the lifetime annotations. Versions prior to 5.0.0 were never affected.

Upgrade to ≥ 5.1.0 (current 6.2.1, released 2026-05-17). No workaround exists for 5.0.0 callers — upgrade is required.

No SECURITY.md / security contact is listed in the repository.

## Dependencies of Note

None flagged; dashmap has minimal dependencies (hashbrown, parking_lot).

## Open Questions

- Are there additional unsoundness concerns in the current 6.x mapref API surface beyond RUSTSEC-2022-0002?
- Does the project plan to add a SECURITY.md / security contact?

## Related Pages

- [[rust/crossbeam]] — alternative concurrent data structures
- [[rust/index]]

---
*Last updated: 2026-09-10 | Sources: 2 (RUSTSEC-2022-0002, GHSA-mpg5-fvwp-42m2)*
