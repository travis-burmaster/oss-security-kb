# regex (crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~183,058,252 (as of 2026-06-20)
**Repository:** https://github.com/rust-lang/regex
**Security Contact:** https://www.rust-lang.org/policies/security (Rust Security Response WG handles all rust-lang/* repositories)
**Disclosure Policy:** https://www.rust-lang.org/policies/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-20 | OSS Security KB | advisory-db lookup | automated | 1 public advisory mapped (ReDoS / complexity-limit DoS) | [rustsec/advisory-db](https://github.com/rustsec/advisory-db/tree/main/crates/regex) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-24713 / RUSTSEC-2022-0013 / GHSA-m5pq-gvj9-9vr8 | High — DoS | The `regex` crate did not properly limit the complexity of parsed regular expressions. Patterns with large repetitions on empty sub-expressions (e.g. `(a*)*`) cause excessive parse time and CPU-exhaustion denial of service. Applications that accept untrusted user-controlled regex patterns are in scope; applications using only hardcoded or internally controlled patterns are not affected. There is no blocklist-based workaround; the fix requires upgrading. | 1.5.5 | [RUSTSEC-2022-0013](https://rustsec.org/advisories/RUSTSEC-2022-0013.html) |

## Security Posture Notes

`regex` is the canonical Rust regular expression library, maintained by the Rust programming language team (`rust-lang/regex`). With ~914M total downloads and ~183M recent weekly downloads it is one of the most downloaded crates across the entire Rust ecosystem, used transitively in most non-trivial Rust projects.

The single published advisory (RUSTSEC-2022-0013 / CVE-2022-24713) follows the classic ReDoS pattern and primarily affects applications that accept user-supplied regex strings as input. Current version 1.12.4 (released 2026-06-09) is well past the 1.5.5 fix boundary; the advisory is only relevant for code pinned to pre-1.5.5 versions or derivative libraries that embed an old copy.

Security reports for `rust-lang/*` repositories are handled by the Rust Security Response Working Group at the policy URL above.

## Dependencies of Note

- `regex-automata` — underlying automata engine split from the main crate in 2023; may carry separate advisory exposure not yet reflected in the top-level `regex` crate advisory record.
- `regex-syntax` — regex parser / AST crate, split from the main crate; independently versioned.
- `aho-corasick` — multi-pattern matching; independently versioned.
- `memchr` — byte-oriented search; independently versioned.

## Open Questions

- Search rustsec/advisory-db for `regex-automata` and `regex-syntax` to determine whether any split-crate advisories have been filed that are not aliased back to the top-level `regex` crate.
- Assess whether the 2022 complexity-limit fix fully addresses all known large-repetition ReDoS patterns or whether partial coverage remains.

## Related Pages

- [[rust/index]]

---
*Last updated: 2026-06-20 | Sources: 2 (rustsec/advisory-db, crates.io API)*
