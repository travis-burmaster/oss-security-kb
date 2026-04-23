# Evidence Review: oss-security-kb Maintenance

## Primary Candidate: `npm/http-proxy`

### Verified Evidence Summary

| Field | Value | Source |
|-------|-------|--------|
| Package | `http-proxy` (npm) | npmjs.com |
| Latest version | 1.18.1 | npm registry |
| Weekly downloads | ~23.75M | npm registry |
| SECURITY.md | **Not found** (404) | GitHub raw fetch |
| Direct package-level advisories | 2 confirmed | OSV package query |

### Advisory Detail

**1. GHSA-6x33-pw7p-hmpq (Denial of Service)**
- **Severity:** High
- **Fixed in:** 1.18.1
- **Fix reference:** PR [#1447](https://github.com/http-party/node-http-proxy/pull/1447)
- **Evidence quality:** Strong — GHSA record maps directly to package, fix version aligns with changelog/release tag, PR is public and merged.

**2. GHSA-9xw9-pvgv-6p76 / CVE-2017-16014 (Insufficient Error Handling / DoS)**
- **Severity:** High
- **Fixed in:** 0.7.0
- **Fix reference:** PR [#101](https://github.com/http-party/node-http-proxy/pull/101)
- **Evidence quality:** Strong — NVD and GHSA both reference the same PR; advisory is directly attributed to the `http-proxy` package.

### Proposed KB Edits

#### Markdown KB Page Draft

```markdown
## npm/http-proxy

- **Ecosystem:** npm
- **Latest version:** 1.18.1
- **Popularity:** ~23.75M weekly downloads
- **SECURITY.md:** Not present (as of review date)
- **Known direct advisories:** 2

### Advisories

| ID | CVE | Type | Severity | Fixed Version | Fix PR |
|----|-----|------|----------|---------------|--------|
| GHSA-6x33-pw7p-hmpq | — | DoS | High | 1.18.1 | [#1447](https://github.com/http-party/node-http-proxy/pull/1447) |
| GHSA-9xw9-pvgv-6p76 | CVE-2017-16014 | DoS (error handling) | High | 0.7.0 | [#101](https://github.com/http-party/node-http-proxy/pull/101) |

### Notes
- Both advisories are **direct package-level vulnerabilities**, not dependency-transitive or operational misconfiguration issues.
- The package is actively depended upon but the repository shows limited recent maintenance activity; absence of SECURITY.md is notable for a package of this download volume.
- Current latest (1.18.1) addresses all known direct advisories.
```

#### Log Entry Draft

```
[YYYY-MM-DD] npm/http-proxy: Added KB entry. 2 direct GHSA advisories confirmed
via OSV package query (GHSA-6x33-pw7p-hmpq, GHSA-9xw9-pvgv-6p76). Both are DoS
class, both fixed in released versions. No SECURITY.md present. Latest 1.18.1
covers all known fixes. No fabricated or inferred data.
```

---

## Comparison Candidates: No Action Recommended

| Package | Ecosystem | OSV Query Result | Recommendation |
|---------|-----------|-----------------|----------------|
| `helmet` | npm | Empty | No KB entry — no direct package-level advisory evidence |
| `cookie-parser` | npm | Empty | No KB entry — no direct package-level advisory evidence |
| `github.com/gorilla/mux` | Go | Empty | No KB entry — no direct package-level advisory evidence |

**Rationale:** Conservative approach — absence of OSV results means no verifiable direct advisory exists for these packages in this pass. Any security concerns for these packages would require separate, independently sourced evidence before KB inclusion. No entries fabricated.

---

## Methodology Notes

- All advisory counts and identifiers sourced from OSV package-ecosystem queries, cross-verified against GHSA and NVD public records.
- Fix versions confirmed against npm registry release data and GitHub PR/tag correlation.
- No dependency-chain or transitive vulnerability data was attributed to packages directly.
- Comparison candidates were evaluated with the same query methodology; empty results are reported as-is, not padded.
