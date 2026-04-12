# Evidence Notes

## basic-ftp
- OSV/GHSA show three package advisories in 5.2.x:
  - GHSA-5rq4-664w-9x2c / CVE-2026-27699 fixed in 5.2.0 (path traversal in downloadToDir)
  - GHSA-chqc-8p9q-pq6q / CVE-2026-39983 introduced in 5.2.0 and fixed in 5.2.1 (FTP command injection via CRLF)
  - GHSA-6v7q-wjvx-w8wg fixed in 5.2.2 (incomplete CRLF injection protection)
- Upstream GitHub releases explicitly mention GHSA-chqc-8p9q-pq6q in v5.2.1 and GHSA-6v7q-wjvx-w8wg in v5.2.2.

## path-to-regexp
- OSV/GHSA show five published package advisories:
  - GHSA-rhx6-c78j-4q9w / CVE-2024-52798 fixed in 0.1.12 (ReDoS)
  - GHSA-9wv6-86v2-598j / CVE-2024-45296 fixed in 8.0.0 (backtracking ReDoS)
  - GHSA-37ch-88jc-xwx2 / CVE-2026-4867 fixed in 0.1.13 (multiple route parameters ReDoS)
  - GHSA-27v5-c462-wpq7 / CVE-2026-4923 fixed in 8.4.0 (multiple wildcards ReDoS)
  - GHSA-j3q9-mxjg-w52f / CVE-2026-4926 fixed in 8.4.0 (sequential optional groups DoS)
- Upstream v8.4.0 release notes explicitly call out fixes for CVE-2026-4923 and CVE-2026-4926, plus wildcard-backtracking restriction and rejection of large optional-route combinations.
- Current KB page also includes a public manual-audit issue (#433); keep it separate from the published advisory set.
