# xz-utils (Linux)

**Registry:** distro (xz-utils on Debian/Ubuntu; xz on Fedora/RHEL/Alpine)
**Weekly Downloads:** N/A — distro package (pre-installed on all major Linux distributions; no registry download count)
**Repository:** https://github.com/tukaani-project/xz
**Security Contact:** https://github.com/tukaani-project/xz/security
**Disclosure Policy:** https://github.com/tukaani-project/xz/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-3094 / GHSA-rxwq-x6h5-x525 | Critical (CVSS 9.8 AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H) | **XZ Utils supply-chain backdoor**: Malicious code was covertly embedded in xz-utils upstream tarballs for versions 5.6.0 and 5.6.1 by the "JiaT75" contributor (a.k.a. Jia Tan), who had been systematically building trust in the project since 2021. The tarballs contained extra `.m4` autoconf files with obfuscated build instructions that extracted a prebuilt object file from test archives and injected it into `liblzma` during compilation. On glibc-based Linux systems where `sshd` is linked against `liblzma` via systemd (primarily Debian unstable, Fedora 41/Rawhide, openSUSE Tumbleweed, and Arch Linux during a brief window), the modified library intercepted `RSA_public_decrypt`, enabling an attacker possessing a specific hard-coded Ed448 private key to authenticate to any vulnerable sshd instance — effectively unauthenticated RCE as root. Discovered 2024-03-29 by Andres Freund (Microsoft) while investigating unexpected sshd CPU usage. Scope was limited to pre-release/rolling-release distro branches; stable releases (Debian stable, Ubuntu LTS, RHEL) were never affected. | Roll back to 5.4.6 (stable branch) or upgrade to ≥ 5.4.7 / 5.6.2 (sanitized rebuild); all affected distros issued emergency updates within 24 hours of disclosure | [GHSA-rxwq-x6h5-x525](https://github.com/advisories/GHSA-rxwq-x6h5-x525) |
| CVE-2022-1271 / GHSA-jrpw-543v-8r62 | High (CVSS 7.2) | **xzgrep arbitrary file overwrite via crafted filename**: The `xzgrep` utility does not properly validate filenames passed to it for processing. An attacker who can control a filename processed by `xzgrep` (e.g., via a batch job, CI pipeline, or automated file-processing workflow) can craft a filename containing embedded newlines to cause `xzgrep` to write attacker-controlled data to an arbitrary file on the filesystem. Parallel flaw to the same issue in GNU gzip's `zgrep` (both were patched simultaneously). | xz 5.2.6 / 5.4.1 | [GHSA-jrpw-543v-8r62](https://github.com/advisories/GHSA-jrpw-543v-8r62) |

## Security Posture Notes

xz-utils provides the `xz` / `lzma` compression utilities and the associated shared library `liblzma`. It is pre-installed on effectively every major Linux distribution and embedded in countless build toolchains and CI pipelines. `liblzma` is a transitive dependency of systemd, which in turn links into OpenSSH's `sshd` on systemd-based distributions — giving liblzma unusually deep coupling to the network-facing daemon on mainstream Linux systems.

**CVE-2024-3094 (XZ backdoor) context — significance and scope:**
This was one of the most sophisticated supply-chain attacks ever documented in open source software. Key forensic details:
- The attacker ("Jia Tan") invested approximately two years building community credibility before executing the backdoor.
- The malicious payload was injected exclusively via the release *tarball*, not the Git repository — bypassing most source-integrity workflows that compare only against the upstream tree.
- The backdoor specifically targeted glibc/systemd-linked sshd. On systems without systemd (or where sshd is not systemd-linked), the backdoor code was inert.
- Stable distro releases (Debian stable, Ubuntu 22.04/24.04 LTS, RHEL 8/9) were never shipped the backdoor versions. The risk window was primarily in bleeding-edge/testing branches.
- The original tukaani-project xz repository was subsequently cleaned; control was returned to the original maintainer (Lasse Collin). The current repository at https://github.com/tukaani-project/xz is considered safe.

**Build-system attack vector**: The backdoor is notable for using autoconf `.m4` macros in the tarball (absent from the Git history) to extract and inject prebuilt object files during `./configure` / `make`. This technique could bypass source-code review and many supply-chain security controls focused on source tree integrity.

**CVE-2022-1271 context**: This vulnerability affects `xzgrep` when it processes files with specially crafted names. In most deployment contexts `xzgrep` operates on user-supplied file arguments and is therefore low-risk in interactive use; the risk is elevated in automated pipelines that pass attacker-influenced filenames to `xzgrep` without prior sanitization.

No formal external security audit of xz-utils is on record. The project gained a SECURITY.md and GitHub advisory policy after the 2024 backdoor incident.

## Dependencies of Note

- **liblzma**: The shared library component; the vector for CVE-2024-3094's sshd compromise on systemd-based distros.
- **systemd**: Links against liblzma, extending its blast radius. See `[[linux/systemd]]`.
- **openssh-server** (systemd-linked): Was the targeted victim of the CVE-2024-3094 backdoor. See `[[linux/openssh]]`.

## Open Questions

- Enumerate any 2024–2026 advisories issued post-CVE-2024-3094 by the new maintainer team at https://github.com/tukaani-project/xz/security/advisories.
- Confirm exact distro backport fixed package versions for CVE-2022-1271 across Debian 9/10, Ubuntu 20.04/22.04, and RHEL 7/8 streams.
- Determine whether a RUSTSEC advisory or other ecosystem-specific advisory was issued for Rust or Go crates that vendor liblzma.

## Related Pages

- [[linux/openssh]]
- [[linux/systemd]]
- [[linux/index]]

---
*Last updated: 2026-09-03 | Sources: 2 GHSA records (GHSA-rxwq-x6h5-x525, GHSA-jrpw-543v-8r62 via github/advisory-database); openwall disclosure https://www.openwall.com/lists/oss-security/2024/03/29/4*
