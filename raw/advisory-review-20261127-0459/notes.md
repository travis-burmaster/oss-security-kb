# Advisory-review pass 2026-11-27 (UTC 0459)

Targets: Apache Roller (new Maven page), Linux kernel nfsd CVE-2026-99362 "NFS2ROOT" (new Linux page).

## News / selection
- WebSearch (extended): "open source vulnerability advisory November 2026 CVE patch". Leads: Drupal SA-CORE-2026-019 (out of scope), Linux nfsd CVE-2026-99362 (opensec.in write-up), nginx / OpenJDK / httpd items already covered by 2026-11-19 to 2026-11-24 passes.
- CISA KEV: https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json (catalogVersion 2026.11.25). Entries added 2026-11-19 to 2026-11-25 reviewed; CVE-2026-129448 (Apache Roller, added 2026-11-20) not yet in KB. CVE-2026-99362 not in KEV.

## Linux kernel CVE-2026-99362
- https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/2026/99xxx/CVE-2026-99362.json (kernel CNA, published 2026-11-19T14:22Z, updated 2026-11-23; CVSS 3.1 9.8; affected 3.16+; fixed 5.10.275, 5.15.226, 6.1.193, 6.6.163, 6.12.117, 6.18.61, 7.3.2, 7.4-rc1)
- Stable fix commits listed in the record:
  - https://git.kernel.org/stable/c/aff12e327620258123f847d7d06565f4555c5cb4
  - https://git.kernel.org/stable/c/6a26c5473bb112d8420ffd48d5331bc5fb5a2065
  - https://git.kernel.org/stable/c/fa85acf074f000ad3d1a5ffb703128ff97de983d
  - https://git.kernel.org/stable/c/cd303eb29cf34a6780f4c42aca5b8ca4a05a5d59
  - https://git.kernel.org/stable/c/1a5a227bca6a8a9f9d31230697aeb84c62a21da6
  - https://git.kernel.org/stable/c/37fc2ec211630360e9aefcaaec8730db964645f2
  - https://git.kernel.org/stable/c/ed98b0c57e5e84290c5b35428144ab26778905f3
  - https://git.kernel.org/stable/c/35ff1a7a7e3835c3e974bc5c45d335897564ceae
- https://opensec.in/blog/nfs2root-cve-2026-99362 (BLOCKED: DNS did not resolve; title seen only in search results; claims not verified)

