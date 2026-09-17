# Advisory Review — 2026-09-17

## Targets selected

1. **linux/php** — Linux ecosystem; PHP 8.x interpreter; 19 Linux pages pre-pass (under-covered relative to npm/Python)
2. **kubernetes/prometheus** — Kubernetes ecosystem; CNCF-graduated monitoring platform; 12 Kubernetes pages pre-pass

## Sources consulted

### PHP

- `https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS` — PHP 8.3 release notes (security fixes 8.3.6 through 8.3.34); primary source for all CVEs except CVE-2024-4577
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/05/GHSA-vxpp-6299-mxw3/GHSA-vxpp-6299-mxw3.json` — GHSA record for CVE-2024-4577 (CGI argument injection / RCE)
- `https://www.php.net/` — blocked (HTTP 403 via network policy)
- `https://services.nvd.nist.gov/` — blocked (HTTP 403 via network policy); CVSS scores not confirmed for most entries
- `https://github.com/php/php-src/blob/master/SECURITY.md` — security policy reference (not fetched, URL from repo knowledge)

### Prometheus

- `mcp__github__search_code` on `repo:github/advisory-database` with queries `prometheus/prometheus`, `prom/prometheus` — identified candidate GHSA files
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/10/GHSA-4v48-4q5m-8vx4/GHSA-4v48-4q5m-8vx4.json` — bcrypt cache poisoning (High CVSS 8.8)
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/08/GHSA-8rm2-7qqf-34qm/GHSA-8rm2-7qqf-34qm.json` — CVE-2026-42154 remote read DoS
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/08/GHSA-wg65-39gg-5wfj/GHSA-wg65-39gg-5wfj.json` — CVE-2026-42151 Azure AD credential exposure
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/07/GHSA-vffh-x6r8-xx99/GHSA-vffh-x6r8-xx99.json` — CVE-2026-40179 stored XSS (new UI)
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/07/GHSA-fw8g-cg8f-9j28/GHSA-fw8g-cg8f-9j28.json` — CVE-2026-44903 stored XSS (old UI)
- `https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2019/03/GHSA-3m87-5598-2v4f/GHSA-3m87-5598-2v4f.json` — CVE-2019-3826 (withdrawn; excluded)
- `https://api.github.com/repos/prometheus/prometheus/releases` — blocked (HTTP 403)

## Blocked sources

- `https://api.osv.dev` — HTTP 403 (network policy)
- `https://www.php.net/` — HTTP 403 (network policy)
- `https://services.nvd.nist.gov/` — HTTP 403 (network policy)
- `https://api.github.com/repos/prometheus/prometheus/releases` — HTTP 403

## Findings summary

| Package | New CVEs | Severity breakdown | Source |
|---------|----------|--------------------|--------|
| linux/php | 22 | 2 Critical, 9 High, 11 Moderate | PHP-8.3/NEWS + GHSA |
| kubernetes/prometheus | 5 (1 withdrawn excluded) | 3 High, 2 Moderate | github/advisory-database |

## Pages created

- `wiki/linux/php.md`
- `wiki/kubernetes/prometheus.md`

## Pages updated

- `wiki/linux/index.md` (19→20 entries)
- `wiki/kubernetes/index.md` (12→13 entries)
- `wiki/index.md` (291→293 pages, Linux 19→20, Kubernetes 12→13, date updated)
- `wiki/log.md` (new entry prepended)
