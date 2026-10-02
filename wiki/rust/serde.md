# serde (rust)

**Registry:** crates.io
**Weekly Downloads:** ~26.1M/week est. (~335.4M recent 90-day; ~1.47B total downloads) (as of 2026-10-02)
**Repository:** https://github.com/serde-rs/serde
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-10-02 | OpenClaw advisory-review | public-source advisory triage (third confirmation pass) | public-source curation (rustsec/advisory-db path `crates/serde/` search, `crate = "serde"` and `crate = "serde_json"` advisory body searches, crates.io API metadata) | No direct package-scoped RUSTSEC advisory confirmed for `serde` or `serde_json` — third independent pass reconfirms prior 2026-04-20 and 2026-07-19 conclusions; download stats updated | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| 2026-07-19 | OpenClaw advisory-review | public-source advisory triage (second pass) | public-source curation (OSV API package query, RustSec advisory search, crates.io metadata) | No advisory confirmed for `serde` or `serde_json`; related adjacent crates documented | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| 2026-04-20 | OpenClaw recurring review | package baseline / public-source triage | public-source curation (OSV API package query, RustSec advisory search, crates.io metadata, upstream README, repository security-policy check) | No direct package-scoped OSV or RustSec advisory confirmed for `serde` itself; page captures disclosure-policy gaps and ecosystem blast radius | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| No package-level RUSTSEC / GHSA record confirmed (reconfirmed 2026-10-02) | — | Three independent search passes (2026-04-20, 2026-07-19, 2026-10-02) found no advisory in rustsec/advisory-db targeting the `serde` or `serde_json` crates directly. Searches included: rustsec/advisory-db path `crates/serde/`, `crate = "serde"` body search, `crate = "serde_json"` body search — all 0 results. Related advisories in the broader Serde ecosystem apply to separate crates: `serde_yaml`, `serde_yml` (RUSTSEC-2025-0068 unmaintained), `serde_cbor` (RUSTSEC-2021-0127 unmaintained), `serde-json-wasm` (RUSTSEC-2024-0012 stack-overflow DoS), `rmp-serde` (RUSTSEC-2022-0092 unsound Deserializer) — **not** to the core `serde` or `serde_json` crates. | — | https://github.com/rustsec/advisory-db/tree/main/crates |

*Full advisory history (OSV): https://osv.dev/list?ecosystem=crates.io&q=serde*

## Security Posture Notes

- `serde` (v1.0.229, July 2026) and `serde_json` (v1.0.151, July 2026) are among the most downloaded Rust crates — ~1.47B and ~1.37B total downloads respectively, each at ~26M downloads per week. Maintained by David Tolnay (@dtolnay) with a consistent release cadence.
- Three independent public-source advisory passes spanning 2026-04-20 through 2026-10-02 found **no advisory in the core `serde` or `serde_json` crates themselves**. This is a notable clean record for crates at this scale and blast radius.
- The distinction between core crates and format adapters matters: findings in `serde_yaml`, `serde_cbor`, `rmp-serde`, `serde-json-wasm`, and similar wrapper/adapter crates should not be attributed to `serde` or `serde_json` unless a public record explicitly scopes the issue to those core crates.
- No repository-level `SECURITY.md` or dedicated disclosure-policy URL has been confirmed. This is a documentation gap; the project does not appear to have a formal vulnerability-reporting path distinct from the public GitHub issue tracker.
- Operationally, security risk around Serde most often materialises in format-specific parsing crates, in application-level decisions about which types are exposed to deserialization, and in derive-generated code for complex types — not in the core trait and visitor framework itself.
- `serde_json` does perform security-relevant operations (number parsing, string decoding, recursion depth bounding) that could theoretically be audited for edge-case correctness; no public audit of these paths has been confirmed across three passes.

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
*Last updated: 2026-10-02 | Sources: 5 (rustsec/advisory-db path crates/serde/ search confirming no direct advisory; rustsec/advisory-db body searches for `crate = "serde"` and `crate = "serde_json"` confirming no direct advisory; crates.io API for serde and serde_json download/version stats; prior 2026-07-19 and 2026-04-20 pass evidence)*
