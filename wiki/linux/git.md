# git (Linux)

**Registry:** distro (upstream: git-scm.com)
**Weekly Downloads:** N/A — pre-installed on virtually all Linux distributions
**Repository:** https://github.com/git/git
**Security Contact:** security@git-scm.com
**Disclosure Policy:** https://github.com/git/git/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-23521 / GHSA-c738-c5qq-xg89 | Critical (CVSS 9.8) | Integer overflow parsing `.gitattributes` — attacker-controlled heap reads and writes, potential RCE when processing a crafted repo | ≥ 2.30.7 / 2.31.6 / 2.32.5 / 2.33.6 / 2.34.6 / 2.35.6 / 2.36.4 / 2.37.5 / 2.38.3 / 2.39.1 (2023-01-17) | [GHSA-c738-c5qq-xg89](https://github.com/git/git/security/advisories/GHSA-c738-c5qq-xg89) |
| CVE-2022-41903 / GHSA-475x-2q3q-hvwq | Critical (CVSS 9.8) | Heap overflow in `git archive` and `git log --format` — RCE via crafted format string / archive operation | ≥ 2.30.7 (same batch, 2023-01-17) | [GHSA-475x-2q3q-hvwq](https://github.com/git/git/security/advisories/GHSA-475x-2q3q-hvwq) |
| CVE-2023-22490 / GHSA-gw92-x3fm-3g3q | Medium (CVSS 5.5) | Local clone optimisation triggered with non-local transport — `objects/` symlink enables filesystem data exfiltration from victim machine | ≥ 2.30.8 / 2.31.7 / 2.32.6 / 2.33.7 / 2.34.7 / 2.35.7 / 2.36.5 / 2.37.6 / 2.38.4 / 2.39.2 (2023-02-14) | [GHSA-gw92-x3fm-3g3q](https://github.com/git/git/security/advisories/GHSA-gw92-x3fm-3g3q) |
| CVE-2023-23946 / GHSA-r87m-v37r-cwfh | Medium | Path traversal via crafted patch in `git apply` — overwrites files outside the working tree | ≥ 2.30.8 (same batch as CVE-2023-22490, 2023-02-14) | [GHSA-r87m-v37r-cwfh](https://github.com/git/git/security/advisories/GHSA-r87m-v37r-cwfh) |
| CVE-2023-29007 / GHSA-v48j-4xgg-4844 | High | `.gitmodules` URL > 1024 chars exploits `config.c` bug — injects arbitrary config into `$GIT_DIR/config` on `git submodule deinit`, enabling RCE via `core.pager` / `core.sshCommand` | ≥ 2.30.9 / 2.31.8 / 2.32.7 / 2.33.8 / 2.34.8 / 2.35.8 / 2.36.6 / 2.37.7 / 2.38.5 / 2.39.3 / 2.40.1 (2023-04-25) | [GHSA-v48j-4xgg-4844](https://github.com/git/git/security/advisories/GHSA-v48j-4xgg-4844) |
| CVE-2024-32002 / GHSA-8h77-4q3w-gfgv | Critical (CVSS 9.0) | Submodule + symlink combination causes hooks to execute during `git clone --recurse-submodules` on case-insensitive filesystems (macOS, Windows) | ≥ 2.39.4 / 2.40.2 / 2.41.1 / 2.42.2 / 2.43.4 / 2.44.1 / 2.45.1 (2024-05-14) | [GHSA-8h77-4q3w-gfgv](https://github.com/git/git/security/advisories/GHSA-8h77-4q3w-gfgv) |
| CVE-2024-32004 / GHSA-xfc6-vwr8-r389 | High | RCE when cloning a locally crafted repository — attacker-prepared local repo triggers hook execution during clone | ≥ 2.39.4 (same batch as CVE-2024-32002, 2024-05-14) | [GHSA-xfc6-vwr8-r389](https://github.com/git/git/security/advisories/GHSA-xfc6-vwr8-r389) |

*OSV reference: https://osv.dev/list?ecosystem=GIT&q=git*

## Security Posture Notes

Git is developed by an open community coordinated through the git-security@googlegroups.com list. The project maintains a documented security policy at `SECURITY.md`. Security releases are announced on the Git mailing list and mirrored to git-scm.com/downloads, distro security trackers, and GitHub's security advisory feed.

**Distro patch lag:** Major distros (Debian, Ubuntu, RHEL/Fedora, SUSE) typically ship security backports within days of upstream release for stable branches. The January 2023 batch (CVE-2022-23521, CVE-2022-41903) and May 2024 batch (CVE-2024-32002, CVE-2024-32004) received broad distro coverage within 1–2 weeks.

**Attack surface context:** Git is a privileged tool that reads untrusted repository data. The primary threat model is: a developer clones or processes a malicious repository. CI/CD pipelines that clone untrusted repos (e.g. for dependency checking or fork testing) are a high-exposure surface. Hooks executing on `git clone --recurse-submodules` (CVE-2024-32002) represent a supply-chain vector on macOS/Windows.

**Current upstream version:** 2.45.x series as of 2026-07-07. No open Critical or High advisories known post-2024-05-14.

## Dependencies of Note

- **libpcre2** — regex support; no directly inherited CVEs flagged
- **libcurl** — used for HTTPS transport (see [[linux/curl]] for curl's own advisory history)
- **OpenSSL / GnuTLS / Secure Transport** — TLS for HTTPS remotes (see [[linux/openssl]])
- **OpenSSH** — used via `git+ssh://`; SSH agent forwarding through compromised remotes could compound credential exposure

## Open Questions

- CVE-2023-25652 (`git apply --reject` path traversal, fixed v2.40.1): GHSA ID not confirmed; page should be updated once the canonical advisory URL is verified.
- Has any distro shipped a git version containing unfixed Critical/High advisories as of 2026? Check Ubuntu 20.04 LTS (git 2.25.x) patch backport status for CVE-2024-32002.
- Credential helper implementations (git-credential-libsecret, osxkeychain) — separate attack surface not covered here; consider a dedicated review.

## Related Pages

- [[linux/openssh]]
- [[linux/curl]]
- [[linux/openssl]]
- [[homebrew/git]]

---
*Last updated: 2026-07-07 | Sources: 7 GHSA advisories (git/git repo), trickest/cve, git-for-windows/build-extra ReleaseNotes, opencve-kb*
