# send (npm)

**Registry:** npm
**Weekly Downloads:** ~30,000,000 (as of 2026-04-13)
**Repository:** https://github.com/pillarjs/send
**Security Contact:** GitHub Security Advisory
**Current Status:** audit-ingested

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-10 | [@travis-burmaster](https://github.com/travis-burmaster) | full-source (as part of Express 5.2.1 audit) | manual review | 1 finding (medium) + 6 areas confirmed safe | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |

**Audit scope:** send 1.1.0, reviewed as a dependency of Express 5.2.1 and serve-static 2.2.0. Path traversal, encoding bypass, symlink handling, range headers, and dotfile behavior audited.

## Findings

### Medium Severity

#### M1: Symlinks Followed by Default — No Opt-Out

`send` uses `fs.stat()` (not `fs.lstat()`) at line 605. Symlinks inside the served root pointing to files outside it are followed transparently. There is no `followSymlinks: false` option.

**Impact:** If an attacker can create a symlink inside the served root (e.g., via file upload or misconfigured shared storage), they can read arbitrary files on the filesystem.

**Code:** `index.js:605` (`fs.stat`)

**Mitigation:** Ensure no untrusted users can create files/symlinks in the served directory. Use chroot or container isolation.

---

### Confirmed Safe (Path Traversal Defenses)

The send module uses a layered defense against path traversal that was verified to be comprehensive:

| Layer | What It Does | Code |
|-------|-------------|------|
| 1. Decode | `decodeURIComponent` decodes `%2e%2e` to `..`, `%2f` to `/`, `%5c` to `\` in one pass | index.js:411 |
| 2. Null byte check | Rejects paths containing `\0` after decoding (returns 400) | index.js:418 |
| 3. Normalize | `path.normalize('.' + sep + path)` collapses `../` sequences | index.js:427 |
| 4. UP_PATH_REGEXP | `/(?:^|[\\/])\.\.(?:[\\/]|$)/` catches any remaining `..` traversal (returns 403) | index.js:61, 431 |

**Bypass vectors tested and blocked:**

| Vector | Result |
|--------|--------|
| `%2e%2e%2f` (encoded `../`) | Decoded then caught by normalize + regex |
| `%252e%252e` (double encoding) | Decoded to `%2e%2e` (literal, not `..`) — safe, file won't exist |
| `%5c..%5c` (backslash traversal) | Regex explicitly matches both `/` and `\` |
| `%00` (null byte) | Blocked after decode (returns 400) |
| Windows `\..\..\` | Regex catches backslash as separator |
| `....//` variants | normalize collapses, regex catches remaining `..` |

### Other Confirmed Safe Areas

| Area | Status |
|------|--------|
| Range header abuse | Multi-range requests served as full response; single ranges clamped to file size (index.js:534-571) |
| Dotfiles | Default `'ignore'` returns 404; `'deny'` returns 403; `'allow'` serves them. `containsDotFile` checks all path segments (index.js:116, 468, 807) |
| `res.sendFile` without root | When root is null, path must be absolute (throws TypeError). UP_PATH_REGEXP still runs but `resolve()` happens in userland before send sees it — documented as out-of-scope per Express threat model |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2014-6394 | Low | Directory traversal when relying on the `root` option to confine paths; similarly named directories outside the intended root could be exposed | 0.8.4 | [GHSA](https://github.com/advisories/GHSA-xwg4-93c6-3h42) |
| CVE-2015-8859 | Moderate | Root path disclosure leaking the configured absolute `root` path in error handling | 0.11.1 | [GHSA](https://github.com/advisories/GHSA-jgqf-hwc5-hh37) |
| CVE-2024-43799 | Medium | Template injection / XSS in redirect HTML rendering when untrusted input reaches `SendStream.redirect()` | 0.19.0 | [GHSA](https://github.com/advisories/GHSA-m6fv-jmcg-4jfg) |

## Security Posture Notes

- `send` is the static file serving engine behind Express's `res.sendFile()` and the `serve-static` middleware. It powers static file serving for a large fraction of Node.js web applications.
- Public advisory history for the package currently consists of three published CVEs / GHSAs: the 2014 `root`-containment traversal bug, the 2015 `root` path disclosure bug, and the 2024 redirect-page template-injection / XSS issue. Current releases in the 1.x line inherit the 0.19.0 fix for the latest published advisory.
- Path traversal defenses are comprehensive and well-layered in the current code. The 4-layer defense (decode, null check, normalize, regex) is a model implementation, but earlier pre-0.8.4 releases had a public `root`-boundary flaw.
- The symlink issue is a known design choice — `send` does not attempt to jail symlinks because `fs.stat` is the standard Node.js approach. Applications needing symlink protection must handle it at the filesystem/container level.
- `serve-static` (2.2.0) adds no additional security logic beyond `send` — it passes `parseUrl(req).pathname` directly to `send`.

## Recommendations for Developers

1. **Always use the `root` option** with `res.sendFile()` to enforce path containment
2. **Ensure no untrusted symlinks** can be created in served directories
3. **Keep dotfiles at the default `'ignore'`** to prevent serving `.env`, `.git`, etc.
4. **Update to send >= 0.19.1** to fix CVE-2024-43799 (XSS in error responses)

## Related Pages

- [[npm/express]]
- [[npm/index]]

---
*Last updated: 2026-04-14 | Sources: 7 (upstream repository, upstream HISTORY.md, source code audit of send 1.1.0 via Express audit, OSV database, GHSA database, npm registry, Express threat model)*
*Auditor contact: [@travis-burmaster](https://github.com/travis-burmaster)*
