# body-parser (npm)

**Registry:** npm
**Weekly Downloads:** ~18,000,000 (as of 2026-04-13)
**Repository:** https://github.com/expressjs/body-parser
**Security Contact:** security@expressjs.com / express-security@lists.openjsf.org
**Disclosure Policy:** https://github.com/expressjs/express/security/policy
**Current Status:** advisory mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-10 | [@travis-burmaster](https://github.com/travis-burmaster) | full-source (as part of Express 5.2.1 audit) | manual review | 3 findings (1 medium, 2 low) + key defenses confirmed | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

**Audit scope:** body-parser 2.2.2, reviewed as a dependency of Express 5.2.1. JSON parser, urlencoded parser, raw parser, and text parser audited for injection, prototype pollution, content-type confusion, and DoS.

## Findings

### Medium Severity

#### M1: Express Passes allowPrototypes: true to qs via Urlencoded Parser

When Express is configured with `app.set('query parser', 'extended')`, the urlencoded body parser inherits qs with `allowPrototypes: true` (set by Express's `parseExtendedQueryString` at `express/lib/utils.js:268`). This allows POST body keys to shadow `Object.prototype` properties like `constructor`, `toString`, and `valueOf`.

Direct `__proto__` is blocked by qs, but `constructor[prototype]` creates attacker-controlled nested objects that can confuse application logic.

**Note:** Express 5.2.1 defaults to `'simple'` mode. This only affects apps that explicitly use `'extended'` mode. The body-parser module itself does NOT set `allowPrototypes` — Express does when configuring the parser.

**Code:** `express/lib/utils.js:268`, `body-parser/lib/types/urlencoded.js:90-97`

#### M1a: Urlencoded Parser Throws 413 on Parameter Limit (Safer Than qs Default)

Unlike qs's silent truncation, body-parser's urlencoded handler throws a 413 status when `parameterLimit` is exceeded. This is **safer** behavior — the request is rejected rather than silently truncated.

**Code:** `lib/types/urlencoded.js:90-97`

---

### Low Severity

#### L1: JSON Body __proto__ as Own Property

body-parser's JSON handler uses native `JSON.parse()` (line 72 of `lib/types/json.js`). `JSON.parse('{"__proto__":{"x":1}}')` creates an own property named `__proto__` on the result — it does NOT pollute `Object.prototype`.

However, if application code later does recursive merge (`Object.assign`, spread, lodash merge) on `req.body`, the `__proto__` own property could be promoted to prototype pollution depending on the merge implementation.

**Code:** `lib/types/json.js:72`

#### L2: Content-Type Confusion Mitigated by shouldParse

Each parser type checks `Content-Type` before processing via `shouldParse(req)` (read.js:60). JSON parser only fires on `application/json`; urlencoded only on `application/x-www-form-urlencoded`. Sending JSON with a form content-type parses it as urlencoded (producing garbage, not a bypass). Charset validation at json.js:84 rejects non-UTF charsets for JSON.

**Code:** `lib/read.js:60`, `lib/types/json.js:84`

---

### Confirmed Safe

| Area | Status |
|------|--------|
| Content-type enforcement | Each parser validates content-type before parsing (shouldParse gate) |
| Charset validation | JSON parser rejects non-UTF charsets |
| Parameter limit handling | Urlencoded throws 413 (safer than qs silent truncation) |
| Raw/text parsers | Minimal attack surface — return Buffer or string directly |
| Request size limits | Configurable via `limit` option (default 100kb for JSON, 100kb for urlencoded) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-45590 / GHSA-qwcr-r2fm-qrc7 | High | Denial of service when url encoding is enabled; upstream 1.20.3 adds a default `depth` limit of `32` in the 1.x line. | 1.20.3 | [GHSA](https://github.com/advisories/GHSA-qwcr-r2fm-qrc7), [HISTORY.md](https://raw.githubusercontent.com/expressjs/body-parser/master/HISTORY.md) |
| CVE-2025-13466 / GHSA-wqch-xfxh-vrr4 | Medium | Denial of service in `2.2.0` from inefficient handling of URL-encoded bodies with very large parameter counts within the default request-size limit. | 2.2.1 | [GHSA](https://github.com/advisories/GHSA-wqch-xfxh-vrr4), [release notes](https://github.com/expressjs/body-parser/releases/tag/v2.2.1) |

## Security Posture Notes

- body-parser is Express's built-in request body parsing middleware (bundled since Express 4.16).
- The JSON parser delegates to native `JSON.parse` — safe against prototype pollution at the parse level, but applications must be careful with downstream merging of parsed bodies.
- The urlencoded parser delegates to qs — security depends on how Express configures qs options (notably `allowPrototypes`).
- Size limits (`limit` option) default to 100kb, providing basic DoS protection, but the public advisory history shows urlencoded parser complexity still matters within that limit when depth / parameter handling regresses.

## Recommendations for Developers

1. **Use `'simple'` query parser mode** (Express 5 default) unless you specifically need nested object parsing
2. **Never recursively merge `req.body` into configuration objects** without sanitizing keys — `__proto__` will be an own property from JSON.parse
3. **Set appropriate size limits** via the `limit` option for your use case
4. **Keep body-parser updated on your active major line** — public advisories currently require at least `1.20.3` on 1.x and `2.2.1` on 2.x

## Related Pages

- [[npm/express]]
- [[npm/qs]]
- [[npm/cookie]]
- [[npm/index]]

---
*Last updated: 2026-04-14 | Sources: 8 (upstream repository, source code audit of body-parser 2.2.2 via Express audit, GitHub Advisory Database, OSV.dev, public CVE records via advisory aliases, upstream HISTORY.md, GitHub release metadata, npm registry)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
