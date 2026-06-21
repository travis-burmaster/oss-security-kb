# Rust / crates.io Index

## Seed Pages
- [[rust/tokio]] — dominant async runtime foundation · advisory mapped · memory-safety / unsoundness and Windows named-pipe boundary history

## Advisory-Mapped / Audited Pages
- [[rust/base64]] — base64 encoding/decoding library · advisory mapped · RUSTSEC-2017-0004 integer overflow / heap overflow in encode path (CVSS 9.8), fixed in 0.5.2; ~250M weekly downloads
- [[rust/chrono]] — dominant date-and-time library · advisory mapped · RUSTSEC-2020-0159 / CVE-2020-26235 localtime_r segfault via concurrent env-var mutation, fixed in 0.4.20; ~125.7M weekly downloads
- [[rust/h2]] — HTTP/2 implementation · advisory mapped · resource-exhaustion / DoS history through 0.3.26 / 0.4.4
- [[rust/hyper]] — foundational Rust HTTP implementation · advisory mapped · HTTP/1 parser/request-smuggling, header-injection, TLS hostname-verification, and parser soundness history
- [[rust/openssl]] — Rust bindings for OpenSSL · advisory mapped · 10 RUSTSEC advisories from MitM / use-after-free / file-read / UB / thread-safety history through RUSTSEC-2025-0022
- [[rust/regex]] — canonical Rust regex engine · advisory mapped · RUSTSEC-2022-0013 / CVE-2022-24713 complexity-limit ReDoS fixed in 1.5.5; ~183M weekly downloads
- [[rust/ring]] — widely used Rust cryptographic library · advisory mapped · RUSTSEC-2025-0009 / CVE-2025-4432 AES/QUIC overflow-check panic DoS fixed in 0.17.12; 0.16.x unmaintained (RUSTSEC-2025-0010)
- [[rust/rustls]] — dominant pure-Rust TLS implementation · advisory mapped · RUSTSEC-2024-0336 close_notify DoS (High) and RUSTSEC-2024-0399 fragmented-ClientHello panic DoS through 0.23.18; ~165M weekly downloads
- [[rust/serde]] — foundational serialization framework · baseline stub · no direct package-scoped OSV / RustSec advisory confirmed in this pass, but very high ecosystem blast radius
- [[rust/serde_yaml_ng]] — actively maintained fork of the archived `serde_yaml` crate · audit ingested · YAML 1.2 Core schema integer-parse conformance gap filed as acatton/serde-yaml-ng#32
- [[rust/reqwest]] — dominant Rust HTTP client · advisory mapped · no direct RustSec/GHSA advisories on record; ~126M weekly downloads with high ecosystem exposure
