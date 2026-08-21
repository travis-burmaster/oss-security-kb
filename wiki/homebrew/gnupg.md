# gnupg (Homebrew)

**Registry:** Homebrew
**Weekly Downloads:** unknown (formulae.brew.sh blocked in this environment; analytics unavailable)
**Repository:** https://github.com/gpg/gnupg (official mirror; canonical at https://git.gnupg.org/)
**Security Contact:** security@gnupg.org
**Disclosure Policy:** https://gnupg.org/contact.html
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2018-9234 | High (CVSS 7.5 AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N) | GnuPG 2.2.4–2.2.5 does not enforce a configuration requiring an offline master Certify key, resulting in apparently valid certifications produced with only a signing subkey; applications relying on GnuPG to validate that a master key was used for certification can be misled | No dedicated fix released; design limitation acknowledged upstream | [GHSA-mq99-p8pq-jp4q](https://github.com/advisories/GHSA-mq99-p8pq-jp4q) |
| CVE-2019-13050 | High (CVSS 9.0 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) | Persistent DoS via certificate spamming attack through the SKS keyserver network; GnuPG through 2.2.16 importing keys from an SKS keyserver host may trigger unbounded certificate flooding that causes GnuPG to become permanently unusable on the affected keyring | No GnuPG patch (design limitation of the SKS keyserver network); mitigation: configure keyserver to `hkps://keys.openpgp.org` or remove keyserver config | [GHSA-ch5h-mpfr-fhxh](https://github.com/advisories/GHSA-ch5h-mpfr-fhxh) |
| CVE-2021-40528 | Moderate (CVSS AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N) | ElGamal implementation in Libgcrypt (GnuPG's cryptographic backend) before 1.9.4 allows plaintext recovery via a cross-configuration attack: a dangerous combination of receiver public-key prime, generator, and sender ephemeral exponents across two interoperating cryptographic libraries enables decryption of previously captured ciphertexts | Libgcrypt 1.9.4 (GnuPG ≥ 2.3.6 ships patched Libgcrypt on Homebrew) | [GHSA-8m2v-68m9-q2c7](https://github.com/advisories/GHSA-8m2v-68m9-q2c7) |
| CVE-2022-34903 | Moderate (CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:L/A:N) | Signature forgery via injection into the GnuPG status line; in specific conditions where an attacker has access to any secret-key material from the victim's keyring and an application uses GPGME or parses the GnuPG status line to determine trust, an attacker can inject crafted status output to forge a successful verification result | GnuPG 2.3.7 / 2.2.36 (July 2022) | [GHSA-356p-pg27-x2cf](https://github.com/advisories/GHSA-356p-pg27-x2cf) |

*OSV reference: https://osv.dev/list?ecosystem=&q=gnupg*

## Security Posture Notes

GnuPG is the GNU Privacy Guard, the dominant open-source OpenPGP implementation and the de facto standard for email signing, software package verification (APT, RPM, Homebrew), and file encryption on Linux and macOS. The Homebrew formula `gnupg` installs the modern 2.x line (currently 2.4.x as of mid-2024).

GnuPG's architecture is multi-component: the `gnupg` binary itself delegates cryptographic operations to **Libgcrypt** (cryptographic primitives, including ElGamal — see CVE-2021-40528), key management to gpg-agent, and smart-card access to scdaemon. Vulnerabilities in Libgcrypt propagate to GnuPG.

Key security observations:
- **CVE-2019-13050 has no fix**: The certificate spamming vulnerability (poisoned keyserver certificates causing unbounded GnuPG hangs) is a structural limitation of the SKS keyserver network. GnuPG ≥ 2.2.17 attempted partial mitigation by not honoring "self-sig" flood, but the recommended long-term mitigation remains switching keyserver to `hkps://keys.openpgp.org` (Hagrid-based, no SPAM allowed).
- **GPGME consumers are sensitive to CVE-2022-34903**: Applications using GPGME (the C API wrapper) to parse GnuPG status lines to determine trust are directly exploitable. Applications that simply invoke `gpg --verify` and check exit code only are less exposed.
- The Homebrew formula tracks upstream closely; macOS users who keep Homebrew current should receive security patches within 1–3 days of upstream releases.
- GnuPG uses `security@gnupg.org` for private disclosure with a minimum 90-day embargo window.

## Dependencies of Note

- **Libgcrypt** — GnuPG's cryptographic backend; CVE-2021-40528 is a Libgcrypt vulnerability with direct GnuPG impact
- **libassuan** — IPC library used between GnuPG components (gpg, gpg-agent, scdaemon)
- **libksba** — X.509/CMS library used for S/MIME support; separate CVE history
- **Pinentry** — passphrase dialog tool; local privilege trust boundary

## Open Questions

- Are there GnuPG 2.4.x advisories published after 2022-07 that have not been captured in this pass? (2024+ search returned GnuTLS results only; deeper search warranted.)
- What is the exact Homebrew formula version and Libgcrypt version shipped as of 2026-08? Confirm Libgcrypt ≥ 1.9.4 is included.
- CVE-2018-9234 affects GnuPG 2.2.4–2.2.5 only; are there later Homebrew formula versions with this design limitation?

## Related Pages

- [[homebrew/openssl@3]] — TLS backend; related cryptographic infrastructure
- [[homebrew/git]] — uses GnuPG for signed commits and tags
- [[homebrew/index]]

---
*Last updated: 2026-08-21 | Sources: 4*
