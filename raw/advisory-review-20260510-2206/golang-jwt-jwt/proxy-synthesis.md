# KB Update Proposal: `github.com/golang-jwt/jwt` (including `/v4` and `/v5`)

## Package Overview

- **Repository**: [github.com/golang-jwt/jwt](https://github.com/golang-jwt/jwt)
- **Description**: Go implementation of JSON Web Tokens (JWT)
- **Module paths**: `github.com/golang-jwt/jwt` (v3), `github.com/golang-jwt/jwt/v4`, `github.com/golang-jwt/jwt/v5`
- **Stars**: ~9,070
- **Default branch**: `main`
- **Last pushed**: 2026-05-01

---

## Normalized Advisories

### Advisory 1: Improper Error Handling in `ParseWithClaims` (v4 only)

| Field | Value |
|---|---|
| **CVE** | CVE-2024-51744 |
| **GHSA** | GHSA-29wx-vh33-7x7r |
| **Go Vuln ID** | GO-2024-3250 |
| **Affected module** | `github.com/golang-jwt/jwt/v4` |
| **Affected range** | `< 4.5.1` |
| **Fixed version** | **v4.5.1** (released 2024-11-03) |
| **Affected symbols** | `Parse`, `ParseWithClaims`, `Parser.Parse`, `Parser.ParseWithClaims` |
| **Summary** | When `ParseWithClaims` returns multiple combined errors (e.g., both `ErrTokenExpired` and `ErrTokenSignatureInvalid`), callers checking only for `ErrTokenExpired` via `errors.Is` could inadvertently accept tokens with invalid signatures. The fix makes the parser return immediately on "dangerous" errors (e.g., invalid signature) rather than combining them with less-severe validation failures. |
| **Severity context** | Logic/documentation flaw that could lead to accepting tokens with invalid signatures if error-checking is incomplete. Not a direct remote code execution. |
| **v5 status** | **Not affected** — v5 already had the corrected error-handling logic (confirmed in release notes for v4.5.1). |
| **Sources** | GHSA advisory, Go vulnerability database (vuln.go.dev), NVD |

### Advisory 2: Excessive Memory Allocation in Header Parsing (v3, v4, v5)

| Field | Value |
|---|---|
| **CVE** | CVE-2025-30204 |
| **GHSA** | GHSA-mh63-6h87-95cp |
| **Go Vuln ID** | GO-2025-3553 |
| **Affected modules & ranges** | `github.com/golang-jwt/jwt/v5`: `5.0.0-rc.1` – `< 5.2.2`; `github.com/golang-jwt/jwt/v4`: `< 4.5.2`; `github.com/golang-jwt/jwt` (v3): `3.2.0` – `3.2.2` (**no fix available**) |
| **Fixed versions** | **v5.2.2** (released 2025-03-21), **v4.5.2** (released 2025-03-21) |
| **v3 status** | `3.2.0`–`3.2.2` listed as **last_affected**; **no fix released** for v3 module path |
| **Affected symbol** | `Parser.ParseUnverified` |
| **Summary** | `ParseUnverified` uses `strings.Split` on untrusted input (the raw token string). A crafted token containing many period characters causes O(n) memory allocation (~16× amplification), enabling a denial-of-service via excessive memory consumption. CWE-405. |
| **Severity context** | Denial-of-service (memory exhaustion). Attacker needs ability to supply a crafted Authorization header / token string to the parsing endpoint. |
| **Sources** | GHSA advisory, Go vulnerability database (vuln.go.dev), NVD, NetApp advisory (ntap-20250404-0002) |

---

## Recommended Minimum Versions

| Module Path | Minimum Safe Version | Rationale |
|---|---|---|
| `github.com/golang-jwt/jwt/v5` | **≥ 5.2.2** | Fixes CVE-2025-30204 (memory DoS). Latest stable is v5.3.1. |
| `github.com/golang-jwt/jwt/v4` | **≥ 4.5.2** | Fixes both CVE-2024-51744 (error handling) and CVE-2025-30204 (memory DoS). |
| `github.com/golang-jwt/jwt` (v3) | **No safe version** | CVE-2025-30204 affects 3.2.0–3.2.2 with no fix. Module is effectively unmaintained. |

---

## Posture Notes

1. **v3 module path is end-of-life.** Per SECURITY.md (updated November 2024): only v5 is fully supported; v4 receives critical back-ports only. The v3 module path (`github.com/golang-jwt/jwt` without `/v4` or `/v5`) has no fix for CVE-2025-30204 and should be treated as **deprecated and vulnerable**. Projects still importing v3 should migrate to v5.

2. **v4 receives security back-ports only.** Both known advisories have been patched in v4, but active feature development occurs on v5. Users on v4 should plan migration to v5.

3. **CVE-2024-51744 behavior change.** The fix in v4.5.1 changes `ParseWithClaims` behavior (immediate return on signature-invalid errors). This is intentionally not fully backwards-compatible. Users unable to upgrade should audit their error-checking order per the workaround in the advisory (check "dangerous" errors like `ErrTokenSignatureInvalid` before `ErrTokenExpired`).

4. **CVE-2025-30204 is network-triggerable DoS.** Any service accepting JWTs from untrusted sources that calls `Parse`, `ParseWithClaims`, or `ParseUnverified` is potentially affected. The fix bounds allocation by avoiding unbounded `strings.Split`.

---

## Source Caveats

- **GHSA-mh63-6h87-95cp (v3 range)**: GHSA lists v