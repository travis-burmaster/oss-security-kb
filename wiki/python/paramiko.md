# Paramiko (python)

**Registry:** PyPI
**Weekly Downloads:** unavailable in this run (PyPIStats returned HTTP 429 on 2026-05-13; do not infer)
**Repository:** https://github.com/paramiko/paramiko
**Security Contact:** GitHub Security Advisories / repository security policy
**Disclosure Policy:** https://github.com/paramiko/paramiko/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-13 | OpenClaw recurring review | package advisory history | public-source curation using OSV.dev, GitHub Advisory Database, public CVE records, upstream changelog, PyPI metadata, repository security policy, and the public OSTIF audit reference for CVE-2026-44405 | 10 OSV records normalized into 6 public vulnerability groups across SSH server-mode authentication state, local private-key file permissions, SSH Terrapin protocol handling, legacy randomness, and the 2026 SHA-1 algorithm record; latest PyPI release observed as 5.0.0 | https://osv.dev/list?ecosystem=PyPI&q=paramiko |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-wqmm-q65g-2hqr / CVE-2008-0299 / PYSEC-2008-8 | High | Legacy `RandomPool` / randomness-state handling could allow one session to obtain sensitive information from another by predicting pool state. | Early 1.7.x fixed/backported; records differ between `1.7.1-3` and `1.7.2` | https://github.com/advisories/GHSA-wqmm-q65g-2hqr |
| GHSA-232r-66cg-79px / CVE-2018-7750 / PYSEC-2018-19 | Critical | SSH server-mode authentication-state flaw: Paramiko could process `channel-open` and other normally post-authentication requests before authentication completed. Upstream changelog explicitly says this affects server mode and not ordinary client use. | 1.17.6, 1.18.5, 2.0.8, 2.1.5, 2.2.3, 2.3.2, 2.4.1 | https://github.com/advisories/GHSA-232r-66cg-79px |
| GHSA-f2j6-wrhh-v25m / CVE-2018-1000805 / PYSEC-2018-69 | High | Separate SSH server-mode authentication bypass where hostile clients could make a Paramiko server believe they were authenticated without valid authentication; advisory text describes possible RCE depending on server behavior. | 2.0.9, 2.1.6, 2.2.4, 2.3.3, 2.4.2 | https://github.com/advisories/GHSA-f2j6-wrhh-v25m |
| GHSA-f8q4-jwww-x3wv / CVE-2022-24302 / PYSEC-2022-166 | High | Race condition between private-key file creation and later mode changes in `PKey.write_private_key_file` could expose newly written private keys to a local attacker who knew the target path. | 2.9.3, 2.10.1 | https://github.com/advisories/GHSA-f8q4-jwww-x3wv |
| GHSA-45x7-px36-x8w8 / CVE-2023-48795 | Medium | SSH Terrapin prefix-truncation attack against SSH channel integrity. For Paramiko, upstream notes impact around encrypt-then-MAC with CBC ciphers in its implemented algorithm set, strict key-exchange cooperation, and `disabled_algorithms` as a mitigation option when upgrade is blocked. | 3.4.0 | https://github.com/advisories/GHSA-45x7-px36-x8w8 |
| GHSA-r374-rxx8-8654 / CVE-2026-44405 | Low | Public advisory says Paramiko through 4.0.0 before commit `a4489456...` allowed the SHA-1 algorithm in `rsakey.py`; references include the public OSTIF audit report and fixing commit. | Commit `a4489456...`; latest PyPI observed as 5.0.0 after advisory publication | https://github.com/advisories/GHSA-r374-rxx8-8654 |

## Security Posture Notes

- Paramiko is an SSH2 protocol implementation, so deployment role matters: SSH server-mode applications face different trust boundaries than client-only automation scripts.
- The two 2018 authentication-bypass advisories are adjacent but distinct server-mode state-machine issues; do not collapse them into one generic record when assessing old deployments.
- Local key-management code should treat `PKey.write_private_key_file` history as a reminder to create private-key material with restrictive permissions atomically, especially in shared directories.
- Terrapin is a protocol-level SSH issue rather than a Paramiko-only parser bug; mitigation depends on peer support for strict key exchange or disabling affected algorithm combinations until upgrades are possible.
- The 2026 SHA-1 record is public and low severity in GitHub's advisory record; this KB entry does not add exploit claims beyond the advisory, public audit reference, and fixing commit.
- PyPI latest release during this pass was `5.0.0` (2026-05-09), while public OSV / GHSA fixed-version metadata for CVE-2026-44405 currently names the fixing commit rather than a normalized first patched version.

## Dependencies of Note

- `cryptography` is the major crypto backend dependency and should be considered when assessing algorithm support and deprecation behavior.
- SSH server deployments should review application authorization after Paramiko reports a user as authenticated; Paramiko library fixes do not replace application-level access-control checks.
- SFTP / key-writing workflows should audit filesystem permissions and path control separately from network SSH protocol posture.

## Open Questions

- Should future KB passes split Paramiko client, server, SFTP, and key-management surfaces into component-level notes?
- Has the public OSTIF audit produced additional non-CVE hardening changes worth summarizing once upstream release notes settle after 5.0.0?
- Which popular automation tools embed Paramiko server mode, if any, and therefore remain exposed to old 2018 server-mode bug classes when pinned to legacy versions?

## Related Pages

- [[python/cryptography]]
- [[python/requests]]
- [[python/twisted]]
- [[python/index]]

---
*Last updated: 2026-05-13 | Sources: 7 (OSV package query, GitHub Advisory Database / GHSA records, public CVE records, upstream changelog, PyPI metadata, repository security policy, and public OSTIF audit reference for CVE-2026-44405)*
