# Advisory-review pass 2026-11-22 (UTC 20261122-0500)

## Target selection
- Priority (a), this week's security news: CISA KEV catalog 2026.11.20 added CVE-2026-90436 (Apache Axis 1.x unsafe reflection, added 2026-11-18, due 2026-11-21). The KB had no Axis page. The same GHSA search surfaced the Apache Axis2/Java 2.0.2 security release (7 CVEs, GHSA published 2026-11-09), so Axis2/Java was added as a companion page.
- Considered and not taken: CVE-2026-129448 (Apache Roller, KEV 2026-11-20): a blog application, not a widely consumed library. OpenJDK CVE-2026-114938 ("Java4Shell"): now has unreviewed record GHSA-6g7j-4xh3-xq2q (Oracle Java SE / GraalVM, CVSS:3.1 AV:N/AC:H, CWE-122), but the KB has no JDK page and it is not in CISA KEV as of 2026.11.20. Lead left for a future pass.
- Log check: neither Axis package handled in the last 7 days.

## Primary sources consulted
- https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json (catalog 2026.11.20). Axis entry: CVE-2026-90436, dateAdded 2026-11-18, dueDate 2026-11-21, forensicTriage Yes, CWE-470. No Axis2 entries.
- GitHub code search (`gh api -X GET search/code`, repo:github/advisory-database) queries: "CVE-2026-90436", "org.apache.axis:axis", "axis:axis", "org.apache.axis2", "Axis2" path:advisories/unreviewed, "Apache Axis" path:advisories/unreviewed/2026, "CVE-2026-114938", "CVE-2026-82384".
- GHSA records fetched from https://raw.githubusercontent.com/github/advisory-database/main/advisories/...:
  - Axis 1.x: unreviewed/2026/11/GHSA-988f-c54m-f8jj; github-reviewed/2024/01/GHSA-hr2c-p8rh-238h; 2023/09/GHSA-rmqp-9w4c-gc7w; 2022/05/GHSA-2c4w-2px5-9x3x; 2020/10/GHSA-55w9-c3g2-4rrh; 2019/05/GHSA-h9gj-rqrw-x4fq; 2018/10/GHSA-96jq-75wh-2658; 2018/10/GHSA-r53v-vm87-f72c
  - Axis2/Java: unreviewed/2026/11/GHSA-p73m-5r4v-xhg8, GHSA-qr3h-4xv7-vc63, GHSA-6qx5-4pcm-5fgh, GHSA-78w3-p65q-wwh7, GHSA-p3g5-3wm8-wh38, GHSA-f58r-c62m-574f, GHSA-84h8-j9vj-p626; unreviewed/2026/07/GHSA-fhh8-qfj4-g948; unreviewed/2022/05/GHSA-9x38-862g-jg8w; github-reviewed/2022/05/GHSA-23vv-v25h-qwqw, GHSA-23x8-j7hm-5xwf, GHSA-66rx-gqx3-p98m, GHSA-88r4-38gc-97p4, GHSA-wwq7-pxwc-p4rc
  - Lead only: unreviewed/2026/11/GHSA-6g7j-4xh3-xq2q (CVE-2026-114938)
- https://raw.githubusercontent.com/apache/axis-axis2-java-core/master/src/site/markdown/release-notes/2.0.2.md (HTTP 200; secure-default changes)
- https://repo1.maven.org/maven2/org/apache/axis2/axis2-kernel/maven-metadata.xml (2.0.2 present, lastUpdated 20261028161924)
- https://repo1.maven.org/maven2/org/apache/axis/axis/maven-metadata.xml (1.4 only, lastUpdated 20060423051651)
- https://repo1.maven.org/maven2/axis/axis/maven-metadata.xml (1.2-alpha-1 through 1.4)

## Excluded (same searches, different products)
- CVE-2026-124023 / GHSA-qv28-p6jq-5h3f and CVE-2012-6107 / GHSA-qjfc-9x3x-5h2r: Apache Axis2/C, not Axis2/Java
- CVE-2026-39920 / GHSA-3f6j-24pw-57fm: BridgeHead FileStore (embeds Axis2 with default credentials)
- CVE-2025-59793 / GHSA-4586-432g-jmvg: Rocket TRUfusion Enterprise
- CVE-2003-1386 / GHSA-p6f6-mqx8-c8mp: AXIS 2400 Video Server (Axis Communications)
- CVE-2026-82384 records: Apache Roller (see above)

## Tried and unreachable
- https://axis.apache.org/axis2/java/core/release-notes/2.0.2.html: no response (curl HTTP 000)
- lists.apache.org and openwall links are cited from the GHSA records' reference lists; not fetched.

## Secondary sources (context only; no table row depends on them)
- https://www.cisa.gov/news-events/alerts/2026/11/18/cisa-adds-four-known-exploited-vulnerabilities-catalog (web search result)
- https://dev.to/devaland/actively-exploited-this-week-12-new-cisa-kev-entries-9-november-to-15-november-2026-3eej (web search result)
