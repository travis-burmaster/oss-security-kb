# Advisory Review Notes — 2026-09-04

## Target: go/github.com/nats-io/nats-server

### Sources consulted

- GitHub advisory database search: `nats-server repo:github/advisory-database path:advisories/github-reviewed` (33 results)
- GHSA-55h8-8g96-x4hj (CVE-2026-33246) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-55h8-8g96-x4hj/GHSA-55h8-8g96-x4hj.json
- GHSA-fhg8-qxh5-7q3w (CVE-2025-30215) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/04/GHSA-fhg8-qxh5-7q3w/GHSA-fhg8-qxh5-7q3w.json
- GHSA-vpjc-4jcv-jc29 (CVE-2022-28357) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/09/GHSA-vpjc-4jcv-jc29/GHSA-vpjc-4jcv-jc29.json
- GHSA-3f24-pcvm-5jqc (CVE-2026-33248) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-3f24-pcvm-5jqc/GHSA-3f24-pcvm-5jqc.json
- GHSA-4frv-5fj6-4p25 (CVE-2023-47090, withdrawn) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/10/GHSA-4frv-5fj6-4p25/GHSA-4frv-5fj6-4p25.json
- GHSA-62mh-w5cv-p88c (CVE-2021-3127) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-62mh-w5cv-p88c/GHSA-62mh-w5cv-p88c.json
- GHSA-qrvq-68c2-7grw (CVE-2026-27571) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/02/GHSA-qrvq-68c2-7grw/GHSA-qrvq-68c2-7grw.json
- GHSA-gwj5-3vfq-q992 (CVE-2020-28466) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/05/GHSA-gwj5-3vfq-q992/GHSA-gwj5-3vfq-q992.json
- GHSA-fcjp-h8cc-6879 (CVE-2026-33215) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-fcjp-h8cc-6879/GHSA-fcjp-h8cc-6879.json
- GHSA-jp4j-47f9-2vc3 (CVE-2019-13126) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/05/GHSA-jp4j-47f9-2vc3/GHSA-jp4j-47f9-2vc3.json
- GHSA-vprv-35vv-q339 (CVE-2026-33218) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-vprv-35vv-q339/GHSA-vprv-35vv-q339.json
- GHSA-9r5x-fjv3-q6h4 (CVE-2021-3127, withdrawn dupe) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-9r5x-fjv3-q6h4/GHSA-9r5x-fjv3-q6h4.json
- GHSA-52jh-2xxh-pwh6 (CVE-2026-29785) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-52jh-2xxh-pwh6/GHSA-52jh-2xxh-pwh6.json
- GHSA-jxxm-27vp-c3m5 (CVE-2026-33217) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-jxxm-27vp-c3m5/GHSA-jxxm-27vp-c3m5.json
- GHSA-h2fg-54x9-5qhq (CVE-2020-26521) — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/02/GHSA-h2fg-54x9-5qhq/GHSA-h2fg-54x9-5qhq.json
- pkg.go.dev: https://pkg.go.dev/github.com/nats-io/nats-server/v2 — latest v2.14.6 (2026-08-27)
- NATS GitHub repository: https://github.com/nats-io/nats-server

### Advisories confirmed (14 mapped, 2 withdrawn-duplicates noted)

| CVE | GHSA | Severity | Fixed |
|-----|------|----------|-------|
| CVE-2019-13126 | GHSA-jp4j-47f9-2vc3 | High CVSS 7.5 | ≥ 2.2.0 |
| CVE-2020-26521 | GHSA-h2fg-54x9-5qhq | High CVSS 7.5 | nats-server ≥ 2.1.9 |
| CVE-2020-28466 | GHSA-gwj5-3vfq-q992 | High CVSS 7.5 | ≥ 2.2.0 |
| CVE-2021-3127 | GHSA-62mh-w5cv-p88c | Critical | nats-server ≥ 2.2.0 |
| CVE-2022-28357 | GHSA-vpjc-4jcv-jc29 | Critical CVSS 9.8 | ≥ 2.7.4 |
| CVE-2023-47090 | GHSA-fr2g-9hjm-wr23 (primary) | Moderate | 2.9.23 / 2.10.2 |
| CVE-2025-30215 | GHSA-fhg8-qxh5-7q3w | Critical | 2.10.27 / 2.11.1 |
| CVE-2026-27571 | GHSA-qrvq-68c2-7grw | Moderate | 2.11.12 / 2.12.3 |
| CVE-2026-29785 | GHSA-52jh-2xxh-pwh6 | High | 2.11.14 / 2.12.5 |
| CVE-2026-33215 | GHSA-fcjp-h8cc-6879 | Moderate | 2.11.15 / 2.12.6 |
| CVE-2026-33217 | GHSA-jxxm-27vp-c3m5 | High | 2.11.15 / 2.12.6 |
| CVE-2026-33218 | GHSA-vprv-35vv-q339 | High | 2.11.15 / 2.12.6 |
| CVE-2026-33246 | GHSA-55h8-8g96-x4hj | Moderate | 2.11.15 / 2.12.6 |
| CVE-2026-33248 | GHSA-3f24-pcvm-5jqc | Moderate | 2.11.15 / 2.12.6 |

Withdrawn/duplicate advisories noted but not cited as primary:
- GHSA-9r5x-fjv3-q6h4 (CVE-2021-3127 dupe)
- GHSA-4frv-5fj6-4p25 (CVE-2023-47090 dupe of GHSA-fr2g-9hjm-wr23)

Total GHSA records for nats-server query: 33 (not all reviewed — remaining may cover nats-io/jwt, nats-io/nats.go client, and older versions; or be companion-package advisories).

### OSV.dev
Blocked (HTTP 403). Not consulted.

### Registry/version metadata
- latest stable: v2.14.6 (2026-08-27)
- pkg.go.dev importers: 0 listed (server binary; not imported as a library)
- CNCF sandbox→incubating project; ~15K+ GitHub stars
- Weekly download stats not available (server binary distributed via direct download / Docker / Helm)
