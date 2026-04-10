# express (npm)

**Registry:** npm
**Weekly Downloads:** ~84,000,000 (as of 2026-04-10)
**Repository:** https://github.com/expressjs/express
**Security Contact:** security@expressjs.com / express-security@lists.openjsf.org
**Disclosure Policy:** https://github.com/expressjs/express/security/policy
**Threat Model:** https://github.com/expressjs/security-wg/blob/main/docs/ThreatModel.md
**Current Status:** audit-ingested

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-10 | [@travis-burmaster](https://github.com/travis-burmaster) | full-source (core + key deps) | hybrid (manual review + automated) | 14 findings (2 high, 4 medium-high, 2 medium, 6 confirmed safe) | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

**Audit scope:** Express 5.2.1 core (2762 lines across 6 files: application.js, express.js, request.js, response.js, utils.js, view.js) plus security-critical dependencies: send 1.1.0, serve-static 2.2.0, qs 6.15.1, cookie 0.7.2, body-parser 2.2.2, proxy-addr 2.0.7, encodeurl 2.0.0, finalhandler 2.1.0. Commit `8e022ed` (expressjs/express main branch, 2026-04-10).

**Not in scope:** Express middleware ecosystem (helmet, cors, csurf, etc.), application-level code, third-party template engines.

## Findings

### High Severity

#### H1: Open Redirect in res.redirect() -- No URL Scheme Validation

**Severity:** High (CWE-601)
**In-scope per threat model:** Yes -- untrusted network data causing unvalidated redirect

`res.redirect()` performs zero validation on the redirect URL. `encodeUrl()` only encodes special characters -- schemes like `javascript:`, `data:`, and protocol-relative URLs (`//evil.com`) pass through intact.

**Code:** `lib/response.js:812-864` (redirect), `lib/response.js:795` (location)

**Exploit:**
```js
// Vulnerable pattern (extremely common in login flows)
app.get('/login', (req, res) => {
  res.redirect(req.query.next || '/');
});

// Attack: /login?next=javascript:alert(document.cookie)
// Attack: /login?next=//evil.com/phish
// Attack: /login?next=data:text/html,<script>alert(1)</script>
```

**Impact:** Credential phishing, XSS via javascript: scheme, token theft. Affects every Express app using user-controlled redirects.

---

#### H2: req.hostname Injection -- Null Bytes, Path Injection, No Sanitization

**Severity:** High (CWE-113 / CWE-644)
**In-scope per threat model:** Yes -- untrusted network data corrupting header-derived values

`req.hostname` reads `X-Forwarded-Host` (trust proxy enabled) or `Host` header with zero validation. Only port stripping via colon-split is applied.

**Code:** `lib/request.js:418-458`

**Attack vectors:**
- Null byte injection: `evil.com\x00.legit.com` -- DNS libraries truncate at null
- Path injection: `evil.com/admin` -- poisons URL construction
- No RFC hostname validation

**Impact:** Cache poisoning, SSRF, password reset poisoning, OAuth callback manipulation.

---

### Medium-High Severity

#### MH1: allowPrototypes: true in Extended Query Parser

Express passes `allowPrototypes: true` to qs in extended mode, allowing queries to shadow `Object.prototype` keys. Direct `__proto__` blocked, but `constructor[prototype]` creates attacker-controlled nested objects.

**Code:** `lib/utils.js:268`

#### MH2: Silent Parameter Truncation in qs

qs silently drops parameters beyond `parameterLimit` (default 1000). Attacker pads query with junk to push security-relevant parameters past the limit.

**Code:** `qs/lib/parse.js:67-71`

#### MH3: req.protocol Accepts Arbitrary Values

`X-Forwarded-Proto` passed through with only `trim()`. No whitelist. `req.secure` bypass trivial.

**Code:** `lib/request.js:297-315`

#### MH4: req.subdomains Routing Confusion

Unsanitized `req.hostname` allows arbitrary subdomain array injection via `X-Forwarded-Host`.

**Code:** `lib/request.js:383-394`

---

### Medium Severity

#### M1: Stack Traces Leaked by Default

Default env is `'development'`. Full stack traces sent to clients unless `NODE_ENV=production` is set.

**Code:** `finalhandler/index.js:157-171`

#### M2: Symlinks Followed by Default in send

`send` uses `fs.stat()` not `fs.lstat()`. Symlinks inside served root pointing outside it are followed.

**Code:** `send/index.js:605`

---

### Out of Scope per Threat Model (Documented for Reference)

- **res.sendFile() path traversal without root option** -- concatenation bypasses send's protections. Out of scope: "accessing files from any accessible path is not a vulnerability."
- **Trust proxy: true enables full IP spoofing** -- configuration issue per threat model.

---

### Confirmed Safe

| Area | Status |
|------|--------|
| Path traversal via encoded chars in send | Defended (layered decode + normalize + regex) |
| Double encoding (%252e) | Safe |
| Windows backslash traversal | Defended |
| Null bytes in static file paths | Blocked |
| JSONP callback injection | Sanitized + nosniff |
| HTTP header injection via res.set() | Blocked by Node.js runtime |
| Range header abuse | Multi-range ignored |
| Dotfiles | Default: ignore (404) |
| Cookie injection via res.cookie() | Strict validation |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-45296 | High | ReDoS in path-to-regexp (transitive dep) | path-to-regexp 8.0.0 | [osv.dev](https://osv.dev/vulnerability/CVE-2024-45296) |
| MAL-2026-2419 | Critical | Typosquatting: express-session-js impersonates express-session | N/A (malicious package) | [osv.dev](https://osv.dev/vulnerability/MAL-2026-2419) |

## Supply Chain Notes

The express-* npm namespace is heavily targeted by typosquatting attacks (e.g., MAL-2026-2419). Operators should audit dependencies and use lockfiles.

## Recommendations for Developers

1. **Never pass user input directly to `res.redirect()`** -- validate against an allowlist
2. **Always set `NODE_ENV=production`** in production
3. **Use `res.sendFile()` with the `root` option** for path containment
4. **Set trust proxy to specific addresses**, never `true`
5. **Validate `req.hostname`** before using in URL construction or cache keys
6. **Use `'simple'` query parser** (Express 5 default) unless you need nesting

## Dependencies of Note

- **path-to-regexp** (via router) -- prior ReDoS, parse() bugs (see [path-to-regexp.md](path-to-regexp.md))
- **qs** -- `allowPrototypes: true` passed by Express in extended mode
- **send** -- symlink following by default
- **proxy-addr** -- IP trust evaluation

## Open Questions (Resolved)

- ~~Has any modern public full-source review of Express core been published?~~ **Resolved:** This audit is the first documented proactive source review.
- ~~Which historical advisories belong on the package page versus the wider middleware ecosystem?~~ **Partially resolved:** Core findings documented above; middleware ecosystem audit remains open.
- ~~What routing and request-parsing assumptions should be tracked alongside path-to-regexp coverage?~~ **Resolved:** Query parsing (qs), hostname parsing, protocol parsing all audited.

## Related Pages

- [[npm/path-to-regexp]]
- [[npm/koa-router]]
- [[npm/index]]

---
*Last updated: 2026-04-10 | Sources: 8 (upstream repository, Express security policy, Express threat model, source code audit of Express 5.2.1 + 8 dependencies, OSV database, npm registry)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
