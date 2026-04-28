# github.com/gorilla/schema (go)

**Registry:** pkg.go.dev
**Weekly Downloads:** unknown (as of 2026-04-27)
**Repository:** https://github.com/gorilla/schema
**Security Contact:** unknown (no published security policy URL in public repo metadata)
**Disclosure Policy:** unknown (no published security policy URL in public repo metadata)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-27 | OpenClaw recurring review | package advisory normalization | public-source curation (OSV package query, Go vuln record, GitHub Advisory Database / GHSA text, public CVE record, upstream fix commit, repository metadata, local proxy draft assist) | Added a new advisory-mapped page for `github.com/gorilla/schema` after confirming a reviewed Go vuln record (GO-2024-2958) and a GitHub advisory (GHSA-3669-72x9-r9p3) for a memory-exhaustion DoS via sparse slice index deserialization in `Decoder.Decode`, fixed in `v1.4.1`. | https://osv.dev/vulnerability/GO-2024-2958 |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-37298 / GHSA-3669-72x9-r9p3 / GO-2024-2958 | (not consistently stated across sources) | Potential memory exhaustion / denial of service via sparse slice deserialization when decoding form values into structs containing slices-of-structs using `schema.Decoder.Decode`. Attacker-controlled indices like `arr.1000000000.Val=1` can force large allocations. | 1.4.1 | https://github.com/gorilla/schema/security/advisories/GHSA-3669-72x9-r9p3 |

*Full OSV history: https://osv.dev/list?ecosystem=Go&q=github.com/gorilla/schema*

## Security Posture Notes

- **What the bug is (public description):** The GitHub advisory describes a denial-of-service scenario where attacker-controlled form keys can specify extremely large sparse indices for a slice-of-struct field, causing `Decoder.Decode()` to allocate a huge slice and exhaust memory.
- **Where it manifests:** The reviewed Go vuln record points at `decoder.go#L223` for the allocation path involved in the sparse slice behavior. (Reference URL below.)
- **Fix and mitigation lever:** The reviewed Go vuln record marks the issue fixed in **v1.4.1**, and the linked fix commit introduces/uses a `Decoder.MaxSize` limit (commit adds tests exercising `MaxSize` behavior), providing a library-level control to cap slice growth from decoded indices.
- **Exposure boundary:** Practical exposure typically involves decoding attacker-controlled query/body form parameters (`r.Form`) into Go structs with slice-of-struct fields.
- **Project activity:** Public GitHub repository metadata shows the repo is **not archived** and had activity as of **2024-08-19**, so this is not primarily an abandoned-project story.
- **Disclosure metadata gap:** Public repository metadata indicates `security_policy_url: null`, and no disclosure policy was confirmed in this pass. Treat the GitHub advisory as the canonical published record for the vulnerability.

## Dependencies of Note

- `gorilla/schema` is commonly used near HTTP request boundaries (form parsing / binding). Its safety depends on how applications validate form keys and whether they decode into nested slice structures.

## Open Questions

- Does the repository publish a security-reporting workflow anywhere outside the standard GitHub security policy URL surface (e.g., a `SECURITY.md` later added)?
- Does the project document recommended safe defaults for `Decoder.MaxSize` for typical web applications?

## Related Pages

- [[go/github.com/gorilla/mux]]
- [[go/github.com/gorilla/websocket]]
- [[go/index]]

---
*Last updated: 2026-04-27 | Sources: 7 (OSV package query via api.osv.dev, reviewed Go vuln record JSON for GO-2024-2958, GitHub advisory GHSA-3669-72x9-r9p3 text, CVE alias in GO record, upstream fix commit cd59f2f12cbdfa9c06aa63e425d1fe4a806967ff, upstream code reference decoder.go#L223, public GitHub repository metadata; local proxy draft assist via the configured Claude-compatible proxy at 127.0.0.1:8319 used only as a drafting aid)*
