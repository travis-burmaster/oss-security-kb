# lodash (npm)

**Registry:** npm
**Weekly Downloads:** ~25,000,000 (as of 2026-04-12)
**Repository:** https://github.com/lodash/lodash
**Security Contact:** none listed
**Disclosure Policy:** none listed
**Current Status:** audit-ingested

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-13 | OpenClaw recurring review | public-advisory refresh | manual | Refreshed published advisory coverage to include the 2025–2026 incomplete-fix chains affecting `_.unset` / `_.omit` and `_.template` | https://osv.dev/list?ecosystem=npm&query=lodash |
| 2026-04-12 | [@travis-burmaster](https://github.com/travis-burmaster) | full-source (all path-walking functions) | hybrid (manual review + automated) | 3 new findings + all CVE patches verified | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

**Audit scope:** lodash 4.18.1 (latest), single-file build `lodash.js` (17,259 lines, 817 functions). Systematic review of all 120+ path-walking functions for prototype pollution and related injection vectors. Commit `cb0b9b9` (lodash/lodash main branch, 2026-04-12).

## Findings

### Critical

#### C1: Template Code Injection via _.template()

**Severity:** Critical (CWE-94 -- Code Injection)
**Status:** By design, but frequently misused

`_.template()` compiles template strings using the `Function()` constructor (line 14992) with no sanitization of template content. The `<% %>` evaluate delimiter injects directly into the function body:

```js
// RCE if attacker controls template string
_.template('<%= constructor.constructor("return process")() %>')({})
```

The `variable` option has `reForbiddenIdentifierChars` guards (line 181), but the **template string itself** is unrestricted. Any attacker-controlled string reaching `_.template()` is a direct RCE vector.

**Code:** `lodash.js:14882-14992`

**Impact:** Remote code execution in any application passing user input to `_.template()`. Common in server-side rendering, email templating, and configuration processing.

---

### Medium

#### M1: Prototype Method Invocation via _.invoke()

**Severity:** Medium (CWE-470 -- Use of Externally-Controlled Input to Select Classes or Code)

`_.invoke()` follows any path including `__proto__` and `constructor.prototype`, then calls the resolved function via `apply()` with no path sanitization:

```js
// Successfully calls Object.prototype.hasOwnProperty with Object.prototype as this
_.invoke({}, '__proto__.hasOwnProperty', 'x')
```

**Code:** `lodash.js:3260`

**Impact:** Attacker can invoke arbitrary prototype methods with controlled arguments. Not directly exploitable for property writes but could be a chain in a larger attack.

#### M2: Prototype Method Invocation via _.result()

**Severity:** Medium (CWE-470)

Same vector as invoke -- traverses any path, calls functions with parent object as `this`, no sanitization:

```js
_.result({}, 'constructor.prototype.toString')
```

**Code:** `lodash.js:13722`

---

### CVE Patch Verification (All Patched Correctly)

| CVE | Patched Function | Defense Mechanism | Verified |
|-----|------------------|-------------------|----------|
| CVE-2019-10744 | defaultsDeep | `safeGet` returns undefined for constructor (forces new object creation instead of traversing to Object.prototype) | Yes |
| CVE-2020-8203 | set, setWith, update, updateWith, zipObjectDeep | `baseSet` line 4040: blocks `__proto__`, `constructor`, `prototype` on every path segment | Yes |
| GHSA-xxjr-mmjv-4gpg | unset, omit | `baseUnset` line 4393/4399: blocks `__proto__` and non-terminal `constructor`/`prototype` | Yes |

### Defense-in-Depth Architecture (Verified)

Lodash 4.18.1 uses three layers of prototype pollution defense:

1. **baseSet guard (line 4040)** -- Checks every path segment against `__proto__`, `constructor`, `prototype`. Returns early on match. Protects: set, setWith, update, updateWith, pick, pickBy, zipObjectDeep.

2. **safeGet (line 6704)** -- Returns `undefined` for `__proto__` (unconditionally) and `constructor` (when value is a function). Protects: merge, mergeWith, defaultsDeep, baseMergeDeep.

3. **baseAssignValue (line 2597)** -- Uses `Object.defineProperty` for `__proto__` writes, creating an own data property rather than traversing the prototype chain. Protects: clone, cloneDeep, assignValue, zipObject.

### Bypass Vectors Tested (All Blocked)

| Vector | Result |
|--------|--------|
| Unicode escapes (`\u005f\u005fproto\u005f\u005f`) | Blocked -- resolved at parse time, string check matches |
| Bracket notation in paths (`["__proto__"]`) | Blocked -- stringToPath extracts literal string |
| Custom toString() returning "__proto__" | Blocked -- toKey runs before checks |
| constructor.prototype via _.set | Blocked at line 4040 |
| constructor.prototype via _.merge | Blocked by safeGet returning undefined |
| constructor.prototype via _.defaultsDeep | Blocked -- same merge internals |
| Array paths bypassing string checks | Blocked -- checks operate on individual keys after toKey |
| Proxy/Symbol keys | Blocked -- cannot equal string "__proto__" |
| Null byte in path strings | Blocked -- no null-byte handling gaps in stringToPath |

### Confirmed Safe Functions

| Function Group | Status |
|----------------|--------|
| set, setWith, update, updateWith | Protected by baseSet guard |
| merge, mergeWith, defaultsDeep | Protected by safeGet + baseAssignValue |
| clone, cloneDeep, cloneDeepWith | Uses defineProperty for __proto__ (own property) |
| pick, pickBy | Protected by baseSet guard |
| zipObject, zipObjectDeep | baseAssignValue + baseSet guards |
| at, get, baseGet | Read-only (minor info leak via prototype chain traversal) |
| has, hasIn, hasPath | Read-only (info leak via `in` operator) |
| unset, omit | __proto__/constructor checks in baseUnset |
| customDefaultsMerge | safeGet + baseAssignValue + keysIn non-enumeration |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2019-1010266 / GHSA-x5rq-j2xg-h7qm | Medium | ReDoS in older string / number parsing paths; public records mark versions before 4.17.11 as affected. | 4.17.11 | https://github.com/advisories/GHSA-x5rq-j2xg-h7qm |
| CVE-2019-10744 / GHSA-jf85-cpcp-j695 | Critical | Prototype pollution in `defaultsDeep`. | 4.17.12 | https://github.com/advisories/GHSA-jf85-cpcp-j695 |
| CVE-2020-8203 / GHSA-p6mc-m468-83gw | High | Prototype pollution via deep-path mutation helpers including `zipObjectDeep`, `set`, `setWith`, `update`, and `updateWith`. | 4.17.19 | https://github.com/advisories/GHSA-p6mc-m468-83gw |
| CVE-2020-28500 / GHSA-29mw-wpgm-hmr9 | Medium | ReDoS in `toNumber`, `trim`, and `trimEnd`. | 4.17.21 | https://github.com/advisories/GHSA-29mw-wpgm-hmr9 |
| CVE-2021-23337 / GHSA-35jh-r3h4-6jhm | High | Command injection via the `_.template` `variable` option when untrusted input reaches template compilation. | 4.17.21 | https://github.com/advisories/GHSA-35jh-r3h4-6jhm |
| CVE-2025-13465 / GHSA-xxjr-mmjv-4gpg | Medium | Prototype pollution in `_.unset` and `_.omit`; public advisory coverage says 4.17.23 patched the initial string-key variant. | 4.17.23 | https://github.com/advisories/GHSA-xxjr-mmjv-4gpg |
| CVE-2026-2950 / GHSA-f23m-r3pf-42rh | Medium | Incomplete-fix bypass for the 2025 `_.unset` / `_.omit` bug: array-wrapped path segments could still reach prototype deletion paths until 4.18.0. | 4.18.0 | https://github.com/advisories/GHSA-f23m-r3pf-42rh |
| CVE-2026-4800 / GHSA-r5fr-rjxr-66jc | High | Incomplete-fix bypass for the 2021 `_.template` bug: `options.imports` key names were not validated and inherited polluted keys could flow into the `Function()` constructor sink. | 4.18.0 | https://github.com/advisories/GHSA-r5fr-rjxr-66jc |

## Security Posture Notes

- Public advisory history now shows **two distinct incomplete-fix chains** that matter operationally: `_.template` injection from `CVE-2021-23337` to `CVE-2026-4800`, and `_.unset` / `_.omit` prototype pollution from `CVE-2025-13465` to `CVE-2026-2950`.
- The published record is no longer just about prototype pollution. Lodash also carries documented **ReDoS** history and a recurring **template-compilation code-injection** surface tied to `Function()`-based compilation.
- For defenders, intermediate patch levels matter: `4.17.21` closed the older `variable`-option template bug but not the later `imports`-key injection path, and `4.17.23` closed the first `_.unset` / `_.omit` bug but not the later array-path bypass.
- The 2026 template-fix advisory is also notable because the published remediation did two things: validate `imports` key names and switch import merging from inherited-property enumeration to own-property enumeration, reducing the chance that prior prototype pollution contaminates template compilation.
- Lodash remains a high-value ecosystem dependency (`~133,124,413` npm downloads in the last week of this review pass, latest `4.18.1`), so even medium-severity parser or object-path bugs can have outsized downstream impact.
- The internal 2026 source audit still suggests the remaining high-risk design area is `_.template()` itself: even on patched versions, applications should treat untrusted template strings or untrusted template options as dangerous.

## Recommendations for Developers

1. **Treat `_.template()` like an unsafe code-generation primitive** — never pass untrusted template strings or untrusted `options.imports` / `variable` values into it.
2. **Upgrade to lodash >= 4.18.0 (preferably latest 4.18.1)** — versions that stopped at 4.17.21 or 4.17.23 still miss later incomplete-fix follow-ups.
3. **Never pass user-controlled object paths to deep mutation helpers** such as `set`, `update`, `zipObjectDeep`, `unset`, or `omit` without strong validation / normalization.
4. **Consider lodash-es or per-method imports** to reduce attack surface.

## Open Questions (Resolved)

- ~~Has any full-source modern audit been published post-2020 fixes?~~ **Resolved:** This is the first systematic audit of all path-walking functions. All CVE patches verified effective.
- ~~Are there remaining dangerous deep-object mutation patterns not covered by prior fixes?~~ **Resolved:** No new prototype pollution vectors found. Template code injection and method invocation via invoke/result are the remaining risks.
- ~~Which downstream packages still expose vulnerable versions indirectly?~~ **Open:** Transitive dependency audit of vulnerable lodash versions remains unperformed.

## Related Pages

- [[npm/index]]
- [[npm/minimist]]
- [[npm/express]]

---
*Last updated: 2026-04-13 | Sources: 9 (OSV package query, GitHub Security Advisories, public CVE / NVD records, npm registry metadata, npm downloads API, upstream public fix commits, plus prior source-audit context already captured on-page)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
