# Advisory Review — 2026-07-23 0600 UTC

## Targets

- linux/wget (new page)
- linux/tar (new page)
- homebrew/ffmpeg (new page)

## Method

- OSV.dev API: blocked (HTTP 403) — not used
- formulae.brew.sh API: blocked (HTTP 403) — not used for stats
- Advisory sources: github/advisory-database via mcp__github__search_code + WebFetch on raw.githubusercontent.com
- Formula versions: Homebrew/homebrew-core raw formula files via raw.githubusercontent.com

## URLs consulted

### linux/wget
- https://github.com/advisories/GHSA-5w8p-rj9f-xvj7 (CVE-2016-4971)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-5w8p-rj9f-xvj7/GHSA-5w8p-rj9f-xvj7.json
- https://github.com/advisories/GHSA-mxm6-6r3r-6wj4 (CVE-2018-20483)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-mxm6-6r3r-6wj4/GHSA-mxm6-6r3r-6wj4.json
- https://github.com/advisories/GHSA-fhwx-v7qv-pjh3 (CVE-2019-5953)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-fhwx-v7qv-pjh3/GHSA-fhwx-v7qv-pjh3.json
- https://github.com/advisories/GHSA-2j66-vp53-phjj (CVE-2024-38428)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2024/06/GHSA-2j66-vp53-phjj/GHSA-2j66-vp53-phjj.json
- https://github.com/advisories/GHSA-mqrm-h2pw-9j9r (CVE-2024-10524)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2024/11/GHSA-mqrm-h2pw-9j9r/GHSA-mqrm-h2pw-9j9r.json
- https://github.com/advisories/GHSA-77jw-q7w3-q2hw (CVE-2026-15146)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2026/07/GHSA-77jw-q7w3-q2hw/GHSA-77jw-q7w3-q2hw.json
- Current version: https://raw.githubusercontent.com/Homebrew/homebrew-core/master/Formula/w/wget.rb → 1.25.0

### linux/tar
- https://github.com/advisories/GHSA-c6fq-h555-8326 (CVE-2002-0399)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/04/GHSA-c6fq-h555-8326/GHSA-c6fq-h555-8326.json
- https://github.com/advisories/GHSA-43w6-q9mv-9cwf (CVE-2007-4131)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-43w6-q9mv-9cwf/GHSA-43w6-q9mv-9cwf.json
- https://github.com/advisories/GHSA-4qpm-74c6-fg44 (CVE-2016-6321 POINTYFEATHER)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-4qpm-74c6-fg44/GHSA-4qpm-74c6-fg44.json
- https://github.com/advisories/GHSA-h2v4-4v4p-2qvc (CVE-2022-48303)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2023/01/GHSA-h2v4-4v4p-2qvc/GHSA-h2v4-4v4p-2qvc.json
- https://github.com/advisories/GHSA-f93m-9mq4-2fjj (CVE-2025-45582)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2025/07/GHSA-f93m-9mq4-2fjj/GHSA-f93m-9mq4-2fjj.json
- Current version: https://raw.githubusercontent.com/Homebrew/homebrew-core/master/Formula/g/gnu-tar.rb → 1.35

### homebrew/ffmpeg
- https://github.com/advisories/GHSA-4p87-h585-c5xj (CVE-2016-1897)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-4p87-h585-c5xj/GHSA-4p87-h585-c5xj.json
- https://github.com/advisories/GHSA-2mw9-cpc8-cf9f (CVE-2016-1898)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2022/05/GHSA-2mw9-cpc8-cf9f/GHSA-2mw9-cpc8-cf9f.json
- https://github.com/advisories/GHSA-7q2g-j3r8-hgwh (CVE-2024-7272)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2024/08/GHSA-7q2g-j3r8-hgwh/GHSA-7q2g-j3r8-hgwh.json
- https://github.com/advisories/GHSA-5gxm-744m-qfgp (CVE-2024-7055)
  - raw: https://raw.githubusercontent.com/github/advisory-database/main/advisories/unreviewed/2024/08/GHSA-5gxm-744m-qfgp/GHSA-5gxm-744m-qfgp.json
- Current version: https://raw.githubusercontent.com/Homebrew/homebrew-core/master/Formula/f/ffmpeg.rb → 8.1.2

## Notes

- github/advisory-database search returned 82 total results for "wget CVE"; 545 for "ffmpeg CVE"; 6 for "GNU tar CVE path-traversal". Representative sets selected from these.
- CVE-2026-15146 (wget FTP PASV) was published 2026-07-10 in advisory-database; no fixed tagged version confirmed as of 2026-07-23.
- CVE-2025-45582 (tar two-step symlink) was published 2025-07-11; no fixed tagged version confirmed.
- FFmpeg total NVD CVE count estimated at 700+ per advisory text and NVD reference in sources; a single pass can map only a representative subset.
