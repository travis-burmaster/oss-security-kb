# express (npm)

**Registry:** npm
**Weekly Downloads:** ~84,000,000 (as of 2026-04-10)
**Repository:** https://github.com/expressjs/express
**Security Contact:** security@expressjs.com / express-security@lists.openjsf.org
**Disclosure Policy:** https://github.com/expressjs/express/security/policy
**Threat Model:** https://github.com/expressjs/security-wg/blob/main/docs/ThreatModel.md
**Current Status:** advisory-mapped

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
| CVE-2014-6393 / GHSA-gpvr-g6gh-9mc2 | Moderate | Missing charset in 400-level `Content-Type` headers could enable browser-side XSS with legacy encodings such as UTF-7 | 3.11.0, 4.5.0 | [GHSA](https://github.com/advisories/GHSA-gpvr-g6gh-9mc2) |
| CVE-2024-29041 / GHSA-rv95-896h-c2vc | Moderate | Open redirect allowlist bypass in malformed URLs passed to `res.location()` / `res.redirect()` | 4.19.2, 5.0.0-beta.3 | [GHSA](https://github.com/expressjs/express/security/advisories/GHSA-rv95-896h-c2vc) |
| CVE-2024-43796 / GHSA-qw6h-vgh9-j6wx | Low | XSS via `response.redirect()` when untrusted input is rendered in the generated redirect HTML body | 4.20.0, 5.0.0 | [GHSA](https://github.com/expressjs/express/security/advisories/GHSA-qw6h-vgh9-j6wx) |
| CVE-2024-45296 | High | ReDoS in path-to-regexp (transitive dep) | path-to-regexp 8.0.0 | [osv.dev](https://osv.dev/vulnerability/CVE-2024-45296) |
| CVE-2024-9266 / GHSA-jj78-5fmv-mv28 | Low | Open redirect in the Express response object affecting the legacy 3.x line | 4.0.0-rc1 | [GHSA](https://github.com/advisories/GHSA-jj78-5fmv-mv28) |
| CVE-2024-10491 / GHSA-cm5g-3pgc-8rg4 | Moderate | Resource injection in `response.links()` via unsanitized `Link` header values on the legacy 3.x line | 4.0.0-rc1 | [GHSA](https://github.com/advisories/GHSA-cm5g-3pgc-8rg4) |
| MAL-2026-2419 | Critical | Typosquatting: express-session-js impersonates express-session | N/A (malicious package) | [osv.dev](https://osv.dev/vulnerability/MAL-2026-2419) |

## Supply Chain Notes

The express-* npm namespace is heavily targeted by typosquatting attacks (e.g., MAL-2026-2419). Operators should audit dependencies and use lockfiles.

## Public Advisory Notes

- Public package advisories now cover both legacy 3.x issues and modern 4.x / 5.x redirect handling flaws. In particular, Express 4.19.2 landed an improved fix for the malformed-URL allowlist-bypass issue tracked as `CVE-2024-29041`, and 4.20.0 removed link rendering in redirect HTML to address `CVE-2024-43796`; both fixes are corroborated in the upstream `History.md` and release notes.
- These published advisories overlap with, but do not fully replace, the higher-level audit finding on `res.redirect()`. The public fixes address specific bypass and HTML-rendering vectors, while the local audit finding still documents residual application-layer risk when developers pass attacker-controlled schemes (`javascript:`, `data:`, `//host`) into redirects without allowlisting.
- The two 2024 GHSA entries affecting only the 3.x line (`CVE-2024-9266` and `CVE-2024-10491`) are still worth tracking because legacy Express deployments remain common in extended-support environments, even though current 4.x / 5.x users are outside those affected ranges.

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
*Last updated: 2026-04-21 | Sources: 12 (upstream repository, Express security policy, Express threat model, source code audit of Express 5.2.1 + 8 dependencies, OSV database, GitHub Advisory Database, public CVE records via advisory aliases, Express release notes, upstream History.md, npm registry)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
