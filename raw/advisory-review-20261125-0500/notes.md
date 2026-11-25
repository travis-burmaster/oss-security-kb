# Advisory review 2026-11-25 05:00 UTC

Targets: linux/glibc (update), dotnet/Idunno.AntiCsrf (new).

## Selection
- CISA KEV catalog 2026.11.24: https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json
  - Additions 2026-11-15 to 2026-11-24 reviewed. New since last pass: CVE-2026-131914 (Idunno AntiCsrf), CVE-2026-132165 (Drupal Core), CVE-2026-132224 (Optimizely). Only AntiCsrf fits a KB ecosystem (.NET).
  - No glibc entry added in 2026 (only CVE-2023-4911, added 2023-11-21).
- Web search (past 7 days of OSS advisories): glibc advisory update 2026-11-19 (oss-security), OpenSSL low-severity advisories, PHP/OpenJDK (already covered 2026-11-21/24), Node.js 2026-11-11.
  - https://www.openwall.com/lists/oss-security/2026/11/19/9 (blocked from this environment; seen only in search results)
  - https://ubuntu.com/security/notices/USN-9065-1 (search result only)
- Search for the 2.44 release date (secondary, used only for the "current stable" line): https://openwall.com/lists/oss-security/2026/07/25/1 , https://gitlab.com/gnutools/glibc/-/tags/glibc-2.44

## glibc
- Upstream advisories GLIBC-SA-2026-0001 to GLIBC-SA-2026-0032 (all fetched, HTTP 200; 0033-0040 returned non-200):
  https://gitlab.com/gnutools/glibc/-/raw/master/advisories/GLIBC-SA-2026-00NN
- Upstream NEWS (2.45 dev section has no security list yet; 2.44 section lists GLIBC-SA-2026-0005/0006/0007; 2.43 lists 0001/0002/0003):
  https://gitlab.com/gnutools/glibc/-/raw/master/NEWS
- Stale mirror (stops at GLIBC-SA-2026-0003; NEWS at 2.43): https://raw.githubusercontent.com/bminor/glibc/master/advisories/
- GitHub code search: `"GNU C Library" path:advisories/unreviewed/2026 repo:github/advisory-database` (31 hits) and `glibc path:advisories/unreviewed/2026 ...` (13 extra hits, all other products except GHSA-7qhw-4fcq-2g37 / CVE-2025-0577, already on page).
- GHSA records fetched from https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/<YYYY>/<MM>/<ID>/<ID>.json:
  GHSA-5pf6-63v3-88hw (CVE-2026-0861), GHSA-xp56-6525-9chf (CVE-2026-0915), GHSA-qg56-4cfq-w9w3 (CVE-2025-15281),
  GHSA-3584-5r39-4gm3 (CVE-2026-3904), GHSA-m5wq-r4r4-4qrh (CVE-2026-4437), GHSA-935r-rfch-9mr7 (CVE-2026-4438),
  GHSA-g7c4-wv7q-gcc6 (CVE-2026-4046), GHSA-jj2g-xq7w-gf88 (CVE-2026-5358, rejected upstream), GHSA-v898-xg3c-w4rj (CVE-2026-5450),
  GHSA-829p-mc9m-7xhr (CVE-2026-5928), GHSA-32rw-r8mp-pw42 (CVE-2026-5435), GHSA-h8wx-jcwq-g3cp (CVE-2026-6238),
  GHSA-cm6j-gmqf-j2cm (CVE-2026-6368), GHSA-qg52-8pr2-xj9v (CVE-2026-18374), GHSA-gwqp-9qgw-c5pv (CVE-2026-89092),
  GHSA-3vcj-mghm-mw9p (CVE-2026-19499), GHSA-hhcv-vc8h-vmrg (CVE-2026-19542), GHSA-g8c6-x9r9-wj7f (CVE-2026-77117),
  GHSA-w45w-pf39-v4pp (CVE-2026-80489), GHSA-qghr-qhfc-4hxp (CVE-2026-8674), GHSA-fmf4-pr35-46c2 (CVE-2026-86805),
  GHSA-h8x4-734c-9753 (CVE-2026-95818), GHSA-qhjw-2xw3-v2hv (CVE-2026-97399), GHSA-8rvm-662m-jvqv (CVE-2026-84243),
  GHSA-5wwm-g25c-cpx8 (CVE-2026-122054), GHSA-rm44-gpwr-xh4q (CVE-2026-115819), GHSA-qvhh-2rc2-h32w (CVE-2026-100290),
  GHSA-2v8f-vf2j-8gc4 (CVE-2026-121757), GHSA-w866-p776-r4v9 (CVE-2026-121758), GHSA-357v-hpjh-7cmw (CVE-2026-124024),
  GHSA-4rvq-wr96-324w (CVE-2026-126765)
- No GHSA found for CVE-2026-6791 (GLIBC-SA-2026-0013).
- Note: GHSA-w866-p776-r4v9 and GHSA-357v-hpjh-7cmw reference "GLIBC-SA-2026-00230" / "-00231"; the upstream files are GLIBC-SA-2026-0030 / -0031 (CVE IDs match).
- Unreachable: sourceware.org gitweb (no response), www.openwall.com (no response).

## Idunno.AntiCsrf
- Mandiant MNDT-2026-0048: https://raw.githubusercontent.com/mandiant/Vulnerability-Disclosures/master/2026/MNDT-2026-0048.md
- GHSA-pj2m-2r8v-h9cp: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/11/GHSA-pj2m-2r8v-h9cp/GHSA-pj2m-2r8v-h9cp.json
- GitHub code search `AntiCsrf repo:github/advisory-database`: also returned GHSA-xxqc-84hc-65cr (xunfeng, Python, unrelated) and GHSA-wfwm-vf76-3692 (Sitecore CVE-2019-9874, different product).
- KEV entry CVE-2026-131914 (catalog 2026.11.24; dateAdded 2026-11-24, dueDate 2026-11-27, forensicTriage Yes).
- NuGet: https://api.nuget.org/v3/registration5-gz-semver2/idunno.anticsrf/index.json returned BlobNotFound (no NuGet package).
- Not fetched: https://codeplexarchive.org/project/AntiCSRF, https://nvd.nist.gov/vuln/detail/CVE-2026-131914 (NVD blocked).
