# curl (Linux)

**Registry:** distro
**Weekly Downloads:** unknown (bundled with virtually all Linux distributions; upstream reports ~20 billion installations worldwide)
**Repository:** https://github.com/curl/curl
**Security Contact:** curl-security@haxx.se
**Disclosure Policy:** https://curl.se/docs/security.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record at the Linux-package level. Upstream curl maintains its own security release history at https://curl.se/docs/vuln.html.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-38545 | High | SOCKS5 heap buffer overflow — during the SOCKS5 proxy handshake, a too-long hostname can overflow a heap buffer via the slow-path SOCKS5 hostname resolution fallback | 8.4.0 | [curl advisory](https://curl.se/docs/CVE-2023-38545.html) |
| CVE-2023-38546 | Low | Cookie injection — an attacker can inject arbitrary cookies when curl is built with cookie support and a certain condition is met during the request | 8.4.0 | [curl advisory](https://curl.se/docs/CVE-2023-38546.html) |
| CVE-2024-2004 | Low | Protocol selection logic error — `--proto -all,-http` disables the full protocol set yet the default allowed set remains active, enabling unexpected plaintext requests | 8.7.1 | [curl advisory](https://curl.se/docs/CVE-2024-2004.html) |
| CVE-2024-7264 | Medium | `CURLINFO_CERTINFO` use-after-free — ASN.1 date parsing can access freed memory when retrieving certificate information via libcurl | 8.9.0 | [curl advisory](https://curl.se/docs/CVE-2024-7264.html) |
| CVE-2024-8096 | Medium | OCSP stapling bypass — curl does not verify the OCSP stapling response when using the GnuTLS backend, allowing revoked certificates to pass TLS verification | 8.10.0 | [curl advisory](https://curl.se/docs/CVE-2024-8096.html) |
| CVE-2025-0167 | Medium | Credential exposure in WHOIS queries — credentials can be sent in cleartext via a WHOIS request when `--proxy-anyauth` or similar is used | 8.12.0 | [curl advisory](https://curl.se/docs/CVE-2025-0167.html) |

*Upstream full history: https://curl.se/docs/vuln.html — curl publishes security advisories for every released fix.*

## Security Posture Notes

`curl` (and `libcurl`) is the foundational URL transfer library present on virtually every Linux distribution. It ships as both a CLI tool and a C library consumed by thousands of downstream packages. Distro packages typically lag upstream releases by days to weeks; the relevant fix version for most production systems is determined by the distro's backport policy rather than the upstream version.

**Distro backport tracking:** When evaluating whether a given CVE is fixed, check:
- Debian Security Tracker: https://security-tracker.debian.org/tracker/source-package/curl
- Ubuntu CVE Tracker: https://ubuntu.com/security/CVE/\<CVE-ID\>
- Red Hat Errata: https://access.redhat.com/security/updates/backport

**CVE-2023-38545 (High)** is the most significant recent vulnerability: a heap buffer overflow in the SOCKS5 proxy hostname-handling slow path, advertised by the curl team as "probably the worst curl security flaw in a long time." Fixed in curl 8.4.0 (released 2023-10-11). All major distros backported within days. Affected curl ≤ 8.3.0 only when `--socks5-hostname` or SOCKS5h proxy is used with a hostname exceeding 255 bytes.

**CVE-2024-7264** involves a use-after-free in ASN.1 date parsing within the `CURLINFO_CERTINFO` code path — exploitable only when the caller explicitly retrieves certificate info. Fixed in 8.9.0.

**OCSP stapling note (CVE-2024-8096):** Curl's GnuTLS backend did not enforce OCSP stapling even when configured to do so. This is a TLS verification bypass affecting deployments using GnuTLS (common on Debian/Ubuntu) rather than OpenSSL.

curl maintains a dedicated security team (curl-security@haxx.se), a published hall of fame, and a well-documented coordinated disclosure process with a typical 7-day embargo window for critical issues. The project uses HackerOne for managed disclosure.

## Dependencies of Note

- `openssl` / `gnutls` / `nss` / `wolfssl` — TLS backends; distro build flags determine which is used. OpenSSL-based builds are affected by OpenSSL CVEs; GnuTLS-based builds (typical on Debian/Ubuntu) additionally expose OCSP stapling gaps as shown in CVE-2024-8096. See [[linux/openssl]].
- `libssh2` — used by curl's SCP/SFTP support; libssh2 CVEs can propagate through curl packages.
- `c-ares` — optional async DNS resolver; used when curl is built with `--enable-ares`.

## Open Questions

- What is the distro-level backport status of CVE-2025-0167 across Debian stable, Ubuntu LTS, and RHEL 8/9?
- Are there any curl CVEs from the 2025–2026 window not yet confirmed covered in this mapping? The upstream advisory page lists new issues quarterly.
- Should this page be split into `linux/libcurl` vs `linux/curl` given that many consumers link libcurl directly rather than shelling out to the CLI?

## Related Pages

- [[linux/openssl]]
- [[linux/index]]

---
*Last updated: 2026-06-15 | Sources: 3 (curl.se/docs/vuln.html advisory trail, github/advisory-database code search, CVE metadata from kubernetes-sigs/cve-feed-osv and anchore/cve-data-enrichment)*
