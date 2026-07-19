# openssl (linux)

**Registry:** distro
**Weekly Downloads:** unknown (install base tracked by distro, not registry download counts)
**Repository:** https://github.com/openssl/openssl
**Security Contact:** https://www.openssl.org/community/omc.html
**Disclosure Policy:** https://www.openssl.org/policies/secpolicy.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No distro-normalized proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

All entries reference the **upstream OpenSSL C library** release lines. Distro packages (Debian `libssl`, RHEL `openssl`, Alpine `libssl3`, etc.) backport fixes and may carry the upstream fix at a different package version — consult the relevant distro security tracker for the patched package release.

### Historical High-Severity CVEs

| CVE / Issue | Severity | Description | Fixed in (upstream) | Source |
|-------------|----------|-------------|---------------------|--------|
| CVE-2014-0160 | Critical | **Heartbleed** — Out-of-bounds read in the TLS/DTLS heartbeat extension (RFC 6520): a malformed heartbeat request with a length field larger than the payload causes OpenSSL to return up to 64 KB of server-process memory per request, exposing private keys, session tokens, and passwords without authentication and without leaving a log trace. Affected 1.0.1a–1.0.1f and 1.0.2-beta1. | 1.0.1g (2014-04-07) | https://www.openssl.org/news/secadv/20140407.txt |
| CVE-2022-0778 | High (CVSS 7.5) | **BN_mod_sqrt() infinite loop** — The BN_mod_sqrt() function enters an infinite loop for non-prime moduli; it is internally used when parsing certificates with compressed EC public keys or explicit EC parameters. A malformed certificate can trigger the loop before signature verification, making any TLS client or server that parses untrusted certificates vulnerable to remote DoS. | 1.0.2zd / 1.1.1n / 3.0.2 (2022-03-15) | https://github.com/advisories/GHSA-x3mh-jvjw-3xwx |
| CVE-2022-3602 | High (CVSS 9.8 — initially Critical) | **X.509 email address 4-byte stack overflow** — A 4-byte stack buffer overrun occurs during X.509 name constraint checking after certificate-chain signature validation. An attacker-controlled malicious CA or a CA-signed certificate can trigger the overrun. RCE is theoretically possible but mitigated by stack-layout variability; DoS (crash) is the practical impact in most deployments. | 3.0.7 (2022-11-01) | https://github.com/advisories/GHSA-8rwr-x37p-mx23 |
| CVE-2022-3786 | High (CVSS 7.5) | **X.509 email address arbitrary-length stack overflow** — A closely related name constraint flaw to CVE-2022-3602; crafting a malicious email address with multiple `.` characters overflows the stack with arbitrary length, reliably crashing the process (DoS). Fixed in the same release as CVE-2022-3602. | 3.0.7 (2022-11-01) | https://github.com/advisories/GHSA-h8jm-2x53-xhp5 |
| CVE-2023-0215 | High (CVSS 7.5) | **BIO_new_NDEF use-after-free** — When `BIO_new_NDEF()` fails (e.g., invalid CMS recipient public key) the BIO chain is not properly cleaned up and the caller's `BIO` retains stale internal pointers. A subsequent `BIO_pop()` call triggers use-after-free, typically crashing. Affected SMIME, CMS, and PKCS7 streaming APIs. | 1.0.2zj / 1.1.1t / 3.0.8 (2023-02-07) | https://github.com/advisories/GHSA-r7jw-wp68-3xch |
| CVE-2023-0286 | High | **X.400 address type confusion in X.509 GeneralName** — Type confusion between `X400Address` (ASN.1 `ASN1_STRING`) and `ASN1_TYPE` allows an attacker to pass arbitrary pointers to a `memcmp()` call, enabling memory reads or DoS. Most likely to affect applications using CRLs obtained from untrusted network sources. | 1.0.2zj / 1.1.1t / 3.0.8 (2023-02-07) | https://www.openssl.org/news/secadv/20230207.txt |
| CVE-2024-0727 | Moderate (CVSS 7.1 / AV:L) | **PKCS12 null pointer dereference** — Processing a maliciously formatted PKCS12 file (which the spec permits to contain NULL fields) causes a null pointer dereference and crash. Affected APIs: `PKCS12_parse()`, `PKCS12_unpack_p7data()`, `PKCS12_unpack_p7encdata()`, `PKCS12_unpack_authsafes()`, `PKCS12_newpass()`. FIPS modules in 3.0/3.1/3.2 unaffected. | 1.1.1y / 3.0.13 / 3.1.5 / 3.2.1 (2024-01-09) | https://github.com/advisories/GHSA-9v9h-cgj8-h64p |
| CVE-2024-5535 | Low | **SSL_select_next_proto buffer overread** — Calling `SSL_select_next_proto` with an empty (zero-length) supported-client-protocols buffer causes it to return a pointer to memory immediately past the list, potentially exposing up to 255 bytes of private data. Typically only reachable when an application accidentally passes an empty list, which ALPN prevents by construction (only NPN callers at risk). FIPS modules unaffected. | 3.0.14 / 3.1.6 / 3.2.2 / 3.3.1 (2024-06-27) | https://github.com/advisories/GHSA-4fc7-mvrr-wv2c |

