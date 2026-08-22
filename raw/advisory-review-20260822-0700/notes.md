# Advisory Review Evidence Notes — 2026-08-22

**Pass date:** 2026-08-22
**Ecosystems targeted:** Maven/Java (Maven Central), Go
**New pages:** 2 (protobuf-java, hashicorp/vault)
**Advisory sources consulted:** github/advisory-database via mcp__github__search_code + WebFetch (raw.githubusercontent.com)
**OSV.dev:** blocked (HTTP 403) — not used

---

## Target Selection

### Rejected targets
- `cert-manager` (Kubernetes/Go): mcp__github__search_code for "cert-manager jetstack" in github/advisory-database returned 0 results. Second search for "cert-manager acme.cert-manager.io" also returned 0. Skipped.
- `homebrew/node` / `homebrew/nodejs`: Homebrew formulas don't typically have their own GHSA entries. Search returned 0 results. Skipped.

### Selected targets
1. `com.google.protobuf:protobuf-java` (Maven) — foundational dep of gRPC-Java, Google Cloud SDKs; expected significant advisory history
2. `github.com/hashicorp/vault` (Go) — dominant OSS secrets management platform; high GHSA count expected

---

## protobuf-java (com.google.protobuf:protobuf-java)

### Search queries
- `mcp__github__search_code`: query `protobuf-java`, repo `github/advisory-database`
  - Returned 7 results

### Advisory records reviewed
1. **GHSA-735f-pc8j-v9w8** (CVE-2024-7254)
   - URL: https://raw.githubusercontent.com/github/advisory-database/main/advisories/github-reviewed/2024/09/GHSA-735f-pc8j-v9w8/GHSA-735f-pc8j-v9w8.json
   - Status: CONFIRMED DIRECT. High (CVSS 7.5). StackOverflow DoS parsing unknown fields/extensions with excessive nesting. Fixed 3.25.5/4.27.5/4.28.2.
   - Included: YES

2. **GHSA-4gg5-vx3j-xwc7** (CVE-2022-3510)
   - Status: CONFIRMED DIRECT. High (CVSS 7.5). Uncontrolled resource consumption in Message-Type Extensions parsing. Fixed 3.16.3/3.19.6/3.20.3/3.21.7.
   - Included: YES

3. **GHSA-g5ww-5jh7-63cx** (CVE-2022-3509)
   - Status: CONFIRMED DIRECT. High (CVSS 7.5). Uncontrolled resource consumption in text-format parsing. Fixed 3.16.3/3.19.6/3.20.3/3.21.7.
   - Included: YES

4. **GHSA-wrvw-hg22-4m67** (CVE-2021-22569)
   - Status: CONFIRMED DIRECT. High (CVSS 7.5). Denial of service via excessive GC pressure parsing unknown fields in binary format (quadratic allocation). Fixed 3.16.1/3.18.2/3.19.2.
   - Included: YES

5. **GHSA-h4h5-3hr4-j3g2** (CVE-2022-3171)
   - Status: CONFIRMED DIRECT. Moderate (CVSS 5.7 AV:A). GC-pressure DoS via repeated embedded messages. Fixed 3.16.3/3.19.6/3.20.3/3.21.7.
   - Included: YES

6. **GHSA-77rm-9x9h-xj3g** (CVE-2021-22570)
   - Status: WITHDRAWN (2025-08-25). Originally NULL pointer dereference in protobuf compiler; re-attributed to compiler build artifact.
   - Included: NOTED (withdrawn)

7. **GHSA-fjh6-p566-wr6q**
   - Status: EXCLUDED. For `io.github.skylot:jadx-core` (bundles vulnerable protobuf-java 3.11.4). Not a direct protobuf-java advisory.
   - Included: EXCLUDED

---

## hashicorp/vault (github.com/hashicorp/vault)

### Search queries
- `mcp__github__search_code`: query `hashicorp/vault`, repo `github/advisory-database`
  - Total count: 61 results

### Advisory sampling strategy
Selected 6 representative advisories by recency and severity. Full list: https://github.com/advisories?query=package%3Agithub.com%2Fhashicorp%2Fvault

### Advisory records reviewed (representative subset)
1. **GHSA-m2w4-8ggf-rj47** (CVE-2026-3605) — High CVSS 7.2. KVv2 glob-policy delete bypass. Fixed CE 2.0.0.
2. **GHSA-6h4p-m86h-hhgh** (CVE-2025-5999) — High CVSS 9.1. Root-namespace identity endpoint privilege escalation. Fixed CE 1.20.0.
3. **GHSA-6c5r-4wfc-3mcx** (CVE-2025-6037) — Moderate CVSS 7.5. TLS cert auth validation bypass. Fixed 1.20.1.
4. **GHSA-rr8j-7w34-xp5j** (CVE-2024-9180) — High CVSS 9.0. Root-namespace identity endpoint privilege escalation. Also affects OpenBao < 2.0.3. Fixed CE 1.18.0.
5. **GHSA-8r5m-3f66-qpr3** (CVE-2026-5052) — Moderate CVSS 5.3. PKI/ACME SSRF via local targets. Fixed CE 2.0.0.
6. **GHSA-vq4h-9ghm-qmrr** (CVE-2023-25000) — Moderate CVSS 5.6. Shamir cache-timing side-channel. Fixed 1.11.9/1.12.5/1.13.1.

### Registry metadata
- pkg.go.dev: 4,923 known importers of github.com/hashicorp/vault/api
- Latest stable: 2.0.4 (released 2026-08-04)
- Security contact: security@hashicorp.com; HackerOne CVD program
- Total GHSA count: 61 reviewed records (as of 2026-08-22)

---

## Index corrections

### wiki/index.md staleness
Confirmed via git show that the 2026-08-21 push_files call omitted wiki/index.md from its payload. Count was stale at 260. Corrected to 264 in this pass (+2 zlib/gnupg from 2026-08-21 pass, +2 protobuf-java/vault from this pass).

---
*Notes generated: 2026-08-22 | Sources: 12 GHSA (6 protobuf-java + 6 vault)*
