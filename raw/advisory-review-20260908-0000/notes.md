# Advisory Review Notes — 2026-09-08

## Pass parameters
- Date: 2026-09-08
- Ecosystems targeted: Maven / Java
- Packages researched: 2 (commons-collections, nimbus-jose-jwt)
- OSV.dev: blocked (HTTP 403) — not consulted
- Evidence sources: github/advisory-database (mcp__github__search_code + WebFetch on raw.githubusercontent.com)

## Packages evaluated

### 1. commons-collections (Maven Central)

**Artifacts:**
- `commons-collections:commons-collections` (3.x, maintenance-only at 3.2.2)
- `org.apache.commons:commons-collections4` (4.x, current stable 4.4)

**GHSAs confirmed as applicable to the library itself:**
- GHSA-fjq5-5j5f-mvxh → CVE-2015-7501 (Critical CVSS 9.8: Deserialization gadget chain via InvokerTransformer/ChainedTransformer)
- GHSA-6hgm-866r-3cjv → CVE-2015-6420 (High: same root cause, Cisco product CVE)

**GHSAs excluded (downstream consumers, not library itself):**
- GHSA-p694-23q3-rvrc — Apache Synapse (uses commons-collections as a vector)
- GHSA-wfw7-6632-xcv2 — Jenkins (uses commons-collections as a vector)

**References consulted:**
- https://github.com/advisories/GHSA-fjq5-5j5f-mvxh
- https://github.com/advisories/GHSA-6hgm-866r-3cjv
- https://github.com/apache/commons-collections
- https://commons.apache.org/proper/commons-collections/

### 2. nimbus-jose-jwt (Maven Central)

**Artifact:** `com.nimbusds:nimbus-jose-jwt`

**GHSAs confirmed (6 direct library advisories):**
- GHSA-xwmg-2g98-w7v9 → CVE-2025-53864 (Moderate CVSS 7.5: nested JSON DoS, fixed 9.37.4/10.0.2)
- GHSA-gvpg-vgmx-xg6w → CVE-2023-52428 (High CVSS 7.5: p2c PBKDF2 iteration-count DoS, fixed 9.37.2)
- GHSA-f6vf-pq8c-69m4 → CVE-2019-17195 (Critical CVSS 9.8: JWT parse exception handling, fixed 7.9)
- GHSA-jfmq-4g4m-99rh → CVE-2017-12973 (Low CVSS 3.1: AES-CBC padding oracle, fixed 4.39)
- GHSA-2qp9-wg27-9pcv → CVE-2017-12972 (High: HMAC integer overflow bypass, fixed 4.39)
- GHSA-pfv2-37f7-9m6w → CVE-2017-12974 (High CVSS 7.5: EC Invalid Curve Attack, fixed 4.36)

**References consulted:**
- https://github.com/advisories/GHSA-xwmg-2g98-w7v9
- https://github.com/advisories/GHSA-gvpg-vgmx-xg6w
- https://github.com/advisories/GHSA-f6vf-pq8c-69m4
- https://github.com/advisories/GHSA-jfmq-4g4m-99rh
- https://github.com/advisories/GHSA-2qp9-wg27-9pcv
- https://github.com/advisories/GHSA-pfv2-37f7-9m6w
- https://connect2id.com/products/nimbus-jose-jwt/security

## Index corrections applied in this pass

The 2026-09-07 pass (mongoose + tracing) updated wiki/log.md but did not update wiki/index.md.
Corrections applied here alongside this pass's new pages:
- npm section: 93 → 94 (mongoose entry added)
- Rust section: 39 → 40 (tracing entry added)
- Mongoose and tracing entries added to their respective index sections
- Maven section: 31 → 33 (commons-collections + nimbus-jose-jwt added)
- Master index total: 282 → 286 (282 + 2 from 09-07 pass + 2 from this pass)
- Master index date: 2026-09-05 → 2026-09-08
