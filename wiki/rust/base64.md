# base64 (Rust / crates.io)

**Registry:** crates.io
**Weekly Downloads:** 250,390,207 (as of 2026-06-18)
**Repository:** https://github.com/marshallpierce/rust-base64
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| RUSTSEC-2017-0004 / CVE-2017-1000430 / GHSA-x67x-vg9m-65c3 | Critical (CVSS 9.8) | Integer overflow in `encode_config_buf` / `encode_config` when calculating buffer size; unsafe write overflows undersized heap buffer — potential RCE on large inputs | 0.5.2 | [RUSTSEC-2017-0004](https://rustsec.org/advisories/RUSTSEC-2017-0004.html) |

*OSV: https://osv.dev/list?ecosystem=crates.io&q=base64*

## Security Posture Notes

Actively maintained by marshallpierce. Current version is 0.22.1 (June 2026), well past the 0.5.2 fix boundary. No formal SECURITY.md or dedicated security contact exists; issues and PRs on GitHub are the de facto disclosure path.

The single RUSTSEC record is from 2017 and has been resolved for over seven years. The vulnerable `encode_config` / `encode_config_buf` API family was substantially redesigned in subsequent major versions, reducing the blast radius of the original integer-overflow root cause. That said, with approximately 250 million weekly downloads, transitive exposure is very high — any consumer still pinned to a pre-0.5.2 version is at risk of heap corruption on large inputs.

## Dependencies of Note

None flagged.

## Open Questions

- No SECURITY.md or formal vulnerability-reporting path exists: is there an issue template or out-of-band maintainer contact for coordinated disclosure?
- The 2017 advisory names `encode_config_buf` / `encode_config`; confirm whether any decode-path functions (e.g., `decode_config_buf`) carried equivalent arithmetic before the 0.5.2 fix.

## Related Pages

- [[rust/openssl]]
- [[rust/index]]

---
*Last updated: 2026-06-18 | Sources: 1*
