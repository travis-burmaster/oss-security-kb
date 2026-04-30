# serde (rust)

**Registry:** crates.io
**Weekly Downloads:** ~156,618,523 recent downloads (as of 2026-04-20)
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
| No package-level OSV / RustSec record clearly confirmed in this review pass | — | Public-source review did **not** surface a direct package-scoped advisory for `crates.io/serde`. Related advisories in the broader Serde ecosystem apply to separate crates such as `serde_yaml`, `serde_yml`, `serde_cbor`, `serde-json-wasm`, and `rmp-serde`, not to the core `serde` crate itself. | — | https://api.osv.dev/v1/query |

*Full advisory history (OSV): https://osv.dev/list?ecosystem=crates.io&q=serde*

## Security Posture Notes

- `serde` is foundational Rust serialization / deserialization infrastructure with an extremely large downstream footprint, so any future package-level advisory would likely have wide ecosystem blast radius.
- Public advisory evidence in this pass remained **empty for the core crate itself**: the OSV package query returned no records, and RustSec search results surfaced only related crates rather than `serde` directly.
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
*Last updated: 2026-04-20 | Sources: 6 (OSV API package query for crates.io/serde, OSV package search page for serde, RustSec advisory search results, crates.io API metadata, upstream README, repository security-policy check, local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid)*
