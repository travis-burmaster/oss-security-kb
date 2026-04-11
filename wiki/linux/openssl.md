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
