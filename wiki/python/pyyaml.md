# pyyaml (python)

**Registry:** PyPI
**Weekly Downloads:** ~236,437,895 (as of 2026-04-22)
**Repository:** https://github.com/yaml/pyyaml
**Security Contact:** mailto:security@pyyaml.org
**Disclosure Policy:** https://github.com/yaml/pyyaml/security
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-04-22 | OpenClaw recurring review | package advisory mapping | public-source curation (OSV.dev, GitHub Advisory Database / PyPA advisory aliases, public CVE records, upstream CHANGES, PyPI metadata, PyPIStats, upstream security-policy page, local Claude-compatible proxy used only as a drafting aid) | Added a new advisory-mapped baseline page for PyYAML's published package security history, centered on the long-running unsafe-deserialization / arbitrary-code-execution fix train through `5.4`. | [oss-security-kb](https://github.com/travis-burmaster/oss-security-kb) |
| *No public proactive audits on record yet.* | — | — | — | — | — |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-18342 / GHSA-rprw-h62v-c2w7 / PYSEC-2018-49 | Critical | Public advisory records say `yaml.load()` could insecurely deserialize untrusted YAML and execute arbitrary code before `4.1`. | 4.1 | https://github.com/advisories/GHSA-rprw-h62v-c2w7 |
| CVE-2019-20477 / GHSA-3pqx-4fqf-j49f / PYSEC-2020-176 | Critical | PyYAML `5.1` through `5.1.2` still allowed dangerous class deserialization through `load` / `load_all`; public records explicitly frame this as an incomplete fix for `CVE-2017-18342`. | 5.2 | https://github.com/advisories/GHSA-3pqx-4fqf-j49f |
| CVE-2020-1747 / GHSA-6757-jp84-gxfx / GHSA-fm6c-f59h-7mmg / PYSEC-2020-96 | Critical | Public advisory records say `full_load` / `FullLoader` remained susceptible to arbitrary code execution through the `python/object/new` constructor before `5.3.1`. | 5.3.1 | https://github.com/advisories/GHSA-6757-jp84-gxfx |
| CVE-2020-14343 / GHSA-8q59-q68h-6hv4 / PYSEC-2021-142 | Critical | Another incomplete-fix record: public advisories say `full_load` / `FullLoader` still allowed arbitrary code execution through `python/object/new` paths before `5.4`. | 5.4 | https://github.com/advisories/GHSA-8q59-q68h-6hv4 |

*Full CVE history: https://osv.dev/list?ecosystem=PyPI&q=pyyaml*

## Security Posture Notes

- PyYAML's public package-advisory history is unusually coherent: the main recurring risk is **unsafe deserialization of attacker-controlled YAML into arbitrary Python objects**, leading to arbitrary code execution rather than low-impact parser-only bugs.
- The public record also shows a clear **fix-then-bypass / incomplete-fix pattern**. `CVE-2019-20477` followed `CVE-2017-18342`, then `CVE-2020-14343` followed `CVE-2020-1747`, so downstream users should not assume the first remediation wave fully closed the loader attack surface.
- Upstream `CHANGES` provides unusually useful public fix breadcrumbs: `5.1` deprecates `yaml.load` and adds `FullLoader` / `UnsafeLoader`; `5.2` says it made `FullLoader` safer by removing `python/object/apply`; `5.3.1` says it prevents arbitrary code execution during `python/object/new` construction; and `5.4` explicitly says it fixes `CVE-2020-14343` by moving arbitrary Python tags to `UnsafeLoader`.
- The project description on PyPI still says PyYAML supports Python-specific tags that can represent arbitrary Python objects. That feature is legitimate functionality, but it also explains why loader selection is a real security boundary rather than a cosmetic API choice.
- Current public metadata shows the package remains extremely widely deployed (~236.4M weekly downloads in this review pass; latest release `6.0.3`), so old unsafe loader behavior can retain large downstream blast radius even when fixes are not new.
- Upstream's security posture is stronger than many infrastructure packages in the KB: the repository exposes a `SECURITY.md`-backed private reporting channel at `security@pyyaml.org` instead of relying only on public issues.
- Public evidence gathered in this pass supports a practical floor of **`5.4+` for the full currently published advisory set** reviewed here, with current maintained releases such as `6.0.3` sitting above that floor.
- The dangerous functionality was not removed entirely; it was pushed behind explicitly unsafe APIs / loaders. That means version upgrades matter, but safe call-site choices still matter too.

## Recommendations for Developers

1. **Prefer `yaml.safe_load()` / `SafeLoader` for untrusted input**; do not treat `yaml.load()` without an explicit safe loader, `full_load`, `FullLoader`, or `UnsafeLoader` as acceptable defaults for attacker-controlled YAML.
2. **Upgrade to `5.4` or newer**; current PyPI metadata in this pass showed `6.0.3` as the latest release.
3. **Search code and dependencies for unsafe loader usage** (`yaml.load(`, `full_load`, `FullLoader`, `UnsafeLoader`) because upgrading the package does not automatically fix unsafe application call patterns.
4. **Treat YAML deserialization as a trust boundary**, especially in config importers, CI/CD tooling, plugin ecosystems, and any workflow that ingests external YAML rather than only developer-authored files.
5. **Watch for follow-on loader hardening advisories**, because the public history shows more than one incomplete fix cycle rather than a single one-off disclosure.

## Dependencies of Note

- PyYAML often sits underneath configuration loaders, CI/CD tooling, infrastructure-as-code helpers, and data-ingestion pipelines rather than only direct top-level application code.
- Security relevance is highest where callers accept YAML from users, tenants, repositories, webhooks, or other semi-trusted sources and then deserialize it into live Python objects.

## Open Questions

- Has the remaining non-`SafeLoader` attack surface received a public comprehensive audit after the `5.4` fix line, or has hardening mainly been advisory-driven so far?
- Which still-maintained Python frameworks, CLIs, or automation stacks continue to pin PyYAML below `5.4` or document unsafe loader usage patterns?
- Should a future KB pass add adjacent Python parser / deserializer pages (for example `ruamel.yaml`) so YAML trust-boundary guidance is easier to compare across ecosystems?
- Are there strong maintainer-authored safe-usage notes beyond the deprecation / changelog breadcrumbs that would help downstream teams migrate away from risky loader choices?

## Related Pages

- [[python/jinja2]]
- [[python/index]]

---
*Last updated: 2026-04-22 | Sources: 8 (OSV.dev package query for PyPI/PyYAML, GitHub Advisory Database entries for the four GHSA records listed above, PyPA advisory aliases via OSV, public CVE / NVD records, upstream `CHANGES`, PyPI project metadata, PyPIStats downloads page, upstream security-policy page)*
