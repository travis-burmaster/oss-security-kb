

# OSS Security KB Maintenance Update Review

## Package: `org.apache.tomcat.embed:tomcat-embed-core`

**Review Date:** Based on public evidence gathered through April 2026
**Source:** OSV/GHSA database, NVD, Apache mailing lists

---

## 1. Executive Summary

The package shows **64 tracked OSV entries** spanning 2008–2026, with a pronounced acceleration: **23 CVEs in 2025–2026 alone** (36% of total). The vulnerability surface is dominated by DoS/HTTP2 issues (33%) and information disclosure (22%), but the recent wave introduces repeated **CLIENT_CERT authentication bypass** and **security constraint bypass** patterns that warrant elevated attention.

---

## 2. Recommended Vulnerability Class Taxonomy

Update the KB index to reflect these representative classes, ranked by frequency:

| # | Class | Count | Representative CVEs | Trend |
|---|-------|-------|-------------------|-------|
| 1 | **DoS / Resource Exhaustion (HTTP/2, multipart)** | 21 | CVE-2023-44487 (Rapid Reset), CVE-2024-34750, CVE-2025-48988, CVE-2025-53506, CVE-2024-24549 | Persistent; HTTP/2 framing continues to produce issues |
| 2 | **Information Disclosure / Logging / Credentials** | 14 | CVE-2021-25122, CVE-2019-12418, CVE-2026-34487, CVE-2026-34483 | Expanding into log-injection (JsonAccessLogValve) |
| 3 | **AuthN/AuthZ / Security-Constraint Bypass** | 13 | CVE-2026-29145, CVE-2026-34500, CVE-2025-66614, CVE-2026-24733 (HTTP/0.9), CVE-2025-46701 (CGI) | **Surging**—CLIENT_CERT bypass recurs across multiple fixes |
| 4 | **HTTP Parsing / Request Smuggling** | 11 | CVE-2020-1935, CVE-2023-46589, CVE-2026-32990 | Steady |
| 5 | **RCE / Deserialization / TOCTOU** | 5 | CVE-2020-1938 (Ghostcat/AJP), CVE-2025-24813 (partial PUT), CVE-2024-50379 (TOCTOU) | Low count but **critical severity** (CVSS 9.8) |
| 6 | **Open Redirect** | 3 | CVE-2023-41080, CVE-2026-25854 | Stable |
| 7 | **Path Traversal** | 1 | CVE-2025-55752 | Rare but high-impact |

**New sub-class to add:** "Escape/Meta-Sequence Injection" (CVE-2025-55754) — doesn't fit neatly into existing categories.

---

## 3. Suggested Page/Index Updates

### 3.1 Top-Level Package Page

```
- Update total known CVE count: 64 → verify against latest OSV snapshot
- Add "Last refreshed" timestamp  
- Highlight active fix cadence: latest fixes target 9.0.117 / 10.1.54 / 11.0.21
- Note: versions ≤8.5.x reached EOL; KB should flag 7.x/8.5.x entries as legacy-only
```

### 3.2 Version Matrix Update

Add rows for recent fix milestones:

| Fix Cluster | Versions | Key CVEs Addressed |
|-------------|----------|-------------------|
| Apr 2026 | 9.0.117, 10.1.54, 11.0.21 | CVE-2026-34500, CVE-2026-34487, CVE-2026-34483 |
| Apr 2026 | 9.0.116, 10.1.53, 11.0.20 | CVE-2026-29145, CVE-2026-25854, CVE-2026-29129, CVE-2026-32990 |
| Mar 2026 | 9.0.115, 10.1.52, 11.0.18 | CVE-2026-24734 |
| Mar 2026 | 9.0.113, 10.1.50, 11.0.15 | CVE-2025-66614, CVE-2026-24733 |
| Feb 2026 | 9.0.110, 10.1.47, 11.0.12 | CVE-2025-61795 |
| Feb 2026 | 9.0.109, 10.1.45, 11.0.11 | CVE-2025-55752, CVE-2025-55754 |

### 3.3 "Recurring Pattern" Callout Box (New)

Add a dedicated callout for the **CLIENT_CERT authentication bypass pattern**:

> ⚠️ **Recurring Pattern:** CLIENT_CERT authentication failures that do not abort the handshake as expected have been addressed in at least three separate CVEs (CVE-2025-66614, CVE-2026-29145, CVE-2026-34500) across consecutive release cycles. Deployers relying on mutual TLS should verify they are on the latest patch within their branch and monitor Apache's `announce@` list.

### 3.4 Cross-Ecosystem Link

Add note for CVE-2023-24998 (Commons FileUpload DoS):

> This CVE originates in `org.apache.commons:commons-fileupload2` but was repackaged/forked into Tomcat's internal multipart handling. The initial fix was incomplete (see CVE-2023-28709). Link to the `commons-fileupload` KB entry for root-cause detail.

### 3.5 High-Severity Highlight Section

Flag the following as **CVSS ≥ 9.0 or known-exploited**:

| CVE | CVSS | Notes |
|-----|------|-------|
| CVE-2020-1938 | 9.8 (E:H) | AJP "Ghostcat"; public exploit available |
| CVE-2025-24813 | 9.8 (E:H) | Partial PUT → RCE via deserialization; active exploitation reported |
| CVE-