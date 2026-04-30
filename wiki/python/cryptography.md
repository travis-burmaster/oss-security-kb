# cryptography (python)

**Registry:** PyPI
**Repository:** https://github.com/pyca/cryptography
**Security Contact:** GitHub Security Advisory
**Disclosure Policy:** https://github.com/pyca/cryptography/security/policy
**Current Status:** advisory-mapped (seed)

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-30 | OpenClaw recurring review | seed advisory mapping | public-source curation (OSV.dev + upstream GitHub Security Advisory); local Claude-compatible proxy used only as a drafting aid | Created an initial page seeded with one publicly disclosed cryptography advisory (name-constraint peer-name validation gap) with remediation guidance. | https://osv.dev/list?ecosystem=PyPI&q=cryptography |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| *(CVE not captured in this pass)* / GHSA-m959-cc7f-wv43 | Medium-to-low (per advisory text) | Prior to 46.0.5, DNS name constraints were validated against SANs in child certificates, but not against the peer name presented during validation. This could allow a peer name to validate against a wildcard leaf cert even if an excluded-subtree name constraint would reject that peer name if it appeared as a SAN. Advisory notes exploitation requires an uncommon X.509 topology and is not typical of Web PKI. | 46.0.5 | https://github.com/pyca/cryptography/security/advisories/GHSA-m959-cc7f-wv43 |

*Full advisory history (OSV query): https://osv.dev/list?ecosystem=PyPI&q=cryptography*

## Security Posture Notes

- cryptography is a foundational dependency in the Python ecosystem for TLS/X.509 and cryptographic primitives; small certificate-validation semantics gaps can have disproportionate downstream impact in non-Web-PKI deployments.
- The reviewed advisory (GHSA-m959-cc7f-wv43) is notable because it is **not** a memory-safety bug or primitive break; it is a correctness gap at the boundary between RFC 5280 name constraints and RFC 9525 service identity semantics, resolved by making validation more conservative.
- Advisory text explicitly characterizes the practical impact as medium-to-low and calls out the uncommon certificate topology required for exploitation; downstream risk is likely concentrated in private PKI / constrained-trust environments rather than typical public Web PKI usage.
- This page is intentionally seeded: only one advisory was curated in this pass; a future pass should expand the advisory table and incorporate OSV + GHSA coverage across historical records.

## Dependencies of Note

- X.509 parsing and verification semantics depend on the underlying cryptographic backend and certificate chain topology; the advisory itself highlights that security semantics may vary between Web PKI norms and other PKI deployments.

## Open Questions

- Which other cryptography advisories (from OSV and GHSA) should be added next to make this page a complete advisory map rather than a seed?
- Are there maintainer-authored release notes for 46.0.5 that further clarify the name-constraint behavior change and compatibility impact?
- Are there downstream packages in this KB (or future pages) that validate peer names against private PKI constraints and should treat this upgrade as higher priority?

## Related Pages

- [[python/requests]]
- [[python/urllib3]]
- [[python/index]]

---
*Last updated: 2026-04-30 | Sources: 2 (OSV vulnerability record for GHSA-m959-cc7f-wv43 + upstream GitHub Security Advisory text; OSV package query page for cryptography used for discovery)*
