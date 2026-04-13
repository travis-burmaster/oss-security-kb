# cookie (npm)

**Registry:** npm
**Weekly Downloads:** ~35,000,000 (as of 2026-04-13)
**Repository:** https://github.com/jshttp/cookie
**Security Contact:** GitHub Security Advisory (private reporting enabled)
**Current Status:** audit-ingested

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-10 | [@travis-burmaster](https://github.com/travis-burmaster) | full-source (as part of Express 5.2.1 audit) | manual review | 2 findings (low) + key defenses confirmed | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

**Audit scope:** cookie 0.7.2, reviewed as a dependency of Express 5.2.1. Parse and serialize paths audited for injection, prototype pollution, and input validation.

## Findings

### Low Severity

#### L1: No Cookie Value Size Limit

`cookie.parse()` imposes no length limit on individual cookie values. An attacker sending extremely large cookie headers can cause memory pressure in the parser. No built-in protection; applications must validate `Cookie` header size upstream (typically at the reverse proxy level).

**Code:** `index.js:105-140` (parse loop)

#### L2: Prototype Key Shadowing via Cookie Names

The result object from `cookie.parse()` is created with `{}` (not `Object.create(null)`). Cookie names like `__proto__` or `constructor` could shadow prototype properties. However, the `hasOwnProperty.call(obj, key)` guard at line 134 uses a saved reference, preventing the worst issues. First-cookie-wins semantics for duplicate names.

**Code:** `index.js:105, 134`

---

### Confirmed Safe

| Area | Status |
|------|--------|
| Cookie injection via `res.cookie()` | Blocked — `cookie.serialize()` validates name via `cookieNameRegExp` and value via `cookieValueRegExp`, throws TypeError on invalid input (index.js:192-200) |
| Duplicate cookies | First-cookie-wins (index.js:134 hasOwnProperty guard) |
| Special characters in values | Percent-encoded by serialize, decoded by parse |
| Null bytes | Passed through by `decodeURIComponent` — not explicitly filtered |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-47764 | Medium | Cookie name validation bypass allowing out-of-spec characters | 0.7.0 | [GHSA](https://github.com/jshttp/cookie/security/advisories/GHSA-pxg6-pf52-xh8x) |

## Security Posture Notes

- The `cookie` module is the low-level parser/serializer used by Express (`res.cookie()`), `cookie-parser` middleware, and many other frameworks.
- Serialize-side validation is strict (name + value regex checks with TypeError on failure), making cookie injection via `res.cookie()` not viable.
- Parse-side validation is minimal by design — the module trusts the HTTP layer to deliver valid `Cookie` headers.
- The lack of size limits is a known concern for DoS but is considered out of scope for a parser library (reverse proxy should enforce).

## Recommendations for Developers

1. **Enforce cookie header size limits** at the reverse proxy (nginx: `large_client_header_buffers`, CloudFlare: automatic)
2. **Use `cookie-parser` or similar middleware** rather than calling `cookie.parse()` directly — middleware can add size checks
3. **Be aware of prototype key shadowing** if iterating parsed cookie keys with `for...in` — use `Object.keys()` instead

## Related Pages

- [[npm/express]]
- [[npm/qs]]
- [[npm/index]]

---
*Last updated: 2026-04-13 | Sources: 4 (upstream repository, source code audit of cookie 0.7.2 via Express audit, GHSA database, npm registry)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
