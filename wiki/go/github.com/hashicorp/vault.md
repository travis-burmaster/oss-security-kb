# github.com/hashicorp/vault (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** 4,923 known importers of `github.com/hashicorp/vault/api` on pkg.go.dev (as of 2026-08-22); distributed primarily as binary releases and Docker images rather than as a consumed library
**Repository:** https://github.com/hashicorp/vault
**Security Contact:** security@hashicorp.com
**Disclosure Policy:** https://github.com/hashicorp/vault/blob/main/SECURITY.md; CVD via HackerOne (https://hackerone.com/hashicorp)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No formal public third-party audits on record in this pass.*

## Known Vulnerabilities

This page covers a representative subset (6 of 61 reviewed GHSA advisories) selected for recency and severity. The full list is available at the OSV / advisory link below.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-3605 / GHSA-m2w4-8ggf-rj47 | High (CVSS 7.2 AV:N/AC:L/PR:L/UI:N/I:H/A:H) | Authenticated user with KVv2 path access through a glob-containing policy can delete secrets they are not authorized to read or write, enabling targeted denial of service. Root cause present since 0.10.0 (~7 years). | CE 2.0.0; Enterprise 2.0.0, 1.21.5, 1.20.10, 1.19.16 | [GHSA-m2w4-8ggf-rj47](https://github.com/advisories/GHSA-m2w4-8ggf-rj47) |
| CVE-2025-5999 / GHSA-6h4p-m86h-hhgh | High (CVSS 9.1 AV:N/AC:L/PR:H/UI:N/C:H/I:H/A:H) | Privileged operator with write access to the root namespace identity endpoint can escalate their own or another user's token to Vault root policy. Affected ≥ 0.10.4, < 1.20.0. | CE 1.20.0; Enterprise 1.20.0, 1.19.6, 1.18.11, 1.16.22 | [GHSA-6h4p-m86h-hhgh](https://github.com/advisories/GHSA-6h4p-m86h-hhgh) |
| CVE-2025-6037 / GHSA-6c5r-4wfc-3mcx | Moderate (CVSS 7.5 AV:N/AC:L/PR:H/UI:R/C:H/I:H/A:H) | TLS certificate auth method performs incorrect validation for non-CA certificates used as trusted credentials; enables certificate crafting for user impersonation. Affected ≥ 0, ≤ 1.20.0. | 1.20.1; 1.19.7; 1.18.12; 1.16.23 | [GHSA-6c5r-4wfc-3mcx](https://github.com/advisories/GHSA-6c5r-4wfc-3mcx) |
| CVE-2024-9180 / GHSA-rr8j-7w34-xp5j | High (CVSS 9.0 AV:N/AC:L/PR:H/UI:N/C:H/I:H/A:H) | Vault operator with write access to the root namespace identity endpoint can escalate privileges to Vault root policy. Also explicitly affects OpenBao fork < 2.0.3. All versions < 1.18.0 affected. | CE 1.18.0; Enterprise 1.17.7, 1.16.11, 1.15.16; OpenBao 2.0.3 | [GHSA-rr8j-7w34-xp5j](https://github.com/advisories/GHSA-rr8j-7w34-xp5j) |
| CVE-2026-5052 / GHSA-8r5m-3f66-qpr3 | Moderate (CVSS 5.3 AV:N/AC:L/PR:N/UI:N/C:L/I:N/A:N) | PKI engine ACME validation does not reject local targets when issuing `http-01` and `tls-alpn-01` challenges; enables SSRF via attacker-controlled DNS when PKI+ACME is enabled. Affected ≥ 1.14.0, ≤ 1.21.4. | CE 2.0.0; Enterprise 2.0.0, 1.21.5, 1.20.10, 1.19.16 | [GHSA-8r5m-3f66-qpr3](https://github.com/advisories/GHSA-8r5m-3f66-qpr3) |
| CVE-2023-25000 / GHSA-vq4h-9ghm-qmrr | Moderate (CVSS 5.6 AV:L/AC:H/PR:L/UI:N/C:H/I:N/A:N) | Vault's Shamir secret-sharing implementation uses precomputed table lookups susceptible to cache-timing side-channel attacks; a host-level attacker observing multiple unseal operations can reduce the brute-force search space for unseal shares. Affected: 1.11.x < 1.11.9, 1.12.0–1.12.4, 1.13.0. | 1.11.9; 1.12.5; 1.13.1 | [GHSA-vq4h-9ghm-qmrr](https://github.com/advisories/GHSA-vq4h-9ghm-qmrr) |

*OSV link: https://osv.dev/list?ecosystem=Go&q=github.com%2Fhashicorp%2Fvault*
*Full advisory list: https://github.com/advisories?query=package%3Agithub.com%2Fhashicorp%2Fvault (61 reviewed records as of 2026-08-22)*

## Security Posture Notes

HashiCorp Vault is the dominant open-source secrets management platform. Since the BSL license change (2023), the community fork **OpenBao** (https://openbao.org) has emerged as an open-source alternative; some advisories (e.g., GHSA-rr8j-7w34-xp5j / CVE-2024-9180) explicitly cover OpenBao.

**Latest stable version:** 2.0.4 (released 2026-08-04). HashiCorp publishes CE releases monthly and maintains Enterprise branches with independent patch timelines. The 2.0.0 CE release addressed multiple accumulated issues, including CVE-2026-3605 (KVv2 glob policy bypass present since 0.10.0 — approximately 7 years).

**Security program:** Vault has a mature coordinated vulnerability disclosure program via HackerOne and a dedicated security team. Advisories are published at https://discuss.hashicorp.com/c/security. The security contact has historically been responsive.

**Recurring pattern — root namespace identity endpoint privilege escalation:** Three separate High-severity advisories (CVE-2024-9180, CVE-2025-5999, and GHSA-6c5r-4wfc-3mcx) all exploit access to the root namespace identity endpoint or authentication method validation to achieve Vault root policy escalation or user impersonation. This recurring vulnerability class suggests persistent enforcement gaps in the identity endpoint authorization model. Operators should restrict root-namespace identity write access to the minimum necessary principals.

**OpenBao impact:** The OpenBao project inherits Vault's codebase. Advisories predating or overlapping the fork date may apply to OpenBao. GHSA-rr8j-7w34-xp5j explicitly lists OpenBao < 2.0.3 as affected.

**Go library consumers:** `github.com/hashicorp/vault/api` (4,923 importers) is the client SDK; most Vault CVEs are server-side vulnerabilities not directly affecting SDK consumers.

## Dependencies of Note

- `github.com/hashicorp/vault/api` depends on `github.com/hashicorp/go-retryablehttp`, `github.com/hashicorp/go-cleanhttp`, and `golang.org/x/net`.
- The Vault server binary embeds gRPC, etcd client libraries, and various cloud SDK libraries with their own security histories.

## Open Questions

- Has the root namespace identity endpoint privilege escalation pattern been architecturally mitigated in 2.0.0, or do the fixes address only specific input validation gaps?
- Does the OpenBao project maintain independent CVE tracking, and what is their patch cadence relative to HashiCorp Vault?
- Are there additional unauthenticated or low-privilege attack vectors in the PKI/ACME engine beyond the SSRF covered by CVE-2026-5052?

## Related Pages

- [[go/github.com/hashicorp/go-getter]]
- [[go/go.etcd.io/etcd-v3]]
- [[kubernetes/helm]]
- [[go/index]]

---
*Last updated: 2026-08-22 | Sources: 6 GHSA (representative subset of 61 reviewed advisories)*
