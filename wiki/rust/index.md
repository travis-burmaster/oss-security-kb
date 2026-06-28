# Rust / crates.io Index

## Seed Pages
- [[rust/tokio]] — dominant async runtime foundation · advisory mapped · memory-safety / unsoundness and Windows named-pipe boundary history

## Advisory-Mapped / Audited Pages
- [[rust/actix-web]] — high-performance Rust web framework · advisory mapped · 2018 memory-safety cluster (RUSTSEC-2018-0019 / CVE-2018-25024/25025/25026 Critical CVSS 9.8), actix-http BodyStream UAF (CVE-2020-35901 High), HTTP/1 request-smuggling (CVE-2021-38512 High), and 2026 actix-files information-exposure and panic-DoS cluster plus actix-http CL.TE smuggling (GHSA-xhj4-vrgc-hr34) fixed in actix-http 3.12.1; ~663K/week
- [[rust/axum]] — high-performance Rust web framework (tokio-rs) · advisory mapped · RUSTSEC-2022-0055 / CVE-2022-3212 no-default-body-limit DoS in axum-core extractors (Form/Json/String), fixed in axum ≥ 0.5.16; ~7.0M/week est., ~361.7M total downloads
- [[rust/base64]] — base64 encoding/decoding library · advisory mapped · RUSTSEC-2017-0004 integer overflow / heap overflow in encode path (CVSS 9.8), fixed in 0.5.2; ~250M weekly downloads
- [[rust/chrono]] — dominant date-and-time library · advisory mapped · RUSTSEC-2020-0159 / CVE-2020-26235 localtime_r segfault via concurrent env-var mutation, fixed in 0.4.20; ~125.7M weekly downloads
- [[rust/h2]] — HTTP/2 implementation · advisory mapped · resource-exhaustion / DoS history through 0.3.26 / 0.4.4
- [[rust/hyper]] — foundational Rust HTTP implementation · advisory mapped · HTTP/1 parser/request-smuggling, header-injection, TLS hostname-verification, and parser soundness history
- [[rust/openssl]] — Rust bindings for OpenSSL · advisory mapped · 10 RUSTSEC advisories from MitM / use-after-free / file-read / UB / thread-safety history through RUSTSEC-2025-0022
- [[rust/rand]] — de facto Rust random-number-generation library · advisory mapped · RUSTSEC-2026-0097 / GHSA-cq8v-f236-94qc unsoundness when log+thread_rng features enabled (aliased mutable references, informational, fixed in 0.10.1 / 0.9.3 / 0.8.6); ~23.7M/week; ~1.3B total downloads
- [[rust/regex]] — canonical Rust regex engine · advisory mapped · RUSTSEC-2022-0013 / CVE-2022-24713 complexity-limit ReDoS fixed in 1.5.5; ~183M weekly downloads
- [[rust/reqwest]] — dominant Rust HTTP client · advisory mapped · no direct RustSec/GHSA advisories on record; ~126M weekly downloads with high ecosystem exposure
- [[rust/ring]] — widely used Rust cryptographic library · advisory mapped · RUSTSEC-2025-0009 / CVE-2025-4432 AES/QUIC overflow-check panic DoS fixed in 0.17.12; 0.16.x unmaintained (RUSTSEC-2025-0010)
- [[rust/rustls]] — dominant pure-Rust TLS implementation · advisory mapped · RUSTSEC-2024-0336 close_notify DoS (High) and RUSTSEC-2024-0399 fragmented-ClientHello panic DoS through 0.23.18; ~165M weekly downloads
- [[rust/rustls-webpki]] — X.509 certificate verification engine for rustls · advisory mapped · 5 advisories from 2023–2026: CPU DoS in cert path building (RUSTSEC-2023-0053), CRL revocation bypass and pre-auth panic DoS (RUSTSEC-2026-0049 / RUSTSEC-2026-0104), and name constraint bypasses (RUSTSEC-2026-0098 / RUSTSEC-2026-0099) fixed in 0.103.13; ~12.1M/week est., ~601.5M total downloads
- [[rust/serde]] — foundational serialization framework · baseline stub · no direct package-scoped OSV / RustSec advisory confirmed in this pass, but very high ecosystem blast radius
- [[rust/serde_json]] — de facto standard Rust JSON library · baseline stub · no direct package-scoped RustSec/GHSA advisory confirmed; 1B+ all-time crates.io downloads (~16.1M/week); high ecosystem blast radius
- [[rust/serde_yaml_ng]] — actively maintained fork of the archived `serde_yaml` crate · audit ingested · YAML 1.2 Core schema integer-parse conformance gap filed as acatton/serde-yaml-ng#32
- [[rust/smallvec]] — small vector optimization library · advisory mapped · 5 advisories 2018–2021 across double-free, memory corruption, unsoundness, and buffer overflow in grow/insert paths (4× Critical CVSS 9.8); all fixed ≥ 1.6.1; ~15.4M/week est., ~930M total downloads
- [[rust/time]] — date-and-time library · advisory mapped · RUSTSEC-2020-0071 localtime_r segfault on Unix (0.1.x permanently affected, 0.2.7–0.2.22 fixed in 0.2.23) and RUSTSEC-2026-0009 / CVE-2026-25727 RFC 2822 stack-exhaustion DoS fixed in 0.3.47; ~10.8M/week est., ~738M total downloads
