# org.yaml:snakeyaml (Maven)

**Registry:** Maven (Maven Central)
**Weekly Downloads:** unknown
**Repository:** https://github.com/snakeyaml/snakeyaml
**Security Contact:** upstream issue tracker / GitHub Security Advisory process
**Disclosure Policy:** not identified in this pass
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-10 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation (OSV.dev package query and vulnerability records, GitHub Advisory Database aliases, public CVE records, upstream Bitbucket/GitHub references, Maven Central metadata; local proxy synthesis used only as a drafting aid) | Added initial Maven package page mapping 8 public SnakeYAML advisories across unsafe Java object construction / deserialization RCE, alias expansion, nested collection resource exhaustion, and parser stack-overflow DoS. | https://osv.dev/list?ecosystem=Maven&q=org.yaml%3Asnakeyaml |

## Known Vulnerabilities

The table below is a package-level public advisory map from OSV.dev for `org.yaml:snakeyaml`, cross-checked against GHSA aliases and upstream/public references listed by the advisories. Maven Central metadata reported `2.6` as the latest release during this pass.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2022-1471 / GHSA-mjmj-j48q-9wg2 | Critical / RCE | Unsafe deserialization through SnakeYAML's `Constructor` path can instantiate attacker-controlled Java types from untrusted YAML before type mismatch handling occurs. The public Google Security Research advisory describes this as remote code execution when a gadget chain is reachable. | 2.0 | https://osv.dev/vulnerability/GHSA-mjmj-j48q-9wg2 ; https://github.com/google/security-research/security/advisories/GHSA-mjmj-j48q-9wg2 |
| CVE-2022-25857 / GHSA-3mc7-4q67-w48m | High / DoS | Uncontrolled resource consumption in nested collections can allow crafted YAML input to exhaust parser resources. | 1.31 | https://osv.dev/vulnerability/GHSA-3mc7-4q67-w48m ; https://bitbucket.org/snakeyaml/snakeyaml/issues/525 |
| CVE-2022-38749 / GHSA-c4r9-r8fh-9vj2 | High / DoS | Crafted YAML with many open nested structures can trigger stack overflow / parser crash behavior; OSV links the issue to upstream and public analysis references. | 1.31 | https://osv.dev/vulnerability/GHSA-c4r9-r8fh-9vj2 ; https://bitbucket.org/snakeyaml/snakeyaml/issues/525/got-stackoverflowerror-for-many-open |
| CVE-2022-38750 / GHSA-hhhw-99gj-p3c3 | High / DoS | OSS-Fuzz-reported stack overflow / denial-of-service variant in SnakeYAML parsing of crafted input. | 1.31 | https://osv.dev/vulnerability/GHSA-hhhw-99gj-p3c3 ; https://bitbucket.org/snakeyaml/snakeyaml/issues/526/stackoverflow-oss-fuzz-47027 |
| CVE-2022-38751 / GHSA-98wm-3w3q-mw94 | High / DoS | OSS-Fuzz-reported stack overflow / denial-of-service variant in SnakeYAML parsing of crafted input. | 1.31 | https://osv.dev/vulnerability/GHSA-98wm-3w3q-mw94 ; https://bitbucket.org/snakeyaml/snakeyaml/issues/530/stackoverflow-oss-fuzz-47039 |
| CVE-2022-38752 / GHSA-9w3m-gqgf-c4p9 | High / DoS | Additional stack overflow / denial-of-service variant associated with OSS-Fuzz issue 47081. | 1.32 | https://osv.dev/vulnerability/GHSA-9w3m-gqgf-c4p9 ; https://bitbucket.org/snakeyaml/snakeyaml/issues/531/stackoverflow-oss-fuzz-47081 |
| CVE-2022-41854 / GHSA-w37g-rhq8-7m4j | High / DoS | Crafted input can lead to stack overflow denial of service; OSV links the advisory to the same upstream issue lineage as CVE-2022-38752. | 1.32 | https://osv.dev/vulnerability/GHSA-w37g-rhq8-7m4j ; https://bitbucket.org/snakeyaml/snakeyaml/issues/531 |
| CVE-2017-18640 / GHSA-rvwf-54qp-4r6v | High / DoS | Entity / alias expansion during `load` can cause denial of service similar to YAML bomb / exponential expansion patterns. | 1.26 | https://osv.dev/vulnerability/GHSA-rvwf-54qp-4r6v ; https://nvd.nist.gov/vuln/detail/CVE-2017-18640 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=org.yaml%3Asnakeyaml*

## Security Posture Notes

- The public advisory pattern has two main clusters: **unsafe object construction / deserialization** before the 2.x line, and **parser resource-exhaustion / stack-overflow denial of service** in the 1.x parser.
- `2.0` is the key security boundary for the critical unsafe-deserialization record (`CVE-2022-1471`). OSV lists `2.0` as the fixed version; operational upgrades should account for API and behavior changes around constructors / safe loading rather than treating it as a purely patch-level update.
- For organizations still pinned to the 1.x line, `1.32` addressed the published 2022 stack-overflow family, but it does **not** address `CVE-2022-1471` according to the OSV fixed-version data. Treat `2.x` as the safer target for untrusted YAML input.
- Exposure is strongly application-dependent. Risk is highest when services parse YAML supplied by users, tenants, CI jobs, plugins, configuration uploads, or other semi-trusted integration paths.
- Several DoS records are linked to OSS-Fuzz / upstream parser bug reports, which is useful evidence that parser hardening has been exercised, while also showing that deeply nested or malformed YAML remains the dominant direct-input risk surface.

## Dependencies of Note

- SnakeYAML is commonly pulled into Java applications through frameworks and build/runtime tooling that parse YAML configuration. Downstream exposure should be checked through SBOMs and dependency trees, not only direct `pom.xml` declarations.
- No transitive dependency advisory was normalized in this pass; this page is focused on direct `org.yaml:snakeyaml` package advisories.

## Open Questions

- Which major Java frameworks or libraries still transitively pin SnakeYAML below 2.0 in supported release lines?
- Should the KB add a cross-ecosystem YAML parser risk page comparing Java SnakeYAML, Python PyYAML, npm `js-yaml` / `yaml`, and related parser hardening patterns?
- Are there public maintainer release notes that should be added here to explain the 1.x-to-2.x constructor behavior change in more detail?

## Related Pages

- [[python/pyyaml]]
- [[npm/js-yaml]]
- [[npm/yaml]]
- [[maven/index]]

---
*Last updated: 2026-05-10 | Sources: 5 (OSV package query and individual vulnerability records, GitHub Advisory Database public aliases, public CVE records, upstream Bitbucket/GitHub advisory references, Maven Central metadata)*
