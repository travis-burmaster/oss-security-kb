# gnupg (Homebrew)

**Registry:** Homebrew
**Weekly Downloads:** unknown (formulae.brew.sh API blocked; anecdotally one of the most widely installed security-tooling formulas on macOS)
**Repository:** https://gnupg.org/ (canonical); https://github.com/gpg/gnupg (mirror/supplementary)
**Security Contact:** security@gnupg.org
**Disclosure Policy:** https://gnupg.org/faq/gnupg-faq.html
**Current Status:** advisory-mapped

## Overview

GNU Privacy Guard (GnuPG / GPG) is the reference implementation of the OpenPGP standard (RFC 4880). The Homebrew `gnupg` formula currently ships **GnuPG 2.5.21** (the current stable series since 2.5.16; even-minor conventions were relaxed for 2.5.x per upstream announcement). Upstream maintains two active branches:

- **2.5.x** — current stable (Homebrew); security fixes land here first
- **2.2.x** — LTS branch; still receives security fixes but features are frozen

The upstream security page is https://www.gnupg.org/faq/gnupg-faq.html and CVEs are tracked via https://gnupg.org/faq/gnupg-faq.html#security. Individual CVEs reference https://dev.gnupg.org/ task tracker entries.

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No public third-party audits on record as of 2026-08-16.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-14855 / GHSA-cpvm-f36g-55vg | Moderate | SHA-1 collision in certificate signature verification: an attacker can forge certificate signatures using SHA-1 chosen-prefix collisions, affecting `gpg --verify` on OpenPGP certificates; disclosed at RWC 2020 (Leurent et al.) | GnuPG ≥ 2.2.18 | [GHSA-cpvm-f36g-55vg](https://github.com/advisories/GHSA-cpvm-f36g-55vg), [dev.gnupg.org/T4755](https://dev.gnupg.org/T4755) |
| CVE-2022-34903 / GHSA-356p-pg27-x2cf | Moderate | Signature spoofing via injected key: GnuPG through 2.3.7 permits a key to be injected into a user's keyring through systems that allow key updates (e.g. Proton Mail); the injected key can enable signature spoofing via a fingerprint-collision attack | GnuPG ≥ 2.3.8 (2.4.x and 2.5.x unaffected) | [GHSA-356p-pg27-x2cf](https://github.com/advisories/GHSA-356p-pg27-x2cf), [dev.gnupg.org/T6027](https://dev.gnupg.org/T6027) |
| CVE-2025-68972 / GHSA-w789-3q45-984r | Moderate | Signature bypass via form-feed in plaintext: if a signed message has `\f` (U+000C form-feed) at the end of a plaintext line, an adversary can construct a modified message that appends additional text after the signed material while still passing `gpg --verify`; an "invalid armor" warning is printed but the verification exit code indicates success; affects GnuPG through 2.4.8 | GnuPG 2.4.9+ / 2.5.x (2.5.16+ recommended); see CCC talk | [GHSA-w789-3q45-984r](https://github.com/advisories/GHSA-w789-3q45-984r), [gpg.fail/formfeed](https://gpg.fail/formfeed) |
| CVE-2025-68973 / GHSA-pj23-86ww-f72p | High | `armor.c` memcpy boundary issue: an attacker-supplied armored OpenPGP message triggers an unsafe `memcpy` in the ASCII armor decoder; the 2.2.x LTS patch is gnupg 2.2.51; the 2.5.x fix train address this in the same cycle | GnuPG 2.2.x: ≥ 2.2.51; 2.5.x: ≥ 2.5.16 recommended | [GHSA-pj23-86ww-f72p](https://github.com/advisories/GHSA-pj23-86ww-f72p), [gpg.fail/memcpy](https://gpg.fail/memcpy) |

*Upstream CVE list: https://gnupg.org/faq/gnupg-faq.html*

## Security Posture Notes

GnuPG is maintained by Werner Koch and the GnuPG project. Security disclosures go to security@gnupg.org; upstream tracks issues at https://dev.gnupg.org/.

**Homebrew patch-lag:** The Homebrew formula typically updates within days of an upstream release. The current formula is 2.5.21; users on older Homebrew installations or pinned versions may lag. `brew outdated gnupg` is the recommended check.

**Signature-verification semantics:** The 2025 CVE batch (CVE-2025-68972, CVE-2025-68973) was presented at CCC 2025 ("To Sign or Not to Sign — Practical Vulnerabilities in OpenPGP") as part of a broader investigation of OpenPGP implementation weaknesses across GnuPG, Sequoia, and other clients. CVE-2025-68972 in particular highlights that callers must not rely solely on the `gpg` exit code; the printed "invalid armor" message must also be checked. Tooling that wraps `gpg --verify` and only inspects the exit code may be misled even on patched versions if the "invalid armor" text is suppressed.

**SHA-1 migration:** CVE-2019-14855 accelerated GnuPG's move away from SHA-1 for key certification. Modern GnuPG defaults to SHA-256 for signatures. Old V4 keys using SHA-1 as the preferred hash remain interoperable but are deprecated; administrators should audit keyrings for lingering SHA-1 certification preferences.

**System GnuPG on macOS:** macOS ships `/usr/bin/gpg` in some configurations but it is typically an outdated stub or absent. Homebrew's `gnupg` formula installs to `/opt/homebrew/bin/gpg` (Apple Silicon) or `/usr/local/bin/gpg` (Intel). PATH ordering matters: shell scripts that call `gpg` unqualified may pick up the system stub rather than the Homebrew-managed version.

## Dependencies of Note

- `libgcrypt` — GnuPG's internal cryptographic library; has its own CVE history
- `libksba` — X.509/CMS certificate handling library; has advisory history (e.g. CVE-2022-3515 Critical heap overflow fixed 1.6.2, 2022)
- `gnutls` — TLS library used by some gnupg components (distinct from gnupg itself)
- `pinentry` — passphrase entry; not directly security-impacting but part of the trust chain

## Open Questions

- Confirm whether CVE-2025-68972 and CVE-2025-68973 are fully addressed in the current Homebrew formula (2.5.21); verify against upstream 2.5.x changelog.
- Enumerate `libksba` advisory history separately (CVE-2022-3515 High is already notable).
- Check whether Homebrew's `gnupg` formula pins `pinentry` version and whether that version has any known issues.
- Investigate gpg-agent long-lived process semantics: a patched `gnupg` binary does not replace a running `gpg-agent`; users must restart the agent after upgrade.

## Related Pages

- [[homebrew/openssl@3]]
- [[homebrew/index]]

---
*Last updated: 2026-08-16 | Sources: 4 CVEs (CVE-2019-14855, CVE-2022-34903, CVE-2025-68972, CVE-2025-68973); Homebrew formula 2.5.21 confirmed via homebrew-core*
