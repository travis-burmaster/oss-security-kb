# OSS Security KB Update Proposal: PyPI `twisted`

## Recommended Page Status

**ACTIVE — High Relevance**

Twisted has a substantial, long-running history of security vulnerabilities spanning over a decade (2014–2026), across multiple subsystems (web, SSH, DNS, HTTP/2). The project is actively maintained with a consistent pattern of security fixes. This package warrants a dedicated, maintained KB page.

---

## Representative Vulnerability Classes

| Category | CVE / Advisory Examples | Description |
|---|---|---|
| **HTTP Request Smuggling / Desync** | CVE-2020-10108, CVE-2020-10109, CVE-2022-24801, GHSA-8r99-h8j2-rw64 | Inconsistent HTTP parsing in `twisted.web` enabling request smuggling via malformed Content-Length, chunked encoding, or ambiguous request boundaries. |
| **HTTP Pipeline Response Disordering** | CVE-2023-46137, CVE-2024-41671 | Responses sent to wrong pipelined requests, potentially leaking data across clients. |
| **Improper Certificate Validation** | CVE-2014-7143, CVE-2019-12855 | `trustRoot` ignored in HTTP client; improper hostname verification in TLS. |
| **CRLF / Header Injection** | CVE-2019-12387, CVE-2022-39348 | Header injection via unsanitized input in HTTP requests or NameVirtualHost routing. |
| **Cookie / Credential Exposure on Redirect** | CVE-2022-21712 | Sensitive headers (cookies, auth) leaked to cross-origin redirect targets. |
| **HTML Injection (Reflected XSS)** | CVE-2024-41810 | Unsanitized user input reflected in HTTP redirect response bodies. |
| **Denial of Service (DoS)** | GHSA-32gv-6cf3-wcmq (HTTP/2 floods), CVE-2022-21716 (SSH handshake), CVE-2026-42304 (DNS compression pointers) | Resource exhaustion via protocol-level abuse in HTTP/2, SSH, and DNS subsystems. |
| **Forced Browsing / Proxy Header Trust** | CVE-2016-1000111 | Trusting `X-Forwarded-For` or similar headers without validation, enabling spoofing. |

---

## Notable Fixed Versions (Chronological)

| Version | Key Fixes |
|---|---|
| **14.0.1** | TLS trustRoot bypass (CVE-2014-7143) |
| **16.3.1** | Proxy header trust / forced browsing (CVE-2016-1000111) |
| **19.2.1** | CRLF injection in HTTP client (CVE-2019-12387) |
| **19.7.0** | Improper certificate validation (CVE-2019-12855) |
| **19.10.0** | HTTP/2 DoS (ping/reset/settings floods) |
| **20.3.0** | HTTP request smuggling cluster — three distinct advisories (CVE-2020-10108, CVE-2020-10109, GHSA-8r99) |
| **22.1.0** | Cookie/header exposure on cross-origin redirect (CVE-2022-21712) |
| **22.2.0** | SSH handshake DoS (CVE-2022-21716) |
| **22.4.0** | HTTP request smuggling in `twisted.web` (CVE-2022-24801) |
| **22.10.0** | NameVirtualHost header injection (CVE-2022-39348) |
| **23.10.0** | HTTP pipeline response disordering (CVE-2023-46137) |
| **24.7.0** | Pipeline disordering recurrence (CVE-2024-41671) + HTML injection in redirects (CVE-2024-41810) |
| **26.4.0** | DNS compression pointer chain DoS (CVE-2026-42304) |

**Minimum recommended version: ≥ 24.7.0** for web-facing deployments; **≥ 26.4.0** if using `twisted.names`.

---

## Cautions & Open Questions

1. **Recurring vulnerability patterns**: HTTP request smuggling and pipeline response disordering have each required multiple fixes across years (2020 → 2022 → 2023 → 2024). This suggests structural parsing complexity in `twisted.web` that may yield further variants.

2. **RC-tagged fixes**: Several advisories list release candidates (e.g., `24.7.0rc1`, `23.10.0rc1`, `26.4.0rc2`) as the fixed version. KB consumers should verify they are using the corresponding **stable** release, not just the RC.

3. **CVE-2026-42304 