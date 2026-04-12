# js-yaml Security Advisory: Denial of Service via YAML Alias Expansion (Billion Laughs)

**Date:** 2026-04-12
**Reporter:** Travis Burmaster ([@travis-burmaster](https://github.com/travis-burmaster))
**Affected Component:** js-yaml -- lib/loader.js (anchor/alias resolution)
**Affected Versions:** All js-yaml versions through 4.1.1
**CWE:** CWE-776 (Improper Restriction of Recursive Entity References in DTDs)
**Severity:** High (CVSS estimated 7.5 -- network/low complexity/high availability impact)

## Summary

js-yaml has zero limits on YAML anchor/alias expansion. A 308-byte YAML payload produces 269 million characters when serialized -- an 873,513x amplification ratio. One additional nesting level would produce ~2.4 billion characters, crashing any Node.js process.

## Proof of Concept

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

**Verified results (Node.js, js-yaml 4.1.1):**
- Payload: 308 bytes
- Parse time: 4ms (creates shared references -- heap stays small)
- `JSON.stringify(parsed.h)`: 269,042,005 characters (269 MB)
- Amplification: 873,513x
- Theoretical leaf nodes: 9^8 = 43,046,721
- Adding one level: 9^9 = 387 million leaves, ~2.4 billion chars

## Technical Details

YAML anchors (`&name`) define reusable nodes, and aliases (`*name`) reference them. js-yaml stores aliases as shared JS object references (loader.js:1366: `state.result = state.anchorMap[alias]`). The in-memory graph stays small, but any traversal operation -- `JSON.stringify()`, deep clone, recursive iteration, logging, response serialization -- triggers exponential expansion.

**Missing protections (verified in source):**
- No `maxAliasCount` option (State constructor, loader.js:147)
- No alias nesting depth limit (composeNode, loader.js:1371)
- No expanded size limit
- No input length limit
- Code acknowledges the risk at loader.js:330 ("deeply nested arrays that explode exponentially using aliases") but only mitigates it for mapping keys, not general expansion

## Impact

Denial of Service against any Node.js service parsing untrusted YAML via js-yaml (~130M weekly downloads):
- API endpoints accepting YAML input (content-type: application/x-yaml)
- CI/CD configuration parsers
- Kubernetes tooling processing user-supplied YAML
- Configuration management systems
- Any service using `yaml.load()` or `yaml.loadAll()` on untrusted input

Single HTTP request with the 308-byte payload can crash the target process. No authentication required.

## Recommended Fix

1. Add a `maxAliasCount` option (default: 100) to cap total alias dereferences
2. Add a `nestingDepth` limit to `composeNode`
3. Add a `maxInputLength` check at entry points
4. Consider deep-copying aliased values to eliminate shared references

## Contact

- **Reporter:** Travis Burmaster
- **GitHub:** [@travis-burmaster](https://github.com/travis-burmaster)
- **Knowledge Base:** https://github.com/travis-burmaster/oss-security-kb
