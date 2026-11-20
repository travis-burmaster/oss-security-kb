# Advisory-review pass 2026-11-20 (UTC 0459)

Targets: python/litellm (stale since 2026-05-06; CVE-2026-40217 added to CISA KEV 2026-11-18) and linux/openssh (CVE-2026-123158 "sshhole" added to CISA KEV 2026-11-09).
Not taken this pass (leads for later): PHP 2026-11-19 security release (no KB page; php.net blocked), OpenJDK "Java4Shell" CVE-2026-114938 (no KB page fits an existing ecosystem), Apache Axis CVE-2026-90436 (KEV 2026-11-18).

## News / triage searches (WebSearch, 2026-11-20)
- https://thehackernews.com/2026/11/php-warns-of-critical-security-flaws.html
- https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html
- https://thehackernews.com/2026/11/cisa-urges-immediate-patching-of.html
- https://cybersecuritynews.com/java-17-rce-vulnerability/
- https://www.helpnetsecurity.com/2026/11/19/nginx2root-nginx-vulnerabilities/
- https://www.cisa.gov/news-events/alerts/2026/11/18/cisa-adds-four-known-exploited-vulnerabilities-catalog
- https://source.android.com/docs/security/bulletin/2026/2026-11-01

## CISA KEV
- https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json (catalogVersion 2026.11.18)
  - LiteLLM: CVE-2026-42208 (2026-05-08), CVE-2026-42271 (2026-06-08), CVE-2026-59822 (2026-09-02), CVE-2026-40217 (2026-11-18, due 2026-12-02)
  - OpenSSH: CVE-2026-123158 (2026-11-09, due 2026-11-12, forensic triage Yes)

## GitHub code search (gh api search/code, repo:github/advisory-database)
- `litellm path:advisories/github-reviewed/2026`
- `"litellm" "PyPI" path:advisories/github-reviewed`
- `CVE-2026-40217`, `CVE-2026-59822`, `CVE-2026-123158`
- `OpenSSH path:advisories/unreviewed/2026/09`, `/10`, `/11`

