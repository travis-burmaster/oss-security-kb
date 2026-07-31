# Advisory Review Notes — 2026-07-31

## Pass summary

Targets: maven/org.apache.struts/struts2-core, maven/org.apache.shiro/shiro-core
Ecosystems: Maven / Java
Pass date: 2026-07-31
Environment constraints: OSV.dev API blocked (HTTP 403); Maven Central stats API blocked (HTTP 403).

## Sources consulted

### Advisory database queries
- `mcp__github__search_code repo:github/advisory-database struts2-core path:advisories` — 60 total GHSA records returned
- `mcp__github__search_code repo:github/advisory-database "shiro-core" path:advisories/github-reviewed` — 12 total GHSA records returned

### GHSA advisory files fetched for struts2-core (via WebFetch on raw.githubusercontent.com)
- GHSA-j77q-2qqg-6989 (CVE-2017-5638 / S2-045): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2018/10/GHSA-j77q-2qqg-6989/GHSA-j77q-2qqg-6989.json
- GHSA-8fx9-5hx8-crhm (CVE-2017-12611 / S2-053): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2018/10/GHSA-8fx9-5hx8-crhm/GHSA-8fx9-5hx8-crhm.json
- GHSA-v8j6-6c2r-r27c (CVE-2021-31805 / S2-062): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/04/GHSA-v8j6-6c2r-r27c/GHSA-v8j6-6c2r-r27c.json
- GHSA-2j39-qcjm-428w (CVE-2023-50164 / S2-066): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/12/GHSA-2j39-qcjm-428w/GHSA-2j39-qcjm-428w.json
- GHSA-43mq-6xmg-29vm (CVE-2024-53677 / S2-067): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/12/GHSA-43mq-6xmg-29vm/GHSA-43mq-6xmg-29vm.json
- GHSA-xm92-v2mq-842q (CVE-2016-4436 / S2-035): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-xm92-v2mq-842q/GHSA-xm92-v2mq-842q.json
- GHSA-864w-r5qj-h6fj (CVE-2016-4461 / S2-029): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-864w-r5qj-h6fj/GHSA-864w-r5qj-h6fj.json
- GHSA-whmq-v94q-34p9 (CVE-2013-1965 / S2-012): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-whmq-v94q-34p9/GHSA-whmq-v94q-34p9.json
- GHSA-729q-fcgp-r5xh (CVE-2023-41835): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/12/GHSA-729q-fcgp-r5xh/GHSA-729q-fcgp-r5xh.json
- GHSA-xx7v-hqxh-cjr9 (CVE-2025-64775 / S2-068): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/12/GHSA-xx7v-hqxh-cjr9/GHSA-xx7v-hqxh-cjr9.json
- GHSA-rg58-xhh7-mqjw (CVE-2025-66675 / S2-068 variant): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2025/12/GHSA-rg58-xhh7-mqjw/GHSA-rg58-xhh7-mqjw.json
- GHSA-ccp5-gg58-pxfm (CVE-2019-0233): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-ccp5-gg58-pxfm/GHSA-ccp5-gg58-pxfm.json
- GHSA-86vq-8qhc-5rqw (CVE-2016-8738 / S2-044): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-86vq-8qhc-5rqw/GHSA-86vq-8qhc-5rqw.json
- GHSA-4qgj-9mvg-3929 (CVE-2015-5209): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-4qgj-9mvg-3929/GHSA-4qgj-9mvg-3929.json
- GHSA-q2cg-xf9p-h457 (CVE-2015-1831): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-q2cg-xf9p-h457/GHSA-q2cg-xf9p-h457.json
- GHSA-8f6x-v685-g2xc (CVE-2023-34149 / S2-063): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2023/06/GHSA-8f6x-v685-g2xc/GHSA-8f6x-v685-g2xc.json

### GHSA advisory files fetched for shiro-core (via WebFetch on raw.githubusercontent.com)
- GHSA-p836-389h-j692 (CVE-2016-4437): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/05/GHSA-p836-389h-j692/GHSA-p836-389h-j692.json
- GHSA-26gr-cvq3-qxgf (CVE-2020-1957): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/05/GHSA-26gr-cvq3-qxgf/GHSA-26gr-cvq3-qxgf.json
- GHSA-72w9-fcj5-3fcg (CVE-2020-11989): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/05/GHSA-72w9-fcj5-3fcg/GHSA-72w9-fcj5-3fcg.json
- GHSA-f6jp-j6w3-w9hm (CVE-2021-41303): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/09/GHSA-f6jp-j6w3-w9hm/GHSA-f6jp-j6w3-w9hm.json
- GHSA-4cf5-xmhp-3xj7 (CVE-2022-32532): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/06/GHSA-4cf5-xmhp-3xj7/GHSA-4cf5-xmhp-3xj7.json
- GHSA-45x9-q6vj-cqgq (CVE-2022-40664): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2022/10/GHSA-45x9-q6vj-cqgq/GHSA-45x9-q6vj-cqgq.json
- GHSA-2vgm-wxr3-6w2j (CVE-2020-13933): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2021/05/GHSA-2vgm-wxr3-6w2j/GHSA-2vgm-wxr3-6w2j.json
- GHSA-r679-m633-g7wc (CVE-2019-12422): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2020/02/GHSA-r679-m633-g7wc/GHSA-r679-m633-g7wc.json
- GHSA-x96m-rh44-vgv8 (CVE-2026-49268): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/06/GHSA-x96m-rh44-vgv8/GHSA-x96m-rh44-vgv8.json
- GHSA-jc7h-c423-mpjc (CVE-2023-46749): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/01/GHSA-jc7h-c423-mpjc/GHSA-jc7h-c423-mpjc.json
- GHSA-fcvm-3cpj-f9qx (CVE-2026-43827): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/05/GHSA-fcvm-3cpj-f9qx/GHSA-fcvm-3cpj-f9qx.json
- GHSA-c4qc-4q9p-m9q9 (CVE-2026-23901): https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2026/02/GHSA-c4qc-4q9p-m9q9/GHSA-c4qc-4q9p-m9q9.json

## Targets not pursued

- rust/zip: rustsec/advisory-db contains no advisory files for the `zip` crate (confirmed via mcp__github__search_code with multiple query formulations). Deferred.
- rust/image: Same result — no advisory files found in rustsec/advisory-db. Deferred.
- rust/nix: No advisory files found. Deferred.
