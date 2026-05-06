# litellm (python)

**Registry:** PyPI
**Repository:** https://github.com/BerriAI/litellm
**Current Status:** advisory-mapped (proxy vulnerabilities + supply-chain incident)

## Summary

`litellm` has both a documented March 2026 malicious-release incident and a broad public advisory history for the legitimate LiteLLM proxy/library. OSV and GitHub Advisory records currently show high/critical issues across exposed proxy endpoints, template rendering, authentication/authorization boundaries, SQL construction, SSRF, logging/secret exposure, MCP stdio test endpoints, and denial-of-service cases.

This page keeps the malicious PyPI releases separate from upstream application vulnerabilities. The malicious-release records (`PYSEC-2026-2`, `MAL-2026-2144`, and `GHSA-5mg7-485q-xm76`) refer to the same March 2026 package-compromise event and should not be counted as three distinct root-cause vulnerabilities.

## Known Vulnerabilities / Incidents

| ID | Severity | Description | Affected | Fixed / Mitigation | Sources |
|----|----------|-------------|----------|--------------------|---------|
| PYSEC-2026-2 / MAL-2026-2144 / GHSA-5mg7-485q-xm76 | Critical (malicious release) | Malicious releases harvested sensitive files and credentials, attempted cloud-metadata credential access, and exfiltrated data to attacker-controlled infrastructure; public reports also describe persistence attempts. | 1.82.7 and 1.82.8 | Remove affected releases, treat exposed environments as compromised, revoke/rotate credentials, and pin/lock dependencies. | [OSV](https://osv.dev/vulnerability/PYSEC-2026-2), [PyPI incident report](https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/), [LiteLLM issue](https://github.com/BerriAI/litellm/issues/24518) |
| CVE-2024-2952 / GHSA-46cm-pfwv-cgf8 | Critical | LiteLLM has Server-Side Template Injection vulnerability in /completions endpoint | introduced 0; fixed 1.34.42 | Fixed in 1.34.42 | [OSV](https://osv.dev/vulnerability/GHSA-46cm-pfwv-cgf8), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-2952) |
| CVE-2024-4264 / GHSA-7ggm-4rjg-594w | High | litellm passes untrusted data to `eval` function without sanitization | introduced 0; last affected 1.28.11 | No fixed version listed in OSV; review upstream advisory before use | [OSV](https://osv.dev/vulnerability/GHSA-7ggm-4rjg-594w), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-4264) |
| CVE-2024-4888 / GHSA-3xr8-qfvj-9p9j | High | Arbitrary file deletion in litellm | introduced 0; fixed 1.35.36 | Fixed in 1.35.36 | [OSV](https://osv.dev/vulnerability/GHSA-3xr8-qfvj-9p9j), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-4888) |
| CVE-2024-4890 / GHSA-8j42-pcfm-3467 | Moderate | SQL injection in litellm | introduced 0; last affected 1.27.14 | No fixed version listed in OSV; review upstream advisory before use | [OSV](https://osv.dev/vulnerability/GHSA-8j42-pcfm-3467), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-4890) |
| CVE-2024-5225 / GHSA-h6m6-jj8v-94jj | Moderate | SQL injection in litellm | introduced 0; fixed 1.40.0 | Fixed in 1.40.0 | [OSV](https://osv.dev/vulnerability/GHSA-h6m6-jj8v-94jj), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-5225) |
| CVE-2024-5751 / GHSA-gppg-gqw8-wh9g | Critical | litellm vulnerable to remote code execution based on using eval unsafely | introduced 0; fixed 1.40.16 | Fixed in 1.40.16 | [OSV](https://osv.dev/vulnerability/GHSA-gppg-gqw8-wh9g), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-5751) |
| CVE-2024-5710 / GHSA-qqcv-vg9f-5rr3 | Moderate | litellm vulnerable to improper access control in team management | introduced 0; fixed 1.40.15 | Fixed in 1.40.15 | [OSV](https://osv.dev/vulnerability/GHSA-qqcv-vg9f-5rr3), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-5710) |
| CVE-2024-6587 / GHSA-g26j-5385-hhw3 | High | LiteLLM Server-Side Request Forgery (SSRF) vulnerability | introduced 0; fixed 1.44.8 | Fixed in 1.44.8 | [OSV](https://osv.dev/vulnerability/GHSA-g26j-5385-hhw3), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-6587) |
| CVE-2024-10188 / GHSA-gw2q-qw9j-rgv7 | High | LiteLLM Vulnerable to Denial of Service (DoS) | introduced 0; fixed 1.53.1.dev1 | Fixed in 1.53.1.dev1 | [OSV](https://osv.dev/vulnerability/GHSA-gw2q-qw9j-rgv7), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-10188) |
| CVE-2024-6825 / GHSA-53gh-p8jc-7rg8 | High | LiteLLM Vulnerable to Remote Code Execution (RCE) | introduced 1.40.3.dev2; last affected 1.40.12 | No fixed version listed in OSV; review upstream advisory before use | [OSV](https://osv.dev/vulnerability/GHSA-53gh-p8jc-7rg8), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-6825) |
| CVE-2024-8984 / GHSA-fh2c-86xm-pm2x | High | LiteLLM Vulnerable to Denial of Service (DoS) via Crafted HTTP Request | introduced 0; fixed 1.56.2 | Fixed in 1.56.2 | [OSV](https://osv.dev/vulnerability/GHSA-fh2c-86xm-pm2x), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-8984) |
| CVE-2024-9606 / GHSA-g5pg-73fc-hjwq | High | LiteLLM Reveals Portion of API Key via a Logging File | introduced 0; fixed 1.44.12 | Fixed in 1.44.12 | [OSV](https://osv.dev/vulnerability/GHSA-g5pg-73fc-hjwq), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-9606) |
| CVE-2025-0330 / GHSA-879v-fggm-vxw2 | High | LiteLLM Has a Leakage of Langfuse API Keys | introduced 0; last affected 1.52.1 | No fixed version listed in OSV; review upstream advisory before use | [OSV](https://osv.dev/vulnerability/GHSA-879v-fggm-vxw2), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-0330) |
| CVE-2025-0628 / GHSA-fjcf-3j3r-78rp | High | LiteLLM Has an Improper Authorization Vulnerability | introduced 0; fixed 1.61.15 | Fixed in 1.61.15 | [OSV](https://osv.dev/vulnerability/GHSA-fjcf-3j3r-78rp), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-0628) |
| CVE-2026-35029 / GHSA-53mr-6c8q-9789 | High | LiteLLM: Privilege escalation via unrestricted proxy configuration endpoint | introduced 0; fixed 1.83.0 | Fixed in 1.83.0 | [OSV](https://osv.dev/vulnerability/GHSA-53mr-6c8q-9789), [GHSA](https://github.com/BerriAI/litellm/security/advisories/GHSA-53mr-6c8q-9789), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-35029) |
| CVE-2026-35030 / GHSA-jjhc-v7c2-5hh6 | Critical | LiteLLM: Authentication bypass via OIDC userinfo cache key collision | introduced 0; fixed 1.83.0 | Fixed in 1.83.0 | [OSV](https://osv.dev/vulnerability/GHSA-jjhc-v7c2-5hh6), [GHSA](https://github.com/BerriAI/litellm/security/advisories/GHSA-jjhc-v7c2-5hh6), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-35030) |
| GHSA-69x8-hrgq-fjj8 | High | LiteLLM: Password hash exposure and pass-the-hash authentication bypass | introduced 0; fixed 1.83.0 | Fixed in 1.83.0 | [OSV](https://osv.dev/vulnerability/GHSA-69x8-hrgq-fjj8), [GHSA](https://github.com/BerriAI/litellm/security/advisories/GHSA-69x8-hrgq-fjj8) |
| CVE-2026-42203 / GHSA-xqmj-j6mv-4862 | High | LiteLLM: Server-Side Template Injection in /prompts/test endpoint | introduced 1.80.5; fixed 1.83.7 | Fixed in 1.83.7 | [OSV](https://osv.dev/vulnerability/GHSA-xqmj-j6mv-4862), [GHSA](https://github.com/BerriAI/litellm/security/advisories/GHSA-xqmj-j6mv-4862), [release](https://github.com/BerriAI/litellm/releases/tag/v1.83.7-stable) |
| CVE-2026-42208 / GHSA-r75f-5x8p-qvmc | Critical | LiteLLM has SQL Injection in Proxy API key verification | introduced 1.81.16; fixed 1.83.7 | Fixed in 1.83.7 | [OSV](https://osv.dev/vulnerability/GHSA-r75f-5x8p-qvmc), [GHSA](https://github.com/BerriAI/litellm/security/advisories/GHSA-r75f-5x8p-qvmc), [release](https://github.com/BerriAI/litellm/releases/tag/v1.83.7-stable) |
| CVE-2026-42271 / GHSA-v4p8-mg3p-g94g | High | LiteLLM: Authenticated command execution via MCP stdio test endpoints | introduced 1.74.2; fixed 1.83.7 | Fixed in 1.83.7 | [OSV](https://osv.dev/vulnerability/GHSA-v4p8-mg3p-g94g), [GHSA](https://github.com/BerriAI/litellm/security/advisories/GHSA-v4p8-mg3p-g94g), [release](https://github.com/BerriAI/litellm/releases/tag/v1.83.7-stable) |

## Security Posture Notes (evidence-backed)

- **Proxy/API attack surface needs recurring review.** Public advisories cover SSTI, RCE/eval misuse, SSRF, SQL injection, auth bypass, privilege escalation, command execution, DoS, and secret exposure in LiteLLM proxy flows.
- **Recent fixed-version floor:** several April 2026 GHSA records list fixes in `1.83.0` or `1.83.7`; users should consult the linked GHSA/OSV records and current release notes before selecting a minimum version.
- **Supply-chain blast radius remains distinct from code vulnerabilities.** For the March 2026 malicious-release incident, affected environments should be treated as compromised and reachable credentials should be rotated; this is separate from patching ordinary code defects.
- Consider ecosystem hardening patterns discussed in the PyPI incident report: dependency pinning/locking with hashes and dependency cooldowns to reduce exposure to rapid supply-chain events.

## Related Pages

- [[python/index]]

---
*Last updated: 2026-05-06 | Sources: OSV query/detail records for PyPI `litellm`; GitHub Advisory Database; NVD CVE records; PyPI incident report; LiteLLM release/advisory links*
