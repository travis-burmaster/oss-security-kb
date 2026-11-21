# Advisory-review pass 2026-11-21 (UTC 20261121-0459)

## Target selection
- Priority (a), this week's security news: the PHP 2026-11-19 security release for all supported branches, and the PHP2Shell pair (CVE-2026-109618, CVE-2026-109619) in the CISA KEV catalog (added 2026-10-26). The KB had no PHP page. The 2026-11-20 log listed PHP as a lead it did not take.
- OpenJDK CVE-2026-114938 ("Java4Shell", Oracle/OpenJDK CPU 2026-11-17) was considered and deferred: openjdk.org and www.openwall.com do not resolve from this environment, and no primary record was reachable. Not in CISA KEV as of catalog 2026.11.20.

## Primary sources consulted
- https://raw.githubusercontent.com/php/php-src/PHP-8.5/NEWS (HTTP 200)
- https://raw.githubusercontent.com/php/php-src/PHP-8.4/NEWS (HTTP 200)
- https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS (HTTP 200)
- https://raw.githubusercontent.com/php/php-src/PHP-8.2/NEWS (HTTP 200)
- https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json (catalog 2026.11.20, released 2026-11-20T17:48:39Z). PHP entries: CVE-2026-109618 and CVE-2026-109619, both added 2026-10-26. No other PHP CVE from the 2026 changelogs is in the catalog.
- php-src GHSA IDs cited on the page are the ones named in the upstream NEWS files, linked as https://github.com/php/php-src/security/advisories/<GHSA-id>.

## Tried and unreachable or empty
- https://github.com/php/php-src/security/advisories/GHSA-658j-r8rw-q6mx: HTTP 403 (proxy)
- `gh api repos/php/php-src/security-advisories/...`: refused (repo outside session scope)
- `gh api search/code` on repo:github/advisory-database for CVE-2026-109618, CVE-2026-115560 and CVE-2026-91768, plus `"php/php-src/security/advisories"`: zero relevant 2026 hits
- https://openjdk.org/groups/vulnerability/advisories/2026-11-17: DNS not resolvable
- https://www.openwall.com/lists/oss-security/2026/11/17/31: DNS not resolvable
- www.php.net: blocked, per CLAUDE.md

## Secondary sources (context only; no table row depends on them)
- https://www.aikido.dev/blog/php-security-release-19-november-2026-cve-2026-115560
- https://securityonline.info/php-security-release-cve-2026-115560/
- https://bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws
- https://pitstop.manageengine.com/portal/en/community/topic/security-alert-two-critical-php-rce-vulnerabilities-php2shell-rated-cvss-9-2-21-10-2026
- https://www.sonatype.com/blog/critical-openjdk-rce-cve-2026-114938-what-to-know
- https://securitylabs.datadoghq.com/articles/java4shell-remote-code-execution-in-openjdk-cve-2026-114938.md
- https://www.esecurityplanet.com/vulnerabilities/news-cisa-kev-gpustack-freeswitch-openssh-ibm-november-2026/

## Method
Parsed each branch's NEWS for release blocks dated 2026 and kept every entry naming a CVE or GHSA. Deduplicated by CVE (or GHSA when no CVE). Recorded the fixed version per branch and the first release date. Result: 52 rows covering 52 unique CVEs plus 8 CVE-less GHSAs (GHSA-ch8v-r6jh-4vvr and 7 bundled-PCRE2 GHSAs on 8.2). 18 CVEs are in the 2026-11-19 release.
