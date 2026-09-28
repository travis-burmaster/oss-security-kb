# Advisory Review Evidence — 2026-09-28

## Pass Summary

- Date: 2026-09-28
- Targets: rust/openssl-src (new), rust/once_cell (new)
- Ecosystem: Rust / crates.io
- OSV.dev: blocked (HTTP 403) — using rustsec/advisory-db + github/advisory-database fallbacks

## URLs Consulted

### openssl-src

- https://crates.io/api/v1/crates/openssl-src — download stats (21.6M recent, 105.6M total, latest 400.0.1+4.0.2)
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2020-0015.md — CVE-2020-1967 SSL_check_chain NULL deref
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2021-0055.md — CVE-2021-3449 signature_algorithms NULL ptr
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2021-0056.md — CVE-2021-3450 CA cert check bypass
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2021-0057.md — CVE-2021-23840 CipherUpdate integer overflow
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2021-0058.md — CVE-2021-23841 X509_issuer_and_serial_hash NULL ptr
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2021-0097.md — CVE-2021-3711 SM2 Buffer Overflow (Critical CVSS 9.8)
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2021-0098.md — CVE-2021-3712 ASN.1 string buffer overruns
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2021-0129.md — CVE-2021-4044 X509_verify_cert mishandled error
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2022-0014.md — CVE-2022-0778 BN_mod_sqrt infinite loop
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2022-0025.md — CVE-2022-1473 OPENSSL_LH_flush resource leak
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2022-0026.md — CVE-2022-1434 RC4-MD5 incorrect MAC key
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2022-0027.md — CVE-2022-1343 OCSP_basic_verify bypass
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2022-0032.md — CVE-2022-2097 AES OCB encryption failure
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2022-0033.md — CVE-2022-2274 RSA heap memory corruption
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2022-0059.md — CVE-2022-3358 NID_undef NULL cipher
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2022-0064.md — CVE-2022-3602 X.509 email 4-byte buffer overflow
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2022-0065.md — CVE-2022-3786 X.509 email variable-length buffer overflow
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2023-0006.md — CVE-2023-0286 X.400 type confusion
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2023-0007.md — CVE-2022-4304 RSA timing oracle
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2023-0008.md — CVE-2022-4203 X.509 name constraints buffer overflow
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2023-0009.md — CVE-2023-0215 BIO_new_NDEF UAF
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2023-0010.md — CVE-2022-4450 PEM_read_bio_ex double free
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2023-0011.md — CVE-2023-0216 d2i_PKCS7 invalid pointer deref
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2023-0012.md — CVE-2023-0217 DSA public key NULL deref
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/openssl-src/RUSTSEC-2023-0013.md — CVE-2023-0401 PKCS7 verification NULL deref
- mcp__github__search_code: `repo:rustsec/advisory-db path:crates/openssl-src` — confirmed 25 total advisories
- https://github.com/alexcrichton/openssl-src-rs — upstream repository

### once_cell

- https://crates.io/api/v1/crates/once_cell — download stats (286.5M recent, 1.3B total, latest 1.21.4)
- https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/once_cell/RUSTSEC-2019-0017.md — CVE-2019-16141 Lazy deref UB on panic
- mcp__github__search_code: `repo:rustsec/advisory-db once_cell` — confirmed 1 advisory for once_cell itself (RUSTSEC-2019-0017; double-checked-cell is a different crate)

## Notes

- All 25 openssl-src advisories read and verified from rustsec advisory-db source files.
- Advisory IDs RUSTSEC-2021-0056, RUSTSEC-2021-0098, RUSTSEC-2021-0129 also confirmed from search listing.
- No RUSTSEC advisories for openssl-src after 2023 (RUSTSEC-2023-0013 is the most recent).
- once_cell RUSTSEC-2019-0017 confirmed as single advisory; current stable 1.21.4 (March 2026) unaffected.
