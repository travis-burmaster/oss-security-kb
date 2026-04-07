# path-to-regexp (npm)

**Registry:** npm
**Weekly Downloads:** ~80,000,000 (as of 2026-04-07)
**Repository:** https://github.com/pillarjs/path-to-regexp
**Security Contact:** none listed
**Disclosure Policy:** none listed (GitHub Issues used for disclosure)

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-03-31 | travis-burmaster | `parse()` function — path tokenization logic (~500 LOC) | manual | 2 bugs found (2 filed) | [Issue #433](https://github.com/pillarjs/path-to-regexp/issues/433) |

### Audit Notes (2026-03-31)
Scope was the `parse()` function in the main source file (~500 lines). This function converts a path string like `/user/:id` into a token array used for route matching. Two bugs found:

**Bug 1 — Trailing backslash appends `undefined` to path token**
`parse('/test\\')` reads past the end of the `chars` array. At end-of-string, `chars[i]` is `undefined`, which gets coerced to the string `"undefined"` and concatenated into the path literal. Result: the route silently becomes `/testundefined`. This can cause route confusion and potential security bypasses in middleware stacks that depend on exact path matching.

**Bug 2 — Null byte passthrough**
Null bytes (`\x00`) are not stripped or rejected from path strings. Depending on downstream handling, this may allow path traversal or cause unexpected behavior in C-backed HTTP servers.

Prior art: this package had CVE-2024-45296 (ReDoS via backtracking) discovered in 2024 — but the `parse()` function's output correctness had not been systematically reviewed.

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-45296 | High | ReDoS via catastrophic backtracking in regex generation | 8.0.0 | [GitHub](https://github.com/pillarjs/path-to-regexp/security/advisories/GHSA-9wv6-86v2-598j) |
| Issue #433 | Medium (TBD) | Trailing backslash produces `undefined` in path token; null byte passthrough | unfixed (as of 2026-04-07) | [Issue #433](https://github.com/pillarjs/path-to-regexp/issues/433) |

*Full CVE history: https://osv.dev/list?ecosystem=npm&q=path-to-regexp*

## Security Posture Notes

Actively maintained by pillarjs org. ~80M weekly downloads — used as a transitive dependency in Express.js and virtually all Express-based apps. No formal security policy (SECURITY.md absent). Historically responsive to CVE reports but no formal bug bounty.

**Transitive exposure:** Any application using `express`, `koa-router`, `react-router` (older versions), or `vue-router` may be transitively affected by path-to-regexp bugs.

## Dependencies of Note

path-to-regexp has zero production dependencies (v8.x). Low transitive risk from deps, but extremely high *reverse* transitive risk given its use in Express.

## Related Pages

- [[npm/express]]
- [[npm/koa-router]]

---
*Last updated: 2026-04-07 | Sources: 1 (GitHub Issue #433, manual audit)*
