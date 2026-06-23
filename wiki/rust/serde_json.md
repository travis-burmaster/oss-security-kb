# serde_json (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~16.1M/week estimated (207,149,044 recent 90-day downloads; 1,001,041,240 all-time as of 2026-06-23)
**Repository:** https://github.com/serde-rs/json
**Security Contact:** none listed (use GitHub issues or the Rust security advisory process at https://www.rust-lang.org/policies/security)
**Disclosure Policy:** none listed
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| (none on record) | — | No package-scoped RustSec advisory confirmed for `serde_json` in this pass. Search of rustsec/advisory-db (path: `crates/serde_json`) returned no direct results. | — | [RustSec DB](https://github.com/rustsec/advisory-db) |

*OSV link: https://osv.dev/list?ecosystem=crates.io&q=serde_json*

## Security Posture Notes

`serde_json` is the de facto standard JSON serialization/deserialization library for Rust, maintained by David Tolnay (`dtolnay`) under the `serde-rs` organization. It is the most-downloaded non-proc-macro crate on crates.io with over 1 billion all-time downloads.

As of this pass (2026-06-23), no direct package-scoped public advisory exists in the RustSec advisory database or GitHub Advisory Database for `serde_json` itself. The crate's design — pure safe Rust with no `unsafe` in the main deserialization path — limits the traditional memory-safety attack surface. Known risk areas based on design:

- **Deeply nested inputs:** JSON parsers are commonly vulnerable to stack overflow or excessive recursion on deeply nested objects/arrays. `serde_json` does not expose a public recursion-limit API; downstream users processing untrusted input should apply an application-level size/depth constraint before passing data to the parser.
- **Number precision:** `serde_json` uses `f64` for arbitrary numbers by default; inputs with more precision than `f64` can represent are silently rounded. Applications requiring exact large-integer handling should use the `arbitrary_precision` feature.
- **Supply-chain exposure:** The crate depends on `serde` (the serialization framework) and `itoa` / `ryu` (number formatting). None of these dependencies have direct active RustSec advisories as of this pass, but the transitive blast radius of `serde_json` means that any future advisory in its dependency graph would affect an extremely large fraction of the Rust ecosystem.
- **Ecosystem blast radius:** Virtually every Rust project that handles JSON — including all major web frameworks (axum, actix-web, warp), async runtimes, and cloud SDKs — depends on `serde_json`. A supply-chain compromise or critical upstream advisory would have broad ecosystem impact.

The crate's current version is 1.0.150 (MIT OR Apache-2.0).

## Dependencies of Note

- `serde` (~1.0.x) — foundational serialization framework; no direct active RUSTSEC advisory confirmed in prior passes (see [[rust/serde]]).
- `itoa`, `ryu` — integer and float formatting; no active RustSec advisories.

## Open Questions

- Has a formal security assessment of `serde_json` been published? The crate's minimal use of `unsafe` reduces but does not eliminate the audit need.
- Does `serde_json` bound maximum nesting depth on untrusted input by default? If not, what is the practical stack limit on common platforms?
- Are there known issues with the `arbitrary_precision` or `raw_value` features on adversarial input?

## Related Pages

- [[rust/serde]]
- [[rust/reqwest]]
- [[rust/index]]

---
*Last updated: 2026-06-23 | Sources: rustsec/advisory-db code search; crates.io API metadata*
