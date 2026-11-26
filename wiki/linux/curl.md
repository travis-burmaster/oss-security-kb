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

### 2025-2026 advisories (upstream curl security advisories)

All 78 curl advisories announced from 2025-02-05 through 2026-10-14, taken from the upstream advisory index (`curl/curl-www` `docs/vuln.pm`). Severity is the curl project's own rating. "Fixed in" is the first upstream release after the last affected version; distro packages backport separately.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-107929 | Low | Local interface connection reuse mixup (affects 8.9.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-107929.html) |
| CVE-2026-107928 | Low | Info leak uploading over WebSockets with GnuTLS (affects 7.86.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-107928.html) |
| CVE-2026-94266 | Low | Password leak in CURLINFO_EFFECTIVE_URL (affects 7.62.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-94266.html) |
| CVE-2026-94265 | Low | Authorization: Negotiate sent to foreign origin (affects 8.21.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-94265.html) |
| CVE-2026-92392 | High | HTTP/2 upload Use-After-Free (affects 8.12.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-92392.html) |
| CVE-2026-92391 | Low | Curl_mime_free stack overflow by recursion (affects 7.56.0 to 8.22.0; libcurl; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-92391.html) |
| CVE-2026-92390 | Low | -J no-clobber guarantee bypassed with 103 early hints (affects 7.20.0 to 8.22.0; curl tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-92390.html) |
| CVE-2026-92389 | Low | TFTP direction confusion (affects 7.15.0 to 8.22.0; libcurl; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-92389.html) |
| CVE-2026-92388 | Low | FTP wildcard write callback mixup (affects 7.21.0 to 8.22.0; libcurl; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-92388.html) |
| CVE-2026-92387 | Low | Never-ending loop via server response omission (affects 8.10.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-92387.html) |
| CVE-2026-92386 | Low | Server-set cookie aborts cookie jar load (affects 8.7.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-92386.html) |
| CVE-2026-86415 | Low | Auto client cert connection reuse mixup (affects 8.21.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-86415.html) |
| CVE-2026-86414 | Low | Leaking host credentials to HTTP proxy (affects 7.10.8 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-86414.html) |
| CVE-2026-86413 | Low | Negotiate credentials sent to redirected origin (affects 8.21.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-86413.html) |
| CVE-2026-87866 | Low | WolfSSL public-key pinning bypass (affects 7.43.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-87866.html) |
| CVE-2026-87865 | Low | Knownhost callback mismatches key as missing (affects 7.69.1 to 8.22.0; libcurl; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-87865.html) |
| CVE-2026-86412 | Low | Server-set cookie erases cookie jar (affects 8.18.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-86412.html) |
| CVE-2026-86411 | Low | FTP connection reuse inherits client-certificate (affects 8.21.0 to 8.21.0; libcurl and tool; announced 2026-10-14) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-86411.html) |
| CVE-2026-86410 | Low | Redirect to SFTP or SCP bypasses host verification (affects 7.81.0 to 8.22.0; curl tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-86410.html) |
| CVE-2026-86409 | Low | Stale SigV4 headers sent unintended (affects 7.75.0 to 8.21.0; libcurl; announced 2026-10-14) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-86409.html) |
| CVE-2026-87864 | Low | IMAP APPEND plus CRLF conversion command injection (affects 7.30.0 to 8.21.0; libcurl and tool; announced 2026-10-14) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-87864.html) |
| CVE-2026-87863 | Low | HSTS response erases persisted entries (affects 8.2.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-87863.html) |
| CVE-2026-87862 | Low | HSTS cache import drops longer-lived child (affects 8.11.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-87862.html) |
| CVE-2026-87861 | Low | Cross-origin reuse of a Negotiate connection (affects 8.21.0 to 8.22.0; libcurl and tool; announced 2026-10-14) | 8.23.0 | [curl advisory](https://curl.se/docs/CVE-2026-87861.html) |
| CVE-2026-82208 | Low | WolfSSL CA-cache hit overrides callback (affects 8.9.1 to 8.21.0; libcurl; announced 2026-09-02) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-82208.html) |
| CVE-2026-82209 | Low | Domain-scoped PSL domain cookie (affects 7.46.0 to 8.21.0; libcurl and tool; announced 2026-09-02) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-82209.html) |
| CVE-2026-80255 | Low | Secure cookie attribute bypass with tab (affects 8.13.0 to 8.21.0; libcurl and tool; announced 2026-09-02) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-80255.html) |
| CVE-2026-80231 | Low | Native CA store conn reuse (affects 7.71.0 to 8.21.0; libcurl and tool; announced 2026-09-02) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-80231.html) |
| CVE-2026-80230 | Low | OpenSSL pinning bypass (affects 7.45.0 to 8.21.0; libcurl and tool; announced 2026-09-02) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-80230.html) |
| CVE-2026-80229 | Low | OpenSSL provider use-after-free (affects 8.14.0 to 8.21.0; libcurl and tool; announced 2026-09-02) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-80229.html) |
| CVE-2026-19931 | Medium | Negotiate ambient user conn reuse (affects 7.64.1 to 8.21.0; libcurl and tool; announced 2026-09-02) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-19931.html) |
| CVE-2026-18924 | Low | HTTP/2 server push UAF (affects 7.44.0 to 8.21.0; libcurl; announced 2026-09-02) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-18924.html) |
| CVE-2026-13608 | Low | OpenLDAP SASL authentication bypass (affects 7.82.0 to 8.21.0; libcurl and tool; announced 2026-09-02) | 8.22.0 | [curl advisory](https://curl.se/docs/CVE-2026-13608.html) |
| CVE-2026-12064 | Low | Proto-default skips SSH verification (affects 7.81.0 to 8.20.0; curl tool; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-12064.html) |
| CVE-2026-11856 | Medium | Cross-origin Digest auth state leak (affects 7.10.6 to 8.20.0; libcurl; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-11856.html) |
| CVE-2026-11586 | Low | WS Auto-PONG memory exhaustion (affects 8.16.0 to 8.20.0; libcurl and tool; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-11586.html) |
| CVE-2026-11564 | Low | Native CA trust persist (affects 8.17.0 to 8.20.0; libcurl; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-11564.html) |
| CVE-2026-11352 | Low | QUIC zero-length UDP datagrams busy-loop (affects 8.18.0 to 8.20.0; libcurl and tool; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-11352.html) |
| CVE-2026-9546 | Low | Sending old referer (affects 8.18.0 to 8.20.0; libcurl; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-9546.html) |
| CVE-2026-10536 | Low | HTTP/2 stream-dependency tree UAF (affects 7.88.0 to 8.20.0; libcurl; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-10536.html) |
| CVE-2026-9547 | Low | SSH improper host validation (affects 7.69.0 to 8.20.0; libcurl; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-9547.html) |
| CVE-2026-9079 | Medium | Stale proxy password leak (affects 8.8.0 to 8.20.0; libcurl; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-9079.html) |
| CVE-2026-9545 | Low | Exposing HTTP/3 early data (affects 8.11.0 to 8.20.0; libcurl and tool; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-9545.html) |
| CVE-2026-9080 | Low | UAF after pause in socket callback (affects 8.13.0 to 8.20.0; libcurl; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-9080.html) |
| CVE-2026-8927 | Medium | Env-set cross-proxy Digest auth state leak (affects 7.12.0 to 8.20.0; libcurl; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-8927.html) |
| CVE-2026-8926 | Low | Password leak with netrc and user in URL (affects 8.11.1 to 8.20.0; libcurl and tool; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-8926.html) |
| CVE-2026-8925 | Medium | SASL double-free (affects 8.15.0 to 8.20.0; libcurl and tool; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-8925.html) |
| CVE-2026-8932 | Low | Incomplete mTLS config matching in conn reuse (affects 7.7 to 8.20.0; libcurl; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-8932.html) |
| CVE-2026-8924 | Low | Trailing dot domain super cookie (affects 7.46.0 to 8.20.0; libcurl and tool; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-8924.html) |
| CVE-2026-8458 | Low | Wrong reuse for different services (affects 7.43.0 to 8.20.0; libcurl and tool; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-8458.html) |
| CVE-2026-8286 | Low | Wrong STARTTLS connection reuse (affects 7.30.0 to 8.20.0; libcurl and tool; announced 2026-06-24) | 8.21.0 | [curl advisory](https://curl.se/docs/CVE-2026-8286.html) |
| CVE-2026-7168 | Medium | Cross-proxy Digest auth state leak (affects 7.12.0 to 8.19.0; libcurl; announced 2026-04-29) | 8.20.0 | [curl advisory](https://curl.se/docs/CVE-2026-7168.html) |
| CVE-2026-7009 | Medium | OCSP stapling bypass with Apple SecTrust (affects 8.17.0 to 8.19.0; libcurl and tool; announced 2026-04-29) | 8.20.0 | [curl advisory](https://curl.se/docs/CVE-2026-7009.html) |
| CVE-2026-6429 | Medium | Netrc credential leak with reused proxy connection (affects 7.14.0 to 8.19.0; libcurl; announced 2026-04-29) | 8.20.0 | [curl advisory](https://curl.se/docs/CVE-2026-6429.html) |
| CVE-2026-6276 | Low | Stale custom cookie host causes cookie leak (affects 7.71.0 to 8.19.0; libcurl; announced 2026-04-29) | 8.20.0 | [curl advisory](https://curl.se/docs/CVE-2026-6276.html) |
| CVE-2026-6253 | Medium | Proxy credentials leak over redirect-to proxy (affects 7.14.1 to 8.19.0; libcurl and tool; announced 2026-04-29) | 8.20.0 | [curl advisory](https://curl.se/docs/CVE-2026-6253.html) |
| CVE-2026-5773 | Low | Wrong reuse of SMB connection (affects 7.40.0 to 8.19.0; libcurl and tool; announced 2026-04-29) | 8.20.0 | [curl advisory](https://curl.se/docs/CVE-2026-5773.html) |
| CVE-2026-5545 | Medium | Wrong reuse of HTTP Negotiate connection (affects 7.10.6 to 8.19.0; libcurl and tool; announced 2026-04-29) | 8.20.0 | [curl advisory](https://curl.se/docs/CVE-2026-5545.html) |
| CVE-2026-4873 | Low | Connection reuse ignores TLS requirement (affects 7.20.0 to 8.19.0; libcurl and tool; announced 2026-04-29) | 8.20.0 | [curl advisory](https://curl.se/docs/CVE-2026-4873.html) |
| CVE-2026-3805 | Medium | Use after free in SMB connection reuse (affects 8.13.0 to 8.18.0; libcurl and tool; announced 2026-03-11) | 8.19.0 | [curl advisory](https://curl.se/docs/CVE-2026-3805.html) |
| CVE-2026-3784 | Low | Wrong proxy connection reuse with credentials (affects 7.7 to 8.18.0; libcurl and tool; announced 2026-03-11) | 8.19.0 | [curl advisory](https://curl.se/docs/CVE-2026-3784.html) |
| CVE-2026-3783 | Medium | Token leak with redirect and netrc (affects 7.33.0 to 8.18.0; libcurl and tool; announced 2026-03-11) | 8.19.0 | [curl advisory](https://curl.se/docs/CVE-2026-3783.html) |
| CVE-2026-1965 | Medium | Bad reuse of HTTP Negotiate connection (affects 7.10.6 to 8.18.0; libcurl and tool; announced 2026-03-11) | 8.19.0 | [curl advisory](https://curl.se/docs/CVE-2026-1965.html) |
| CVE-2025-15224 | Low | Libssh key passphrase bypass without agent set (affects 7.58.0 to 8.17.0; libcurl and tool; announced 2026-01-07) | 8.18.0 | [curl advisory](https://curl.se/docs/CVE-2025-15224.html) |
| CVE-2025-15079 | Low | Libssh global known_hosts override (affects 7.58.0 to 8.17.0; libcurl and tool; announced 2026-01-07) | 8.18.0 | [curl advisory](https://curl.se/docs/CVE-2025-15079.html) |
| CVE-2025-14819 | Low | OpenSSL partial chain store policy bypass (affects 7.87.0 to 8.17.0; libcurl; announced 2026-01-07) | 8.18.0 | [curl advisory](https://curl.se/docs/CVE-2025-14819.html) |
| CVE-2025-14524 | Low | Bearer token leak on cross-protocol redirect (affects 7.33.0 to 8.17.0; libcurl and tool; announced 2026-01-07) | 8.18.0 | [curl advisory](https://curl.se/docs/CVE-2025-14524.html) |
| CVE-2025-14017 | Medium | Broken TLS options for threaded LDAPS (affects 7.17.0 to 8.17.0; libcurl; announced 2026-01-07) | 8.18.0 | [curl advisory](https://curl.se/docs/CVE-2025-14017.html) |
| CVE-2025-13034 | Medium | No QUIC certificate pinning with GnuTLS (affects 8.8.0 to 8.17.0; libcurl and tool; announced 2026-01-07) | 8.18.0 | [curl advisory](https://curl.se/docs/CVE-2025-13034.html) |
| CVE-2025-10966 | Low | Missing SFTP host verification with wolfSSH (affects 7.69.0 to 8.16.0; libcurl and tool; announced 2025-11-05) | 8.17.0 | [curl advisory](https://curl.se/docs/CVE-2025-10966.html) |
| CVE-2025-10148 | Low | Predictable WebSocket mask (affects 8.11.0 to 8.15.0; libcurl and tool; announced 2025-09-10) | 8.16.0 | [curl advisory](https://curl.se/docs/CVE-2025-10148.html) |
| CVE-2025-9086 | Low | Out of bounds read for cookie path (affects 8.13.0 to 8.15.0; libcurl; announced 2025-09-10) | 8.16.0 | [curl advisory](https://curl.se/docs/CVE-2025-9086.html) |
| CVE-2025-5399 | Low | WebSocket endless loop (affects 8.13.0 to 8.14.0; libcurl; announced 2025-06-04) | 8.14.1 | [curl advisory](https://curl.se/docs/CVE-2025-5399.html) |
| CVE-2025-5025 | Medium | No QUIC certificate pinning with wolfSSL (affects 8.5.0 to 8.13.0; libcurl and tool; announced 2025-05-28) | 8.14.0 | [curl advisory](https://curl.se/docs/CVE-2025-5025.html) |
| CVE-2025-4947 | Medium | QUIC certificate check skip with wolfSSL (affects 8.8.0 to 8.13.0; libcurl and tool; announced 2025-05-28) | 8.14.0 | [curl advisory](https://curl.se/docs/CVE-2025-4947.html) |
| CVE-2025-0725 | Low | Gzip integer overflow (affects 7.10.5 to 8.11.1; libcurl and tool; announced 2025-02-05) | 8.12.0 | [curl advisory](https://curl.se/docs/CVE-2025-0725.html) |
| CVE-2025-0665 | Low | Eventfd double close (affects 8.11.1 to 8.11.1; libcurl and tool; announced 2025-02-05) | 8.12.0 | [curl advisory](https://curl.se/docs/CVE-2025-0665.html) |
| CVE-2025-0167 | Low | Netrc and default credential leak (affects 7.76.0 to 8.11.1; libcurl and tool; announced 2025-02-05) | 8.12.0 | [curl advisory](https://curl.se/docs/CVE-2025-0167.html) |

### Earlier advisories

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-38545 | High | SOCKS5 heap buffer overflow — during the SOCKS5 proxy handshake, a too-long hostname can overflow a heap buffer via the slow-path SOCKS5 hostname resolution fallback | 8.4.0 | [curl advisory](https://curl.se/docs/CVE-2023-38545.html) |
| CVE-2023-38546 | Low | Cookie injection — an attacker can inject arbitrary cookies when curl is built with cookie support and a certain condition is met during the request | 8.4.0 | [curl advisory](https://curl.se/docs/CVE-2023-38546.html) |
| CVE-2024-2004 | Low | Protocol selection logic error — `--proto -all,-http` disables the full protocol set yet the default allowed set remains active, enabling unexpected plaintext requests | 8.7.1 | [curl advisory](https://curl.se/docs/CVE-2024-2004.html) |
| CVE-2024-7264 | Medium | `CURLINFO_CERTINFO` use-after-free — ASN.1 date parsing can access freed memory when retrieving certificate information via libcurl | 8.9.0 | [curl advisory](https://curl.se/docs/CVE-2024-7264.html) |
| CVE-2024-8096 | Medium | OCSP stapling bypass — curl does not verify the OCSP stapling response when using the GnuTLS backend, allowing revoked certificates to pass TLS verification | 8.10.0 | [curl advisory](https://curl.se/docs/CVE-2024-8096.html) |

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

**2025-2026 advisory volume.** curl announced 78 CVEs in this window: 1 High, 17 Medium, 60 Low by the project's rating. The 2026-10-14 announcement covered 24 CVEs (21 fixed in 8.23.0; 3 already fixed in 8.22.0), the largest single batch in this mapping. The previous page listed CVE-2025-0167 as a Medium WHOIS credential issue; the upstream record is a Low netrc and default credential leak, corrected here. Most are connection-reuse, credential-forwarding, cookie/HSTS and TLS-backend verification mistakes rather than memory corruption.

**CVE-2026-92392 (High, HTTP/2 upload use-after-free).** Affects 8.12.0 to 8.22.0. The upstream advisory says the UAF has been shown convertible to remote code execution by a malicious server under a long list of preconditions (known build layout, allocator, two parallel transfers, about 23 bytes of command). Fixed in 8.23.0, with backport fixes on the 8.20.x (8.20.2), 8.16.x (8.16.2) and 8.14.x (8.14.3) branches per the advisory. No curl CVE is in CISA KEV (catalog 2026.11.25).

**Medium-rated 2026 themes:** HTTP Negotiate / Digest / proxy credential leaks across connection reuse and redirects (CVE-2026-1965, CVE-2026-3783, CVE-2026-5545, CVE-2026-6253, CVE-2026-6429, CVE-2026-7168, CVE-2026-8927, CVE-2026-9079, CVE-2026-11856, CVE-2026-19931), a SASL double free (CVE-2026-8925), an SMB connection-reuse use-after-free (CVE-2026-3805), and an OCSP stapling bypass with Apple SecTrust (CVE-2026-7009).

curl maintains a dedicated security team (curl-security@haxx.se), a published hall of fame, and a well-documented coordinated disclosure process with a typical 7-day embargo window for critical issues. The project uses HackerOne for managed disclosure.

## Dependencies of Note

- `openssl` / `gnutls` / `nss` / `wolfssl` — TLS backends; distro build flags determine which is used. OpenSSL-based builds are affected by OpenSSL CVEs; GnuTLS-based builds (typical on Debian/Ubuntu) additionally expose OCSP stapling gaps as shown in CVE-2024-8096. See [[linux/openssl]].
- `libssh2` — used by curl's SCP/SFTP support; libssh2 CVEs can propagate through curl packages.
- `c-ares` — optional async DNS resolver; used when curl is built with `--enable-ares`.

## Open Questions

- What is the distro-level backport status of CVE-2025-0167 across Debian stable, Ubuntu LTS, and RHEL 8/9?
- 2025-2026 is now mapped from the upstream index through 2026-10-14. Re-check `docs/vuln.pm` after the next curl release.
- Which distros have shipped the CVE-2026-92392 fix (or the 8.20.2 / 8.16.2 / 8.14.3 backports)?
- [[homebrew/curl]] still stops at CVE-2025-0167; bring it up to date on a later pass.
- Should this page be split into `linux/libcurl` vs `linux/curl` given that many consumers link libcurl directly rather than shelling out to the CLI?

## Related Pages

- [[linux/openssl]]
- [[linux/index]]

---
*Last updated: 2026-11-26 | Sources: 5 (curl/curl-www `docs/vuln.pm` and per-CVE advisory markdown via raw.githubusercontent.com, curl/curl release tags, CISA KEV catalog 2026.11.25, curl.se/docs/vuln.html advisory trail, github/advisory-database code search, CVE metadata from kubernetes-sigs/cve-feed-osv and anchore/cve-data-enrichment)*