## Apache Roller
- https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/2026/129xxx/CVE-2026-129448.json (Apache CNA; 4.0.0 to <6.1.5; active exploitation; CISA ADP KEV 2026-11-20; workaround text)
- https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/2026/82xxx/CVE-2026-82384.json
- gh api search/code: `"Apache Roller" repo:github/advisory-database` (paginated) and `org.apache.roller repo:github/advisory-database`; 47 unique records, all under advisories/unreviewed/, none with a package mapping
- GHSA raw records, each fetched from https://raw.githubusercontent.com/github/advisory-database/main/<path>:
  - advisories/unreviewed/2022/05/GHSA-2p7r-hc45-r2qc/GHSA-2p7r-hc45-r2qc.json
  - advisories/unreviewed/2022/05/GHSA-38f5-5m8x-c6h5/GHSA-38f5-5m8x-c6h5.json
  - advisories/unreviewed/2022/05/GHSA-9x4r-29pc-p3hh/GHSA-9x4r-29pc-p3hh.json
  - advisories/unreviewed/2022/05/GHSA-f4j4-8x73-vjx4/GHSA-f4j4-8x73-vjx4.json
  - advisories/unreviewed/2022/05/GHSA-g2p9-qx45-9p93/GHSA-g2p9-qx45-9p93.json
  - advisories/unreviewed/2022/05/GHSA-gm66-g5rh-xr6p/GHSA-gm66-g5rh-xr6p.json
  - advisories/unreviewed/2022/05/GHSA-mwgg-25xm-cfpx/GHSA-mwgg-25xm-cfpx.json
  - advisories/unreviewed/2022/05/GHSA-pgr4-3qq3-xcpv/GHSA-pgr4-3qq3-xcpv.json
  - advisories/unreviewed/2022/05/GHSA-pmpw-mfxc-wvmv/GHSA-pmpw-mfxc-wvmv.json
  - advisories/unreviewed/2023/08/GHSA-mccf-357g-w594/GHSA-mccf-357g-w594.json
  - advisories/unreviewed/2024/07/GHSA-g9rf-qc6j-h2f7/GHSA-g9rf-qc6j-h2f7.json
  - advisories/unreviewed/2024/10/GHSA-m3gr-45jc-g2rp/GHSA-m3gr-45jc-g2rp.json
  - advisories/unreviewed/2025/04/GHSA-fqfw-5jc9-hw27/GHSA-fqfw-5jc9-hw27.json
  - advisories/unreviewed/2026/09/GHSA-33v7-638r-hch5/GHSA-33v7-638r-hch5.json
  - advisories/unreviewed/2026/09/GHSA-4hv4-w9v7-8mr5/GHSA-4hv4-w9v7-8mr5.json
  - advisories/unreviewed/2026/09/GHSA-4jqc-cjj3-x26w/GHSA-4jqc-cjj3-x26w.json
  - advisories/unreviewed/2026/09/GHSA-7gp3-prr3-4599/GHSA-7gp3-prr3-4599.json
  - advisories/unreviewed/2026/09/GHSA-9rhg-vvf7-p29p/GHSA-9rhg-vvf7-p29p.json
  - advisories/unreviewed/2026/09/GHSA-c34v-mgwv-92x6/GHSA-c34v-mgwv-92x6.json
  - advisories/unreviewed/2026/09/GHSA-cp7g-8wv7-92w2/GHSA-cp7g-8wv7-92w2.json
  - advisories/unreviewed/2026/09/GHSA-crwh-hjp8-p7q9/GHSA-crwh-hjp8-p7q9.json
  - advisories/unreviewed/2026/09/GHSA-f2jw-h484-m8xv/GHSA-f2jw-h484-m8xv.json
  - advisories/unreviewed/2026/09/GHSA-fp83-p2jc-p38w/GHSA-fp83-p2jc-p38w.json
  - advisories/unreviewed/2026/09/GHSA-gxxm-hxjp-gc3f/GHSA-gxxm-hxjp-gc3f.json
  - advisories/unreviewed/2026/09/GHSA-hc2f-pj8f-5vww/GHSA-hc2f-pj8f-5vww.json
  - advisories/unreviewed/2026/09/GHSA-hfqv-pmcp-9hpg/GHSA-hfqv-pmcp-9hpg.json
  - advisories/unreviewed/2026/09/GHSA-j4w8-34rj-87r3/GHSA-j4w8-34rj-87r3.json
  - advisories/unreviewed/2026/09/GHSA-j58r-vr8w-6j93/GHSA-j58r-vr8w-6j93.json
  - advisories/unreviewed/2026/09/GHSA-mw5j-2pgh-fm6m/GHSA-mw5j-2pgh-fm6m.json
  - advisories/unreviewed/2026/09/GHSA-v625-qw46-3c92/GHSA-v625-qw46-3c92.json
  - advisories/unreviewed/2026/09/GHSA-xg59-jgm4-xmq5/GHSA-xg59-jgm4-xmq5.json
  - advisories/unreviewed/2026/11/GHSA-6rpr-3cmq-j84c/GHSA-6rpr-3cmq-j84c.json
  - advisories/unreviewed/2026/11/GHSA-6v7m-223w-55wp/GHSA-6v7m-223w-55wp.json
  - advisories/unreviewed/2026/11/GHSA-7jhv-jpvr-w92r/GHSA-7jhv-jpvr-w92r.json
  - advisories/unreviewed/2026/11/GHSA-chjw-mx5g-h9jm/GHSA-chjw-mx5g-h9jm.json
  - advisories/unreviewed/2026/11/GHSA-fp2h-r7g9-hq37/GHSA-fp2h-r7g9-hq37.json
  - advisories/unreviewed/2026/11/GHSA-g82c-vmxh-2c3f/GHSA-g82c-vmxh-2c3f.json
  - advisories/unreviewed/2026/11/GHSA-hhp3-h5fc-wr9j/GHSA-hhp3-h5fc-wr9j.json
  - advisories/unreviewed/2026/11/GHSA-hrf9-352c-rrmj/GHSA-hrf9-352c-rrmj.json
  - advisories/unreviewed/2026/11/GHSA-jm23-4q7g-qcr4/GHSA-jm23-4q7g-qcr4.json
  - advisories/unreviewed/2026/11/GHSA-jq4j-xm3m-rwf8/GHSA-jq4j-xm3m-rwf8.json
  - advisories/unreviewed/2026/11/GHSA-m6c4-53vv-535v/GHSA-m6c4-53vv-535v.json
  - advisories/unreviewed/2026/11/GHSA-pxp4-phq9-fx2q/GHSA-pxp4-phq9-fx2q.json
  - advisories/unreviewed/2026/11/GHSA-q96p-m6xp-j9ch/GHSA-q96p-m6xp-j9ch.json
  - advisories/unreviewed/2026/11/GHSA-x95f-2r7c-5mv3/GHSA-x95f-2r7c-5mv3.json
  - advisories/unreviewed/2026/11/GHSA-xw5v-gjqf-qvpm/GHSA-xw5v-gjqf-qvpm.json
  - advisories/unreviewed/2026/11/GHSA-xwqc-wpw7-xxrq/GHSA-xwqc-wpw7-xxrq.json
- `git ls-remote --tags https://github.com/apache/roller` (newest release tag roller-6.1.7; roller-6.1.8-rc1..rc3 and roller-7.0.0-rc1 present)
- https://raw.githubusercontent.com/apache/roller/roller-6.1.7/app/pom.xml (artifact roller-webapp, packaging war)
- https://repo1.maven.org/maven2/org/apache/roller/{roller-weblogger,roller-webapp,roller-project}/maven-metadata.xml (HTTP 404; one earlier request hit HTTP 429 rate limit)

## Environment notes
- git push via session proxy works (dry-run to refs/heads/access-check succeeded).
- raw.githubusercontent.com/CVEProject/cvelistV5 works for full CVE JSON (CNA + CISA ADP containers).
- opensec.in: DNS blocked.
