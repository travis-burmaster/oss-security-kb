# Advisory Review Notes — 2026-07-22

**Pass:** 2026-07-22 automated nightly advisory-review
**Targets:** kubernetes/ingress-nginx, go/github.com/jackc/pgx
**OSV.dev:** HTTP 403 (blocked); all advisory data sourced from github/advisory-database via mcp__github__search_code + WebFetch on raw.githubusercontent.com

---

## Target 1: kubernetes/ingress-nginx

**Search queries used:**
- `CVE-2025-1974 ingress-nginx repo:github/advisory-database` → GHSA-mgvx-rpfc-9mpv
- `CVE-2025-1097 ingress-nginx repo:github/advisory-database` → GHSA-823x-fv5p-h7hw
- `CVE-2025-1098 ingress-nginx repo:github/advisory-database` → GHSA-vg63-w3p9-jc9m
- `CVE-2025-24514 ingress-nginx repo:github/advisory-database` → GHSA-fwwp-xcxw-39vq
- `CVE-2024-7646 ingress-nginx repo:github/advisory-database` → GHSA-qx8j-xj5q-v7r3
- `CVE-2023-5043 ingress-nginx repo:github/advisory-database` → GHSA-5wj4-wffq-3378
- `CVE-2023-5044 ingress-nginx repo:github/advisory-database` → GHSA-fp9f-44c2-cw27
- `CVE-2022-4886 ingress-nginx repo:github/advisory-database` → GHSA-gvrm-w2f9-f77q
- `CVE-2021-25742 ingress-nginx repo:github/advisory-database` → GHSA-4pp2-3663-mcw8
- `CVE-2021-25745 ingress-nginx repo:github/advisory-database` → GHSA-pvmg-xgmx-9mxh
- `CVE-2021-25746 ingress-nginx repo:github/advisory-database` → GHSA-79xv-4hmm-pw72
- `CVE-2021-25748 ingress-nginx repo:github/advisory-database` → GHSA-863x-868h-968x

**Advisory URLs fetched:**
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/03/GHSA-mgvx-rpfc-9mpv/GHSA-mgvx-rpfc-9mpv.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/03/GHSA-823x-fv5p-h7hw/GHSA-823x-fv5p-h7hw.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/03/GHSA-vg63-w3p9-jc9m/GHSA-vg63-w3p9-jc9m.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/03/GHSA-fwwp-xcxw-39vq/GHSA-fwwp-xcxw-39vq.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2024/08/GHSA-qx8j-xj5q-v7r3/GHSA-qx8j-xj5q-v7r3.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/10/GHSA-gvrm-w2f9-f77q/GHSA-gvrm-w2f9-f77q.json

**Advisories confirmed (12):**
1. GHSA-mgvx-rpfc-9mpv / CVE-2025-1974 — Critical CVSS 9.8 — Unauthenticated RCE via admission webhook — fixed 1.11.5 / 1.12.1
2. GHSA-vg63-w3p9-jc9m / CVE-2025-1098 — Critical CVSS 9.9 — mirror annotation config injection → RCE — fixed 1.11.5 / 1.12.1
3. GHSA-823x-fv5p-h7hw / CVE-2025-1097 — Critical CVSS 9.1 — auth-tls-match-cn annotation config injection → RCE — fixed 1.11.5 / 1.12.1
4. GHSA-fwwp-xcxw-39vq / CVE-2025-24514 — Critical CVSS 9.1 — auth-url annotation config injection → RCE — fixed 1.11.5 / 1.12.1
5. GHSA-qx8j-xj5q-v7r3 / CVE-2024-7646 — Critical CVSS 9.9 — annotation validation bypass → command injection — unreviewed, no specific version in advisory
6. GHSA-5wj4-wffq-3378 / CVE-2023-5043 — High CVSS 7.6 — configuration-snippet annotation injection → commands + credential theft — fixed v1.9.0 + --enable-annotation-validation flag
7. GHSA-fp9f-44c2-cw27 / CVE-2023-5044 — High — permanent-redirect annotation injection — fixed v1.9.0
8. GHSA-gvrm-w2f9-f77q / CVE-2022-4886 — High CVSS 8.1 — path sanitization bypass via log_format — fixed 1.8.0
9. GHSA-4pp2-3663-mcw8 / CVE-2021-25742 — Moderate — custom snippets → cluster secrets — fixed v1.1.0
10. GHSA-pvmg-xgmx-9mxh / CVE-2021-25745 — High — path field → controller credential disclosure — fixed v1.2.0
11. GHSA-79xv-4hmm-pw72 / CVE-2021-25746 — High — metadata.annotations → credential disclosure — fixed v1.2.0
12. GHSA-863x-868h-968x / CVE-2021-25748 — Moderate — path sanitization newline bypass → credential disclosure — fixed v1.2.0

