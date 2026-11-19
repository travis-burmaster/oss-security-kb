# Advisory review 20261119-1757 UTC — nginx 2026 update

Routine: nightly OSS KB maintenance pass (2026-11-19). Trigger: nginx 1.31.9 / 1.30.7 security release on 2026-11-18 ("nginx2root").

## Reachability
- Reachable: raw.githubusercontent.com, GitHub code search (`gh api search/code`), git push to origin.
- Blocked (proxy 403 / DNS): api.osv.dev, nginx.org, services.nvd.nist.gov, www.cve.org, my.f5.com, www.php.net, cert.europa.eu, api.github.com (unauthenticated REST for nginx/nginx).

## Web searches (secondary, used only to pick targets and for exploitation context)
- Query "open source vulnerability advisory November 2026 CVE nginx OpenSSL PHP": surfaced https://cert.europa.eu/publications/security-advisories/2026-022/ (not fetchable), https://www.aikido.dev/blog/php-security-release-19-november-2026-cve-2026-115560, https://dev.to/devtalk94/php-security-release-nov-2026-fixes-in-8513-8428-5fj3
- Query "CISA KEV added November 2026 open source": https://www.cisa.gov/news-events/alerts/2026/11/18/cisa-adds-four-known-exploited-vulnerabilities-catalog , https://safeguard.sh/resources/blog/cisa-kev-additions-october-20-to-november-13-2026
- Query on CVE-2026-42945 exploitation: https://securityaffairs.com/192289/uncategorized/experts-warn-of-active-exploitation-of-critical-nginx-flaw-cve-2026-42945.html , https://thehackernews.com/2026/05/nginx-cve-2026-42945-exploited-in-wild.html (secondary; VulnCheck attribution)

## Primary sources
- Upstream changelog (fix versions): https://raw.githubusercontent.com/nginx/nginx/master/docs/xml/nginx/changes.xml , https://raw.githubusercontent.com/nginx/nginx/stable-1.30/docs/xml/nginx/changes.xml , https://raw.githubusercontent.com/nginx/nginx/stable-1.28/docs/xml/nginx/changes.xml
- CISA KEV catalog: https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json (catalogVersion 2026.11.18, 1786 entries; no entry mentions nginx)
- GHSA search: `gh api -X GET search/code -f q='nginx path:advisories/unreviewed/2026/<MM> repo:github/advisory-database'` for months 09-11, plus 'NGINX Open Source path:advisories/unreviewed/2026', plus targeted CVE-ID searches for CVE-2026-1642, CVE-2026-118899, CVE-2026-42946.

