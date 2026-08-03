# vim (Linux)

**Registry:** distro
**Weekly Downloads:** N/A (system package, pre-installed on most Linux distributions; tens of millions of active installs)
**Repository:** https://github.com/vim/vim
**Security Contact:** security@vim.org
**Disclosure Policy:** https://github.com/vim/vim/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-08-03 | oss-security-kb | advisory-mapping | automated | 12 of 174+ confirmed vim/vim GHSA advisories mapped | [github/advisory-database](https://github.com/github/advisory-database) |

*No independent audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2004-1138 / GHSA-jx5v-4rgm-j8mg | High | Modeline code execution — VIM/gVim allows local users to execute arbitrary commands via a crafted modeline using options such as termcap, printdevice, titleold, filetype, syntax, backupext, keymap, patchmode, or langmenu | 6.3 | [GHSA](https://github.com/advisories/GHSA-jx5v-4rgm-j8mg) |
| CVE-2022-0158 / GHSA-72hg-72h4-39fg | Moderate | Heap-based buffer overflow in vim prior to 8.2 — CWE-122; CVSS v3.1 AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N | 8.2 (commit 5f25c38) | [GHSA](https://github.com/advisories/GHSA-72hg-72h4-39fg) |
| CVE-2022-0351 / GHSA-vq66-5g5m-5rgg | High | Access of memory location before start of buffer in vim prior to 8.2 — CWE-786; CVSS v3.1 AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H | 8.2 (commit fe6fb26) | [GHSA](https://github.com/advisories/GHSA-vq66-5g5m-5rgg) |
| CVE-2022-0443 / GHSA-qfh8-x72v-whwp | Critical | Use-after-free in vim prior to 8.2 — CWE-416; locally exploitable via crafted file | 8.2 (commit 9b4a80a) | [GHSA](https://github.com/advisories/GHSA-qfh8-x72v-whwp) |
| CVE-2022-1381 / GHSA-pq29-2m6m-938v | High | Global heap buffer overflow in skip_range in vim prior to 8.2.4763 — CWE-122/CWE-787; CVSS v3.1 AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | 8.2.4763 (commit f50808e) | [GHSA](https://github.com/advisories/GHSA-pq29-2m6m-938v) |
| CVE-2022-2284 / GHSA-8c77-jprp-cxfj | High | Heap-based buffer overflow in vim prior to 9.0 — CWE-122; CVSS v3.1 AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | 9.0 (commit 3d51ce1) | [GHSA](https://github.com/advisories/GHSA-8c77-jprp-cxfj) |
| CVE-2022-2946 / GHSA-qqpf-7vhq-8phw | High | Use-after-free in vim prior to 9.0.0245 — CWE-416; CVSS v3.1 AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | 9.0.0245 (commit adce965) | [GHSA](https://github.com/advisories/GHSA-qqpf-7vhq-8phw) |
| CVE-2022-3705 / GHSA-vwcr-hcq5-36jr | High | Use-after-free in qf_update_buffer (quickfix.c autocmd handler) in vim prior to 9.0.0805 — CWE-416; NVD-scored AV:N (locally triggered in practice) | 9.0.0805 (commit d0fab10) | [GHSA](https://github.com/advisories/GHSA-vwcr-hcq5-36jr) |
| CVE-2023-0433 / GHSA-hv9j-pr23-x4hf | High | Heap-based buffer overflow in vim prior to 9.0.1225 — CWE-122; CVSS v3.1 AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | 9.0.1225 (commit 11977f9) | [GHSA](https://github.com/advisories/GHSA-hv9j-pr23-x4hf) |
| CVE-2023-2610 / GHSA-6v7c-pq5w-2jwg | High | Integer overflow or wraparound in vim prior to 9.0.1532 — CWE-190; CVSS v3.0 AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | 9.0.1532 (commit ab9a2d8) | [GHSA](https://github.com/advisories/GHSA-6v7c-pq5w-2jwg) |
| CVE-2023-4734 / GHSA-424w-j4hf-8cgp | High | Integer overflow or wraparound in vim prior to 9.0.1846 — CWE-190; CVSS v3.0 AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | 9.0.1846 (commit 4c6fe2e) | [GHSA](https://github.com/advisories/GHSA-424w-j4hf-8cgp) |
| CVE-2023-4750 / GHSA-ph6h-mvrc-7rq5 | High | Use-after-free in vim prior to 9.0.1857 — CWE-416; CVSS v3.0 AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H | 9.0.1857 (commit fc68299) | [GHSA](https://github.com/advisories/GHSA-ph6h-mvrc-7rq5) |

*174+ confirmed vim/vim GHSA advisories exist in the database; 788+ total when a broader "vim" keyword search is used. The 12 rows above are a representative sample covering the principal vulnerability classes (heap buffer overflow, use-after-free, integer overflow, modeline code execution) across the 8.x–9.0.x version progression. See the full advisory feed at https://github.com/advisories?query=vim%2Fvim for exhaustive coverage.*

## Security Posture Notes

Vim is pre-installed on virtually every Linux server distribution (RHEL, Ubuntu, Debian, Fedora, Alpine) and is among the most widely installed interactive text editors globally. Its advisory history is among the largest of any open-source project — 174+ confirmed GHSA records from the `vim/vim` repository, with dozens of new CVEs filed each year through GitHub's automated security tooling and community fuzzing.

The overwhelming majority of advisories involve **local exploitation of crafted files**: an attacker causes a victim to open a malicious file in vim, triggering memory corruption in script/buffer/UI subsystems (ex.c, getchar.c, spellfile.c, quickfix.c, etc.). Three primary attack classes:

- **Modelines** (the oldest class): a crafted modeline at the top/bottom of a file can execute arbitrary commands if `modeline` and `modelineexpr` are enabled
- **Ex-mode / script parsing**: heap buffer overflow and integer overflow in ex-commands and the regex engine when processing specially constructed files
- **Autocmds and quickfix**: use-after-free when buffer manipulation triggers autocmd callbacks during script execution

Patch cadence is very high — near-weekly patch releases on the 9.x line, each a single-commit fix propagated from the upstream repository. Stable distribution channels backport critical fixes; rolling-release distributions (Arch, Fedora Rawhide) receive patches within days.

**Key configuration mitigations:**
- `set nomodeline` / `set nomodelieexpr` in `~/.vimrc` prevents the modeline code-execution class
- `vim -Z` (restricted mode) for opening untrusted files
- Keeping the system vim package current; distro backports handle most critical CVEs without requiring a full upstream upgrade

## Dependencies of Note

Vim links against system libc, libncurses, and optionally libpython (if compiled with Python scripting support), libRuby, and libPerl. Exploitation via bundled library CVEs is uncommon; the dominant risk is the editor's own VimL/ex parser subsystems.

## Open Questions

- Map the 2024–2026 advisory cohort (estimated 40+ additional GHSA records in that window)
- Determine which current distro LTS versions ship a patched 9.x vs. a backport-patched older branch
- Confirm Neovim CVE overlap — Neovim forks the same codebase; many but not all vim CVEs apply

## Related Pages

- [[linux/bash]]
- [[linux/index]]

---
*Last updated: 2026-08-03 | Sources: github/advisory-database (174+ vim/vim records; primary GHSA links above)*
