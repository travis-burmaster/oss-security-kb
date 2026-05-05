# cryptography (python)

**Registry:** PyPI
**Weekly Downloads:** ~261,373,622 (last week, as of 2026-05-05; PyPIStats)
**Repository:** https://github.com/pyca/cryptography
**Security Contact:** GitHub Security Advisories / project issue tracker (public policy file not located in this pass)
**Disclosure Policy:** none located in this pass
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-05 | OpenClaw recurring review | package advisory history | public-source advisory mapping using OSV package query, GHSA records, CVE aliases, upstream changelog, PyPI metadata, and PyPIStats | 20 unique public package advisories curated across cryptographic primitive misuse, X.509 / certificate parsing, Python buffer handling, and bundled OpenSSL wheel exposure | https://osv.dev/list?ecosystem=PyPI&q=cryptography |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-39892 / GHSA-p423-j2cm-9vmq | Moderate | Non-contiguous Python buffers could be passed to APIs that accept buffers, creating a buffer-overflow condition. | 46.0.7 | https://github.com/pyca/cryptography/security/advisories/GHSA-p423-j2cm-9vmq |
| CVE-2026-34073 / GHSA-m959-cc7f-wv43 | Moderate | X.509 path verification could fail to apply DNS name constraints to peer names when the leaf certificate contained a wildcard DNS SAN; upstream notes ordinary Web PKI topologies are not affected. | 46.0.6 | https://github.com/pyca/cryptography/security/advisories/GHSA-m959-cc7f-wv43 |
| CVE-2026-26007 / GHSA-r6ph-v2qm-q3c2 | High | Missing subgroup validation for uncommon `SECT*` binary elliptic curves could allow a malicious public key to reveal portions of a private key; upstream deprecated those curves in the same fix train. | 46.0.5 | https://github.com/pyca/cryptography/security/advisories/GHSA-r6ph-v2qm-q3c2 |
| CVE-2024-12797 / GHSA-79v4-65xg-pq4g | Unknown | Wheels included a vulnerable OpenSSL version, so users relying on bundled wheels needed a cryptography wheel refresh. | 44.0.1 | https://github.com/pyca/cryptography/security/advisories/GHSA-79v4-65xg-pq4g |
| GHSA-h4gh-qq45-vh27 | Unknown | Wheels included a vulnerable OpenSSL version, requiring an updated cryptography wheel build for users of bundled OpenSSL artifacts. | 43.0.1 | https://github.com/pyca/cryptography/security/advisories/GHSA-h4gh-qq45-vh27 |
| CVE-2024-26130 / GHSA-6vqw-3v5j-54x4 | High | `pkcs12.serialize_key_and_certificates()` could NULL-dereference when given a certificate/private-key mismatch plus an `hmac_hash` override, crashing the Python process instead of raising `ValueError`. | 42.0.4 | https://github.com/pyca/cryptography/security/advisories/GHSA-6vqw-3v5j-54x4 |
| CVE-2024-0727 / GHSA-9v9h-cgj8-h64p | Moderate | PKCS#12 parsing inherited an OpenSSL NULL-pointer dereference / denial-of-service exposure through bundled wheels. | 42.0.2 | https://nvd.nist.gov/vuln/detail/CVE-2024-0727 |
| CVE-2023-50782 / GHSA-3ww4-gg4f-jr7f | High | RSA PKCS#1 v1.5 decryption remained vulnerable to a timing-oracle / Bleichenbacher-style attack under affected conditions. | 42.0.0 | https://nvd.nist.gov/vuln/detail/CVE-2023-50782 |
| CVE-2023-49083 / GHSA-jfhm-5ghh-2f97 | High | Loading PKCS#7 certificates could trigger a NULL dereference and crash on crafted input. | 41.0.6 | https://github.com/pyca/cryptography/security/advisories/GHSA-jfhm-5ghh-2f97 |
| GHSA-v8gr-m533-ghj9 | Unknown | Wheels included a vulnerable OpenSSL version, requiring a refreshed bundled OpenSSL build. | 41.0.4 | https://github.com/pyca/cryptography/security/advisories/GHSA-v8gr-m533-ghj9 |
| GHSA-jm77-qphf-c4w8 | Unknown | Wheels included a vulnerable OpenSSL version, requiring a refreshed bundled OpenSSL build. | 41.0.3 | https://github.com/pyca/cryptography/security/advisories/GHSA-jm77-qphf-c4w8 |
| CVE-2023-38325 / GHSA-cf7p-gm2m-833m | High | SSH certificate parsing mishandled critical-extension semantics, creating an authorization / certificate-interpretation integrity issue. | 41.0.2 | https://nvd.nist.gov/vuln/detail/CVE-2023-38325 |
| GHSA-5cpq-8wj7-hf2v | Unknown | Wheels included a vulnerable OpenSSL version, requiring an updated cryptography wheel release for bundled-wheel consumers. | 41.0.0 | https://github.com/pyca/cryptography/security/advisories/GHSA-5cpq-8wj7-hf2v |
| CVE-2023-23931 / GHSA-w7pp-m8wf-vj6r | Moderate | `Cipher.update_into()` accepted immutable buffer-protocol objects as an output buffer, allowing mutation/corruption of objects that should have been immutable. | 39.0.1 | https://github.com/pyca/cryptography/security/advisories/GHSA-w7pp-m8wf-vj6r |
| CVE-2023-0286 / GHSA-x4qr-2fvf-3mr5 | High | Wheels included an OpenSSL build affected by the X.400 address type-confusion vulnerability, requiring refreshed bundled wheels. | 39.0.1 | https://github.com/pyca/cryptography/security/advisories/GHSA-x4qr-2fvf-3mr5 |
| GHSA-39hc-v87j-747x | Unknown | Wheels included a vulnerable OpenSSL version, requiring a refreshed cryptography wheel build. | 38.0.3 | https://github.com/pyca/cryptography/security/advisories/GHSA-39hc-v87j-747x |
| CVE-2020-36242 / GHSA-rhm9-p9w5-fwm7 | High | Certain sequences of symmetric-encryption update calls on multi-GB values could trigger integer overflow / buffer overflow behavior, including via Fernet usage. | 3.3.2 | https://github.com/advisories/GHSA-rhm9-p9w5-fwm7 |
| CVE-2020-25659 / GHSA-hggm-jpg3-v476 | High | RSA decryption using PKCS#1 v1.5 padding could leak timing information consistent with a Bleichenbacher-style oracle. | 3.2.1 | https://github.com/advisories/GHSA-hggm-jpg3-v476 |
| CVE-2018-10903 / GHSA-fcf9-3qw3-gxmj | Critical | `finalize_with_tag()` did not enforce a minimum GCM tag length, enabling tag-forgery chances when callers accepted attacker-controlled short tags. | 2.3 | https://github.com/advisories/GHSA-fcf9-3qw3-gxmj |
| CVE-2016-9243 / GHSA-q3cj-2r34-2cwc | High | HKDF could return an empty byte string when called with a length shorter than the digest size, creating improper key-derivation output. | 1.5.3 | https://github.com/advisories/GHSA-q3cj-2r34-2cwc |

