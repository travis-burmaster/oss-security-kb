# OSS Security Knowledge Base: PyPI `pydantic`

## Package Overview

| Field | Value |
|-------|-------|
| **Package** | `pydantic` |
| **Ecosystem** | PyPI |
| **Summary** | Data validation using Python type hints |
| **Latest Version** | 2.13.4 |
| **Source** | https://github.com/pydantic/pydantic |
| **Documentation** | https://docs.pydantic.dev |

---

## Known Vulnerabilities

### CVE-2021-29510 — Infinite loop via "infinity" input to datetime/date fields

| Field | Detail |
|-------|--------|
| **IDs** | GHSA-5jqp-qgf6-3pvh / PYSEC-2021-47 / CVE-2021-29510 |
| **Note** | GHSA-5jqp-qgf6-3pvh and PYSEC-2021-47 are **duplicates** describing the same vulnerability. |
| **Severity** | MODERATE (CVSS 3.1: AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L) |
| **Type** | Denial of Service (CPU exhaustion) |
| **Affected** | `< 1.6.2`, `1.7.0–1.7.3`, `1.8.0–1.8.1` |
| **Fixed in** | `1.6.2`, `1.7.4`, `1.8.2` |
| **Status** | **Resolved.** Latest version 2.13.4 is not affected. |

### CVE-2024-3772 — Regular expression denial of service via crafted email string

| Field | Detail |
|-------|--------|
| **IDs** | GHSA-mr82-8j83-vxmv / CVE-2024-3772 |
| **Severity** | MODERATE (CVSS 3.1: AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H) |
| **Type** | ReDoS in `validate_email` |
| **Affected** | `< 1.10.13` (v1.x branch), `2.0.0–2.3.x` (v2.x branch) |
| **Fixed in** | `1.10.13`, `2.4.0` |
| **Fix details** | v1.10.13 backported max-length check to `validate_email` (PR #7673). v2.4.0 included the fix via PR #7360. |
| **Status** | **Resolved.** Latest version 2.13.4 is not affected. |

---

## Security Posture Notes

- **All known CVEs are fixed** in the current latest version (2.13.4). Users on any version ≥ 2.4.0 are clear of all listed vulnerabilities.
- **Both historical vulnerabilities are DoS-class** (availability impact only); neither involves data confidentiality or integrity compromise.
- CVE-2024-3772 is network-exploitable (AV:N) but requires high attack complexity (AC:H), making it the more impactful of the two in practice for internet-facing services accepting user-supplied email strings.
- The project has an active security advisory process via GitHub Security Advisories and has demonstrated timely backporting to the v1.x maintenance branch.
- No code execution, authentication bypass, or data leakage vulnerabilities have been reported.

## Users on Legacy v1.x Branch

- Must be on **≥ 1.10.13** to be patched against CVE-2024-3772 (ReDoS).
- Must be on **≥ 1.8.2** (or 1.7.4 / 1.6.2 for respective minor lines) to be patched against CVE-2021-29510.
- v1.x is in maintenance mode; migration to v2.x is recommended for ongoing security support.

---

## Open Questions

1. **Pydantic-core attack surface**: Since v2, much validation logic has moved to the Rust-based `pydantic-core` crate. Are there separate vulnerability disclosures tracked for `pydantic-core` that should be cross-referenced here?
2. **Email validation delegation**: In v2.x, email validation may partially depend on the `email-validator` package. Is the ReDoS fix entirely within pydantic, or does it also require a minimum `email-validator` version?
3. **v1.x EOL date**: No clear end-of-life date found in the evidence. When will security backports to v1.x cease?

---

## Next Review Targets

- **`pydantic-core`** (PyPI) — Rust-based validation engine used by pydantic v2+