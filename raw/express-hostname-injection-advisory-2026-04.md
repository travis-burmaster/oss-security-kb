# Express.js Security Advisory: req.hostname Injection via Unsanitized Headers

**Date:** 2026-04-10
**Reporter:** Travis Burmaster ([@travis-burmaster](https://github.com/travis-burmaster))
**Affected Component:** express -- lib/request.js (req.hostname / req.host)
**Affected Versions:** All Express versions through 5.2.1
**CWE:** CWE-113 (Improper Neutralization of CRLF Sequences in HTTP Headers) / CWE-644 (Improper Neutralization of HTTP Headers)
**Severity:** High

## Summary

`req.hostname` reads the `X-Forwarded-Host` header (when trust proxy is enabled) or the `Host` header with zero validation or sanitization. Attackers can inject null bytes, path components, and arbitrary strings that downstream code will treat as a valid hostname.

## Details

The `hostname` getter at `lib/request.js:444-458` strips the port via colon-splitting but performs no further validation:

```js
var index = host.indexOf(':', offset);
return index !== -1
  ? host.substring(0, index)
  : host;
```

**Attack vectors:**

1. **Null byte injection:** `X-Forwarded-Host: evil.com\x00.legit.com`
   - `req.hostname` returns the full string with embedded null
   - Downstream C libraries (DNS resolution, cURL) truncate at the null byte, resolving `evil.com`

2. **Path injection:** `X-Forwarded-Host: evil.com/admin`
   - No path stripping -- `req.hostname` returns `evil.com/admin`
   - URL construction like `https://${req.hostname}/callback` becomes `https://evil.com/admin/callback`

3. **No RFC 952/1123 hostname validation** -- any string is accepted

## In-Scope per Express Threat Model

This is untrusted network data (headers) corrupting API-returned values beyond documented behavior. `req.hostname` is documented as returning "the hostname derived from the Host HTTP header" -- not arbitrary strings with null bytes and paths.

## Impact

- **Cache poisoning:** Web caches keying on Host header serve attacker-controlled content
- **SSRF:** Applications using `req.hostname` in outbound requests reach attacker-controlled servers
- **Password reset poisoning:** Reset emails with links to attacker hostname
- **OAuth callback manipulation:** OAuth redirect URIs constructed from req.hostname

## Recommended Fix

1. Validate `req.hostname` against RFC 952/1123 hostname characters
2. Reject null bytes (`\x00`)
3. Reject path separators (`/`, `\`)
4. Consider stripping or rejecting values that don't match a hostname pattern

## Contact

- **Reporter:** Travis Burmaster
- **GitHub:** [@travis-burmaster](https://github.com/travis-burmaster)
- **Knowledge Base:** https://github.com/travis-burmaster/oss-security-kb
