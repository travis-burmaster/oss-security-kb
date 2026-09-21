# pyOpenSSL (Python / PyPI)

**Registry:** PyPI
**Weekly Downloads:** unknown (pypistats.org blocked; one of the most-downloaded TLS/SSL Python packages)
**Repository:** https://github.com/pyca/pyopenssl
**Security Contact:** security@python.org (PyCA org) / https://github.com/pyca/pyopenssl/security
**Disclosure Policy:** https://github.com/pyca/pyopenssl/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No formal third-party audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-27459 / GHSA-5pwr-322w-8jr4 | High (CVSS 7.5) | Buffer overflow in DTLS cookie generation — if a user-provided callback registered via `set_cookie_generate_callback` returns a value greater than 256 bytes, pyOpenSSL overflows an OpenSSL-provided buffer. | 26.0.0 | [GHSA-5pwr-322w-8jr4](https://github.com/advisories/GHSA-5pwr-322w-8jr4) |
| CVE-2026-27448 / GHSA-vp96-hxj8-p424 | Low (CVSS 4.0) | TLS SNI callback exception bypass — unhandled exceptions in user-provided callbacks registered via `set_tlsext_servername_callback` caused the TLS connection to be accepted rather than rejected, allowing security checks in the callback to be silently bypassed on exception. | 26.0.0 | [GHSA-vp96-hxj8-p424](https://github.com/advisories/GHSA-vp96-hxj8-p424) |
| CVE-2018-1000807 / GHSA-p28m-34f6-967q | High (CVSS 9.0 AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H) | X509 object use-after-free — improper memory management of X509 objects could allow remote attackers to trigger application crashes or potentially execute arbitrary code depending on calling-application memory management. | 17.5.0 | [GHSA-p28m-34f6-967q](https://github.com/advisories/GHSA-p28m-34f6-967q) |
| CVE-2018-1000808 / GHSA-2rcm-phc9-3945 | High (CVSS 7.5) | PKCS#12 denial of service — a remote attacker could cause pyOpenSSL to consume excessive resources when processing PKCS#12 certificates, resulting in a denial of service. Can be triggered via TLS connections that cause applications to reload certificates from a PKCS#12 store. | 17.5.0 | [GHSA-2rcm-phc9-3945](https://github.com/advisories/GHSA-2rcm-phc9-3945) |
| CVE-2013-4314 / GHSA-6748-36qp-fx6r | High (CVSS 7.5) | X509Extension null byte in Subject Alternative Name — the `X509Extension` component did not properly handle a `\0` character in a domain name within the Subject Alternative Name (SAN) field of X.509 certificates, allowing attackers to craft malicious certificates that impersonate legitimate SSL servers even when issued by a trusted CA. | 0.13.1 | [GHSA-6748-36qp-fx6r](https://github.com/advisories/GHSA-6748-36qp-fx6r) |

## Security Posture Notes

pyOpenSSL is maintained by the Python Cryptographic Authority (PyCA) — the same organization that maintains the `cryptography` package. The PyCA team itself recommends using the `cryptography` package directly for most use cases; pyOpenSSL is positioned primarily as a wrapper for applications that need direct OpenSSL primitives or legacy compatibility.

The two March 2026 advisories (CVE-2026-27459 and CVE-2026-27448) were both fixed in pyOpenSSL 26.0.0 and affect callbacks that applications supply at runtime; applications not using `set_cookie_generate_callback` or `set_tlsext_servername_callback` are unaffected by those specific issues.

pyOpenSSL wraps OpenSSL via the `cryptography` crate's `openssl` bindings and is therefore also indirectly affected by upstream OpenSSL CVEs when the bundled or linked OpenSSL version is vulnerable. The `cryptography` package page tracks those wheel-bundled OpenSSL advisories.

Current stable: 26.4.0 (released 2026-08-01). The 26.x release line moved to `cryptography`'s Rust-backed OpenSSL bindings.

## Dependencies of Note

- `cryptography` — the underlying cryptographic implementation; see [[python/cryptography]] for its advisory history.
- OpenSSL (system or wheel-bundled) — pyOpenSSL is a thin wrapper; upstream OpenSSL CVEs can affect exposed surfaces depending on which OpenSSL APIs pyOpenSSL exposes.

## Open Questions

- Obtain current PyPI weekly download count (pypistats.org blocked in this environment).
- Verify whether pyOpenSSL 26.x bundled-OpenSSL version on the wheel inherits any 2026 OpenSSL advisories.
- Cross-check the pyca/pyopenssl GitHub security advisory list for any advisories not yet in the GitHub Advisory Database.

## Related Pages

- [[python/cryptography]]
- [[python/index]]

---
*Last updated: 2026-09-21 | Sources: 5 GHSA advisories (github/advisory-database)*
