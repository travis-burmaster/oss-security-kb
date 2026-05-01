# openssl (linux)

**Registry:** distro
**Weekly Downloads:** unknown (as of 2026-04-11)
**Repository:** https://github.com/openssl/openssl
**Security Contact:** https://www.openssl.org/community/omc.html
**Disclosure Policy:** https://www.openssl.org/policies/secpolicy.html
**Current Status:** baseline stub

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No distro-normalized proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| Review pending | — | This page has not yet been normalized across distro package names. Start with upstream OpenSSL advisories, Debian/Ubuntu/RHEL trackers, and distro backport notes. | — | https://www.openssl.org/news/vulnerabilities.html |

## Security Posture Notes

- OpenSSL is one of the clearest first Linux anchors because it is packaged across essentially every major distribution and sits directly on cryptographic, certificate-validation, and TLS trust boundaries.
- Linux packaging introduces an extra documentation problem the KB should eventually model: the same upstream vulnerability may map to different package names, versions, and backport states across Debian, Ubuntu, Red Hat, Alpine, and others.
- This page is intentionally upstream-first for now so the KB has a stable cross-distro reference point without pretending that one version string describes every Linux environment.

## Dependencies of Note

- Distro package trackers for `openssl`, `libssl`, and related subpackages will need separate normalization notes once the Linux section deepens.
- Pages for `curl`, `openssh`, and `nginx` should eventually cross-link here because TLS library patch level often shapes their real-world exposure.

## Open Questions

- What is the cleanest page structure for representing upstream OpenSSL advisories alongside distro-specific backports and package naming differences?
- Which Linux distributions should be treated as first-class coverage targets in the KB's initial distro normalization pass?
- Should future Linux pages add explicit fields for "upstream fixed in" versus "distro patched in" to support site-side filtering?

## Related Pages

- [[homebrew/openssl@3]]
- [[linux/index]]

---
*Last updated: 2026-04-11 | Sources: 3 (upstream repository, OpenSSL security policy, upstream vulnerability history index)*

## Upstream Advisories (selected)

The Linux packaging story for OpenSSL is distro-specific (backports and version
strings differ). Until distro normalization exists, this KB page tracks **upstream
OpenSSL** advisory anchors and fix versions, and expects downstream readers to map
those to their distribution's patched package release notes.

## Recent Upstream Vulnerabilities (2026-04-07 advisory)

| CVE / Issue | Severity | Description | Fixed in (upstream) | Source |
|-------------|----------|-------------|---------------------|--------|
| CVE-2026-31790 | Moderate | Incorrect failure handling in RSA KEM RSASVE encapsulation. If applications use `EVP_PKEY_encapsulate()` with RSA/RSASVE on an attacker-supplied invalid RSA public key **without validating it first**, encapsulation can return success and disclose uninitialized/stale ciphertext buffer contents. Workaround mentioned upstream: validate the public key first via `EVP_PKEY_public_check()` / `EVP_PKEY_public_check_quick()`. | 3.0.20 / 3.3.7 / 3.4.5 / 3.5.6 / 3.6.2 | https://openssl-library.org/news/secadv/20260407.txt |
| CVE-2026-28386 | Low | Out-of-bounds read in AES-CFB-128 on x86_64 with AVX-512 + VAES support when processing partial cipher blocks; may crash (DoS) if over-read hits an unmapped page boundary; advisory notes no info disclosure because over-read bytes are not written to output. TLS/DTLS not affected because they do not use CFB mode. | 3.6.2 | https://openssl-library.org/news/secadv/20260407.txt |

## Notes

- The upstream vulnerability index lists current and historical OpenSSL CVEs by year and branch:
  https://openssl-library.org/news/vulnerabilities/index.html
- The 2026-04-07 upstream advisory describes multiple CVEs; this page currently captures only the two above as an evidence-backed starting point for 2026 tracking.

---
*Last updated: 2026-05-01 | Sources: 2 (OpenSSL upstream vulnerability index; OpenSSL Security Advisory 20260407)*
