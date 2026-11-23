# Advisory-review pass 2026-11-23 (UTC 20261123-0459)

## Target selection
- Priority (a), this week's security news: Apache HTTP Server 2.4.71 (2026-11-11) fixes CVE-2026-119618, a mod_http2 RCE that news coverage reports as exploited. `wiki/linux/apache2.md` was last updated 2026-08-08 and had no CVE newer than 2.4.60, so it was also stale (priority b).
- Considered and not taken: OpenJDK CVE-2026-114938 "Java4Shell" (Oracle CPU 2026-11-17; no JDK page; not in CISA KEV as of 2026.11.20; openjdk.org unreachable in earlier passes). OpenSSL advisories of 2026-11-10 and 2026-11-17 (Low severity per secondary summaries; fixed releases scheduled for 2026-12-01). Apache Roller CVE-2026-129448 (KEV 2026-11-20; application). node-opcua / Rack items from a Corgea summary (no Ruby ecosystem in KB; unverified).
- Log check: apache2 not handled in the last 7 days.

## Primary sources consulted
- https://raw.githubusercontent.com/apache/httpd/2.4.x/CHANGES (HTTP 200; SECURITY entries for 2.4.61 through 2.4.71; 2.4.72 section empty)
- https://raw.githubusercontent.com/apache/httpd/trunk/CHANGES (HTTP 200; fetched, not used for rows)
- https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json (catalog 2026.11.20). Apache HTTP Server entries: CVE-2019-0211, CVE-2021-41773, CVE-2021-42013 (2021-11-03), CVE-2021-40438 (2021-12-01, product "Apache"), CVE-2024-38475 (2025-05-01). None of the 64 new rows.
- `gh api -X GET search/code -f q='"CVE-2026-119618" repo:github/advisory-database'` -> advisories/unreviewed/2026/11/GHSA-hjhf-gpg9-qqfj/GHSA-hjhf-gpg9-qqfj.json
- https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-hjhf-gpg9-qqfj/GHSA-hjhf-gpg9-qqfj.json (published 2026-11-11, HIGH, CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H, CWE-362)
- Apache per-CVE records (all HTTP 200), https://raw.githubusercontent.com/apache/httpd-site/main/content/security/json/<CVE>.json for:
  - CVE-2026-119618
  - CVE-2026-109163
  - CVE-2026-106023
  - CVE-2026-93546
  - CVE-2026-79768
  - CVE-2026-73637
  - CVE-2026-73636
  - CVE-2026-63718
  - CVE-2026-63686
  - CVE-2026-63292
  - CVE-2026-63045
  - CVE-2026-59797
  - CVE-2026-59685
  - CVE-2026-58415
  - CVE-2026-57941
  - CVE-2026-56449
  - CVE-2026-56154
  - CVE-2026-56153
  - CVE-2026-48005
  - CVE-2026-47360
  - CVE-2026-46729
  - CVE-2026-42528
  - CVE-2026-42356
  - CVE-2026-49975
  - CVE-2026-48913
  - CVE-2026-44631
  - CVE-2026-44186
  - CVE-2026-44185
  - CVE-2026-44119
  - CVE-2026-43951
  - CVE-2026-42536
  - CVE-2026-42535
  - CVE-2026-34356
  - CVE-2026-34355
  - CVE-2026-29170
  - CVE-2026-29167
  - CVE-2026-34059
  - CVE-2026-34032
  - CVE-2026-33857
  - CVE-2026-33523
  - CVE-2026-33007
  - CVE-2026-33006
  - CVE-2026-29169
  - CVE-2026-29168
  - CVE-2026-28780
  - CVE-2026-24072
  - CVE-2026-23918
  - CVE-2025-66200
  - CVE-2025-65082
  - CVE-2025-59775
  - CVE-2025-58098
  - CVE-2025-55753
  - CVE-2025-54090
  - CVE-2025-53020
  - CVE-2025-49812
  - CVE-2025-49630
  - CVE-2025-23048
  - CVE-2024-47252
  - CVE-2024-43394
  - CVE-2024-43204
  - CVE-2024-42516
  - CVE-2024-40898
  - CVE-2024-40725
  - CVE-2024-39884

## Notes on the records
- Severity in the table is the `metrics[].other.content.text` value (Apache's textual rating). Counts: 1 critical, 5 important, 22 moderate, 36 low.
- Fixed-in dates come from each record's timeline entry "2.4.x released". 2.4.67 records with a "fixed in 2.4.x by r..." last entry use the 2026-05-04 date that the other 2.4.67 records give for the release.
- Several records carry `CNA_private.state` DRAFT or RESERVED in the site repository; their content matches the CHANGES SECURITY entries for the same release.

## Tried and unreachable
- https://httpd.apache.org/security/vulnerabilities_24.html: no response (curl HTTP 000). Table links point to this page's anchors and to the httpd-site JSON records.

## Secondary sources (context only; no table row depends on them)
- https://cybersecuritynews.com/apache-http-server-rce-exploitation/ (reports exploitation of CVE-2026-119618; unconfirmed)
- https://www.securityweek.com/critical-apache-roller-axis-vulnerabilities-exploited-in-attacks/
- https://www.bleepingcomputer.com/news/security/critical-java4shell-flaw-allows-rce-attacks-on-major-java-applications/
- https://www.sonatype.com/blog/critical-openjdk-rce-cve-2026-114938-what-to-know
- https://groups.google.com/a/openssl.org/g/openssl-announce/c/RjPdEDdZiiM (OpenSSL 2026-11-10 advisory announcement; search result only)
- https://securityonline.info/openssl-security-advisory-november-2026/
- https://corgea.com/research/cve-2026-95860-112307-125110-125121-102943-125742-node-opcua-sqlparse-compose-lint-rack-dagu-7zip-november-2026
- https://www.action1.com/patch-tuesday/vulnerability-digest-november-2026-third-party-updates/

