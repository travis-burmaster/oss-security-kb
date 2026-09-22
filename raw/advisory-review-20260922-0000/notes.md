# Advisory Review — 2026-09-22

## Session

- Date: 2026-09-22
- Targets: Maven/Java ecosystem — logback-classic, okhttp
- OSV.dev: blocked (HTTP 403) — not used
- Maven Central download stats API: blocked — marked "unknown" on all new pages

## Sources Consulted

### ch.qos.logback:logback-classic

- GHSA-vmfg-rjjm-rjrj.json — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/06/GHSA-vmfg-rjjm-rjrj/GHSA-vmfg-rjjm-rjrj.json
  → CVE-2017-5929, Critical CVSS 9.8, deserialization RCE in SocketServer, fixed 1.2.0; GitHub-reviewed

- GHSA-668q-qrv7-99fm.json — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/12/GHSA-668q-qrv7-99fm/GHSA-668q-qrv7-99fm.json
  → CVE-2021-42550, Moderate CVSS 6.6 AV:N/AC:H/PR:H, JNDI config code loading, fixed 1.2.9; GitHub-reviewed

- GHSA-vmq6-5m68-f53m.json — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/11/GHSA-vmq6-5m68-f53m/GHSA-vmq6-5m68-f53m.json
  → CVE-2023-6378, High AV:L/AC:L/PR:N/UI:N/S:C/A:H, receiver serialization DoS, affects <1.2.13 / 1.3.x<1.3.12 / 1.4.x<1.4.12; GitHub-reviewed

- GHSA-9mh8-hq67-v26g.json — https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/08/GHSA-9mh8-hq67-v26g/GHSA-9mh8-hq67-v26g.json
  → CVE-2026-19880, Moderate CWE-22 path traversal, MDC-discriminator → FileAppender path injection, affects 0.9.14–1.6.2, fixed 1.6.3; NOT yet GitHub-reviewed (unreviewed advisory)

Search used: mcp__github__search_code query="logback-classic GHSA repo:github/advisory-database"

### com.squareup.okhttp3:okhttp

- GHSA-4hc2-jh7r-wrc3.json — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-4hc2-jh7r-wrc3/GHSA-4hc2-jh7r-wrc3.json
  → CVE-2016-2402, Moderate CVSS 5.9 AV:N/AC:H, certificate pinning bypass via non-pinned CA in chain, affects <2.7.4 and 3.x<3.1.2; GitHub-reviewed

- GHSA-3cqm-mf7h-prrj.json — https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-3cqm-mf7h-prrj/GHSA-3cqm-mf7h-prrj.json
  → High CVSS 7.5 AV:N, Android hostname verification bypass (OkHostnameVerifier.verifyHostName), affects <4.9.2; Android 8.1–11; GitHub-reviewed

- GHSA-w28c-cgxf-w8gv.json — https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2023/07/GHSA-w28c-cgxf-w8gv/GHSA-w28c-cgxf-w8gv.json
  → CVE-2023-3782, Moderate CVSS 5.9 AV:N/AC:H, Brotli zip-bomb DoS via BrotliInterceptor; NOT yet GitHub-reviewed; no fixed version in advisory

Excluded: GHSA-8fhc-q55v-jvx2 / CVE-2023-0833 — Red Hat AMQ-Streams product advisory referencing OkHttp; AV:L local-only; Red Hat-specific product issue, not a direct okhttp package advisory; not mapped.

Search used: mcp__github__search_code query="okhttp3 GHSA repo:github/advisory-database"

## Notes

- logback GHSA-vmfg-rjjm-rjrj was the first search result but the fetched content described CVE-2017-5929 (deserialization in SocketServer/RemoteStreamAppenderClient) — data confirms Critical CVSS 9.8.
- logback CVE-2021-42550 (JNDI config injection) is frequently conflated with Log4Shell severity; the GHSA shows Moderate CVSS 6.6 AV:N/AC:H/PR:H — requires attacker already having config write access, making exploitation a separate privilege issue entirely.
- okhttp advisory GHSA-3cqm-mf7h-prrj has no CVE alias in the GHSA JSON; it is referenced in NVD as CVE-2021-0341 (Android platform assignment).
- Brotli DoS GHSA-w28c-cgxf-w8gv: no fixed version listed — upstream issue #7738 would need to be checked for resolution status. Mapped as-is with open question.
