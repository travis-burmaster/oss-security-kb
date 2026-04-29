# openssl (npm)

**Registry:** npm
**Weekly Downloads:** (not captured in this review)
**Repository:** (not confirmed from the evidence bundle)
**Security Contact:** (not confirmed)
**Disclosure Policy:** https://github.com/advisories/GHSA-75w2-qv55-x7fv
**Current Status:** deprecated + advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-29 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database JSON, public NVD CVE record, npm registry metadata) | Added a new page capturing the single published advisory for the deprecated `openssl` npm package. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2023-49210 / GHSA-75w2-qv55-x7fv | Critical | The `openssl` (aka `node-openssl`) npm package (through 2.0.0) accepts an `opts` argument containing a `verb` field used for command execution; public advisory text states this can enable command execution. The advisory also notes the package is unsupported by the maintainer. | *No fix published (package is deprecated / unsupported)* | https://github.com/advisories/GHSA-75w2-qv55-x7fv |

## Security Posture Notes

- Public advisory records describe the npm package `openssl` as a wrapper that can execute system commands based on caller-controlled option fields.
- The npm registry metadata for the latest release (`2.0.0`) marks the package as **deprecated** (“Package no longer supported”).
- Because the package is deprecated/unsupported and the advisory does not identify a fixed version, the safest posture is to **avoid this package entirely**.

## Recommendations for Developers

1. **Do not use `openssl` (npm)** in new or maintained deployments.
2. Prefer platform primitives:
   - Node.js built-in `crypto` and `tls` modules for cryptography and TLS.
   - If you must invoke the OpenSSL CLI, call it directly via `child_process` with careful argument handling (do not pass attacker-controlled strings into a shell).
3. Audit dependency trees for accidental transitive use (e.g., `npm ls openssl`).

## Open Questions

- Which (if any) downstream packages still depend on `openssl` (npm) transitively, and can they migrate to maintained alternatives?

## Related Pages

- [[npm/index]]

---
*Last updated: 2026-04-29 | Sources: 4 (OSV.dev package query for npm/openssl, GitHub Advisory Database JSON for GHSA-75w2-qv55-x7fv, NVD CVE record for CVE-2023-49210, npm registry metadata for `openssl`)*