## GHSA records fetched (raw.githubusercontent.com/github/advisory-database/main/...)
- GHSA-2wqp-q3c6-ccj5 CVE-2026-115886 | mlflow | 2026-10-23 
- GHSA-3926-2jvf-fg29  | litellm | 2026-04-10 | withdrawn
- GHSA-3cv6-jpf6-8222 CVE-2026-84377 | litellm,litellm,litellm,litellm,litellm,litellm,litellm,litellm,litellm | 2026-09-30 
- GHSA-4g5m-c9r5-49xf CVE-2026-59819 | litellm | 2026-07-22 
- GHSA-4jcj-7x88-m979 CVE-2026-12773 | litellm | 2026-06-21 
- GHSA-4xpc-pv4p-pm3w CVE-2026-49468 | litellm | 2026-06-16 
- GHSA-53mr-6c8q-9789 CVE-2026-35029 | litellm | 2026-04-03 
- GHSA-5jmr-gcrj-2c9q CVE-2026-59820 | litellm | 2026-07-22 
- GHSA-69x8-hrgq-fjj8  | litellm | 2026-04-08 
- GHSA-6qr3-3g89-m4jj CVE-2026-12770 | litellm | 2026-06-21 
- GHSA-6wvf-77m9-58rm CVE-2026-37004 | litellm | 2026-08-27 
- GHSA-72m8-9m7m-h278 CVE-2026-59821 | litellm | 2026-07-22 
- GHSA-7488-6r32-c95q CVE-2026-59822 | litellm | 2026-07-22 
- GHSA-7hp6-4w63-5g45 CVE-2026-114612 | litellm,litellm,litellm,litellm,litellm | 2026-10-27 
- GHSA-98x5-vq43-vc5p  | semantic-router | 2026-06-26 
- GHSA-c693-x898-5g4h CVE-2026-12798 | litellm | 2026-06-21 
- GHSA-g5ff-637f-6q2m  | litellm | 2026-10-27 
- GHSA-hhww-mrg2-969h  | litellm | 2026-10-27 
- GHSA-hx8v-g79f-8w5f CVE-2026-59823 | litellm | 2026-09-17 
- GHSA-j37q-q7p9-vpwm CVE-2026-12795 | litellm | 2026-06-21 
- GHSA-jjhc-v7c2-5hh6 CVE-2026-35030 | litellm | 2026-04-03 
- GHSA-m2v5-74w2-qhcj CVE-2026-12799 | litellm | 2026-06-21 
- GHSA-mf52-j94g-746m CVE-2026-12772 | litellm | 2026-06-21 
- GHSA-p897-vf7j-f5h8 CVE-2026-12797 | litellm | 2026-06-21 
- GHSA-qmf3-4767-5fg3 CVE-2026-12771 | litellm | 2026-06-21 
- GHSA-qrc4-49gv-mv9m CVE-2026-47101 | litellm | 2026-05-21 
- GHSA-r75f-5x8p-qvmc CVE-2026-42208 | litellm | 2026-04-24 
- GHSA-v4p8-mg3p-g94g CVE-2026-42271 | litellm | 2026-04-25 
- GHSA-w2mh-qq9q-453x CVE-2026-12796 | litellm | 2026-06-21 
- GHSA-wpfp-gwwc-vwq6 CVE-2026-47102 | litellm | 2026-05-21 
- GHSA-wxxx-gvqv-xp7p CVE-2026-40217 | litellm | 2026-05-11 
- GHSA-x6m9-gxvr-7jpv CVE-2026-34936 | praisonai | 2026-04-01 
- GHSA-xqmj-j6mv-4862 CVE-2026-42203 | litellm | 2026-04-24 
- GHSA-2jr9-cjff-c97w CVE-2026-83769 | unreviewed | 2026-10-13 
- GHSA-2rq5-4vw4-m3vg CVE-2026-105429 | unreviewed | 2026-10-14 
- GHSA-2xxv-m3rc-rvrm CVE-2026-106553 | unreviewed | 2026-10-06 
- GHSA-3j57-3pc4-v67v CVE-2026-110926 | unreviewed | 2026-10-15 
- GHSA-4fcc-vm97-gx3x CVE-2026-123158 | unreviewed | 2026-11-05 
- GHSA-622r-jq6j-964m CVE-2026-83754 | unreviewed | 2026-10-13 
- GHSA-695p-3q57-gff4 CVE-2026-106552 | unreviewed | 2026-10-06 
- GHSA-74g8-x9g6-gwmc CVE-2026-106588 | unreviewed | 2026-10-07 
- GHSA-7p96-34g5-jqvf CVE-2026-69397 | unreviewed | 2026-09-08 
- GHSA-8fmq-pfxf-6hmc CVE-2026-106587 | unreviewed | 2026-10-07 
- GHSA-8wpc-x9xg-9q94 CVE-2026-106589 | unreviewed | 2026-10-07 
- GHSA-99hr-wq4p-x49q CVE-2026-106583 | unreviewed | 2026-10-07 
- GHSA-9hq3-hc6p-gc8q CVE-2026-106584 | unreviewed | 2026-10-06 
- GHSA-9xxf-58mh-q784 CVE-2026-106582 | unreviewed | 2026-10-06 
- GHSA-cv5v-cq2q-vv46 CVE-2026-110923 | unreviewed | 2026-10-15 
- GHSA-fgcr-pfrh-mf25 CVE-2026-88157 | unreviewed | 2026-10-13 
- GHSA-fj5v-qh2p-6v8f CVE-2026-94029 | unreviewed | 2026-09-30 
- GHSA-h54q-2vm3-97qv CVE-2026-110925 | unreviewed | 2026-10-15 
- GHSA-hq2f-vwrj-48j9 CVE-2026-110927 | unreviewed | 2026-10-15 
- GHSA-j45v-7hgc-xv9x CVE-2026-106555 | unreviewed | 2026-10-06 
- GHSA-j4h6-744f-q3hq CVE-2026-106585 | unreviewed | 2026-10-06 
- GHSA-jrjw-pc9r-c624 CVE-2026-106586 | unreviewed | 2026-10-06 
- GHSA-m3x3-p27c-whhp CVE-2026-17508 | unreviewed | 2026-10-02 
- GHSA-q953-q6mf-pwpq CVE-2026-110924 | unreviewed | 2026-10-15 
- GHSA-qc4p-9828-mv83 CVE-2026-93994 | unreviewed | 2026-09-30 
- GHSA-v5h7-r869-8r86 CVE-2026-83871 | unreviewed | 2026-10-13 
- GHSA-x2g7-hfcp-7xm9 CVE-2026-83923 | unreviewed | 2026-10-13 
- GHSA-x8mp-74ph-4f29 CVE-2026-97816 | unreviewed | 2026-10-13 
- GHSA-xm7c-pq6h-c8j2 CVE-2026-70163 | unreviewed | 2026-10-13 
- GHSA-xvfx-9f2p-qj57 CVE-2026-97811 | unreviewed | 2026-10-13 
- GHSA-xw36-3g63-5wfw CVE-2026-109786 | unreviewed | 2026-10-13 
- GHSA-xx8j-qhmg-cj8f CVE-2026-94140 | unreviewed | 2026-10-22 

## Blocked this run
- www.openssh.org and www.openssh.com (HTTP 403 from egress proxy): release notes for 10.6 / 10.6p2 not read directly; fix versions taken from GHSA text.

## Decisions
- LiteLLM: 23 new GHSA rows. GHSA-3926-2jvf-fg29 withdrawn duplicate, excluded. mlflow / semantic-router / praisonai records excluded (other packages).
- OpenSSH: 17 new rows (12 portable OpenSSH records citing openssh.org 10.6 / 10.6p2 release notes, 5 Red Hat CVE-2026-1109xx records with no upstream fix version stated). Excluded: 9 Microsoft OpenSSH for Windows records, 2 Apache MINA SSHD, 1 fail2ban.
- Secondary-source claim that LiteLLM fix for CVE-2026-40217 is 1.83.11 not used; GHSA record says fixed 1.83.10.
