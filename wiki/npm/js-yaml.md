# js-yaml (npm)

**Registry:** npm
**Weekly Downloads:** ~130,000,000 (as of 2026-04-12)
**Repository:** https://github.com/nodeca/js-yaml
**Security Contact:** GitHub Security Advisory (private reporting enabled)
**Current Status:** audit-ingested

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-12 | [@travis-burmaster](https://github.com/travis-burmaster) | full-source (loader, dumper, all types, schema) | hybrid (manual review + PoC) | 6 findings (1 high, 3 medium, 2 low) | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

**Audit scope:** js-yaml 4.1.1, 3867 lines across 24 files. Loader (1733 lines), dumper (965 lines), all 13 type handlers, schema system. Commit `f8e56bd` (nodeca/js-yaml main branch, 2026-04-12).

## Findings

### High Severity

#### H1: Billion Laughs / Alias Expansion Bomb (CWE-776)

**Severity:** High
**Status:** Unfixed as of 4.1.1

js-yaml has zero limits on YAML anchor/alias expansion. A 308-byte payload produces 269 million characters when serialized (873,513x amplification).

**PoC:**
```yaml
a: &a ['lol','lol','lol','lol','lol','lol','lol','lol','lol']
b: &b [*a,*a,*a,*a,*a,*a,*a,*a,*a]
c: &c [*b,*b,*b,*b,*b,*b,*b,*b,*b]
d: &d [*c,*c,*c,*c,*c,*c,*c,*c,*c]
e: &e [*d,*d,*d,*d,*d,*d,*d,*d,*d]
f: &f [*e,*e,*e,*e,*e,*e,*e,*e,*e]
g: &g [*f,*f,*f,*f,*f,*f,*f,*f,*f]
h: &h [*g,*g,*g,*g,*g,*g,*g,*g,*g]
```

**Verified:** 308 bytes input, 4ms parse, 269MB on stringify, 873,513x amplification.

Missing protections: no maxAliasCount, no nesting depth limit, no expanded size limit, no input length limit. Code acknowledges risk at loader.js:330 but only mitigates for mapping keys.

**Impact:** DoS against any service parsing untrusted YAML. ~130M weekly downloads.

---

### Medium Severity

#### M1: Implicit Type Coercion on Untrusted Input

Scalars like `yes`, `no`, `on`, `off`, `true`, `false`, `null`, `~` silently coerce to native JS types under the default schema. Applications must use `FAILSAFE_SCHEMA` to prevent this.

**Code:** loader.js:1498-1508

#### M2: Binary Type OOM -- No Size Limit

`constructYamlBinary` (type/binary.js:35) decodes base64 with no size limit. Intermediate JS array uses 8+ bytes per byte. A 1GB base64 input could consume several GB of heap.

**Code:** type/binary.js:35

#### M3: json:true Disables Duplicate Key Detection

When `json: true`, the duplicate key check (loader.js:368) is skipped. An attacker can craft YAML with a benign first value and a malicious duplicate that silently overwrites it.

**Code:** loader.js:368-375

---

### Low Severity

#### L1: Anchor Name Collision Silently Overwrites

Two nodes with the same anchor name: second silently replaces first. Subsequent aliases resolve to the last-defined anchor.

**Code:** loader.js:1472

#### L2: Key Coercion Collapses Distinct Types

`null`/`~` both become string `"null"`, `0x7B`/`123` both become `"123"`. Different YAML keys can collide after coercion.

**Code:** loader.js:353

---

### Confirmed Safe

| Area | Status |
|------|--------|
| `__proto__` prototype pollution | Mitigated via defineProperty (loader.js:127) |
| `constructor.prototype` global pollution | Not exploitable (clobbers own property only) |
| Merge key (`<<`) bypass | Not vulnerable (setProperty guard applies) |
| All regex patterns (6 tested) | No catastrophic backtracking (ReDoS-safe) |
| Dangerous YAML tags (`!!js/function`, `!!js/regexp`) | Removed in v4 default schema |
| Cross-document contamination | Not possible (anchorMap reset per document) |
| Tag injection via string values | Not possible (tags parsed by dedicated syntax) |
| toString-based code execution in keys | Blocked (loader.js:348) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2013-4660 | Critical | Arbitrary code execution via `!!js/function` tag | 3.0.0 (removed dangerous types) | [osv.dev](https://osv.dev/vulnerability/CVE-2013-4660) |
| **NEW: Billion Laughs** | High | Alias expansion bomb, 873K amplification, no limits | **Unfixed** | This audit |

## Recommendations for Developers

1. **Never parse untrusted YAML without size limits** -- validate input length before calling `yaml.load()`
2. **Use `FAILSAFE_SCHEMA`** for untrusted input to prevent implicit type coercion
3. **Deep-copy or limit alias expansion** in parsed output before serializing or traversing
4. **Monitor memory usage** in services that parse YAML from external sources
5. **Consider alternatives** for untrusted YAML: use JSON where possible, or a YAML parser with built-in expansion limits

## Related Pages

- [[npm/index]]
- [[npm/express]]

---
*Last updated: 2026-04-12 | Sources: 5 (upstream repository, npm registry, source code audit of js-yaml 4.1.1, CVE databases, PoC verification)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
