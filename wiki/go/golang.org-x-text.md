# golang.org/x/text (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-06-22)
**Repository:** https://cs.opensource.google/go/x/text (mirror: https://github.com/golang/text)
**Security Contact:** https://go.dev/security/policy
**Disclosure Policy:** https://go.dev/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-06-22 | OSS Security KB | GHSA database lookup | automated | 3 public advisories mapped (CVE-2020-14040 through CVE-2022-32149) | [github/advisory-database](https://github.com/github/advisory-database) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-14040 / GHSA-5rcv-m4m3-hfh7 | Moderate | UTF-16 decoder infinite loop in `encoding/unicode`: a single-byte input to a UTF-16 decoder instantiated with `UseBOM` or `ExpectBOM` could cause the decoder to enter an infinite loop, crashing the program or exhausting memory. Triggered by calling `String()` on the decoder or passing the decoder to `golang.org/x/text/transform.String`. | 0.3.3 | [GHSA-5rcv-m4m3-hfh7](https://github.com/advisories/GHSA-5rcv-m4m3-hfh7) |
| CVE-2021-38561 / GHSA-ppp9-7jff-5vj2 | High — CVSS 7.5 | Out-of-bounds read in `golang.org/x/text/language` BCP 47 language tag parser: mishandled index calculation during parsing of untrusted language tag input could cause a panic (out-of-bounds read), enabling denial of service. Affects the `language.Parse` family of functions when fed user-controlled input. | 0.3.7 | [GHSA-ppp9-7jff-5vj2](https://github.com/advisories/GHSA-ppp9-7jff-5vj2) |
| CVE-2022-32149 / GHSA-69ch-w2m2-3vjp | High — CVSS 7.5 | Quadratic time complexity in `language.ParseAcceptLanguage`: the BCP 47 tag parser had inherent quadratic time complexity due to design constraints and could not be rewritten easily. An attacker sending crafted `Accept-Language` HTTP headers with many dashes could force significant CPU time in servers parsing them. Fix imposes a limit of 1000 dashes in the input string. | 0.3.8 | [GHSA-69ch-w2m2-3vjp](https://github.com/advisories/GHSA-69ch-w2m2-3vjp) |

## Security Posture Notes

`golang.org/x/text` is a foundational Go module maintained by the Go team, providing text processing, Unicode normalization, encoding conversion, internationalization (i18n), and language-tag handling. It is a transitive dependency of virtually every Go web application that handles non-ASCII text or parses HTTP headers with language negotiation.

**Recurring vulnerability class — BCP 47 / language tag parsing:** CVE-2021-38561 and CVE-2022-32149 are both rooted in the `golang.org/x/text/language` sub-package's BCP 47 parser. The OOB panic (0.3.7 fix) and the quadratic complexity DoS (0.3.8 fix) arose from the inherent complexity of the BCP 47 specification and the difficulty of safely bounding untrusted parser inputs. Applications that expose `Accept-Language` or similar header values to `language.ParseAcceptLanguage` without pre-validation are the primary exposure surface.

**`golang.org/x/text/search` misuse (2026, downstream):** GHSA-3g8v-8r37-cgjm (FrankenPHP, CVE-2026-45062) and GHSA-m675-2p33-xv9g (Caddy, CVE-2026-45135) demonstrate that `search.New(language.Und, search.IgnoreCase)` performs Unicode equivalence matching far beyond what callers typically expect, leading to CGI path-splitting bypasses in PHP runtimes. These vulnerabilities are in downstream users of `golang.org/x/text/search`, not in the `golang.org/x/text` package itself, but they illustrate a subtle API footgun worth tracking.

**Latest version:** v0.38.0 (2026-06-08). Actively maintained by the Go team.

## Dependencies of Note

None flagged at the module level. `golang.org/x/text` has minimal external dependencies; its security surface is primarily the correctness of parser and decoder logic for complex text standards (BCP 47, Unicode normalization, ISO-8859-x, etc.).

## Open Questions

- Verify whether any advisories were added to the Go vuln database (pkg.go.dev/vuln) for `golang.org/x/text` between 2022 and the current pass; the OSV API is blocked in this environment.
- Track whether the `golang.org/x/text/search` `IgnoreCase` behavior gets a documentation warning or behavior change upstream in response to the 2026 FrankenPHP/Caddy findings.
- Check weekly download stats via a future pass (pkg.go.dev does not expose download counts directly; module proxy telemetry is unpublished).

## Related Pages

- [[go/golang.org-x-net]]
- [[go/golang.org-x-crypto]]
- [[go/index]]

---
*Last updated: 2026-06-22 | Sources: github/advisory-database (GHSA-5rcv-m4m3-hfh7, GHSA-ppp9-7jff-5vj2, GHSA-69ch-w2m2-3vjp), pkg.go.dev/golang.org/x/text*
