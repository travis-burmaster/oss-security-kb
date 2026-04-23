# vite (npm)

**Registry:** npm
**Weekly Downloads:** ~110,057,895 (2026-04-16 to 2026-04-22)
**Repository:** https://github.com/vitejs/vite
**Security Contact:** GitHub Security Advisories / repository security policy page
**Disclosure Policy:** https://github.com/vitejs/vite/security/policy
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-23 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev package query, GitHub Advisory Database / public GHSA pages, public CVE records, upstream GitHub security policy page, upstream release notes, npm registry metadata, npm downloads API) | Added a new advisory-mapped baseline page for `vite` covering a dense public dev-server advisory history. The strongest recurring theme is repeated `server.fs` / file-serving boundary bypasses, with smaller but still important clusters around dev-server cross-origin exposure and XSS in Vite-controlled HTML / injected bundle code. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive full-source audit on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2026-39363 / GHSA-p9ff-h696-f583 | High | The Vite dev-server WebSocket exposed `fetchModule` without enforcing the normal `server.fs` boundary, allowing arbitrary file reads via `file://...` combined with `?raw` / `?inline` when the dev server was network-accessible. | 6.4.2, 7.3.2, 8.0.5 | https://github.com/advisories/GHSA-p9ff-h696-f583 |
| CVE-2026-39364 / GHSA-v2wj-q39q-566r | High | Another 2026 `server.fs.deny` bypass let attackers reach restricted files through crafted query handling on affected 7.x and 8.x releases. | 7.3.2, 8.0.5 | https://github.com/advisories/GHSA-v2wj-q39q-566r |
| CVE-2026-39365 / GHSA-4w7w-66w2-5vf9 | Moderate | Optimized-dependency `.map` handling in the dev server allowed path traversal to source-map files outside the intended project boundary. | 6.4.2, 7.3.2, 8.0.5 | https://github.com/advisories/GHSA-4w7w-66w2-5vf9 |
| CVE-2025-24010 / GHSA-vg6x-rcgg-rjx6 | Moderate | Default dev-server CORS behavior plus missing Origin / Host validation let malicious sites read dev-server responses and abuse WebSocket connections; the advisory explicitly says this could matter even for local-only development setups. | 4.5.6, 5.4.12, 6.0.9 | https://github.com/advisories/GHSA-vg6x-rcgg-rjx6 |
| CVE-2025-32395 / GHSA-356w-63v5-8wf4 | Moderate | An invalid `request-target` could bypass `server.fs.deny` protections on multiple maintained release lines. | 4.5.13, 5.4.18, 6.0.15, 6.1.5, 6.2.6 | https://github.com/advisories/GHSA-356w-63v5-8wf4 |
| CVE-2025-31125 / GHSA-4r4m-qw57-chr8 | Moderate | `server.fs.deny` could be bypassed for `inline` and `raw` handling through crafted `?import` query usage. | 4.5.11, 5.4.16, 6.0.13, 6.1.3, 6.2.4 | https://github.com/advisories/GHSA-4r4m-qw57-chr8 |
| CVE-2025-30208 / GHSA-x574-m823-4x7w | Moderate | Another 2025 `server.fs.deny` bypass allowed restricted file access through `?raw??` query parsing. | 4.5.10, 5.4.15, 6.0.12, 6.1.2, 6.2.3 | https://github.com/advisories/GHSA-x574-m823-4x7w |
| CVE-2025-31486 / GHSA-xcj6-pq6g-qj4x | Moderate | `server.fs.deny` could also be bypassed with crafted `.svg` or relative-path inputs on multiple maintained branches. | 4.5.12, 5.4.17, 6.0.14, 6.1.4, 6.2.5 | https://github.com/advisories/GHSA-xcj6-pq6g-qj4x |
| CVE-2025-46565 / GHSA-859w-5945-r5v3 | Moderate | A `/.` path trick bypassed `server.fs.deny` for files under the project root. | 4.5.14, 5.4.19, 6.1.6, 6.2.7, 6.3.4 | https://github.com/advisories/GHSA-859w-5945-r5v3 |
| CVE-2025-62522 / GHSA-93m4-6634-74q7 | Moderate | On Windows, backslash handling could bypass `server.fs.deny` protections. | 5.4.21, 6.4.1, 7.0.8, 7.1.11 | https://github.com/advisories/GHSA-93m4-6634-74q7 |
| CVE-2025-58751 / GHSA-g4jq-h2w9-997c | Low | Middleware file-serving could return files whose names shared a prefix with files inside the public directory. | 5.4.20, 6.3.6, 7.0.7, 7.1.5 | https://github.com/advisories/GHSA-g4jq-h2w9-997c |
| CVE-2025-58752 / GHSA-jqfw-vq24-v9c3 | Low | `server.fs` settings were not applied to HTML files on affected versions. | 5.4.20, 6.3.6, 7.0.7, 7.1.5 | https://github.com/advisories/GHSA-jqfw-vq24-v9c3 |
| CVE-2024-45812 / GHSA-64vr-g452-qvp3 | Moderate | A DOM-clobbering gadget in Vite-injected bundled scripts could lead to XSS in production bundles that used the affected injected code path. | 3.2.11, 4.5.4, 5.1.8, 5.2.14, 5.3.6, 5.4.6 | https://github.com/advisories/GHSA-64vr-g452-qvp3 |
| CVE-2024-45811 / GHSA-9cwx-2883-4wfx | Moderate | `server.fs.deny` could be bypassed with `?import&raw` handling. | 3.2.11, 4.5.4, 5.1.8, 5.2.14, 5.3.6, 5.4.6 | https://github.com/advisories/GHSA-9cwx-2883-4wfx |
| CVE-2024-31207 / GHSA-8jhw-289h-jh2g | Moderate | `server.fs.deny` did not correctly deny patterns with directories, creating another dev-server file-boundary bypass. | 2.9.18, 3.2.10, 4.5.3, 5.0.13, 5.1.7, 5.2.6 | https://github.com/advisories/GHSA-8jhw-289h-jh2g |
| CVE-2024-23331 / GHSA-c24v-8rfc-w8vw | High | On case-insensitive filesystems, dev-server `server.fs.deny` protections could be bypassed. | 2.9.17, 3.2.8, 4.5.2, 5.0.12 | https://github.com/advisories/GHSA-c24v-8rfc-w8vw |
| CVE-2023-49293 / GHSA-92r3-m2mg-pj97 | Moderate | `server.transformIndexHtml` could be abused for XSS through a crafted URL payload on affected 4.x and 5.x releases. | 4.4.12, 4.5.1, 5.0.5 | https://github.com/advisories/GHSA-92r3-m2mg-pj97 |
| CVE-2023-34092 / GHSA-353f-5xf4-qw67 | High | A double-forward-slash path trick bypassed `server.fs.deny`, starting the now-visible public pattern of repeated file-boundary bypasses in Vite's dev server. | 2.9.16, 3.2.7, 4.0.5, 4.1.5, 4.2.3, 4.3.9 | https://github.com/advisories/GHSA-353f-5xf4-qw67 |
| CVE-2022-35204 / GHSA-mv48-hcvh-8jj8 | High | Older Vite versions were vulnerable to directory traversal through a crafted URL to the dev server. | 2.9.13, 3.0.0-beta.4 | https://github.com/advisories/GHSA-mv48-hcvh-8jj8 |

