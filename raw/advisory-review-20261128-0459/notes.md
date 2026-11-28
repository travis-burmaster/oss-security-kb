# Advisory-review pass 2026-11-28 04:59 UTC — GeoServer

Trigger: CISA KEV catalog 2026.11.27 added GeoServer CVE-2026-120705 and CVE-2026-129243 on 2026-11-27 (due 2026-11-30). No KB page for GeoServer existed.

## Sources consulted

### CISA KEV
- https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json (catalogVersion 2026.11.27, released 2026-11-27T18:03Z)
  - New since last pass: CVE-2026-120705, CVE-2026-129243 (GeoServer), CVE-2026-136716 (Drupal core, out of scope)
  - Earlier GeoServer KEV entries: CVE-2024-36401 (2024-07-15), CVE-2025-58360 (2025-12-11), CVE-2022-24816 (jai-ext, listed under GeoServer, 2024-06-26)
  - KEV notes cite https://geoserver.org/vulnerability/2026/11/23/cve-update.html, GHSA-39mw-5chv-jh47, GHSA-rv5g-g2r9-58rj

### GeoServer upstream (via GitHub; geoserver.org blocked)
- https://raw.githubusercontent.com/geoserver/geoserver.github.io/main/_posts/2026-11-23-cve-update.md (17 October-release CVEs, RCE chain order, CVE-2025-53607, CVE-2024-35233)
- https://raw.githubusercontent.com/geoserver/geoserver.github.io/main/_posts/2026-09-28-cve-update.md (CVE-2026-76904 zero-day, June 2026 CVEs, GHSA-cpc9-c4h3-2jwx supply-chain advisory, AI report policy)
- geoserver/geoserver.github.io _posts (sparse clone, last commit 2026-11-23): 2026-10-19-geoserver-3-0-2-released.md, 2026-10-19-geoserver-2-28-6-released.md, 2026-10-19-geoserver-2-27-7-released.md (per-release CVE lists; CVE-2026-129245 listed only in 3.0.2), 2026-08-14-geoserver-{3-0-1,2-28-5,2-27-6}-released.md, 2026-06-11-geoserver-3-0-0-released.md, 2026-05-25-geoserver-2-28-4-released.md, 2026-11-18-java4shell-mitigation.md
- git ls-remote --tags https://github.com/geoserver/geoserver (latest tags 3.0.2, 2.28.6, 2.27.7)
- Repository advisories cited (HTML pages not fetched; github.com advisory HTML is blocked): https://github.com/geoserver/geoserver/security/advisories/ GHSA-hgm3-wq4h-8vvq, GHSA-39mw-5chv-jh47, GHSA-rv5g-g2r9-58rj, GHSA-9wf2-fcgq-vxhq, GHSA-wc3v-48j7-xf57, GHSA-3x82-qq72-g4p3, GHSA-5v3x-f56f-2xm8, GHSA-37mm-jp7f-64jp, GHSA-9j5h-q8xc-hppq, GHSA-vv34-hm2r-7h59, GHSA-65mr-5frw-93xf, GHSA-3xvw-cfcr-v3h7, GHSA-4v26-c537-jvxc, GHSA-rg89-jmrw-x26f, GHSA-9vfc-p7x6-xxwh, GHSA-8w5h-q76f-7mc7, GHSA-jvpx-6qxg-whgc, GHSA-cggp-wx63-hrxr, GHSA-hw87-7mx2-47cw; https://github.com/GeoWebCache/geowebcache/security/advisories/GHSA-xqwh-vc83-cp7g

### GitHub Advisory Database
- gh api search/code: `"org.geoserver" repo:github/advisory-database` (35 paths), `GeoServer repo:github/advisory-database` (40 paths); none of the October 2026 records.
- Sparse clone of github/advisory-database (HEAD 2026-11-28 03:35 UTC), grep for the 2026 GeoServer CVE IDs: no records for the 17 October CVEs, CVE-2025-53607 or CVE-2024-35233. Found GeoTools GHSA-mqjf-5f49-2fjh (CVE-2026-76904, gt-jdbc-postgis, fixed 35.1/34.5/33.6).
- Raw records fetched from https://raw.githubusercontent.com/github/advisory-database/main/<path> for: GHSA-382v-j99g-hw2p, GHSA-4pm3-f52j-8ggh, GHSA-56r3-f536-5gf7, GHSA-59x6-g4jr-4hxc, GHSA-5gw5-jccf-6hxw, GHSA-5pr3-m5hm-9956, GHSA-68cf-j696-wvv9, GHSA-6jj6-gm7p-fcvv, GHSA-6pfc-w86r-54q6, GHSA-75m5-hh4r-q9gx, GHSA-7g5f-wrx8-5ccf, GHSA-7qmg-grcp-qf25, GHSA-7x76-57fr-m5r5, GHSA-826p-4gcg-35vw (GeoTools, deps only), GHSA-88wc-fcj9-q3r9, GHSA-8g7v-vjrc-x4g5, GHSA-8hmh-mhqv-7638, GHSA-9rfr-pf2x-g4xf, GHSA-9v5q-2gwq-q9hq, GHSA-cqpc-x2c6-2gmf, GHSA-fcpm-hchj-mh72, GHSA-fg9v-56hw-g525, GHSA-fh7p-5f6g-vj2w, GHSA-fjf5-xgmq-5525, GHSA-g628-r368-6vh7, GHSA-gr67-pwcv-76gf, GHSA-h86g-x8mm-78m5, GHSA-j59v-vgcr-hxvf, GHSA-jhqx-5v5g-mpf3, GHSA-jj54-8f66-c5pc, GHSA-jm79-7xhw-6f6f, GHSA-mc43-4fqr-c965, GHSA-r4hf-r8gj-jgw2, GHSA-rr33-j5p5-ppf8, GHSA-v92f-jx6p-73rx (jai-ext, deps only), GHSA-w66h-j855-qr72, GHSA-wf6j-gr27-g7ch, GHSA-x4r9-gmw3-hxww. Excluded GeoNode records GHSA-mcmc-c59m-pqq8 and GHSA-pxg5-h34r-7q8p.

### Other
- https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/2026/120xxx/CVE-2026-120705.json (and 129242-129245): HTTP 404
- https://repo1.maven.org/maven2/org/geoserver/web/gs-web-app/maven-metadata.xml: HTTP 404 (GeoServer not on Maven Central)
- repo.osgeo.org, geoserver.org: blocked by proxy (HTTP 403)
- WebSearch "open source vulnerability actively exploited November 2026": no further in-scope lead (Xen Orchestra, Chromium out of scope or covered)

## Counts
- 56 advisories: 36 GHSA-database (4 Critical, 14 High, 18 Moderate) + 20 upstream-only (2 Critical, 14 High, 4 Medium). 4 GeoServer CVEs on CISA KEV.
