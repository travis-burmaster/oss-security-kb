# mongoose (npm)

**Registry:** npm
**Weekly Downloads:** unknown (npm API blocked at time of this pass)
**Repository:** https://github.com/Automattic/mongoose
**Security Contact:** https://github.com/Automattic/mongoose/security/advisories
**Disclosure Policy:** GitHub Security Advisories (https://github.com/Automattic/mongoose/security/advisories)
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| GHSA-r5xw-q988-826m | Moderate (CVSS 3.1 AV:L/AC:H) | Remote memory exposure: saving a numeric value to a Buffer-type field allocates uninitialized memory and persists it to the database | 3.8.39, 4.3.6 | [GHSA](https://github.com/advisories/GHSA-r5xw-q988-826m) |
| CVE-2019-17426 / GHSA-8687-vv9j-hgph | Critical (CVSS 9.x AV:N/AC:L) | `_bsontype` attribute bypass: Mongoose fails to validate query objects containing a `_bsontype` field, enabling access-control bypass in applications relying on Mongoose filter validation against older BSON parsers | 4.13.21, 5.7.5 | [GHSA](https://github.com/advisories/GHSA-8687-vv9j-hgph) |
| CVE-2022-2564 / GHSA-f825-f98c-gj3g | High (CVSS AV:N/AC:H) | Schema.path() prototype pollution: `indexOf()` called on array inputs rather than strings enables bypass of the `__proto__` guard, allowing `Object.prototype` manipulation and potential DoS | 5.13.15, 6.4.6 | [GHSA](https://github.com/advisories/GHSA-f825-f98c-gj3g) |
| CVE-2022-24304 / GHSA-h8hf-x3f4-xwgp | Critical (CVSS 9.8 AV:N/AC:L) | Schema.path() prototype pollution: `Schema._getSchema/path` getter allows `__proto__`-prefixed paths to pollute `Object.prototype`; in Express and EJS environments could enable RCE | 5.13.15, 6.4.6 | [GHSA](https://github.com/advisories/GHSA-h8hf-x3f4-xwgp) |
| CVE-2023-3696 / GHSA-9m93-w8w6-76hh | Critical | Prototype pollution in `document.js` functions including `findByIdAndUpdate()`: attacker-controlled field paths containing `__proto__` pollute `Object.prototype`; could enable RCE in Express/EJS environments | 5.13.20, 6.11.3, 7.3.3 | [GHSA](https://github.com/advisories/GHSA-9m93-w8w6-76hh) |
| CVE-2024-53900 / GHSA-m7xq-9374-9rvx | High (CVSS 9.8 AV:N/AC:L) | `$where` operator enables arbitrary JavaScript execution in MongoDB queries when user-controlled input reaches Mongoose query construction — authentication bypass, unauthorized data access, and potential code injection | 5.13.23, 6.13.5, 7.8.3, 8.8.3 | [GHSA](https://github.com/advisories/GHSA-m7xq-9374-9rvx) |
| CVE-2025-23061 / GHSA-vg7j-7cwx-8wgw | Critical (CVSS AV:N/AC:H/S:C) | Incomplete fix for CVE-2024-53900: `$where` operator injection remained exploitable in certain MongoDB query paths despite the prior patch | 6.13.6, 7.8.4, 8.9.5 | [GHSA](https://github.com/advisories/GHSA-vg7j-7cwx-8wgw) |
| CVE-2026-42334 / GHSA-wpg9-53fq-2r8h | High (CVSS 9.1 AV:N/AC:L) | `sanitizeFilter` fails to recursively sanitize `$nor` clauses, allowing injection of `$ne`, `$gt`, or `$regex` operators inside `$nor` — authentication bypass, unauthorized data access, and data exfiltration | 6.13.9, 7.8.9, 8.22.1, 9.1.6 | [GHSA](https://github.com/advisories/GHSA-wpg9-53fq-2r8h) |
| CVE-2026-73562 / GHSA-664h-wqgq-64gw | Moderate (CVSS 3.1 AV:N/AC:L) | Prototype pollution in update casting: user-controlled updates with `__proto__`-prefixed dotted paths pollute `Object.prototype` with `$fullPath` and `$parentSchemaDocArray` properties via `Schema._getSchema/path` | 6.13.10, 7.8.10, 8.24.1, 9.7.2 | [GHSA](https://github.com/advisories/GHSA-664h-wqgq-64gw) |

## Security Posture Notes

Mongoose is the dominant MongoDB ODM for Node.js, maintained by Automattic. Its security profile is dominated by two recurring vulnerability classes:

**1. Prototype pollution (5 advisories, 2022–2026):** The `Schema.path()` / `Schema._getSchema/path` code path and the update-casting layer are repeatedly affected. Any application that passes user-controlled input directly to Mongoose update methods (e.g., `Model.updateOne(filter, req.body)`) without prior sanitization is at risk. Mongoose introduced the `sanitizeFilter` option as a mitigation, but CVE-2026-42334 shows the sanitizer itself had a `$nor` blind spot, compounding the risk.

**2. `$where` operator injection (2 advisories, 2024–2025):** CVE-2024-53900 and its incomplete-fix follow-on CVE-2025-23061 exploit MongoDB's `$where` operator executing arbitrary server-side JavaScript. The risk is highest on MongoDB deployments with `--enableJavaScriptEngine` enabled (disabled by default since MongoDB 4.4). Mitigation: disable JavaScript execution at the MongoDB server level.

The maintainer (vkarpov15 / Automattic) self-discloses via GitHub Security Advisories with typically 1–2 week disclosure-to-fix latency. Security patches are backported to older major lines (5.x and 6.x were still receiving patches in 2026), which is a positive signal for users who cannot migrate immediately.

## Dependencies of Note

- `mpath` — path-based object traversal helper used internally; had its own prototype-pollution advisory (CVE-2021-23438 / GHSA-p92x-r36w-9395, fixed mpath 0.8.4) which indirectly affects Mongoose consumers.
- `bson` — MongoDB BSON serialization library; CVE-2019-17426 relates to an interaction with a `_bsontype` field in older BSON parser versions.
- `kareem` — hook/middleware system for Mongoose; no known direct advisories.

## Open Questions

- Current weekly download count unknown (npm registry API blocked during this pass; check https://npmjs.com/package/mongoose for current figure).
- Are there additional `__proto__`-adjacent schema-resolution paths in 8.x / 9.x that were not covered by the CVE-2026-73562 patch?
- Does the `$where` fix train fully eliminate the attack surface when combined with `allowDiskUse`, query projection, or aggregation pipeline stages?

## Related Pages

- [[npm/express]]
- [[npm/body-parser]]
- [[npm/index]]

---
*Last updated: 2026-09-07 | Sources: 9*