---

## Target 2: go/github.com/jackc/pgx

**Search queries used:**
- `CVE-2024-27289 pgx repo:github/advisory-database` → GHSA-m7wr-2xf7-cm9p
- `CVE-2024-27304 pgx repo:github/advisory-database` → GHSA-mrww-27vc-gghv
- `CVE-2026-33815 pgx repo:github/advisory-database` → GHSA-xgrm-4fwx-7qm8
- `CVE-2026-33816 pgx repo:github/advisory-database` → GHSA-9jj7-4m8r-rfcm
- `jackc pgx repo:github/advisory-database path:advisories/github-reviewed` → full list (9 results; GHSA-x6gf-mpr2-68h6 is WITHDRAWN)

**Advisory URLs fetched:**
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/07/GHSA-fqpg-rq76-99pq/GHSA-fqpg-rq76-99pq.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-jqcq-xjh3-6g23/GHSA-jqcq-xjh3-6g23.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/04/GHSA-j88v-2chj-qfwx/GHSA-j88v-2chj-qfwx.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/03/GHSA-x6gf-mpr2-68h6/GHSA-x6gf-mpr2-68h6.json (WITHDRAWN — excluded)

**Advisories confirmed (7):**
1. GHSA-m7wr-2xf7-cm9p / CVE-2024-27289 — Moderate — SQL injection via line comment in simple protocol (v4 only) — fixed v4.18.2
2. GHSA-mrww-27vc-gghv / CVE-2024-27304 — Moderate — SQL injection via protocol message size integer overflow (v4 + v5) — fixed v4.18.2 / v5.5.4
3. GHSA-fqpg-rq76-99pq — Moderate — Pipeline panic DoS (v5, PgConn busy/closed) — no CVE — fixed v5.5.2
4. GHSA-jqcq-xjh3-6g23 / CVE-2026-32286 — High CVSS 7.5 — pgproto3/v2 DataRow.Decode negative field length panic DoS from malicious server — fixed pgproto3/v2 > 2.3.3
5. GHSA-xgrm-4fwx-7qm8 / CVE-2026-33815 — High — memory-safety vulnerability in pgx/v5 < 5.9.0 — fixed v5.9.0
6. GHSA-9jj7-4m8r-rfcm / CVE-2026-33816 — High — second memory-safety vulnerability in pgx/v5 < 5.9.0 — fixed v5.9.0
7. GHSA-j88v-2chj-qfwx / CVE-2026-41889 — Moderate — SQL injection via dollar-quoted string literal placeholder confusion in simple protocol (v5 fixed v5.9.2; v4/v3 EOL) — fixed v5.9.2

**Dropped/excluded:** GHSA-x6gf-mpr2-68h6 (WITHDRAWN — duplicate of GHSA-jqcq-xjh3-6g23)

---

## Targets Considered but Not Selected

- `zip` (Rust crate): initial search for RustSec advisories in `crates/zip/` path returned 0 results. No confirmed RUSTSEC advisory in the advisory-db crates/zip directory at time of pass. Dropped.
