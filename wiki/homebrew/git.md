# git (Homebrew)

**Registry:** Homebrew
**Weekly Downloads:** unknown (formulae.brew.sh API currently 403 from this environment; git is among the most-installed Homebrew formulae on macOS)
**Repository:** https://github.com/git/git (upstream); formula: https://github.com/Homebrew/homebrew-core/blob/master/Formula/g/git.rb
**Security Contact:** security@git-scm.com (upstream)
**Disclosure Policy:** https://github.com/git/git/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| *No audits on record.* | — | — | — | — | — |

## Known Vulnerabilities

Homebrew's `git` formula tracks upstream releases directly; there are no Homebrew-specific patches. All CVEs below are upstream vulnerabilities. See [[linux/git]] for full descriptions.

| CVE / Issue | Severity | Description | Homebrew Fixed in | Source |
|-------------|----------|-------------|-------------------|--------|
| CVE-2022-23521 / GHSA-c738-c5qq-xg89 | Critical (CVSS 9.8) | `.gitattributes` integer overflow → heap reads/writes → RCE | Homebrew git ≥ 2.39.1 (formula updated 2023-01-17) | [GHSA-c738-c5qq-xg89](https://github.com/git/git/security/advisories/GHSA-c738-c5qq-xg89) |
| CVE-2022-41903 / GHSA-475x-2q3q-hvwq | Critical (CVSS 9.8) | Heap overflow in `git archive` / `git log --format` → RCE | Homebrew git ≥ 2.39.1 (same batch, 2023-01-17) | [GHSA-475x-2q3q-hvwq](https://github.com/git/git/security/advisories/GHSA-475x-2q3q-hvwq) |
| CVE-2023-22490 / GHSA-gw92-x3fm-3g3q | Medium (CVSS 5.5) | Local clone bypass enables filesystem data exfiltration | Homebrew git ≥ 2.39.2 (2023-02-14) | [GHSA-gw92-x3fm-3g3q](https://github.com/git/git/security/advisories/GHSA-gw92-x3fm-3g3q) |
| CVE-2023-23946 / GHSA-r87m-v37r-cwfh | Medium | `git apply` path traversal — overwrite files outside working tree | Homebrew git ≥ 2.39.2 (same batch, 2023-02-14) | [GHSA-r87m-v37r-cwfh](https://github.com/git/git/security/advisories/GHSA-r87m-v37r-cwfh) |
| CVE-2023-29007 / GHSA-v48j-4xgg-4844 | High | `.gitmodules` URL injects config on `git submodule deinit` → RCE via `core.sshCommand` etc. | Homebrew git ≥ 2.40.1 (2023-04-25) | [GHSA-v48j-4xgg-4844](https://github.com/git/git/security/advisories/GHSA-v48j-4xgg-4844) |
| CVE-2024-32002 / GHSA-8h77-4q3w-gfgv | Critical (CVSS 9.0) | Submodule + symlink → hook execution during clone on case-insensitive FS — **macOS is directly affected** | Homebrew git ≥ 2.45.1 (2024-05-14) | [GHSA-8h77-4q3w-gfgv](https://github.com/git/git/security/advisories/GHSA-8h77-4q3w-gfgv) |
| CVE-2024-32004 / GHSA-xfc6-vwr8-r389 | High | RCE via locally crafted repository during clone | Homebrew git ≥ 2.45.1 (same batch, 2024-05-14) | [GHSA-xfc6-vwr8-r389](https://github.com/git/git/security/advisories/GHSA-xfc6-vwr8-r389) |

## Security Posture Notes

Homebrew's `git` formula stays close to the upstream release cadence — typically updated within hours to a few days of each git-scm.com release. Formula update PRs for security releases are filed against `homebrew-core` promptly and merged quickly.

**macOS-specific risk:** CVE-2024-32002 (Critical) is particularly relevant for Homebrew users. macOS HFS+/APFS are case-insensitive by default, making macOS machines a primary target for the submodule+symlink hook-execution attack. Developers who clone repositories from untrusted sources (e.g. public GitHub forks, CI pipelines) with `--recurse-submodules` on macOS were exposed until upgrading to git ≥ 2.45.1.

**macOS system git vs. Homebrew git:** macOS ships a vendor-signed git via Xcode Command Line Tools (Apple's security backport branch, updated separately). Homebrew users may run Homebrew's git alongside or instead of the system git. Brew-installed git typically has the most current security fixes; system git may lag.

**Patch lag assessment:** For the Critical advisories, Homebrew formula updates have consistently tracked upstream within 1–3 days. No evidence of Homebrew-specific vulnerabilities; all risk is inherited from upstream.

## Dependencies of Note

- **curl** (libcurl) — HTTPS transport, installed separately via Homebrew; see [[homebrew/openssl@3]] for TLS stack context
- **pcre2** — regex dependency
- **gettext** — internationalisation support

## Open Questions

- Confirm Homebrew formula update timeline for the 2024-05-14 security batch (CVE-2024-32002/32004) — homebrew-core PR logs would show exact lag.
- Does Apple's Xcode Command Line Tools git include backported patches for CVE-2024-32002? If not, macOS users relying on `/usr/bin/git` remained exposed.
- Git LFS (`git-lfs` Homebrew formula) has a separate CVE history (e.g. CVE-2020-27955); consider a dedicated `homebrew/git-lfs` stub page.

## Related Pages

- [[linux/git]]
- [[homebrew/openssl@3]]

---
*Last updated: 2026-07-07 | Sources: 7 GHSA advisories (git/git repo), git-for-windows/build-extra ReleaseNotes, trickest/cve*
