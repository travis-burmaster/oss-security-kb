# lettre (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~5,452,102 recent (as of 2026-08-29); 16,047,511 total
**Repository:** https://github.com/lettre/lettre
**Security Contact:** none listed (advisories filed via GitHub Security Advisories)
**Disclosure Policy:** https://github.com/lettre/lettre/security/advisories
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-28247 / GHSA-vc2p-r46x-m3vx | Moderate | Sendmail transport: forged recipient addresses inject arbitrary arguments into the sendmail command, potentially enabling write of email data to arbitrary filesystem paths depending on the sendmail binary used; SMTP and other transports unaffected | 0.7.1 / 0.8.4 / 0.9.5 | [GHSA-vc2p-r46x-m3vx](https://github.com/advisories/GHSA-vc2p-r46x-m3vx) |
| CVE-2021-38189 / GHSA-qc36-q22q-cjw3 / RUSTSEC-2021-0069 | Critical | SMTP command injection: period-escaping logic in `SmtpTransport::send()` failed to detect a period following a double-CRLF sequence, allowing attacker-controlled message body to inject arbitrary SMTP commands and terminate / re-author the message prematurely | 0.9.6 / 0.10.0-rc.3 | [GHSA-qc36-q22q-cjw3](https://github.com/advisories/GHSA-qc36-q22q-cjw3) |
| CVE-2026-46428 / GHSA-4pj9-g833-qx53 | Critical | `boring-tls` backend: inverted boolean passes `accept_invalid_hostnames` directly (without negation) to boring's `verify_hostname()`, reversing strict and permissive modes; default strict configuration silently disables TLS hostname verification, enabling network MITM of SMTP submissions with any valid certificate; `native-tls` and `rustls` backends unaffected | 0.11.22 | [GHSA-4pj9-g833-qx53](https://github.com/advisories/GHSA-4pj9-g833-qx53) |

## Security Posture Notes

lettre is the dominant Rust email sending library with ~5.4M recent crates.io downloads (16M+ total), supporting SMTP, the Sendmail transport, file-system and file-stub transports, and a full async API via Tokio. The current stable version is 0.11.23.

Three advisories across 2020–2026 cover two transport-layer injection classes and one TLS implementation error:

- **Sendmail argument injection** (CVE-2020-28247, Moderate): Affects only users of the `sendmail` transport feature. The fix validated recipient addresses before passing them as arguments, but the vulnerability window spans 0.7.0–0.9.4 across three simultaneous patch lines.
- **SMTP command injection** (CVE-2021-38189, Critical): Affects the SMTP transport broadly; the period-dot-stuffing algorithm (RFC 5321 §4.5.2) must handle the `CRLF.CRLF` end-of-data sequence correctly. The bug was that a period following `CRLFCRLF` was not escaped, allowing a message body to inject `SMTP DATA` termination and new commands. Both the stable 0.9.x and the pre-release 0.10.x lines required patching.
- **TLS hostname verification bypass** (CVE-2026-46428, Critical CVSS 9.1): The `boring-tls` Cargo feature (which substitutes BoringSSL for the default TLS stack) contained an API-contract mismatch: `accept_invalid_hostnames(true)` was passed to `verify_hostname()`, a method that takes the *inverse* semantics. Affected all uses of the `boring-tls` feature from 0.10.1 through 0.11.21; fixed 0.11.22. Users on `native-tls` or `rustls-tls` (the default) were never affected.

No dedicated security contact email is published; maintainers accept reports through GitHub Security Advisories. The project has a history of prompt CVE assignment and same-day patching across multiple version lines.

## Dependencies of Note

- **boring** (optional Cargo feature): BoringSSL Rust bindings. The inverted `verify_hostname` semantics (CVE-2026-46428) illustrate how a boolean-polarity mismatch in a security-critical TLS API can silently negate a security invariant; callers should audit which TLS feature they have selected in Cargo.toml.
- **rustls** / **native-tls** (default features): Neither backend was affected by CVE-2026-46428.

## Open Questions

- Do the three unreviewed GHSA records found under "lettre" in the advisory database (GHSA-4229-qg79-m48h, GHSA-53xp-3w48-mgww, GHSA-xr84-8x72-rcj7, 2022-05) and GHSA-7cmx-pq9m-76p5 (2023-06) apply to the lettre crate itself or downstream consumers?
- Is the async SMTP transport (`AsyncSmtpTransport`) subject to any DoS or connection-handling issues not yet reported?
- Has a formal security audit been conducted against the SMTP state machine implementation?

## Related Pages

- [[rust/actix-web]]
- [[rust/axum]]
- [[rust/rocket]]
- [[rust/index]]

---
*Last updated: 2026-08-29 | Sources: 3*
