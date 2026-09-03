# Advisory Review — 2026-09-03 ~08:00 UTC

## Targets

- linux/xz-utils (new page)
- linux/polkit (new page)

## Sources consulted

### xz-utils
- mcp__github__search_code query: `CVE-2024-3094 repo:github/advisory-database` → found GHSA-rxwq-x6h5-x525 (unreviewed/2024/03/)
- WebFetch: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2024/03/GHSA-rxwq-x6h5-x525/GHSA-rxwq-x6h5-x525.json — CVE-2024-3094 Critical CVSS 9.8, xz 5.6.0+, confirmed
- mcp__github__search_code query: `CVE-2022-1271 xz xzgrep repo:github/advisory-database` → found GHSA-jrpw-543v-8r62 (unreviewed/2022/09/)
- WebFetch: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/09/GHSA-jrpw-543v-8r62/GHSA-jrpw-543v-8r62.json — CVE-2022-1271 High CVSS 7.2, xzgrep arbitrary file write, confirmed
- Openwall disclosure: https://www.openwall.com/lists/oss-security/2024/03/29/4 (original CVE-2024-3094 post by Andres Freund)

### polkit
- mcp__github__search_code query: `CVE-2021-4034 polkit pkexec repo:github/advisory-database` → found GHSA-qgr2-xgqv-24x8 (unreviewed/2022/01/)
- WebFetch: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/01/GHSA-qgr2-xgqv-24x8/GHSA-qgr2-xgqv-24x8.json — CVE-2021-4034 High CVSS 7.8 AV:L, pkexec local root, CISA KEV, confirmed
- mcp__github__search_code query: `CVE-2021-3560 polkit repo:github/advisory-database` → found GHSA-7c49-j253-wq5r (unreviewed/2022/02/)
- WebFetch: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/02/GHSA-7c49-j253-wq5r/GHSA-7c49-j253-wq5r.json — CVE-2021-3560 High, D-Bus bypass → root, CISA KEV, confirmed
- Additional historical records noted in Security Posture Notes (CVE-2019-6133, CVE-2018-19788) not yet mapped to table rows; deferred to future pass.

## GHSA records confirmed for this pass

| GHSA | CVE | Package | Severity |
|------|-----|---------|----------|
| GHSA-rxwq-x6h5-x525 | CVE-2024-3094 | xz-utils | Critical CVSS 9.8 |
| GHSA-jrpw-543v-8r62 | CVE-2022-1271 | xz-utils (xzgrep) | High CVSS 7.2 |
| GHSA-qgr2-xgqv-24x8 | CVE-2021-4034 | polkit (pkexec) | High CVSS 7.8 |
| GHSA-7c49-j253-wq5r | CVE-2021-3560 | polkit | High CVSS 7.8 |

## URLs blocked / unavailable

- https://api.osv.dev — HTTP 403 (network policy; known constraint per CLAUDE.md)
- https://formulae.brew.sh — not consulted this pass (Linux-only targets)
