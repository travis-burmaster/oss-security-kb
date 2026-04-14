# serde_yaml_ng (rust)

**Registry:** crates.io
**Weekly Downloads:** ~3,000,000 recent downloads (as of 2026-04-14)
**Repository:** https://github.com/acatton/serde-yaml-ng
**Security Contact:** none listed (no `SECURITY.md` in repo as of 2026-04-14)
**Disclosure Policy:** none listed
**Current Status:** audit-ingested

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-14 | travis-burmaster | Integer scalar parsing in `src/de.rs` | Manual read of `parse_unsigned_int` / `parse_negative_int` against the YAML 1.2 Core schema integer production; compared code paths against the archived `dtolnay/serde-yaml` upstream from which this fork inherits. | Reported a YAML 1.2 Core schema conformance gap around signed hex / octal / binary literals as public issue #32; behavior is inherited unchanged from the upstream archived crate. | https://github.com/acatton/serde-yaml-ng/issues/32 |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| acatton/serde-yaml-ng#32 | Low | `parse_unsigned_int` (`src/de.rs:936`) strips a leading `+` before inspecting `0x` / `0o` / `0b` prefixes, and `parse_negative_int` (`src/de.rs:1034`) explicitly accepts `-0x` / `-0o` / `-0b` prefixes. Inputs like `+0x10`, `+0o17`, `+0b11`, `-0x10`, `-0o17`, `-0b11` therefore deserialize as integers even though the YAML 1.2 Core schema forbids signs on non-decimal literals. In `#[serde(untagged)]` enums a value the author wrote as a string can silently dispatch to the integer variant, creating a type-confusion footgun for config and credential parsers that accept YAML from partly-untrusted sources. | Open | https://github.com/acatton/serde-yaml-ng/issues/32 |

*Full CVE history: https://osv.dev/list?ecosystem=crates.io&q=serde_yaml_ng* (no package-scoped OSV entries at time of review)

## Security Posture Notes

- `serde_yaml_ng` is one of several active forks that arose after [dtolnay/serde-yaml was archived in March 2024](https://github.com/dtolnay/serde-yaml). Its fork siblings at the time of this review are `serde_yml` (highest installs but archived September 2025), `serde_norway` (slower-moving), and `serde-yaml-bw` (security-focused but much smaller install base).
- It is the most actively maintained fork in the 1M+ weekly-downloads band that is still accepting community bug reports, which makes it the right target for conformance fixes even when the underlying bug class was inherited.
- Because parser code is essentially unchanged from the upstream archived crate, several YAML 1.2 Core schema edge cases in integer and float scalar parsing are likely to be shared across all forks derived from `dtolnay/serde-yaml`. Issues reported here may surface matching issues in `serde_yml`, `serde_norway`, and downstream consumers.
- Silent type confusion in `#[serde(untagged)]` dispatch is the highest-leverage downstream concern: a field that is semantically a string (token, tag, CLI flag) but happens to match a numeric scalar pattern will deserialize as the numeric variant.
- No `SECURITY.md` in the repository, so disclosure currently defaults to public issues and the public issue tracker.

## Dependencies of Note

- `serde` and `serde_derive` are the core downstream interfaces; most practically exploitable scenarios involve `#[serde(untagged)]` enums or custom `Deserialize` impls that trust scalar type dispatch.
- `unsafe-libyaml` provides the parser event stream; scalar classification and type coercion happen in `serde_yaml_ng`'s own `de.rs`, not in `unsafe-libyaml`.

## Open Questions

- Will the maintainer add a `SECURITY.md` so private vulnerability reports can route through GitHub Security Advisories instead of public issues?
- Which sibling forks (`serde_yml`, `serde_norway`, `serde-yaml-bw`) have diverged far enough from upstream parsing code that findings filed here no longer apply, and which still share the code path?
- Beyond the sign / non-decimal case documented in issue #32, are there additional YAML 1.2 Core schema conformance gaps — for example around `±.inf` / `±.nan` acceptance, leading-zero decimals, or unusual boolean literals — worth enumerating in a follow-on pass?
- Should the fork expose a strict parsing mode that rejects any scalar not matching the Core schema productions, giving downstream consumers a belt-and-braces guard against silent type confusion?

## Related Pages

- [[rust/serde]]
- [[rust/index]]

---
*Last updated: 2026-04-14 | Sources: 4 (crates.io crate API, `serde_yaml_ng` `src/de.rs` source at tip of main, YAML 1.2 spec §10.3 Core schema, filed public issue acatton/serde-yaml-ng#32)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
