# Advisory review 2026-11-26 (UTC 0459): curl (Linux), Django (Python)

## Target selection
- Weekly news scan (WebSearch, 2026-11-26): CISA KEV additions 2026-11-18 to 2026-11-25 were all either already covered (LiteLLM, Axis, MONAI Label, Idunno.AntiCsrf, OpenSSH) or outside KB ecosystems (Drupal, Optimizely, Mitel, Danfoss, Juniper, Xen Orchestra, VMware, Cisco, SAP, Synology, REDCap, N-able, Apache Roller). OpenSSL fixed releases are scheduled for 2026-12-01.
- Fell back to stale pages: linux/curl (last updated 2026-06-15, newest row CVE-2025-0167) and python/django (last updated 2026-05-08, newest row CVE-2026-5766).

## URLs consulted
- https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json (catalog 2026.11.25; no curl or Django entries)
- https://raw.githubusercontent.com/curl/curl-www/master/docs/vuln.pm (upstream advisory index: first/last affected version, announce date, severity, scope)
- https://raw.githubusercontent.com/curl/curl-www/master/docs/CVE-2026-92392.md (HTTP/2 upload UAF; RCE preconditions; 8.20.2 / 8.16.2 / 8.14.3 backports)
- https://raw.githubusercontent.com/curl/curl/master/include/curl/curlver.h (master at 8.23.1-DEV)
- git ls-remote --tags https://github.com/curl/curl (release tags through curl-8_23_0, used to derive first fixed release)
- https://curl.se/docs/vuln.json (blocked, HTTP 403 from proxy)
- https://raw.githubusercontent.com/django/django/main/docs/releases/security.txt (Django security archive)
- https://github.com/django/django (sparse clone of docs/releases: 4.2.27-4.2.30, 5.2.11-5.2.20, 6.0.2-6.0.11, 6.1-6.1.4 release notes; CVE titles, Django severity, fixed releases, dates)
- https://pypi.org/pypi/django/json (latest version 6.1.3)
- Django weblog security posts cited per row (not fetched; URLs from security.txt): https://www.djangoproject.com/weblog/2026/{feb/03,mar/03,apr/07,jun/03,jul/07,aug/04,oct/06,nov/03}/security-releases/
- WebSearch: CISA KEV November 2026 roundups (dev.to, securityaffairs.com, shattered.io, senserva.com), only for lead discovery

## Results
- curl: 78 advisories 2025-02-05 to 2026-10-14 (1 High, 17 Medium, 60 Low). 77 new rows; CVE-2025-0167 corrected (was described as Medium WHOIS issue; upstream: Low netrc and default credential leak).
- Django: 29 rows added (2 CVE-2025, 27 CVE-2026) not previously listed. Django 5.2.20 / 6.0.11 / 6.1.4 notes dated 2026-12-02 pre-announce 2 high, 1 moderate, 4 low security fixes; not mapped (no details yet).

## Not done
- GHSA IDs for new Django and curl rows (upstream advisories cited instead).
- homebrew/curl still stops at CVE-2025-0167.
