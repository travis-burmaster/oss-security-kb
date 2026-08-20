# rsa (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** ~5.1M/week est. (46.1M recent; ~202.9M total, as of 2026-08-20)
**Repository:** https://github.com/RustCrypto/RSA
**Security Contact:** https://github.com/RustCrypto/RSA/security/advisories/new
**Disclosure Policy:** https://github.com/RustCrypto/RSA/blob/master/SECURITY.md (90-day responsible disclosure; security fixes applied to most recent release only)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-49092 / RUSTSEC-2023-0071 / GHSA-c38w-74pg-36hr / GHSA-4grx-2x9w-596c | Moderate (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N — 5.9) | Marvin Attack: non-constant-time RSA decryption and signing operations leak private key material via a timing side-channel observable over the network; an adversary who can measure decryption timing may recover the private key; affects all versions through 0.9.10 (latest stable) and 0.10.0-rc.18 (latest pre-release); no patched version available as of 2026-08-20 | No fix available — see security posture notes | [RUSTSEC-2023-0071](https://rustsec.org/advisories/RUSTSEC-2023-0071.html) / [GHSA-c38w-74pg-36hr](https://github.com/advisories/GHSA-c38w-74pg-36hr) / [CVE-2023-49092](https://nvd.nist.gov/vuln/detail/CVE-2023-49092) |

## Security Posture Notes

Pure Rust RSA implementation maintained by the [RustCrypto](https://github.com/RustCrypto) organization (volunteer, best-effort). Total downloads ~202.9M on crates.io; 46.1M recent downloads. Latest stable 0.9.10 (released 2026-01-06); pre-release 0.10.0-rc.18 available (2026-04-27). Repository: https://github.com/RustCrypto/RSA.

**Marvin Attack (CVE-2023-49092 / RUSTSEC-2023-0071) — unfixed since November 2023.** The [Marvin Attack](https://people.redhat.com/~hkario/marvin/) is a class of timing side-channel attacks against RSA implementations identified by Hubert Kario (Red Hat). The `rsa` crate was identified as vulnerable during a broad survey of RSA implementations: its decryption and signing operations are not constant-time, allowing a network-positioned adversary who can observe timing information to extract the private key. The RustCrypto team has ongoing work to implement a constant-time solution (tracked in [RustCrypto/RSA#626](https://github.com/RustCrypto/RSA/issues/626)), but no fixed version has shipped as of the date of this pass.

**The GHSA records the affected range as "0 through 0.9.6" (with "patch in development" at filing time), but versions 0.9.7–0.9.10 were released after the advisory and the RUSTSEC advisory continues to list no patched versions.** Callers should assume all 0.9.x and 0.10.0-rc.x versions are affected.

**Workaround:** Avoid use in network-accessible environments where adversaries can observe timing. The official workaround is to use the crate only on locally-run, non-compromised machines where timing observations are not possible.

Security disclosures: GitHub private advisory at https://github.com/RustCrypto/RSA/security/advisories/new. 90-day minimum responsible disclosure window.

## Dependencies of Note

- **`num-bigint-dig`** — the custom BigInteger implementation used for RSA arithmetic; the non-constant-time behavior is rooted in this dependency. Track for upstream constant-time remediation.
- **`rsa-export`** (RUSTSEC-2024-0333, separate crate) — a companion key-export crate with its own distinct advisory; do not confuse with the `rsa` crate.

## Open Questions

- Has 0.10.0 stable addressed RUSTSEC-2023-0071 with a constant-time implementation? The 0.10.0-rc.x series has been in development since early 2025; review its changelog before treating any 0.10.x release as safe.
- Are downstream crates that re-export or wrap RustCrypto RSA primitives (e.g., `ssh-key`, `pkcs1`, `pkcs8`, `p256`-based hybrid schemes) transitively exposing the timing leak?
- When RUSTSEC-2023-0071 is eventually patched, verify that the advisory DB is updated and that dependency-audit tools (`cargo audit`) correctly surface the old-vs-new status.

## Related Pages

- [[rust/ring]] — alternative cryptographic library using ring/aws-lc-rs for RSA; RUSTSEC-2025-0009 / CVE-2025-4432 AES DoS fixed in 0.17.12; no timing-channel advisory on RSA path
- [[rust/rustls]] — TLS implementation using ring or aws-lc-rs (not the `rsa` crate) for key operations
- [[rust/ed25519-dalek]] — related RustCrypto signing library; RUSTSEC-2022-0093 timing-adjacent issue
- [[rust/curve25519-dalek]] — timing side-channel precedent in the RustCrypto ecosystem: RUSTSEC-2024-0344
- [[rust/index]]

---
*Last updated: 2026-08-20 | Sources: 3 (RUSTSEC-2023-0071, GHSA-c38w-74pg-36hr, GHSA-4grx-2x9w-596c)*
