# js-yaml (npm)

**Registry:** npm
**Weekly Downloads:** ~130,000,000 (as of 2026-04-12)
**Repository:** https://github.com/nodeca/js-yaml
**Security Contact:** GitHub Security Advisory (private reporting enabled)
**Current Status:** advisory-mapped + audit-ingested (finding disputed)

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-12 | [@travis-burmaster](https://github.com/travis-burmaster) | full-source (loader, dumper, all types, schema) | hybrid (manual review + PoC) | 6 findings reviewed; highest-severity alias-expansion DoS claim disputed by maintainer as downstream serialization behavior rather than package vulnerability | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| 2026-04-20 | OpenClaw recurring review | published advisory reconciliation | public-source curation (OSV.dev, public CVE records, upstream changelog / fix references, GitHub Security Advisories) | Reconciled the page against the published advisory set and added three previously missing public records (`3.13.0`, `3.13.1`, `3.14.2` / `4.1.1`) while preserving the clearly disputed internal audit note separately from package-level advisories. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

**Audit scope:** js-yaml 4.1.1, 3867 lines across 24 files. Loader (1733 lines), dumper (965 lines), all 13 type handlers, schema system. Commit `f8e56bd` (nodeca/js-yaml main branch, 2026-04-12).

## Findings

### Disputed Finding

#### D1: Alias Expansion / Serialization Amplification (maintainer-disputed as package vulnerability)

**Severity:** Under review / disputed
**Status:** Maintainer response says this is downstream `JSON.stringify` behavior, not a js-yaml parser vulnerability

A 308-byte YAML payload was observed to produce 269 million characters when the resulting structure was serialized (`JSON.stringify`), approximately 873,513x amplification. The maintainer response on issue #742 argues the parser is returning the requested structure and that the blow-up is being attributed to downstream serialization rather than a package security defect.

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

**Impact:** At minimum, this is an operational safety / dangerous-defaults concern for applications that parse attacker-controlled YAML and then serialize or traverse the expanded structure. Whether it should be classified as a package vulnerability is currently disputed by the maintainer.

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
| GHSA-xxvw-45rp-3mj2 / CVE-2013-4660 | Critical | Deserialization code execution through the legacy `!!js/function` constructor in older releases. | 2.0.5 | [GitHub Advisory Database](https://github.com/advisories/GHSA-xxvw-45rp-3mj2) |
| GHSA-2pr6-76vf-7546 | Moderate | `safeLoad()` could hang on crafted input that used arrays with nested references as mapping keys; upstream `3.13.0` changed that path to throw instead. | 3.13.0 | [OSV.dev](https://osv.dev/vulnerability/GHSA-2pr6-76vf-7546) |
| GHSA-8j8c-7jfh-h6hx | High | Possible code execution in the already-unsafe `.load()` path until the `3.13.1` security fix. | 3.13.1 | [OSV.dev](https://osv.dev/vulnerability/GHSA-8j8c-7jfh-h6hx) |
| GHSA-mh29-5h37-fv8m / CVE-2025-64718 | Moderate | Prototype pollution in YAML merge (`<<`) handling; upstream fixed the main line in `4.1.1` and backported the fix to `3.14.2`. | 3.14.2 / 4.1.1 | [GitHub Advisory Database](https://github.com/advisories/GHSA-mh29-5h37-fv8m) |
| **REPORTED / DISPUTED: Alias expansion amplification** | Under review | Alias expansion can lead to extreme downstream serialization amplification; maintainer disputes that this is a package vulnerability | disputed | This audit + upstream issue #742 |

## Recommendations for Developers

1. **Never parse untrusted YAML without size limits** -- validate input length before calling `yaml.load()`
2. **Use `FAILSAFE_SCHEMA`** for untrusted input to prevent implicit type coercion
3. **Prefer `4.1.1+` on the modern line or `3.14.2+` on the legacy v3 line** so the full currently published advisory set is covered
4. **Be cautious serializing or recursively traversing expanded alias structures**
5. **Monitor memory usage** in services that parse YAML from external sources
6. **Treat the alias-expansion issue as disputed** until upstream accepts it as a package vulnerability or a stronger parser-level exhaustion case is demonstrated

## Related Pages

- [[npm/index]]
- [[npm/express]]

---
*Last updated: 2026-04-20 | Sources: 9 (upstream repository, OSV.dev package query and vulnerability records, GitHub Security Advisories / GitHub Advisory Database, public CVE / NVD records, upstream changelog and fix references, npm registry, source code audit of js-yaml 4.1.1, PoC verification, upstream issue #742 maintainer response)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
