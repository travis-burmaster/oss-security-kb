# github.com/aws/aws-sdk-go (Go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (high; 8,675 GitHub stars; latest stable v1.55.8; EOL as of 2025-07-31 — repository archived)
**Repository:** https://github.com/aws/aws-sdk-go (archived)
**Security Contact:** aws-security@amazon.com
**Disclosure Policy:** https://aws.amazon.com/security/vulnerability-reporting/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-08-26 | oss-security-kb pass | public advisory database | advisory-mapping | 3 GHSA advisories mapped (1 withdrawn excluded) | [GHSA search](https://github.com/advisories?query=aws-sdk-go) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2020-8911 / GHSA-f5pg-7wfw-84q9 | Moderate (CVSS AV:L/AC:H/PR:L/S:C/C:H) | S3 Crypto SDK (`s3crypto`) uses AES-CBC without MAC computation; attacker with write access to the S3 bucket who can observe decryption failures can exploit a classic CBC padding oracle to reconstruct plaintext; affects `EncryptionClient` and `EncryptionClientV2` | github.com/aws/aws-sdk-go 1.34.0 | [GHSA-f5pg-7wfw-84q9](https://github.com/advisories/GHSA-f5pg-7wfw-84q9) |
| CVE-2020-8912 / GHSA-7f33-f4f5-xwgw | Low (CVSS 2.5 AV:L/AC:H/PR:L/UI:N) | S3 Crypto SDK does not authenticate algorithm parameters for the data encryption key (in-band key negotiation); attacker with write access to the bucket can switch the encryption algorithm (e.g., AES-GCM to AES-CBC) by modifying object metadata, undermining ciphertext integrity | github.com/aws/aws-sdk-go 1.34.0 | [GHSA-7f33-f4f5-xwgw](https://github.com/advisories/GHSA-7f33-f4f5-xwgw) |
| CVE-2022-2582 / GHSA-6jvc-q2x7-pchv | Moderate (CVSS AV:N/AC:L/PR:L/UI:N) | S3 Crypto SDK sends an unencrypted MD5 hash of the plaintext as a readable metadata field alongside the ciphertext; attacker with read access to encrypted S3 objects may recover low-entropy plaintext via offline brute force | github.com/aws/aws-sdk-go 1.34.0 | [GHSA-6jvc-q2x7-pchv](https://github.com/advisories/GHSA-6jvc-q2x7-pchv) |

*GHSA-76wf-9vgp-pj7w is WITHDRAWN as a duplicate of GHSA-6jvc-q2x7-pchv and is excluded above.*

## Security Posture Notes

**EOL notice:** `github.com/aws/aws-sdk-go` (v1) reached end-of-support on 2025-07-31. The GitHub repository is archived and no further security patches will be issued. AWS recommends migrating to `github.com/aws/aws-sdk-go-v2`. Latest v1 release: v1.55.8.

All three public advisories affect only the **S3 client-side encryption (CSE) sub-package** (`service/s3/s3crypto`), not general SDK usage. They represent a cluster of cryptographic design weaknesses: unauthenticated algorithm selection (CVE-2020-8912), CBC mode without MAC allowing a padding oracle (CVE-2020-8911), and unprotected plaintext metadata that can enable offline brute force (CVE-2022-2582). CVE-2020-8911 and CVE-2020-8912 were coordinated and fixed together in v1.34.0 (August 2020). CVE-2022-2582 was separately disclosed in 2022 but addressed by the same v1.34.0 fix.

**Impact scope:** Only callers using `s3crypto.NewEncryptionClient()` or `s3crypto.NewEncryptionClientV2()` to encrypt objects client-side are affected. Standard S3 operations (PutObject, GetObject without the crypto wrapper) are not impacted.

**aws-sdk-go-v2:** The current AWS Go SDK (`github.com/aws/aws-sdk-go-v2`) carries one independent advisory: GHSA-xmrv-pmrh-hhx2 (Medium CVSS 5.9 AV:N/AC:H: malformed EventStream response frames with invalid header type bytes can cause the host process to panic and terminate; fixed across multiple service clients including eventstream v1.7.8, s3 v1.97.3, bedrockruntime v1.50.4 and others; 2026-03-23).

AWS security disclosures follow the AWS Vulnerability Reporting Process at aws.amazon.com/security/vulnerability-reporting/.

## Dependencies of Note

- `github.com/jmespath/go-jmespath` — used for JSON query support in AWS API responses
- Core HTTP plumbing uses only the Go standard library
- S3 CSE uses standard library `crypto/aes` — no external crypto dependency

## Open Questions

- Are there advisories specific to the credential-provider chain or STS client affecting non-S3 workflows?
- Has the `aws-sdk-go-v2` S3 encryption client (equivalent CSE path in `service/s3/s3crypto`) received a published cryptographic review?

## Related Pages

- [[go/golang.org-x-crypto]]
- [[go/index]]

---
*Last updated: 2026-08-26 | Sources: 3 GHSA advisories (github/advisory-database)*
