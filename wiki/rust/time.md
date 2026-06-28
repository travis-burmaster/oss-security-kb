# time (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~10.8M/week estimated (as of 2026-06-28)
**Repository:** https://github.com/time-rs/time
**Security Contact:** GitHub Security Advisories — https://github.com/time-rs/time/security
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2020-0071 | Medium (no CVSS assigned) | `UtcOffset::local_offset_at` and `OffsetDateTime::now_local` manipulate the `TZ` environment variable via `localtime_r` without thread synchronisation; concurrent env-var reads in other threads trigger a segfault. All of `time` 0.1.x permanently affected; `time` 0.2.7–0.2.22 also vulnerable. Unix/Linux only — Windows and WASM unaffected. | ≥ 0.2.23 (0.1.x: no fix — upgrade to 0.2.23+ or 0.3.x) | [RUSTSEC-2020-0071](https://rustsec.org/advisories/RUSTSEC-2020-0071.html) |
| RUSTSEC-2026-0009 / CVE-2026-25727 / GHSA-r6v5-fh4h-64xc | Moderate (DoS) | Stack exhaustion when parsing RFC 2822 formatted date strings with maliciously crafted input; recursive parser lacks a depth limit, allowing callers to exhaust thread stack memory via crafted strings | ≥ 0.3.47 | [RUSTSEC-2026-0009](https://rustsec.org/advisories/RUSTSEC-2026-0009.html) |

## Security Posture Notes

`time` is a widely used Rust date-and-time library targeting full `std` interoperability and `#![no_std]` compatibility. It is the successor to the `time` 0.1.x series and is actively maintained by Jacob Pratt and contributors. Current latest stable: 0.3.51 (released 2026-06-22).

**RUSTSEC-2020-0071 context:** The `time` 0.1.x branch is permanently affected; the crate author does not intend to issue a fix for the 0.1 line. Users on 0.1.x must migrate to 0.2.23+ or the 0.3 series. The 0.2.x fix (0.2.23) removed the vulnerable functions from the default API surface. The 0.3.x series takes a stricter approach: these functions panic at runtime when called in a multi-threaded context (detectable via `std::thread::available_parallelism`), rather than invoking `localtime_r` unsafely. The `chrono` crate has a closely related advisory (RUSTSEC-2020-0159 / CVE-2020-26235) because chrono's `oldtime` feature historically delegated to `time` 0.1.x.

**RUSTSEC-2026-0009 context:** Introduced in 0.3.6, the RFC 2822 parser used unbounded recursion. The fix in 0.3.47 (released 2026-02-05) adds a depth limit to the parser, returning an error rather than exhausting stack. Callers using `format_description::well_known::Rfc2822` on untrusted input should ensure they run ≥ 0.3.47.

## Dependencies of Note

None flagged — `time` has minimal core dependencies; feature-gated formatting adds lightweight crates such as `itoa` and `num_threads`.

## Open Questions

- Is `time_macros` (the companion proc-macro crate) covered by the same advisory history, or does it warrant a separate pass?
- Are there soundness concerns in `#![no_std]` feature combinations beyond what RUSTSEC-2020-0071 covers?

## Related Pages

- [[rust/chrono]] — related date/time library with parallel RUSTSEC-2020-0159 / CVE-2020-26235 localtime_r issue
- [[rust/index]]

---
*Last updated: 2026-06-28 | Sources: 2*
