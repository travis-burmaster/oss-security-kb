# http (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~18.1M/week est. (as of 2026-09-13)
**Repository:** https://github.com/hyperium/http
**Security Contact:** none listed (GitHub security advisories)
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|
| RUSTSEC-2019-0033 / CVE-2019-25008 / CVE-2020-25574 | High (CVSS 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | Integer overflow in `HeaderMap::reserve()`: `next_power_of_two()` wraps to zero for sufficiently large input in release builds; if the map is non-empty, the code attempts to grow it with size 0 → infinite probing loop → remote DoS | ≥ 0.1.20 | [RUSTSEC-2019-0033](https://rustsec.org/advisories/RUSTSEC-2019-0033) |
| RUSTSEC-2019-0034 / CVE-2019-25009 | Critical (CVSS 9.8) | `HeaderMap::Drain` API memory-safety unsoundness: (1) not dropping the `Drain` struct causes double-free; (2) the `Drain` iterator implementation violates Rust's aliasing rules, enabling a data race — both reachable from safe code | ≥ 0.1.20 | [RUSTSEC-2019-0034](https://rustsec.org/advisories/RUSTSEC-2019-0034) |

## Security Posture Notes

The `http` crate provides the foundational HTTP types used throughout the Rust async web ecosystem: `Request`, `Response`, `HeaderMap`, `Uri`, `Method`, `StatusCode`, `HeaderName`, and `HeaderValue`. It is a direct dependency of hyper, reqwest, axum, warp, tower-http, tonic, actix-web, and virtually every other Rust HTTP library. Total crates.io downloads exceed 1 billion (~1.005B); the 90-day recent download count is ~232.8M (~18.1M/week estimated).

Both confirmed advisories were disclosed simultaneously on 2019-11-16 and both fixed in 0.1.20. The `HeaderMap::reserve()` overflow (RUSTSEC-2019-0033) requires the attacker to control the reserve argument — callers that derive this value from untrusted input (e.g., a `Content-Length`-derived pre-allocation) are most exposed. The `Drain` unsoundness (RUSTSEC-2019-0034) is triggered by normal safe code that neglects to drop the iterator or uses it concurrently.

Current stable is 1.5.0. The 1.x major line (released 2023) is a significant API rewrite; it retains the same `HeaderMap` internals philosophy but with revised bounds-checking. Neither 0.1.20+ nor any 0.2.x or 1.x release carries these advisories. The hyperium organization (maintainers of hyper and http) does not publish a formal SECURITY.md; security issues should be reported through GitHub security advisories on the repository.

## Dependencies of Note

The `http` crate has minimal dependencies (primarily std and small utility crates with no known security history). Its blast radius is indirect: ecosystem-wide exposure flows from consumers (hyper, reqwest, axum, etc.) inheriting the `HeaderMap` and `Uri` APIs.

## Open Questions

- Confirm that the 1.x `Uri` and `HeaderMap` implementations have not introduced new integer-arithmetic edge cases analogous to RUSTSEC-2019-0033.
- Verify whether the `http` 1.x release carried an independent security review given the API surface changes.

## Related Pages

- [[rust/hyper]]
- [[rust/axum]]
- [[rust/reqwest]]
- [[rust/tower-http]]
- [[rust/h2]]
- [[rust/index]]

---
*Last updated: 2026-09-13 | Sources: 2*
