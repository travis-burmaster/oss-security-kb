# openssl-src (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~21.6M (as of 2026-09-28)
**Repository:** https://github.com/alexcrichton/openssl-src-rs
**Security Contact:** https://github.com/alexcrichton/openssl-src-rs/issues
**Disclosure Policy:** none listed (defers to upstream OpenSSL: https://www.openssl.org/policies/secpolicy.html)
**Current Status:** advisory-mapped

## Role in the Rust Ecosystem

`openssl-src` is not an API crate — it is a **build-time vendor crate** that downloads and compiles the OpenSSL C library from source so that Rust crates can statically link against it. It is the primary mechanism by which many Rust TLS stacks (e.g. `native-tls`, `openssl`) ship a bundled OpenSSL rather than requiring a system library.

Version numbering encodes the bundled OpenSSL release:
- `111.x.y+1.1.1z` → OpenSSL 1.1.1z
- `300.0.x+3.0.y` → OpenSSL 3.0.y
- `400.0.x+4.0.y` → OpenSSL 4.0.y (current; latest stable: **400.0.1+4.0.2**)

Each upstream OpenSSL CVE that affects a bundled version is tracked as a separate RUSTSEC advisory. All 25 advisories span 2020–2023; the 111.x and 300.0.x lines have since been superseded by the 400.0.x line.

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No Rust-ecosystem audits on record. Security posture is inherited entirely from upstream OpenSSL audits and CVE disclosures.*

## Known Vulnerabilities

All advisories are upstream OpenSSL CVEs re-filed against the bundled source crate. Source links point to the rustsec.org advisory record.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2021-0097 / CVE-2021-3711 / GHSA-5ww6-px42-wc85 | Critical (CVSS 9.8 AV:N) | SM2 decryption buffer overflow: two-step `EVP_PKEY_decrypt()` call returns insufficient size estimate on first call; second call overflows allocated buffer by up to 62 bytes on attacker-controlled SM2 data — heap corruption, potential RCE | >= 111.16 | [RUSTSEC-2021-0097](https://rustsec.org/advisories/RUSTSEC-2021-0097.html) |
| RUSTSEC-2020-0015 / CVE-2020-1967 / GHSA-jq65-29v4-4x35 | High (CVSS 7.5 AV:N) | `SSL_check_chain()` NULL ptr deref via unrecognized `signature_algorithms_cert` TLS extension — pre-auth DoS | >= 111.9 | [RUSTSEC-2020-0015](https://rustsec.org/advisories/RUSTSEC-2020-0015.html) |
| RUSTSEC-2021-0056 / CVE-2021-3450 / GHSA-8hfj-xrj2-pm22 | High (CVSS 7.4 AV:N) | CA certificate check bypass: elliptic-curve parameter processing overwrites the CA verification flag when `X509_V_FLAG_X509_STRICT` is set without a configured purpose — non-CA certs can issue certificates | >= 111.15 | [RUSTSEC-2021-0056](https://rustsec.org/advisories/RUSTSEC-2021-0056.html) |
| RUSTSEC-2021-0055 / CVE-2021-3449 / GHSA-83mx-573x-5rw9 | High (AV:N DoS) | NULL ptr deref in `signature_algorithms` processing: renegotiation ClientHello omitting `signature_algorithms` but including `signature_algorithms_cert` crashes TLS servers (renegotiation enabled by default) | >= 111.15 | [RUSTSEC-2021-0055](https://rustsec.org/advisories/RUSTSEC-2021-0055.html) |
| RUSTSEC-2021-0098 / CVE-2021-3712 / GHSA-q9wj-f4qw-6vfj | High (CVSS 7.1) | Read buffer overruns in ASN.1 string handling: NUL-unterminated `ASN1_STRING` values passed to print functions trigger OOB reads — DoS or potential private-key disclosure | >= 111.16 | [RUSTSEC-2021-0098](https://rustsec.org/advisories/RUSTSEC-2021-0098.html) |
| RUSTSEC-2022-0033 / CVE-2022-2274 / GHSA-735f-pg76-fxc4 | High (AV:N) | Heap memory corruption in RSA private-key operations on x86_64 CPUs with AVX512IFMA: OpenSSL 3.0.4 regression corrupts memory during 2048-bit RSA computation — DoS or potential RCE | >= 300.0.9 | [RUSTSEC-2022-0033](https://rustsec.org/advisories/RUSTSEC-2022-0033.html) |
| RUSTSEC-2022-0064 / CVE-2022-3602 / GHSA-8rwr-x37p-mx23 | High (downgraded from Critical) | X.509 email address 4-byte stack buffer overflow in name constraint checking: attacker-controlled dot characters overwrite 4 bytes on the stack — DoS or potential RCE via malicious CA or server | >= 300.0.11 | [RUSTSEC-2022-0064](https://rustsec.org/advisories/RUSTSEC-2022-0064.html) |
| RUSTSEC-2022-0025 / CVE-2022-1473 / GHSA-g323-fr93-4j3c | High (CVSS 7.5 AV:N) | Resource leakage in `OPENSSL_LH_flush()`: hash-table entries are not reused after flushing, causing unbounded memory growth and increasingly slow empty-table traversal in long-running TLS servers that perform client-certificate auth | >= 300.0.6 | [RUSTSEC-2022-0025](https://rustsec.org/advisories/RUSTSEC-2022-0025.html) |
| RUSTSEC-2022-0026 / CVE-2022-1434 / GHSA-638m-m8mh-7gw2 | High (CVSS 7.5 integrity) | Incorrect MAC key in RC4-MD5 ciphersuite: OpenSSL 3.0 uses AAD data as the MAC key, making it predictable — MitM integrity bypass (requires non-default legacy provider + explicit ciphersuite configuration) | >= 300.0.6 | [RUSTSEC-2022-0026](https://rustsec.org/advisories/RUSTSEC-2022-0026.html) |
| RUSTSEC-2022-0014 / CVE-2022-0778 / GHSA-x3mh-jvjw-3xwx | High (DoS) | `BN_mod_sqrt()` infinite loop on non-prime moduli: reachable during certificate parsing via compressed EC public keys or explicit curve parameters — pre-auth DoS via certificate chain | >= 111.18 (1.1.1 line) or >= 300.0.5 (3.0 line) | [RUSTSEC-2022-0014](https://rustsec.org/advisories/RUSTSEC-2022-0014.html) |
| RUSTSEC-2022-0065 / CVE-2022-3786 / GHSA-h8jm-2x53-xhp5 | Moderate (DoS) | X.509 email address variable-length stack buffer overflow in name constraint checking: period characters overflow the stack — DoS (released same day as CVE-2022-3602) | >= 300.0.11 | [RUSTSEC-2022-0065](https://rustsec.org/advisories/RUSTSEC-2022-0065.html) |
| RUSTSEC-2023-0007 / CVE-2022-4304 / GHSA-p52g-cm5j-mjv4 | Moderate | Timing Oracle in RSA decryption: response-time differences across PKCS#1 v1.5 / RSA-OEAP / RSASVE padding modes enable Bleichenbacher-style plaintext recovery attacks over the network | >= 111.25 (1.1.1 line) or >= 300.0.12 (3.0 line) | [RUSTSEC-2023-0007](https://rustsec.org/advisories/RUSTSEC-2023-0007.html) |
| RUSTSEC-2023-0006 / CVE-2023-0286 / GHSA-x4qr-2fvf-3mr5 | Moderate | X.400 address type confusion in X.509 `GeneralName`: type mismatch in `GENERAL_NAME_cmp` allows passing arbitrary pointers to `memcmp` — memory read or DoS when CRL checking is enabled | >= 111.25 or >= 300.0.12 | [RUSTSEC-2023-0006](https://rustsec.org/advisories/RUSTSEC-2023-0006.html) |
| RUSTSEC-2023-0009 / CVE-2023-0215 / GHSA-r7jw-wp68-3xch | Moderate | Use-after-free following `BIO_new_NDEF`: filter BIO freed on certain failures but caller retains dangling pointer — UAF in `BIO_pop()` cascading through PEM/SMIME/PKCS7 write APIs | >= 111.25 or >= 300.0.12 | [RUSTSEC-2023-0009](https://rustsec.org/advisories/RUSTSEC-2023-0009.html) |
| RUSTSEC-2023-0010 / CVE-2022-4450 / GHSA-v5w6-wcm8-jm4q | Moderate | Double free after `PEM_read_bio_ex`: zero-payload PEM leaves header pointer to freed memory — double-free DoS via `PEM_read_bio()`, `SSL_CTX_use_serverinfo_file()` | >= 111.25 or >= 300.0.12 | [RUSTSEC-2023-0010](https://rustsec.org/advisories/RUSTSEC-2023-0010.html) |
| RUSTSEC-2023-0008 / CVE-2022-4203 / GHSA-w67w-mw4j-8qrv | Moderate | X.509 name constraints read buffer overflow: malformed certificate triggers OOB read during name constraint verification — DoS/info disclosure | >= 300.0.12 | [RUSTSEC-2023-0008](https://rustsec.org/advisories/RUSTSEC-2023-0008.html) |
| RUSTSEC-2023-0011 / CVE-2023-0216 / GHSA-29xx-hcv2-c4cp | Moderate (DoS) | Invalid pointer dereference in `d2i_PKCS7`: malformed PKCS7 data triggers OOB read → crash; affects third-party apps processing untrusted PKCS7 (TLS unaffected) | >= 300.0.12 | [RUSTSEC-2023-0011](https://rustsec.org/advisories/RUSTSEC-2023-0011.html) |
| RUSTSEC-2023-0012 / CVE-2023-0217 / GHSA-vxrh-cpg7-8vjr | Moderate (DoS) | NULL deref validating DSA public key via `EVP_PKEY_public_check()` with malformed key — crash; affects apps with FIPS 140-3 validation requirements | >= 300.0.12 | [RUSTSEC-2023-0012](https://rustsec.org/advisories/RUSTSEC-2023-0012.html) |
| RUSTSEC-2023-0013 / CVE-2023-0401 | Moderate (DoS) | NULL deref during PKCS7 data verification: missing digest initialization check causes crash when hash algorithm implementation is unavailable — affects SMIME and TS library callers | >= 300.0.12 | [RUSTSEC-2023-0013](https://rustsec.org/advisories/RUSTSEC-2023-0013.html) |
| RUSTSEC-2021-0057 / CVE-2021-23840 / GHSA-qgm6-9472-pwq7 | Moderate | Integer overflow in `EVP_CipherUpdate`/`EncryptUpdate`/`DecryptUpdate`: near-integer-max input lengths produce negative output length despite success return — crash or incorrect behavior | >= 111.14 | [RUSTSEC-2021-0057](https://rustsec.org/advisories/RUSTSEC-2021-0057.html) |
| RUSTSEC-2021-0058 / CVE-2021-23841 / GHSA-84rm-qf37-fgc2 | Moderate | NULL ptr deref in `X509_issuer_and_serial_hash()`: insufficient error handling during issuer field parsing — DoS for callers that pass untrusted certificates | >= 111.14 | [RUSTSEC-2021-0058](https://rustsec.org/advisories/RUSTSEC-2021-0058.html) |
| RUSTSEC-2022-0032 / CVE-2022-2097 / GHSA-3wx7-46ch-7rq2 | Moderate | AES OCB encryption failure: 32-bit x86 with AES-NI assembly leaves up to 16 bytes unencrypted in certain in-place operations — plaintext exposure (TLS/DTLS unaffected; OCB not used in TLS cipher suites) | >= 111.22 (1.1.1 line) or >= 300.0.9 | [RUSTSEC-2022-0032](https://rustsec.org/advisories/RUSTSEC-2022-0032.html) |
| RUSTSEC-2022-0059 / CVE-2022-3358 / GHSA-4f63-89w9-3jjv | Moderate | NULL cipher via `NID_undef` in `EVP_CIPHER_meth_new()`: custom ciphers registered with `NID_undef` are resolved to the NULL cipher, causing plaintext to be emitted as ciphertext — only affects non-standard custom cipher usage | >= 300.0.10 | [RUSTSEC-2022-0059](https://rustsec.org/advisories/RUSTSEC-2022-0059.html) |
| RUSTSEC-2021-0129 / CVE-2021-4044 / GHSA-mmjf-f5jw-w72q | Low (DoS) | Libssl mishandles negative return from `X509_verify_cert()`: unexpected `SSL_ERROR_WANT_RETRY_VERIFY` propagation can cause crash, infinite loop, or undefined behavior in most applications | >= 300.0.4 | [RUSTSEC-2021-0129](https://rustsec.org/advisories/RUSTSEC-2021-0129.html) |
| RUSTSEC-2022-0027 / CVE-2022-1343 / GHSA-mfm6-r9g2-q4r7 | Low | `OCSP_basic_verify` with `OCSP_NOCHECKS` flag returns success despite signing certificate validation failure — integrity bypass under non-default OCSP configuration | >= 300.0.6 | [RUSTSEC-2022-0027](https://rustsec.org/advisories/RUSTSEC-2022-0027.html) |

## Security Posture Notes

`openssl-src` is a thin build harness maintained by Alex Crichton (formerly Mozilla/Rust core team). Its security surface is almost entirely inherited from upstream OpenSSL:

- **All 25 RUSTSEC advisories** (2020–2023) map directly to upstream OpenSSL CVEs filed against the vendored source versions 1.1.1 and 3.0.x. The version encoding (`111.x+1.1.1z`, `300.0.x+3.0.y`) makes it straightforward to correlate openssl-src versions with upstream security bulletins.
- **Post-2023 posture:** No RUSTSEC advisories have been filed for openssl-src after RUSTSEC-2023-0013. Upstream OpenSSL 4.0.x (bundled as 400.0.x) is the current supported line. The OpenSSL project's own security bulletins at https://www.openssl.org/news/vulnerabilities.html remain the authoritative source for current vulnerability tracking.
- **Static linking implications:** Applications that use `openssl-src` to statically link OpenSSL do not automatically pick up OS-level OpenSSL security patches. Each advisory requires a dependency update and rebuild. Operators should monitor cargo audit / cargo deny alerts.
- **Relationship to `openssl` and `openssl-sys`:** This crate is a build-time dependency of `openssl-sys` when the `vendored` feature is enabled. The `openssl` bindings crate (see [[rust/openssl]]) has its own separate RUSTSEC advisory history covering Rust binding–layer flaws.
- **Cargo audit coverage:** `cargo audit` and `cargo deny audit` will flag outdated openssl-src versions against all 25 advisories above.

## Dependencies of Note

- Bundles the full OpenSSL C source tree; no additional Rust crate dependencies.
- Downstream affected when used as a build dependency of `openssl-sys` (which is a dependency of `openssl`, `native-tls`, and many network-layer crates).

## Open Questions

- Are there upstream OpenSSL 4.x CVEs (post-2023) that warrant new RUSTSEC advisories for `openssl-src`, or is the Rust ecosystem relying on upstream CVE tracking directly?
- Verify current download stats via crates.io API (as of this pass: ~21.6M recent / ~105.6M total).

## Related Pages

- [[rust/openssl]] — Rust bindings for OpenSSL; separate advisory history covering binding-layer flaws
- [[linux/openssl]] — upstream OpenSSL CVE history including Heartbleed, 2022 buffer overflows, and 2026 fixes
- [[rust/rustls]] — pure-Rust TLS alternative that avoids the OpenSSL dependency chain

---
*Last updated: 2026-09-28 | Sources: 25 (rustsec/advisory-db via raw.githubusercontent.com)*
