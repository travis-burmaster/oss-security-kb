# hyper (rust)

**Registry:** crates.io
**Recent Downloads:** ~131,073,063 (recent window reported by crates.io, fetched 2026-05-08)
**Repository:** https://github.com/hyperium/hyper
**Security Contact:** GitHub Security Advisory private reporting / Hyperium security policy
**Disclosure Policy:** https://github.com/hyperium/hyper/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-08 | OpenClaw recurring review | crate advisory history | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database / GitHub Security Advisory records surfaced through OSV, RustSec records, public CVE / NVD aliases, crates.io metadata, and upstream security policy / changelog references) | Added advisory-mapped coverage for the public hyper vulnerability trail: HTTP/1 parser/request-smuggling issues, header injection, Windows TLS hostname-verification failure, and one HTTP parser memory-safety / soundness issue. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2016-10932 / GHSA-9xjr-m6f3-v5wm / RUSTSEC-2016-0002 | Moderate | On Windows, pre-0.9.4 hyper HTTPS clients did not perform hostname verification, allowing certificate-name mismatches to undermine TLS server authentication. | 0.9.4 | https://rustsec.org/advisories/RUSTSEC-2016-0002.html |
| CVE-2017-18587 / GHSA-q89x-f52w-6hj2 / RUSTSEC-2017-0002 | Moderate | Header serialization did not filter newline bytes in header values, so applications that built headers from unsanitized input could create request / response splitting risk. | 0.9.18 / 0.10.2 | https://rustsec.org/advisories/RUSTSEC-2017-0002.html |
| CVE-2020-35863 / GHSA-h3qr-rq2j-74w4 / RUSTSEC-2020-0008 | Critical | HTTP/1 request-boundary confusion around GET requests with bodies could allow request-smuggling-style behavior when hyper's interpretation differed from surrounding infrastructure. | 0.12.34 | https://rustsec.org/advisories/RUSTSEC-2020-0008.html |
| CVE-2021-21299 / GHSA-6hfq-h8hq-87mf / RUSTSEC-2021-0020 | Moderate | Hyper's server-side HTTP/1 parser mishandled requests with multiple `Transfer-Encoding` headers, creating request-smuggling / desync risk when an upstream proxy interpreted the same request differently. | 0.12.36 / 0.13.10 / 0.14.3 | https://rustsec.org/advisories/RUSTSEC-2021-0020.html |
| CVE-2021-32714 / GHSA-5h46-h7hh-c6x9 / RUSTSEC-2021-0079 | Moderate | Chunk-size parsing in chunked transfer decoding could overflow on oversized values, causing data loss and possible desynchronization when paired with infrastructure that accepted a different chunk boundary. | 0.14.10 | https://rustsec.org/advisories/RUSTSEC-2021-0079.html |
| CVE-2021-32715 / GHSA-f3pg-qwvg-p99c / RUSTSEC-2021-0078 | Low | HTTP/1 `Content-Length` parsing accepted a leading plus sign that stricter proxies might reject or ignore, creating another parser-differential request-smuggling condition. | 0.14.10 | https://rustsec.org/advisories/RUSTSEC-2021-0078.html |
| GHSA-f67m-9j94-qv9j / RUSTSEC-2022-0022 | High | Affected HTTP/1 parser code created `httparse::Header` values with `mem::uninitialized()`, which is unsound for a type containing references; the fix switched away from that invalid initialization pattern. | 0.14.12 | https://rustsec.org/advisories/RUSTSEC-2022-0022.html |

*Full advisory history (OSV): https://osv.dev/list?ecosystem=crates.io&q=hyper*

## Security Posture Notes

- Hyper is a foundational Rust HTTP implementation with very large transitive reach: crates.io metadata in this review showed ~637M total downloads and ~131M recent downloads. Many applications inherit it through higher-level clients and frameworks rather than depending on it directly.
- The public advisory cluster is dominated by **HTTP/1 parser differential and request-boundary bugs**. These are best framed as desynchronization / request-smuggling risks that depend on how hyper is combined with proxies, gateways, or other HTTP parsers.
- Several older records affect legacy 0.x trains only. Current consumers should still scan lockfiles because old hyper versions can remain reachable through transitive dependencies even after direct application code has moved on.
- The 2022 `mem::uninitialized()` advisory is different from the parser-differential records: it is a Rust memory-safety / soundness defect in parser internals rather than a request-routing semantic issue.
- The upstream security policy provides a documented private-reporting path and says publicly disclosed issues are coordinated through GitHub Security Advisories and RustSec, which is a useful maturity signal for downstream consumers.
- No active vulnerability hunting was performed in this pass; the page records only already-published public advisory and maintainer evidence.

## Dependencies of Note

- `httparse` is security-relevant because one hyper advisory directly involved unsafe initialization of `httparse::Header` values in hyper's HTTP/1 parser path.
- `tokio`, `h2`, `http`, and related Hyperium companion crates are natural adjacent review targets because modern Rust web stacks often combine them with hyper.
- TLS posture can depend on connector crates and platform choices; the historical Windows hostname-verification advisory is a reminder not to treat the core HTTP crate alone as the whole transport-security boundary.

## Open Questions

- Which high-usage downstream crates still pull old vulnerable hyper 0.x versions transitively, and should those downstream pages cross-link this one?
- Should `h2`, `http`, `reqwest`, and `axum` receive dedicated pages so hyper-adjacent HTTP parsing and framework-mode risks are easier to navigate?
- Are there public independent audit reports for hyper beyond the advisory / RustSec / maintainer trail captured here?

## Related Pages

- [[rust/tokio]]
- [[rust/serde]]
- [[rust/index]]

---
*Last updated: 2026-05-08 | Sources: 7 (OSV package query and vulnerability records, GitHub Advisory Database / GitHub Security Advisory records surfaced through OSV, RustSec advisory pages, public CVE / NVD aliases, crates.io metadata, upstream Hyper security policy, upstream changelog / repository metadata)*
