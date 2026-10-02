# MailKit / MimeKit (dotnet)

**Registry:** NuGet
**Weekly Downloads:** unknown (NuGet registration API does not expose download counts; as of 2026-10-02)
**Repository:** https://github.com/jstedfast/MailKit · https://github.com/jstedfast/MimeKit
**Security Contact:** GitHub Private Security Advisory (preferred) · jestedfa@microsoft.com (fallback)
**Disclosure Policy:** https://github.com/jstedfast/MailKit/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-10-02 | OpenClaw advisory-review | package baseline / public-source triage | public-source curation (GHSA search via github/advisory-database, NuGet registration metadata, upstream SECURITY.md review) | 3 package-scoped GHSA advisories confirmed: 1 transitive DoS (MimeKit, High CVSS 7.5, 2024), 1 CRLF injection enabling SMTP command injection (MimeKit + MailKit, Moderate CVSS 4.0, 2026), 1 STARTTLS response injection (MailKit, High CVSS 7.5, 2026); all patched in current 4.18.1 | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-gmc6-fwg3-75m5 | High CVSS:3.1 7.5 (AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | **MimeKit DoS via vulnerable System.Security.Cryptography.Pkcs transitive dependency.** MimeKit 3.0.0–4.7.0 ships a version of `System.Security.Cryptography.Pkcs` affected by upstream advisory GHSA-447r-wph3-92pm; triggering S/MIME decryption, incoming message signature verification, or third-party X.509 certificate import against attacker-controlled input causes unauthenticated network-reachable denial of service. | MimeKit ≥ 4.7.1 | [GHSA-gmc6-fwg3-75m5](https://github.com/advisories/GHSA-gmc6-fwg3-75m5) |
| GHSA-g7hc-96xr-gvvx / CVE-2026-30227 | Moderate CVSS 4.0 | **MimeKit CRLF injection in quoted local-part of MailboxAddress enabling SMTP command injection.** MimeKit ≤ 4.15.0 accepted CR and LF characters inside the quoted local-part of a MailboxAddress, violating RFC 5321 qtextSMTP grammar. When user-controlled input is passed as a MailboxAddress local-part, an attacker can inject arbitrary SMTP protocol commands (RCPT TO, DATA, RSET, etc.) into the session. Affects both MimeKit and MailKit because MailKit depends on MimeKit for address construction during SMTP delivery. | MimeKit ≥ 4.15.1 · MailKit ≥ 4.15.1 | [GHSA-g7hc-96xr-gvvx](https://github.com/advisories/GHSA-g7hc-96xr-gvvx) |
| GHSA-9j88-vvj5-vhgr / CVE-2026-41319 | High CVSS:3.1 7.5 (AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N) | **MailKit STARTTLS response injection (read buffer not flushed on TLS upgrade).** MailKit did not flush its internal socket-read buffer when upgrading from plaintext to TLS via STARTTLS; data injected by an on-path attacker before the TLS handshake remained buffered and was processed as if it arrived from the trusted post-TLS session, allowing command injection and potential session hijacking. Affects SMTP, IMAP, and POP3 connections using the `StartTls` connection option. Same vulnerability class as CVE-2021-23993 (Thunderbird), CVE-2021-33515 (Dovecot), and CVE-2011-0411 (Postfix). | MailKit ≥ 4.16.0 | [GHSA-9j88-vvj5-vhgr](https://github.com/advisories/GHSA-9j88-vvj5-vhgr) |

## Security Posture Notes

- MailKit is a mature, actively maintained cross-platform .NET email client library (SMTP, IMAP, POP3, S/MIME, PGP/MIME) maintained by Jeffrey Stedfast; 3,729+ commits, ~6,900 GitHub stars, MIT-licensed; latest stable 4.18.1 (September 2026).
- MimeKit is MailKit's MIME parsing foundation (separate NuGet package, same author); both packages version-stepped to 4.18.1 in tandem. All three confirmed advisories are fully patched in ≥ 4.16.0.
- Only the current 4.x major version line receives security patches per SECURITY.md; MimeKit 3.x users remain exposed to GHSA-gmc6-fwg3-75m5 with no planned backport.
- Advisory pattern to date: two injection classes (SMTP command injection via malformed address local-part; protocol-level injection via STARTTLS read-buffer flushing flaw) and one transitive DoS via a Microsoft cryptography dependency. None of the three advisories result from novel protocol parsing logic but from input-validation gaps and protocol-upgrade ordering.
- Because MailKit depends on MimeKit, MimeKit advisories (GHSA-gmc6-fwg3-75m5, GHSA-g7hc-96xr-gvvx) directly cascade to MailKit consumers; both packages must be updated in tandem when a MimeKit advisory is patched.
- Security disclosure: preferred channel is GitHub Private Security Advisory; maintainer targets 24-hour acknowledgement; fallback contact jestedfa@microsoft.com.

## Dependencies of Note

- `MimeKit` — MailKit's mandatory MIME dependency; MimeKit advisories cascade to all MailKit consumers.
- `System.Security.Cryptography.Pkcs` — Microsoft CMS/PKCS library used in S/MIME paths; the 2024 DoS (GHSA-gmc6-fwg3-75m5) originated in a vulnerable version bundled in MimeKit 3.0.0–4.7.0.
- `System.Formats.Asn1` — ASN.1 parsing library used in S/MIME certificate paths; future advisory surface to watch.

## Open Questions

- Are there pre-2024 advisories not yet indexed in the GitHub advisory database, especially around legacy S/MIME decryption or IMAP protocol edge cases?
- NuGet.org total download counts for MailKit and MimeKit are not available via the public NuGet registration API; a future pass should retrieve them via the NuGet.org stats page for ecosystem blast-radius context.
- Does MailKit validate the server certificate identity before performing STARTTLS, and does it enforce strict server-name validation to prevent opportunistic downgrade by an on-path attacker?

## Related Pages

- [[dotnet/RestSharp]]
- [[dotnet/System.Security.Cryptography.Xml]]
- [[dotnet/index]]

---
*Last updated: 2026-10-02 | Sources: 3 (github/advisory-database GHSA search via mcp__github__search_code + raw GHSA JSON via WebFetch; NuGet registration index for version metadata; jstedfast/MailKit SECURITY.md and GitHub repository metadata)*
