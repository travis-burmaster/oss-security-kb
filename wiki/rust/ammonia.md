# ammonia (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~4.4M/week (as of 2026-09-26)
**Repository:** https://github.com/rust-ammonia/ammonia
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-15542 / RUSTSEC-2019-0001 | High (CVSS 9.8) | Stack overflow via deeply-nested HTML input in serialization (`to_string`, `write_to`, `clean`) — DoS / process abort; recursive serializer replaced with iterative approach | ≥ 2.1.0 | [RUSTSEC-2019-0001](https://rustsec.org/advisories/RUSTSEC-2019-0001.html) |
| CVE-2021-38193 / RUSTSEC-2021-0074 | — | Mutation XSS via namespace-incompatible raw-text elements (script, style, textarea, title, iframe, noscript) in SVG/MathML contexts — crafted input produces an "impossible DOM" that appears safe but injects markup on browser re-parse | ≥ 2.1.3 (2.x) / ≥ 3.1.0 (3.x) | [RUSTSEC-2021-0074](https://rustsec.org/advisories/RUSTSEC-2021-0074.html) |
| RUSTSEC-2022-0003 / GHSA-p2g9-94wh-65c2 | — | Form-feed character injection in `clean_text` via incorrect ASCII mapping — allows attribute injection when output is placed in unquoted HTML attributes; not exploitable when attributes are quoted or `clean_text` is unused | ≥ 3.1.3 | [RUSTSEC-2022-0003](https://rustsec.org/advisories/RUSTSEC-2022-0003.html) |
| RUSTSEC-2025-0071 / GHSA-mm7x-qfjj-5g2c | Low (CVSS 4.0) | Mutation XSS via namespace-incompatible tags when `svg` or `math` tag is allowed alongside raw-text HTML elements — incomplete fix of the RUSTSEC-2021-0074 class for certain tag combinations; fixed Sep 2025 | ≥ 3.3.1 / ≥ 4.0.1 / ≥ 4.1.2 | [RUSTSEC-2025-0071](https://rustsec.org/advisories/RUSTSEC-2025-0071.html) |
| CVE-2026-63430 / RUSTSEC-2026-0193 | — | Mutation XSS via `math` + `annotation-xml` when the `encoding` attribute is explicitly disabled — attribute filter strips `encoding`, causing namespace-incompatible raw-text elements to parse as MathML; exploitable only when both `math` and `annotation-xml` are explicitly allowed | ≥ 3.3.2 / ≥ 4.0.2 / ≥ 4.1.3 | [RUSTSEC-2026-0193](https://rustsec.org/advisories/RUSTSEC-2026-0193.html) |
| RUSTSEC-2026-0213 | — | XSS via SVG animation tags (`animate`, `set`) — `to`, `from`, `values` attributes not filtered based on `attributeName`, allowing `javascript:` URL injection via SVG animation; exploitable only when these animation tags are explicitly allowed (blocked by default) | ≥ 3.3.3 / ≥ 4.0.3 / ≥ 4.1.4 | [RUSTSEC-2026-0213](https://rustsec.org/advisories/RUSTSEC-2026-0213.html) |

*OSV link: https://osv.dev/list?ecosystem=crates.io&q=ammonia*

## Security Posture Notes

`ammonia` is the dominant Rust HTML sanitization library (~4.4M/week, ~16.7M total downloads), comparable in role to DOMPurify in the JavaScript ecosystem. It uses `html5ever` (Mozilla/Servo HTML parser) internally and applies an allowlist model: only tags, attributes, and URL schemes explicitly permitted by the caller are passed through.

The advisory history reveals two persistent vulnerability classes:

1. **Stack overflow in early versions** (RUSTSEC-2019-0001): recursive DOM serialization replaced with an iterative approach in 2.1.0.

2. **Mutation XSS via namespace confusion** (RUSTSEC-2021-0074, RUSTSEC-2025-0071, RUSTSEC-2026-0193, RUSTSEC-2026-0213): a recurring class exploiting how browsers reparse HTML when SVG and MathML namespace boundaries are crossed. All four share the same root cause pattern. Exploitability in practice requires the application to explicitly enable the relevant tags (`svg`, `math`, `annotation-xml`, `animate`, `set`), all of which are **blocked by default**.

The `clean_text` attribute-injection issue (RUSTSEC-2022-0003) is a narrower flaw affecting only callers using `clean_text` who embed output in unquoted HTML attributes.

No formal `SECURITY.md` or security contact is listed in the repository; disclosures have been handled via GitHub issues and RustSec advisory submissions. Current stable: **4.2.0** (2026-09-26).

## Dependencies of Note

- `html5ever` (Servo/Mozilla HTML parser): no direct RustSec advisories; namespace-parsing behavior is a contributing factor to the mutation-XSS class.
- `maplit`, `tendril`, `url`: no known advisories.

## Open Questions

- No formal security contact / SECURITY.md in the repository — does the project plan to formalize a disclosure path?
- Are further namespace-confusion patterns possible with other non-default tag allowlists not yet audited?
- Track CVE assignment for RUSTSEC-2026-0213 (none assigned at time of this pass).

## Related Pages

- [[npm/dompurify]] — analogous JavaScript HTML sanitizer with dense mutation-XSS history
- [[npm/sanitize-html]] — analogous Node.js HTML sanitizer
- [[rust/axum]] — Rust web framework commonly serving sanitized HTML
- [[rust/actix-web]] — Rust web framework
- [[rust/index]]

---
*Last updated: 2026-09-26 | Sources: 3*