## GHSA records mapped (CVSS 3.1 base computed from the record's vector)
| CVE | GHSA | GHSA severity | CVSS 3.1 | Published | Record |
|---|---|---|---|---|---|
| CVE-2026-1642 | GHSA-7chh-rv6q-8pp3 | HIGH | 5.9 | 2026-02-04 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/02/GHSA-7chh-rv6q-8pp3/GHSA-7chh-rv6q-8pp3.json |
| CVE-2026-27651 | GHSA-82w2-x7hf-5h8r | HIGH | 7.5 | 2026-03-24 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/03/GHSA-82w2-x7hf-5h8r/GHSA-82w2-x7hf-5h8r.json |
| CVE-2026-27654 | GHSA-6r46-2qjx-j5j3 | HIGH | 8.2 | 2026-03-24 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/03/GHSA-6r46-2qjx-j5j3/GHSA-6r46-2qjx-j5j3.json |
| CVE-2026-27784 | GHSA-hwq5-42j9-jvqj | HIGH | 7.8 | 2026-03-24 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/03/GHSA-hwq5-42j9-jvqj/GHSA-hwq5-42j9-jvqj.json |
| CVE-2026-28753 | GHSA-ggr6-fmr8-2m8g | MODERATE | 3.7 | 2026-03-24 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/03/GHSA-ggr6-fmr8-2m8g/GHSA-ggr6-fmr8-2m8g.json |
| CVE-2026-28755 | GHSA-hgfr-jmpr-2p89 | MODERATE | 5.4 | 2026-03-24 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/03/GHSA-hgfr-jmpr-2p89/GHSA-hgfr-jmpr-2p89.json |
| CVE-2026-32647 | GHSA-6364-x4qj-7w59 | HIGH | 7.8 | 2026-03-24 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/03/GHSA-6364-x4qj-7w59/GHSA-6364-x4qj-7w59.json |
| CVE-2026-40460 | GHSA-h7rq-f9gq-mc8r | MODERATE | 6.5 | 2026-05-13 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/05/GHSA-h7rq-f9gq-mc8r/GHSA-h7rq-f9gq-mc8r.json |
| CVE-2026-40701 | GHSA-x88q-x2r7-vg3g | MODERATE | 4.8 | 2026-05-13 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/05/GHSA-x88q-x2r7-vg3g/GHSA-x88q-x2r7-vg3g.json |
| CVE-2026-42926 | GHSA-v43f-895r-chhh | MODERATE | 5.8 | 2026-05-13 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/05/GHSA-v43f-895r-chhh/GHSA-v43f-895r-chhh.json |
| CVE-2026-42934 | GHSA-6vmc-2wh4-77qp | MODERATE | 4.8 | 2026-05-13 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/05/GHSA-6vmc-2wh4-77qp/GHSA-6vmc-2wh4-77qp.json |
| CVE-2026-42945 | GHSA-gcgv-v5gf-c543 | CRITICAL | 8.1 | 2026-05-13 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/05/GHSA-gcgv-v5gf-c543/GHSA-gcgv-v5gf-c543.json |
| CVE-2026-42946 | GHSA-fm65-xrrr-c358 | HIGH | 6.5 | 2026-05-13 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/05/GHSA-fm65-xrrr-c358/GHSA-fm65-xrrr-c358.json |
| CVE-2026-9256 | GHSA-h78r-86c6-jgp4 | CRITICAL | 8.1 | 2026-05-26 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/05/GHSA-h78r-86c6-jgp4/GHSA-h78r-86c6-jgp4.json |
| CVE-2026-42055 | GHSA-78jw-ww3g-9wp7 | CRITICAL | 8.1 | 2026-06-17 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/06/GHSA-78jw-ww3g-9wp7/GHSA-78jw-ww3g-9wp7.json |
| CVE-2026-42530 | GHSA-5mcp-3252-f5vr | CRITICAL | 8.1 | 2026-06-17 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/06/GHSA-5mcp-3252-f5vr/GHSA-5mcp-3252-f5vr.json |
| CVE-2026-48142 | GHSA-2388-jp8v-fg9w | MODERATE | 4.8 | 2026-06-17 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/06/GHSA-2388-jp8v-fg9w/GHSA-2388-jp8v-fg9w.json |
| CVE-2026-42533 | GHSA-fxfg-v4rj-hp95 | CRITICAL | 8.1 | 2026-07-15 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/07/GHSA-fxfg-v4rj-hp95/GHSA-fxfg-v4rj-hp95.json |
| CVE-2026-56434 | GHSA-m73p-xg7q-m8f2 | HIGH | 6.5 | 2026-07-15 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/07/GHSA-m73p-xg7q-m8f2/GHSA-m73p-xg7q-m8f2.json |
| CVE-2026-60005 | GHSA-vxcv-h5wj-jxr5 | HIGH | 8.2 | 2026-07-15 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/07/GHSA-vxcv-h5wj-jxr5/GHSA-vxcv-h5wj-jxr5.json |
| CVE-2026-90439 | GHSA-fjgw-pmcm-g7j7 | MODERATE | 6.5 | 2026-09-15 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/09/GHSA-fjgw-pmcm-g7j7/GHSA-fjgw-pmcm-g7j7.json |
| CVE-2026-15176 | GHSA-cvv4-j4mx-w8q5 | CRITICAL | 8.1 | 2026-10-14 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/10/GHSA-cvv4-j4mx-w8q5/GHSA-cvv4-j4mx-w8q5.json |
| CVE-2026-93479 | GHSA-v72q-v4vf-2mx7 | CRITICAL | 8.1 | 2026-10-14 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/10/GHSA-v72q-v4vf-2mx7/GHSA-v72q-v4vf-2mx7.json |
| CVE-2026-95101 | GHSA-g6r5-95cx-mpp9 | MODERATE | 5.3 | 2026-10-14 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/10/GHSA-g6r5-95cx-mpp9/GHSA-g6r5-95cx-mpp9.json |
| CVE-2026-97205 | GHSA-ff5w-vvxc-fm9x | CRITICAL | 8.1 | 2026-10-14 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/10/GHSA-ff5w-vvxc-fm9x/GHSA-ff5w-vvxc-fm9x.json |
| CVE-2026-97629 | GHSA-qhwc-5g9q-3669 | HIGH | 6.5 | 2026-10-14 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/10/GHSA-qhwc-5g9q-3669/GHSA-qhwc-5g9q-3669.json |
| CVE-2026-113425 | GHSA-rmpv-v5m5-rr27 | CRITICAL | 8.1 | 2026-11-18 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-rmpv-v5m5-rr27/GHSA-rmpv-v5m5-rr27.json |
| CVE-2026-118899 | GHSA-mjqw-rmmf-hgxf | HIGH | 7.5 | 2026-11-18 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-mjqw-rmmf-hgxf/GHSA-mjqw-rmmf-hgxf.json |
| CVE-2026-120967 | GHSA-q9wg-m5cc-h828 | MODERATE | 4.8 | 2026-11-18 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-q9wg-m5cc-h828/GHSA-q9wg-m5cc-h828.json |
| CVE-2026-120993 | GHSA-39qv-989q-vg33 | MODERATE | 5.3 | 2026-11-18 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-39qv-989q-vg33/GHSA-39qv-989q-vg33.json |
| CVE-2026-121810 | GHSA-fxx2-rrmx-x4v2 | CRITICAL | 8.1 | 2026-11-18 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-fxx2-rrmx-x4v2/GHSA-fxx2-rrmx-x4v2.json |
| CVE-2026-123007 | GHSA-m4q8-cf44-f42r | CRITICAL | 8.1 | 2026-11-18 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-m4q8-cf44-f42r/GHSA-m4q8-cf44-f42r.json |
| CVE-2026-123633 | GHSA-7xxj-p8w5-434q | CRITICAL | 8.1 | 2026-11-18 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-7xxj-p8w5-434q/GHSA-7xxj-p8w5-434q.json |
| CVE-2026-123634 | GHSA-qxf8-26hv-4jh5 | CRITICAL | 8.1 | 2026-11-18 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-qxf8-26hv-4jh5/GHSA-qxf8-26hv-4jh5.json |
| CVE-2026-123640 | GHSA-c32q-x8cv-vhfr | MODERATE | 5.3 | 2026-11-18 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-c32q-x8cv-vhfr/GHSA-c32q-x8cv-vhfr.json |
| CVE-2026-125283 | GHSA-cgqq-hx2v-pf8c | MODERATE | 5.3 | 2026-11-18 | https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-cgqq-hx2v-pf8c/GHSA-cgqq-hx2v-pf8c.json |

## Excluded
- CVE-2026-50107 / GHSA-gx48-gh32-62q5: NGINX Gateway Fabric control-plane configuration injection; not an nginx core bug and not in the nginx changelog.
- Remaining search hits (about 55 records) mention nginx only incidentally (other products' advisories) and were not mapped.

## Not done this pass
- PHP 8.5.13 / 8.4.28 / 8.3.37 / 8.2.36 security release (2026-11-19): released today, php.net unreachable, and no PHP page exists in the KB yet. Candidate for the next pass.
- CISA KEV 2026-11-18 additions (LiteLLM CVE-2026-40217, Apache Axis CVE-2026-90436): candidates for future pages (python/litellm; maven Axis).

