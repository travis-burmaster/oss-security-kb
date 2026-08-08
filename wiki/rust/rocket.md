# Rocket (rust)

**Registry:** crates.io
**Weekly Downloads:** ~1.2M (as of 2026-08-08)
**Repository:** https://github.com/SergioBenitez/Rocket
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|---------|
| RUSTSEC-2020-0028 | Moderate | `LocalRequest::clone` reuses the raw pointer to the inner `Request` object, creating multiple aliased mutable references — undefined behaviour enabling data races or memory corruption when both instances are used; affects 0.4.0–0.4.4 | 0.4.5 | [RUSTSEC-2020-0028](https://rustsec.org/advisories/RUSTSEC-2020-0028.html) |
| RUSTSEC-2021-0044 | Low | Use-after-free in `uri::Formatter`: a `&str` is transmuted to `&'static str` and pushed to a stack vec; a panic in a user callback between push and pop causes the transmuted reference to dangle, enabling use-after-free during unwind or via `catch_unwind`; affects < 0.4.7 | 0.4.7 | [RUSTSEC-2021-0044](https://rustsec.org/advisories/RUSTSEC-2021-0044.html) |

## Security Posture Notes

Rocket is a type-safety-focused Rust web framework. Both advisories affect the 0.4.x release line, which has been superseded by the 0.5.x line (current stable: 0.5.1, a significant async rewrite). Neither advisory has a CVE number assigned. The crate does not publish a SECURITY.md or a formal disclosure contact. All-time downloads: ~12.5M; recent weekly: ~1.2M (crates.io, 2026-08-08). Download volume is moderate for a Rust web framework — axum and actix-web see substantially higher weekly usage.

## Dependencies of Note

- **hyper / tokio**: Rocket 0.5.x uses tokio and hyper as the async runtime foundation; see [[rust/hyper]] and [[rust/tokio]].

## Open Questions

- Confirm whether a SECURITY.md or formal disclosure contact has been added in the 0.5.x series.
- Check for advisories against 0.5.x-specific async code paths (async guards, async fairings, async handlers).
- Assess whether the 0.4.x line is still actively used in production given 0.5.0 was released in May 2024.

## Related Pages

- [[rust/axum]]
- [[rust/actix-web]]
- [[rust/hyper]]
- [[rust/tokio]]
- [[rust/index]]

---
*Last updated: 2026-08-08 | Sources: 2*