*Full advisory history: https://osv.dev/list?ecosystem=PyPI&q=cryptography*

## Security Posture Notes

- `cryptography` is a foundational Python cryptographic library with very high downstream blast radius; this pass measured roughly 261M weekly PyPI downloads.
- The public advisory record clusters around four recurring surfaces: low-level cryptographic API misuse or validation gaps, Python buffer / memory-safety boundaries in native-backed code, X.509 / PKCS parsing and verification, and bundled OpenSSL exposure in published wheels.
- Bundled OpenSSL wheel advisories deserve separate interpretation from first-party cryptography code flaws: they are still package-consumer upgrade events, but the underlying defect may live in OpenSSL rather than pyca/cryptography itself.
- Recent upstream changelog entries line up with OSV/GHSA records for the 2026 fix train: 46.0.5 added subgroup checks for uncommon `SECT*` curves, 46.0.6 fixed wildcard-DNS name-constraint handling, and 46.0.7 fixed non-contiguous-buffer handling.
- Upgrade guidance should distinguish source-built deployments from wheel consumers because source builds link against the local OpenSSL while many Python installations consume wheels with bundled OpenSSL.

## Dependencies of Note

- OpenSSL is the most important dependency boundary for this page, both for source builds and for bundled wheel builds.
- [[python/requests]] and [[python/urllib3]] are adjacent high-blast-radius consumers of Python TLS and certificate-verification behavior, though their package advisories should not be double-counted here.
- Native Rust / C extension boundaries matter for buffer-handling and memory-safety advisories surfaced in recent cryptography releases.

## Open Questions

- Is there a maintainer-published security policy or preferred private disclosure path that should be captured once located?
- Should future KB maintenance split bundled-OpenSSL wheel advisories into a dedicated subsection so first-party code flaws and dependency-bundle refreshes are easier to compare?
- Are there public audit reports for pyca/cryptography's X.509 verification layer or hazardous-materials APIs that can be cited without relying on private assessments?

## Related Pages

- [[python/requests]]
- [[python/urllib3]]
- [[python/index]]

---
*Last updated: 2026-05-05 | Sources: 6 (OSV package query, GitHub Advisory Database / GHSA pages, public CVE/NVD records, upstream CHANGELOG.rst, PyPI metadata, PyPIStats downloads)*
