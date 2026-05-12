# OSS Security KB Update Proposal: `io.netty:netty-codec-http`

## Package Overview

| Field | Value |
|-------|-------|
| **Ecosystem** | Maven |
| **Group:Artifact** | `io.netty:netty-codec-http` |
| **Total tracked CVEs** | 15 |
| **Latest stable fix baseline** | 4.1.133.Final (4.1.x) / 4.2.13.Final (4.2.x) |
| **Maven latest release** | 5.0.0.Alpha2 (pre-release; not recommended for production) |

---

## Vulnerability Inventory (Chronological by Fix Version)

### 1. Legacy / Pre-2021 Fixes

| CVE | GHSA | Summary | Type | Fixed In |
|-----|------|---------|------|----------|
| CVE-2019-20444 | GHSA-cqqj-4p63-rrmm | HTTP Request Smuggling via malformed headers | Request Smuggling | 4.1.44 |

### 2. 2021 Fixes

| CVE | GHSA | Summary | Type | Fixed In |
|-----|------|---------|------|----------|
| CVE-2021-21290 | GHSA-5mcr-gq6c-3hq2 | Local info disclosure on Unix-like systems (temp file handling) | Info Disclosure | 4.1.59.Final |
| CVE-2021-43797 | GHSA-wx5j-54mm-rqqq | HTTP request smuggling via improper whitespace/control-char handling | Request Smuggling | 4.1.71.Final |

### 3. 2022 Fixes

| CVE | GHSA | Summary | Type | Fixed In |
|-----|------|---------|------|----------|
| CVE-2022-24823 | GHSA-269q-hmxg-m83q | Local info disclosure in HTTP codec temp file handling | Info Disclosure | 4.1.77.Final |
| CVE-2022-41915 | GHSA-hh82-3pmq-7frp | HTTP Response Splitting via header value iterator | Response Splitting | 4.1.86.Final |

### 4. 2024 Fixes

| CVE | GHSA | Summary | Type | Fixed In |
|-----|------|---------|------|----------|
| CVE-2024-29025 | GHSA-5jpm-x58v-624v | HttpPostRequestDecoder unbounded memory allocation (OOM/DoS) | DoS | 4.1.108.Final |

### 5. 2025 Fixes

| CVE | GHSA | Summary | Type | Fixed In (4.1.x / 4.2.x) |
|-----|------|---------|------|----------|
| CVE-2025-58056 | GHSA-fghv-69vj-qj49 | Request smuggling via incorrect chunk extension parsing | Request Smuggling | 4.1.125.Final / 4.2.5.Final |
| CVE-2025-67735 | GHSA-84h7-rjj3-6jx4 | CRLF Injection in HttpRequestEncoder | Injection | 4.1.129.Final / 4.2.8.Final |

### 6. 2026 Fixes (May 2026 Cluster — 6 CVEs)

| CVE | GHSA | Summary | Type | Fixed In (4.1.x / 4.2.x) |
|-----|------|---------|------|----------|
| CVE-2026-33870 | GHSA-pwqr-wmgm-9rr8 | Request smuggling via chunked extension quoted-string parsing | Request Smuggling | 4.1.132.Final / 4.2.10.Final |
| CVE-2026-42580 | GHSA-m4cv-j2px-7723 | Request smuggling via incorrect chunk size parsing | Request Smuggling | 4.1.133.Final / 4.2.13.Final |
| CVE-2026-42581 | GHSA-xxqh-mfjm-7mv9 | HTTP/1.0 TE+CL coexistence bypasses smuggling sanitization | Request Smuggling | 4.1.133.Final / 4.2.13.Final |
| CVE-2026-42584 | GHSA-57rv-r2g8-2cj3 | HttpClientCodec response desynchronization | Request Smuggling | 4.1.133.Final / 4.2.13.Final |
| CVE-2026-42585 | GHSA-38f8-5428-x5cv | Request smuggling via malformed Transfer-Encoding | Request Smuggling | 4.