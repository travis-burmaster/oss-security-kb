# curl (Homebrew)

**Registry:** Homebrew
**Weekly Downloads:** unknown (Homebrew analytics blocked; curl is among the most-installed Homebrew formulas on macOS, widely used in scripts, CI pipelines, and developer tooling as of 2026-07-10)
**Repository:** https://github.com/curl/curl
**Security Contact:** curl-security@haxx.se
**Disclosure Policy:** https://curl.se/docs/security.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record at the Homebrew-formula level. Upstream curl maintains its own security release history at https://curl.se/docs/vuln.html.*

## Known Vulnerabilities

The Homebrew `curl` formula tracks upstream curl releases without custom Homebrew patches. All upstream curl CVEs apply directly to the Homebrew formula; the patching lag equals the time between the upstream release and Homebrew bottle publication (typically hours to days for security releases). The vulnerabilities below reflect the advisory set documented in [[linux/curl]], cross-referenced here for Homebrew consumers.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-38545 | High (CVSS ~7.5) | SOCKS5 heap buffer overflow — during SOCKS5 proxy handshake, a too-long hostname can overflow a heap buffer via the slow-path hostname-resolution fallback; described by the curl team as "probably the worst curl security flaw in a long time" | curl ≥ 8.4.0 (Homebrew bottle updated 2023-10-11) | [curl advisory](https://curl.se/docs/CVE-2023-38545.html) |
| CVE-2023-38546 | Low | Cookie injection — an attacker can inject arbitrary cookies when curl is built with cookie support and a specific request condition is met | curl ≥ 8.4.0 | [curl advisory](https://curl.se/docs/CVE-2023-38546.html) |
| CVE-2024-2004 | Low | Protocol selection logic error — `--proto -all,-http` disables the full protocol set yet the default allowed set remains active, enabling unexpected plaintext requests | curl ≥ 8.7.1 | [curl advisory](https://curl.se/docs/CVE-2024-2004.html) |
| CVE-2024-7264 | Medium | `CURLINFO_CERTINFO` use-after-free — ASN.1 date parsing accesses freed memory when retrieving certificate information via libcurl | curl ≥ 8.9.0 | [curl advisory](https://curl.se/docs/CVE-2024-7264.html) |
| CVE-2024-8096 | Medium | OCSP stapling bypass — curl does not verify the OCSP stapling response when using the GnuTLS backend, allowing revoked certificates to pass TLS verification | curl ≥ 8.10.0 | [curl advisory](https://curl.se/docs/CVE-2024-8096.html) |
| CVE-2025-0167 | Medium | Credential exposure in WHOIS queries — credentials can be sent in cleartext via a WHOIS request when `--proxy-anyauth` or similar is used | curl ≥ 8.12.0 | [curl advisory](https://curl.se/docs/CVE-2025-0167.html) |

*Upstream full history: https://curl.se/docs/vuln.html — curl publishes security advisories for every released fix.*

## Security Posture Notes

macOS ships a system `curl` binary from Apple (bundled via the Xcode Command Line Tools or the base OS). The Apple-bundled curl has a separate backport/patch cadence and uses the macOS **Secure Transport** TLS backend rather than OpenSSL. By contrast, the Homebrew `curl` formula typically links against OpenSSL (or Homebrew's openssl@3) and provides a more up-to-date version with the upstream TLS stack.

**Key macOS-specific considerations:**

- **TLS backend difference**: The Homebrew curl formula uses OpenSSL-based TLS. CVE-2024-8096 (OCSP stapling bypass) affects the GnuTLS backend, which is not the default for Homebrew builds on macOS. However, operators using Homebrew curl with a custom `--with-gnutls` build flag could be affected.

- **Conflicting binary**: Homebrew curl is installed to a versioned Homebrew path (e.g. `/opt/homebrew/opt/curl/bin/curl`). Scripts using `/usr/bin/curl` will still use Apple's system curl; PATH ordering determines which is invoked for interactive shell sessions. CI images and Docker environments on macOS should pin which binary is in use.

- **CVE-2023-38545 (High)**: The SOCKS5 heap overflow affects all curl ≤ 8.3.0. Most Homebrew users on a post-October-2023 bottle would have received the fix. `brew outdated | grep curl` can confirm.

- **Supply chain note**: Homebrew formula bottles are served from GitHub Releases. Homebrew's SHA-256 checksum verification and code-signing of bottles (on macOS ARM via Apple Silicon signing) provide integrity protection for the binary distribution.

The upstream curl project maintains a dedicated security team (curl-security@haxx.se) with HackerOne for managed disclosure and a typical 7-day embargo window for critical issues.

## Dependencies of Note

- [[homebrew/openssl@3]] — Homebrew curl links against openssl@3; OpenSSL CVEs in the 3.x line can affect the libcurl TLS surface in Homebrew builds.
- Scripts and Dockerfiles on macOS using `brew install curl` should verify that `which curl` resolves to the Homebrew binary when security updates are required.
- `libssh2` — used by curl's SCP/SFTP support in Homebrew builds; libssh2 CVEs can propagate through the Homebrew curl bottle.

## Open Questions

- What is the current Homebrew bottle version of `curl` and what is its first-available date vs. the upstream 8.12.x security release for CVE-2025-0167?
- Does any additional CVE post-CVE-2025-0167 apply to the current Homebrew curl formula? Check `brew info curl` and upstream advisory feed at https://curl.se/docs/vuln.html.
- Are there Homebrew-specific build-time flags (e.g. `--with-libssh2`, `--with-brotli`) that introduce additional attack surface beyond the default formula build?

## Related Pages

- [[linux/curl]]
- [[homebrew/wget]]
- [[homebrew/openssl@3]]
- [[homebrew/index]]

---
*Last updated: 2026-07-10 | Sources: 3 (curl.se/docs/vuln.html advisory trail, linux/curl advisory mapping, Homebrew formula context)*
