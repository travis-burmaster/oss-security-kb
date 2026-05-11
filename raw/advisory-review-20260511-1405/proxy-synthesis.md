

# OSS Security KB Update Proposal: Spring Security Maven Packages

## Executive Summary

Two Spring Security Maven packages lack dedicated KB pages and have significant public advisory histories. This proposal synthesizes exclusively public-source evidence (GHSA/OSV advisories, NVD, Spring security bulletins) to propose page content. All findings are package-scoped per advisory metadata; application reachability is **not** assessed.

---

## 1. `org.springframework.security:spring-security-web`

### Proposed Page Content

**Description:** Core web security module for Spring Security, providing servlet filter chain infrastructure, HTTP security headers, CSRF protection, request matching, and authentication/authorization mechanisms for servlet-based applications.

**Repository:** https://github.com/spring-projects/spring-security

### Known Vulnerabilities (Package-Scoped)

| Advisory | CVE | Severity | Summary | Fixed Versions |
|----------|-----|----------|---------|----------------|
| GHSA-mf92-479x-3373 | CVE-2026-22732 | **CRITICAL** | HTTP security headers silently not written under certain conditions, leaving responses unprotected | 6.5.9, 7.0.4 |
| GHSA-hh32-7344-cg2f | CVE-2022-22978 | **CRITICAL** | Authorization bypass via `RegexRequestMatcher` when regex does not account for multiline input (dot-all mode) | 5.4.11, 5.5.7, 5.6.4 |
| GHSA-c4q5-6c82-3qpw | CVE-2024-38821 | **CRITICAL** | Authorization bypass of static resources in WebFlux applications | 5.7.13, 5.8.15, 6.0.13, 6.1.11, 6.2.7, 6.3.4 |
| GHSA-gq28-h5vg-8prx | CVE-2021-22112 | **HIGH** | Privilege escalation when switching security contexts via `SecurityContext` manipulation | 5.2.9, 5.3.8, 5.4.4 |
| GHSA-2jrg-rf5x-568g | CVE-2026-22747 | **MODERATE** | Unauthorized user impersonation when using X.509 client certificate authentication | 7.0.5 |

### Security Posture Notes

- **Pattern of authorization bypass flaws:** Three of five advisories (CVE-2022-22978, CVE-2024-38821, CVE-2026-22747) involve authorization bypass or identity confusion, indicating this module's request matching and authentication extraction logic is a recurring attack surface.
- **CVE-2022-22978 specifics:** The vulnerability is localized to `RegexRequestMatcher.java` (confirmed by GHSA ref linking directly to the source file). Applications using `RegexRequestMatcher` with patterns not anchored with `\A...\z` or lacking `Pattern.DOTALL` were vulnerable. This is a **package-level fact**; actual reachability depends on whether the application configures regex-based request matching.
- **CVE-2024-38821 scope distinction:** Despite being filed under `spring-security-web`, the advisory title explicitly states "WebFlux Applications." This affects the reactive stack. Applications using only the servlet stack may not be reachable, but the advisory is **catalogued against this artifact** in GHSA/OSV.
- **CVE-2026-22732 (headers not written):** Rated CRITICAL — silent failure to write security headers (e.g., `X-Content-Type-Options`, `Strict-Transport-Security`) could leave applications exposed to clickjacking, MIME-sniffing, and downgrade attacks without any visible error.
- **CVE-2026-22747 (X.509 impersonation):** Only rated MODERATE, suggesting exploitation requires specific preconditions (X.509 client cert authentication enabled, likely combined with particular subject DN extraction configuration).
- **Downstream impact noted:** CVE-2021-22112 was flagged in Jenkins security advisory (2021-02-19) and multiple Oracle CPUs (April, July, October 2021), confirming real-world downstream consumption.

### Open Questions

1. **CVE-2024-38821 artifact scoping:** Why is this advisory filed against `spring-security-web` rather than `spring-security-webflux`? Is the vulnerable code shared across both stacks, or is this an OSV/GHSA metadata artifact? The commit `0e257b56` should be examined to confirm which module contains the fix.
2. **CVE-2026-22732 trigger conditions:** The advisory states headers are not written "under some conditions" but public details are sparse. What specific conditions cause the silent failure? Is it related to error handling paths, async dispatch, or filter ordering?
3. **CVE-2026-22747 and CVE-2026-22732 timeline:** Both CVEs carry `2026` identifiers. These appear to be genuinely recent (2025-era) advisories. The `2026` prefix in CVE numbering reflects CVE Numbering Authority assignment batches, not necessarily calendar year. Confirm these are not pre-publication or synthetic entries.
4. **No advisory coverage for older critical issues:** Are there unlisted advisories for this artifact prior to 2021, or is the 5.x line the effective starting point for GHSA tracking?

---

## 2. `org.springframework.security:spring-security-config`

### Proposed Page Content

**Description:** Configuration module for Spring Security, providing Java configuration (`HttpSecurity`, `@EnableWebSecurity`), XML namespace support (`spring-security.xsd`), and authorization rule DSL for both servlet and reactive stacks.

**Repository:** https://github.com/spring-projects/spring-security

### Known Vulnerabilities (Package-Scoped)

| Advisory | CVE | Severity | Summary | Fixed Versions |
|----------|-----|----------|---------|----------------|
| GHSA-3h6f-g5f3-gc4w | CVE-2023-34034 | **CRITICAL** | Access control bypass via misconfigured path matching rules (using `**` in the middle of patterns) | 5.6.12, 5.7.10, 5.8.5, 6.0.5, 6.1.2 |
| GHSA-4vrc-j85c-598c | CVE-2026-22754 | **HIGH** | XML authorization rules don't correctly include servlet path in path matching | 7.0.5 |
| GHSA-4wrg-8wpc-h923 | CVE-2026-22753 | **HIGH** | `HttpSecurity#securityMatchers` doesn't correctly include servlet path in path matching | 7.0.5 |
| GHSA-4vpr-xfrp-cj64 | CVE-2023-34035 | **HIGH** | Authorization rules can be misconfigured when using multiple servlets (rules may not apply to intended servlet) | 5.8.5, 6.0.5, 6.1.2 |
| GHSA-9gp8-6cg8-7h34 | CVE-2023-34042 | **MODERATE** | `spring-security.xsd` schema file installed with world-writable permissions (local privilege escalation risk) | 5.7.11, 5.8.7, 6.0.7, 6.1.4 