### 2026 Advisories (already on record)

| CVE / Issue | Severity | Description | Fixed in (upstream) | Source |
|-------------|----------|-------------|---------------------|--------|
| CVE-2026-31790 | Moderate | Incorrect failure handling in RSA KEM RSASVE encapsulation — `EVP_PKEY_encapsulate()` can return success with stale ciphertext buffer contents when given an invalid RSA public key without prior key validation via `EVP_PKEY_public_check()`. | 3.0.20 / 3.3.7 / 3.4.5 / 3.5.6 / 3.6.2 | https://openssl-library.org/news/secadv/20260407.txt |
| CVE-2026-28386 | Low | OOB read in AES-CFB-128 on x86_64 with AVX-512 + VAES support during partial cipher-block processing; DoS only if over-read hits an unmapped page; no info disclosure because over-read bytes are not written to output; TLS/DTLS unaffected (CFB mode not used). | 3.6.2 | https://openssl-library.org/news/secadv/20260407.txt |

## Security Posture Notes

- OpenSSL is the most widely deployed TLS/cryptographic library on Linux and is a direct security boundary for essentially every TLS-terminating service on the internet.
- **Distro packaging complicates version tracking**: upstream fix versions above are for the OpenSSL release; Debian, Ubuntu, RHEL/CentOS, Alpine, and others backport fixes to their own package versions (e.g., Debian Bullseye ships `openssl 1.1.1n-0+deb11u6` even though upstream 1.1.1 EOL is 2023-09-11). Always check the distro security tracker for the actual patched package release.
- OpenSSL 1.0.2 reached EOL 2019-12-31 (premium support only), 1.1.1 reached EOL 2023-09-11, 3.0.x LTS until 2026-09-07. Actively maintained branches are 3.1, 3.2, 3.3, 3.4, 3.5 and 3.6 (latest stable as of 2026).
- The Heartbleed (CVE-2014-0160) incident remains the most impactful OpenSSL vulnerability and shaped the modern security landscape; its architecture (heartbeat without bounds check) motivated deep structural audits.
- The November 2022 pair (CVE-2022-3602 / CVE-2022-3786) was initially designated Critical, causing widespread concern given the "next Log4Shell" narrative; the actual RCE risk was lower than feared due to stack-layout mitigations, and the advisory was later revised to High.

## Dependencies of Note

- Nearly every TLS-dependent Linux package (`curl`, `openssh`, `nginx`, `postgresql`, `python` cryptography wheels) either links or bundles OpenSSL. Pages for [[linux/curl]], [[linux/openssh]], and [[linux/nginx]] should be read alongside this page for a fuller TLS-stack picture.
- The Rust `openssl` (sfackler/rust-openssl) and `openssl-src` crates are language bindings and a bundled source copy respectively; their advisory history is tracked separately at [[rust/openssl]].
- [[homebrew/openssl@3]] tracks the macOS Homebrew formula for the 3.x branch.

## Open Questions

- Which distros should be tracked as first-class coverage targets for distro-specific backport notes (Debian, RHEL, Alpine)?
- Should future Linux pages add "distro-patched-in" columns to support easier filtering for site operators?
- Are there any significant OpenSSL CVEs between 2024-06 and 2026-04 not yet captured here (2024-09 / 2025 advisory windows)?

## Related Pages

- [[homebrew/openssl@3]]
- [[linux/curl]]
- [[linux/openssh]]
- [[linux/nginx]]
- [[rust/openssl]]
- [[linux/index]]

---
*Last updated: 2026-07-19 | Sources: 8 (GHSA-x3mh-jvjw-3xwx, GHSA-8rwr-x37p-mx23, GHSA-h8jm-2x53-xhp5, GHSA-r7jw-wp68-3xch, GHSA-9v9h-cgj8-h64p, GHSA-4fc7-mvrr-wv2c via github/advisory-database; openssl-library.org advisory references for CVE-2014-0160 / CVE-2023-0286 / CVE-2026-31790 / CVE-2026-28386)*
