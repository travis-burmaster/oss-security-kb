# Express.js Security Advisory: Open Redirect in res.redirect()

**Date:** 2026-04-10
**Reporter:** Travis Burmaster ([@travis-burmaster](https://github.com/travis-burmaster))
**Affected Component:** express -- lib/response.js (res.redirect / res.location)
**Affected Versions:** All Express versions through 5.2.1
**CWE:** CWE-601 (URL Redirection to Untrusted Site)
**Severity:** High

## Summary

`res.redirect()` performs no validation on the redirect URL scheme or destination. Any application that passes user-controlled input to `res.redirect()` is vulnerable to open redirect attacks via `javascript:`, `data:`, and protocol-relative (`//evil.com`) URLs.

## Details

`res.redirect(url)` calls `this.location(address)` (response.js line 836), which runs `encodeUrl(url)` (line 795). The `encodeUrl` function only encodes characters outside the printable ASCII range. Colons, slashes, and letters all pass through, meaning URL schemes are never validated.

**Attack vectors:**
```
GET /login?next=javascript:alert(document.cookie)
GET /login?next=//evil.com/phish
GET /login?next=data:text/html,<script>alert(1)</script>
```

**Vulnerable pattern (extremely common):**
```js
app.get('/login', (req, res) => {
  // After authentication...
  res.redirect(req.query.next || '/');
});
```

## In-Scope per Express Threat Model

This falls within Express's documented threat model: untrusted network data (query parameters) initiates actions (redirect to attacker-controlled URL) beyond those documented for the API. The redirect API does not document that it will redirect to arbitrary schemes including `javascript:`.

## Impact

- Credential phishing via redirect to attacker-controlled login pages
- Cross-site scripting via `javascript:` scheme redirects
- Token theft via redirect to attacker-controlled OAuth callback URLs
- Session fixation via redirect to attacker-controlled session setup pages

This is an OWASP Top 10 vulnerability. The `req.query.next` / `req.query.returnTo` pattern is ubiquitous in Express login/logout flows.

## Recommended Fix

Validate the redirect URL in `res.location()`:
1. Reject `javascript:`, `data:`, `vbscript:`, and other dangerous schemes
2. Reject protocol-relative URLs (`//...`) unless explicitly opted in
3. Consider defaulting to same-origin redirects only, with an explicit opt-out for cross-origin

## Contact

- **Reporter:** Travis Burmaster
- **GitHub:** [@travis-burmaster](https://github.com/travis-burmaster)
- **Knowledge Base:** https://github.com/travis-burmaster/oss-security-kb
