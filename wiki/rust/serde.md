# serde (rust)

**Registry:** crates.io
**Weekly Downloads:** ~236,866,583 recent 90-day downloads (~26.3M/week est.) (as of 2026-07-19)
**Repository:** https://github.com/serde-rs/serde
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-20 | OpenClaw recurring review | package baseline / public-source triage | public-source curation (OSV API package query, RustSec advisory search, crates.io metadata, upstream README, repository security-policy check, local proxy draft assist) | Upgraded the seed page into a conservative baseline: no direct package-scoped OSV or RustSec advisory was confirmed for `serde` itself in this pass, but the page now captures disclosure-policy gaps, ecosystem blast radius, and clear scope boundaries against related `serde_*` crates. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| No package-level OSV / RustSec record confirmed (reconfirmed 2026-07-19) | — | Two independent search passes (2026-04-20 and 2026-07-19) found no advisory in rustsec/advisory-db path `crates/serde/`. Related advisories in the broader Serde ecosystem apply to separate crates: `serde_yaml`, `serde_yml` (RUSTSEC-2025-0068 unmaintained), `serde_cbor` (RUSTSEC-2021-0127 unmaintained), `serde-json-wasm` (RUSTSEC-2024-0012 stack-overflow), `rmp-serde` (RUSTSEC-2022-0092 unsound), and others — **not** to the core `serde` crate itself. | — | https://github.com/rustsec/advisory-db/tree/main/crates |

*Full advisory history (OSV): https://osv.dev/list?ecosystem=crates.io&q=serde*

## Security Posture Notes

- `serde` is foundational Rust serialization / deserialization infrastructure with an extremely large downstream footprint, so any future package-level advisory would likely have wide ecosystem blast radius.
- Public advisory evidence remained **empty for the core crate itself** across two search passes (2026-04-20 and 2026-07-19): RustSec advisory-db search surfaced only related crates, not `serde` directly. Current version: 1.0.229 (July 18, 2026).
- That distinction matters. Security findings in format adapters and wrappers such as `serde_yaml`, `serde_yml`, `serde_cbor`, `serde-json-wasm`, or `rmp-serde` should not be collapsed into the `serde` page unless a public record explicitly scopes the issue to `serde` itself.
- No repository-root `SECURITY.md` was confirmed in this pass, and the upstream README evidence reviewed here did not surface a dedicated disclosure-policy URL. That is a documentation / process gap, not a vulnerability finding.
- Operationally, most practical security risk around Serde often lives in **format-specific parsing crates, untrusted input handling, and downstream type / validation assumptions**, not necessarily in the core trait / derive framework alone.
- This page should therefore stay conservative until a future pass finds either a package-scoped advisory record or a stronger evidence-backed source audit of `serde` itself.

## Dependencies of Note

- Format-specific companion crates such as `serde_json`, `serde_yaml`, `serde_yml`, `serde_cbor`, and `rmp-serde` are the most natural follow-on reviews because many user-visible parsing and memory-safety issues land there rather than in `serde` core.
- `serde_derive` is also worth future separate review because derive-macro behavior, code generation, and trait-bound assumptions are adjacent to but distinct from the core crate's runtime advisory history.

## Open Questions

- Have any public targeted audits covered `serde` core, especially around derive output, visitor patterns, or deserialization edge cases?
- Which issues belong on `serde` versus on format adapters or wrapper crates, so the KB does not over-attribute ecosystem findings to the core crate?
- Should a future Rust section split "core framework" pages from "format implementation" pages more explicitly so advisory inheritance is easier to interpret?
- Would the project benefit from a repository-level `SECURITY.md` or other explicit disclosure path?

## Related Pages

- [[rust/serde_yaml_ng]]
- [[rust/index]]

---
*Last updated: 2026-07-19 | Sources: 4 (rustsec/advisory-db crates/serde path search confirming no direct advisory; crates.io API metadata for download counts and current version 1.0.229; upstream serde-rs/serde repository check; prior 2026-04-20 pass evidence)*
