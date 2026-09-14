# Advisory Review Notes — 2026-09-14

## Pass summary

- **Date:** 2026-09-14
- **Target:** go/github.com/nats-io/nats-server (NATS messaging server)
- **Ecosystems:** Go
- **OSV.dev:** HTTP 403 (blocked); all advisory content sourced from github/advisory-database via mcp__github__search_code + WebFetch on raw.githubusercontent.com

## URLs consulted

### Advisory database search
- mcp__github__search_code query: `nats-server nats-io repo:github/advisory-database path:advisories` → 33 total results
- mcp__github__search_code query: `nats-io/nats-server repo:github/advisory-database "go"` → 33 total results
- mcp__github__search_code query: `nats-io repo:github/advisory-database path:advisories/github-reviewed/2021` → 6 results
- mcp__github__search_code query: `nats-io repo:github/advisory-database path:advisories/github-reviewed/2026` → 14 results

### Advisory JSON files fetched (all via raw.githubusercontent.com/github/advisory-database/main/)

**Historical batch (2019–2022):**
1. advisories/github-reviewed/2021/05/GHSA-jp4j-47f9-2vc3/GHSA-jp4j-47f9-2vc3.json — CVE-2019-13126, integer overflow, ACTIVE
2. advisories/github-reviewed/2022/02/GHSA-h2fg-54x9-5qhq/GHSA-h2fg-54x9-5qhq.json — CVE-2020-26521, JWT nil ptr DoS, ACTIVE
3. advisories/github-reviewed/2021/05/GHSA-2c64-vj8g-vwrq/GHSA-2c64-vj8g-vwrq.json — CVE-2020-26892, JWT expiry bypass, ACTIVE
4. advisories/github-reviewed/2021/05/GHSA-gwj5-3vfq-q992/GHSA-gwj5-3vfq-q992.json — CVE-2020-28466, import loops DoS, ACTIVE
5. advisories/github-reviewed/2021/05/GHSA-j756-f273-xhp4/GHSA-j756-f273-xhp4.json — CVE-2021-3127, import token bypass (superseded by GHSA-62mh-w5cv-p88c)
6. advisories/github-reviewed/2022/02/GHSA-62mh-w5cv-p88c/GHSA-62mh-w5cv-p88c.json — CVE-2021-3127, import bypass CRITICAL, ACTIVE
7. advisories/github-reviewed/2022/02/GHSA-9r5x-fjv3-q6h4/GHSA-9r5x-fjv3-q6h4.json — CVE-2021-3127, WITHDRAWN duplicate of GHSA-62mh-w5cv-p88c, excluded
8. advisories/github-reviewed/2022/02/GHSA-g6w6-r76c-28j7/GHSA-g6w6-r76c-28j7.json — CVE-2022-24450, account impersonation, ACTIVE
9. advisories/github-reviewed/2023/09/GHSA-vpjc-4jcv-jc29/GHSA-vpjc-4jcv-jc29.json — CVE-2022-28357, directory traversal CRITICAL, ACTIVE
10. advisories/github-reviewed/2024/07/GHSA-2h2x-8hh2-mfq8/GHSA-2h2x-8hh2-mfq8.json — CVE-2022-29946, queue wildcard bypass, ACTIVE
11. advisories/github-reviewed/2021/04/GHSA-prmc-5v5w-c465/GHSA-prmc-5v5w-c465.json — CVE-2020-26149, npm nats client only, NOT included (different ecosystem/package)
12. advisories/github-reviewed/2021/05/GHSA-hmm9-r2m2-qg9w/GHSA-hmm9-r2m2-qg9w.json — CVE-2020-26521, likely duplicate of GHSA-h2fg-54x9-5qhq, not individually mapped

**2023:**
13. advisories/github-reviewed/2023/10/GHSA-4frv-5fj6-4p25/GHSA-4frv-5fj6-4p25.json — CVE-2023-47090, WITHDRAWN duplicate of GHSA-fr2g-9hjm-wr23, excluded
14. advisories/github-reviewed/2023/10/GHSA-fr2g-9hjm-wr23/GHSA-fr2g-9hjm-wr23.json — CVE-2023-47090, auth bypass in system-account-only config, ACTIVE

**2025:**
15. advisories/github-reviewed/2025/04/GHSA-fhg8-qxh5-7q3w/GHSA-fhg8-qxh5-7q3w.json — CVE-2025-30215, JetStream cross-account admin CRITICAL, ACTIVE

