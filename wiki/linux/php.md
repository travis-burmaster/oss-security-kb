# PHP (Linux)

**Registry:** distro (Debian/Ubuntu: `php`, `php8.x`; RHEL/Fedora: `php`, `php-cli`)
**Weekly Downloads:** unknown (system-level package managed by distro repositories)
**Repository:** https://github.com/php/php-src
**Security Contact:** security@php.net
**Disclosure Policy:** https://github.com/php/php-src/blob/master/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-09-17 | oss-security-kb nightly | advisory-review 2024–2026 | advisory-mapping (PHP 8.3/NEWS + GHSA) | 22 CVEs confirmed | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-4577 | Critical (CVSS 9.8) | CGI argument injection via Windows Best-Fit character substitution — unauthenticated RCE in PHP-CGI on Windows/Apache; CISA KEV; widely exploited | PHP 8.1.29 / 8.2.20 / 8.3.8 | [GHSA-vxpp-6299-mxw3](https://github.com/advisories/GHSA-vxpp-6299-mxw3) |
| CVE-2024-11236 | Critical | Integer overflow in DBLIB and Firebird database quoters — buffer overflow on attacker-controlled input | PHP 8.2.25 / 8.3.14 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-8926 | High | Bypass of CVE-2024-4577 CGI fix — incomplete mitigation allows argument injection on some Windows/IIS configurations | PHP 8.2.23 / 8.3.12 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-8927 | High | PHP-CGI `force_redirect` environment variable collision — bypass of redirect validation enables unauthorized CGI execution | PHP 8.2.23 / 8.3.12 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-1874 | High | Command injection via array parameter in `proc_open()` — array arguments bypass shell-argument escaping on Windows | PHP 8.1.28 / 8.2.18 / 8.3.6 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-3096 | High | `password_verify()` may return true for invalid password — authentication bypass risk with BCrypt | PHP 8.1.28 / 8.2.18 / 8.3.6 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-8929 | High | Heap buffer over-read in MySQLnd — memory disclosure to attacker-controlled MySQL server | PHP 8.2.25 / 8.3.14 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-8932 | High | Out-of-bounds access in `ldap_escape()` — crash or info leak on attacker-controlled input | PHP 8.2.25 / 8.3.14 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-11234 | High | CRLF injection via `stream_socket_client()` HTTP stream proxy context — enables HTTP request smuggling | PHP 8.2.25 / 8.3.14 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2025-6491 | High | NULL pointer dereference in SOAP XML namespace handling — crash on attacker-crafted SOAP response | PHP 8.3.23 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2026-17543 | High | SQL injection via backslash escaping in the PostgreSQL extension — incorrect escaping enables injection | PHP 8.3.34 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-2756 | Moderate | `__Host-`/`__Secure-` cookie prefix bypass in cookie parser | PHP 8.1.28 / 8.2.18 / 8.3.6 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-2757 | Moderate | Infinite loop in `mb_encode_mimeheader()` — DoS via attacker-controlled input | PHP 8.3.6 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-5458 | Moderate | URL validation bypass in `filter_var()` with `FILTER_VALIDATE_URL` | PHP 8.1.29 / 8.2.20 / 8.3.8 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-8925 | Moderate | Multipart form data parsing boundary detection error in SAPI | PHP 8.2.23 / 8.3.12 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-9026 | Moderate | PHP-FPM child process can alter parent log entries — log injection / tampering | PHP 8.2.23 / 8.3.12 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-11233 | Moderate | Single byte over-read in quoted-printable decode filter | PHP 8.2.25 / 8.3.14 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2024-2408 | Moderate | Marvin Attack timing side-channel in OpenSSL RSA decryption (PHP built against OpenSSL 3.2+) | PHP 8.3.8 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2025-1220 | Moderate | NULL byte termination vulnerability in hostname validation | PHP 8.2.28 / 8.3.22 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2025-1735 | Moderate | PostgreSQL extension escaping failure during query construction | PHP 8.2.29 / 8.3.23 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2026-6735 | Moderate | Stored XSS in PHP-FPM status endpoint — attacker-controlled request data reflected without escaping | PHP 8.3.31 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |
| CVE-2026-7259 | Moderate | NULL pointer dereference in MBString encoding detection — crash on attacker-crafted multi-byte input | PHP 8.3.31 | [PHP-8.3 NEWS](https://raw.githubusercontent.com/php/php-src/PHP-8.3/NEWS) |

## Security Posture Notes

PHP powers approximately 77% of web servers with a known server-side language. The vulnerability history shows recurring risk in three areas: CGI/SAPI boundary (CVE-2024-4577 and its bypass CVE-2024-8926 are the highest-impact — exploit code is publicly available and CISA KEV-listed), database extension escaping (DBLIB/Firebird integer overflow, PostgreSQL escaping failures, MySQLnd over-read), and standard library functions (ldap_escape, password_verify, proc_open, filter_var, mb_encode_mimeheader).

Support lifecycle: PHP 8.1 reached End of Life on 2024-11-25 and no longer receives security fixes. PHP 8.2 is in security-fixes-only mode through 2026-12-31. PHP 8.3 and 8.4 are actively maintained. Operators on distro-packaged PHP should verify that security backports are current; Debian Bookworm ships PHP 8.2, RHEL 9 ships PHP 8.1 (EOL).

CGI deployments on Windows remain the highest-severity attack surface. Migrating to PHP-FPM eliminates the CGI argument-injection class entirely.

CVSS scores are confirmed for CVE-2024-4577 (9.8) from GHSA. Scores for most other entries were sourced from the PHP NEWS file descriptions and are not independently confirmed against NVD (NVD was inaccessible during this pass).

## Dependencies of Note

- **libxml2** — PHP's XML/DOM/SimpleXML extensions link against system libxml2; libxml2 CVEs directly affect PHP's XML processing surface
- **OpenSSL** — PHP's OpenSSL extension links against system OpenSSL; CVE-2024-2408 is a direct PHP manifestation of the OpenSSL Marvin Attack timing side-channel
- **mysqlnd** — PHP's bundled MySQL Native Driver (not system libmysqlclient); mysqlnd bugs are PHP-internal, not MySQL Server bugs

## Open Questions

- CVE-2024-2408 Marvin Attack: affects only PHP built against OpenSSL ≥ 3.2 in RSA decryption paths. Distro packages may use older OpenSSL; scope not fully characterized.
- PHP 8.4 (released 2024-11-21): minimal CVE history mapped in this pass; NEWS file for 8.4 branch not yet reviewed.
- NVD CVSS scores: not confirmed due to NVD access block during this pass. Severity labels above follow PHP team severity language where available; CVE-2024-4577 (9.8) is the only GHSA-confirmed score.

## Related Pages

- [[linux/openssl]] — system OpenSSL linked by PHP's openssl extension
- [[linux/nginx]] — common LEMP stack reverse proxy in front of PHP-FPM
- [[linux/apache2]] — common LAMP stack pairing; PHP-CGI/mod_php deployments