## Security Posture Notes

- `vite` has a **large, clearly real package-level advisory history**. The public package query used in this pass returned 19 published records spanning 2022 through 2026.
- The dominant recurring theme is **dev-server file-boundary enforcement**. Most public advisories gathered here are variants of arbitrary file read, path traversal, or `server.fs.deny` / file-serving bypass behavior rather than classic production-runtime bugs.
- A second clear theme is **dev-server trust boundaries**. `GHSA-vg6x-rcgg-rjx6` shows that permissive CORS plus missing Origin / Host validation could expose dev-server responses and HMR-related behavior to malicious sites, including in some local-development scenarios.
- Vite also has a smaller but important **XSS lineage** in Vite-controlled output paths: `GHSA-92r3-m2mg-pj97` affected `server.transformIndexHtml`, while `GHSA-64vr-g452-qvp3` affected Vite-injected bundled scripts via DOM clobbering.
- The upstream repository security policy is unusually explicit about threat modeling. It says inbound network requests to the dev and preview servers must be treated as hostile, explicitly treats plugins/config/project files as trusted, and notes that some availability-only issues fall outside the vulnerability bar even if they are still fixed.
- Release tags `v4.5.6`, `v5.4.12`, and `v6.0.9` explicitly say they contain **breaking changes due to security fixes** for `GHSA-vg6x-rcgg-rjx6`, which is a useful public signal that upstream was willing to change defaults or compatibility for dev-server hardening.
- The newest three public advisories gathered in this pass all landed together in the April 2026 fix train for `v6.4.2`, `v7.3.2`, and `v8.0.5`, reinforcing that Vite still receives coordinated security backports across multiple major lines.
- Current npm metadata in this pass showed `latest=8.0.10`, which is newer than the latest fix point reviewed here (`8.0.5`).

## Recommendations for Developers

1. **Upgrade to a patched Vite release on your supported major line**, and treat `8.0.5` / `7.3.2` / `6.4.2` or newer as the minimum safe floor for the newest 2026 dev-server file-read and traversal issues reviewed here.
2. **Do not assume the dev server is harmless because it is "just development."** Vite's public record shows repeated confidentiality-boundary failures that matter in shared workstations, containers, remote dev environments, CI, port-forwarded setups, and accidentally exposed local services.
3. **Review any custom use of `server.fs`, `server.host`, reverse proxies, and HMR/WebSocket exposure** during upgrades, especially around the security-driven release lines that introduced behavioral changes.
4. **Be careful with Vite-controlled HTML and injected script paths** if you generate pages from untrusted data; public XSS records exist even though the package's dominant theme is file access.
5. **Treat plugins and proxy targets as separate trust boundaries**, because the upstream policy explicitly considers them trusted-by-developer inputs rather than Vite-core vulnerabilities.

## Dependencies of Note

- Vite is both a **build tool and a network-facing dev server**, so its risk profile is different from parser-only or utility-only npm packages in this KB.
- The public advisory set gathered here is mostly about Vite core request handling and file serving, not a single transitive dependency chain.
- Downstream projects that expose Vite over a LAN, reverse proxy, container port, cloud IDE, or shared dev platform deserve extra attention because that repeatedly appears in advisory preconditions.

## Open Questions

- Has anyone published a dedicated full-source security review of modern Vite dev-server surfaces beyond the individual advisory disclosures?
- Which hosted development environments or starter templates still pin Vite below the 2026 fix train on active branches?
- Should the KB eventually build a comparison cluster for development-server trust boundaries across `vite`, `webpack-dev-server`, and `esbuild`?

## Related Pages

- [[npm/esbuild]]
- [[npm/webpack-dev-server]]
- [[npm/index]]

---
*Last updated: 2026-04-23 | Sources: 26 (OSV.dev package query for npm/vite, 19 OSV / GHSA vulnerability records, public CVE records, upstream GitHub security policy page, upstream release notes for v4.5.6, v5.4.12, v6.0.9, v6.4.2, v7.3.2, and v8.0.5, npm registry metadata, npm downloads API, plus a successful local proxy drafting pass used only as a synthesis aid)*