**2026 batch (February–March):**
16. advisories/github-reviewed/2026/02/GHSA-qrvq-68c2-7grw/GHSA-qrvq-68c2-7grw.json — CVE-2026-27571, WebSocket compression bomb, ACTIVE
17. advisories/github-reviewed/2026/03/GHSA-pq2q-rcw4-3hr6/GHSA-pq2q-rcw4-3hr6.json — CVE-2026-27889, WebSocket pre-auth crash, ACTIVE
18. advisories/github-reviewed/2026/03/GHSA-52jh-2xxh-pwh6/GHSA-52jh-2xxh-pwh6.json — CVE-2026-29785, leafnode compression crash, ACTIVE
19. advisories/github-reviewed/2026/03/GHSA-fcjp-h8cc-6879/GHSA-fcjp-h8cc-6879.json — CVE-2026-33215, MQTT session hijack, ACTIVE
20. advisories/github-reviewed/2026/03/GHSA-v722-jcv5-w7mc/GHSA-v722-jcv5-w7mc.json — CVE-2026-33216, MQTT password monitoring leak, ACTIVE
21. advisories/github-reviewed/2026/03/GHSA-jxxm-27vp-c3m5/GHSA-jxxm-27vp-c3m5.json — CVE-2026-33217, MQTT ACL bypass, ACTIVE
22. advisories/github-reviewed/2026/03/GHSA-vprv-35vv-q339/GHSA-vprv-35vv-q339.json — CVE-2026-33218, leafnode pre-auth panic, ACTIVE
23. advisories/github-reviewed/2026/03/GHSA-8r68-gvr4-jh7j/GHSA-8r68-gvr4-jh7j.json — CVE-2026-33219, WebSocket bandwidth DoS, ACTIVE
24. advisories/github-reviewed/2026/03/GHSA-9983-vrx2-fg9c/GHSA-9983-vrx2-fg9c.json — CVE-2026-33222, JetStream restore bypass, ACTIVE
25. advisories/github-reviewed/2026/03/GHSA-pwx7-fx9r-hr4h/GHSA-pwx7-fx9r-hr4h.json — CVE-2026-33223, Nats-Request-Info header spoofing, ACTIVE
26. advisories/github-reviewed/2026/03/GHSA-55h8-8g96-x4hj/GHSA-55h8-8g96-x4hj.json — CVE-2026-33246, leafnode identity spoofing, ACTIVE
27. advisories/github-reviewed/2026/03/GHSA-x6g4-f6q3-fqvv/GHSA-x6g4-f6q3-fqvv.json — CVE-2026-33247, debug/vars credential exposure, ACTIVE
28. advisories/github-reviewed/2026/03/GHSA-3f24-pcvm-5jqc/GHSA-3f24-pcvm-5jqc.json — CVE-2026-33248, mTLS DN bypass, ACTIVE
29. advisories/github-reviewed/2026/03/GHSA-8m2x-3m6q-6w8j/GHSA-8m2x-3m6q-6w8j.json — CVE-2026-33249, message trace redirect, ACTIVE

### Registry / metadata
- https://api.github.com/repos/nats-io/nats-server — stars: 20,699, forks: 1,949
- https://api.github.com/repos/nats-io/nats-server/releases/latest — latest: v2.14.6
- https://pkg.go.dev/github.com/nats-io/nats-server/v2 — 0 importers (server binary, not a library)

## Decisions / exclusions

- GHSA-9r5x-fjv3-q6h4 excluded: WITHDRAWN, duplicate of GHSA-62mh-w5cv-p88c
- GHSA-4frv-5fj6-4p25 excluded: WITHDRAWN, duplicate of GHSA-fr2g-9hjm-wr23
- GHSA-prmc-5v5w-c465 excluded: affects npm `nats` client package, not Go nats-server
- GHSA-hmm9-r2m2-qg9w: same CVE (2020-26521) as GHSA-h2fg-54x9-5qhq, treated as duplicate, not separately mapped
- Additional advisories for `nats-streaming-server` and `nats-io/jwt` as standalone modules not mapped (separate packages)

## Page created

- `wiki/go/github.com/nats-io/nats-server.md` — 24 active advisories mapped

## Index changes

- `wiki/go/index.md`: added nats-server entry (33 → 34 pages)
- `wiki/index.md`: Go 33 → 34, total 288 → 289, date updated
- `wiki/log.md`: prepended 2026-09-14 entry
