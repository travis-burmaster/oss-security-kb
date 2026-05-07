# com.fasterxml.jackson.core:jackson-databind (Maven)

**Registry:** Maven (Maven Central)  
**Weekly Downloads:** unknown  
**Repository:** https://github.com/FasterXML/jackson-databind  
**Security Contact:** FasterXML / GitHub Security Advisories  
**Disclosure Policy:** https://github.com/FasterXML/jackson-databind/security/policy  
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2026-05-07 | OpenClaw recurring review | advisory mapping (public records only) | public-source curation (OSV.dev Maven package query, GitHub Advisory Database aliases, public CVE aliases, FasterXML maintainer CVE-criteria wiki, Maven Central metadata; local proxy synthesis used only as a drafting aid) | Added initial Maven package page. OSV returned 69 public package records; this page maps representative high-signal records and separates polymorphic-deserialization gadget CVEs from XXE and resource-exhaustion advisories. | https://osv.dev/list?ecosystem=Maven&q=com.fasterxml.jackson.core%3Ajackson-databind |

## Known Vulnerabilities

The table below is a representative package-level public advisory map for `com.fasterxml.jackson.core:jackson-databind`. OSV currently lists 69 package records, heavily concentrated in the 2017-2020 polymorphic-deserialization gadget era; the full package listing should be consulted for exhaustive gadget-blocklist records.

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2017-7525 / GHSA-qxxx-2pp7-5hmx | High / deserialization RCE risk | Early public `jackson-databind` deserialization flaw affecting applications that accepted untrusted JSON while enabling polymorphic typing / default typing with exploitable gadget classes available. | 2.6.7.1, 2.7.9.1, 2.8.9 | https://osv.dev/vulnerability/GHSA-qxxx-2pp7-5hmx |
| CVE-2017-15095 / GHSA-h592-38cm-4ggp | Critical / deserialization RCE risk | Unauthenticated remote-code-execution risk through unsafe deserialization under the same polymorphic typing and gadget-class preconditions. | 2.8.11, 2.9.4, 2.6.7.3, 2.7.9.2 | https://osv.dev/vulnerability/GHSA-h592-38cm-4ggp |
| CVE-2018-7489 / GHSA-cggj-fvv3-cqwv | Critical / deserialization RCE risk | Additional unauthenticated RCE gadget-chain advisory in the pre-2.10 blocklist era. | 2.8.11.1, 2.9.5, 2.7.9.3, 2.6.7.5 | https://osv.dev/vulnerability/GHSA-cggj-fvv3-cqwv |
| CVE-2018-14719 / GHSA-4gq5-ch57-c2mg | High / arbitrary code execution | Polymorphic deserialization gadget advisory recorded as arbitrary code execution in `jackson-databind`. | 2.9.7, 2.8.11.3, 2.7.9.5 | https://osv.dev/vulnerability/GHSA-4gq5-ch57-c2mg |
| CVE-2019-12086 / GHSA-5ww9-j83m-q7qx | Moderate / information exposure | File-content information exposure under unsafe deserialization conditions, distinct from direct code execution but still part of the polymorphic typing risk family. | 2.9.9, 2.8.11.4, 2.7.9.6, 2.6.7.3 | https://osv.dev/vulnerability/GHSA-5ww9-j83m-q7qx |
| CVE-2019-20330 / GHSA-gww7-p5w4-wrfv | High / deserialization RCE risk | Later 2019 deserialization gadget record; fixed across maintained legacy lines including 2.9.10.2. | 2.6.7.4, 2.7.9.7, 2.8.11.5, 2.9.10.2 | https://osv.dev/vulnerability/GHSA-gww7-p5w4-wrfv |
| CVE-2020-8840 / GHSA-4w82-r329-3q67 | Critical / deserialization RCE risk | High-profile unsafe-deserialization gadget advisory; fixed in multiple legacy lines and 2.9.10.3. | 2.6.7.4, 2.7.9.7, 2.8.11.5, 2.9.10.3 | https://osv.dev/vulnerability/GHSA-4w82-r329-3q67 |
| CVE-2020-25649 / GHSA-288c-cq4h-88gq | High / XXE | XML external entity issue in Jackson Databind. Unlike most gadget-chain records, this is not primarily a default-typing gadget advisory. | 2.6.7.4, 2.9.10.7, 2.10.5.1 | https://osv.dev/vulnerability/GHSA-288c-cq4h-88gq |
| CVE-2020-36518 / GHSA-57j2-w4cx-62h2 | High / DoS | Deeply nested JSON can trigger uncontrolled resource consumption / denial of service. | 2.13.2.1, 2.12.6.1 | https://osv.dev/vulnerability/GHSA-57j2-w4cx-62h2 |
| CVE-2021-46877 / GHSA-3x8x-79m2-3w2w | Moderate / DoS | Possible denial of service when using JDK serialization to serialize `JsonNode`. | 2.12.6, 2.13.1 | https://osv.dev/vulnerability/GHSA-3x8x-79m2-3w2w |
| CVE-2022-42003 / GHSA-jjjh-jjxp-wpff | High / DoS | Uncontrolled resource consumption in Jackson Databind; one of the post-gadget-era nested-input DoS records. | 2.12.7.1, 2.13.4.2 | https://osv.dev/vulnerability/GHSA-jjjh-jjxp-wpff |
| CVE-2022-42004 / GHSA-rgv9-q543-rqg4 | High / DoS | Uncontrolled resource consumption in Jackson Databind related to deeply nested arrays when certain deserialization features are used. | 2.12.7.1, 2.13.4 | https://osv.dev/vulnerability/GHSA-rgv9-q543-rqg4 |

*Full OSV package listing: https://osv.dev/list?ecosystem=Maven&q=com.fasterxml.jackson.core%3Ajackson-databind*

## Security Posture Notes

- The advisory history is unusually dense, but the largest cluster is **configuration- and classpath-dependent polymorphic deserialization**. The FasterXML maintainer criteria page says the classic gadget-chain condition requires all of: untrusted JSON input, default typing or equivalent `@JsonTypeInfo` on `Object`-typed values, a vulnerable gadget class on the classpath, and Jackson 2.9.x or lower.
- Jackson 2.10 changed the mitigation model: unsafe default-typing methods were deprecated / documented as risky, and safer allow-list based polymorphic typing via `PolymorphicTypeValidator` became the preferred model. This matters when interpreting old gadget CVEs; version alone is not always enough to determine application exploitability.
- Not all records are gadget-chain issues. XXE (CVE-2020-25649) and resource-exhaustion / deeply nested input DoS records (CVE-2020-36518, CVE-2021-46877, CVE-2022-42003, CVE-2022-42004) should be tracked separately because their exposure conditions differ.
- For operational review, prioritize applications that deserialize attacker-controlled JSON, enable default typing or broad polymorphic typing, expose XML/DOM binding paths, or accept deeply nested / adversarial JSON without request-size and parse-depth controls.
- The maintainer wiki notes regular additions to the 2.9 block list ended after the 2.9.10.8 micro-patch line; downstreams still on old 2.9.x or older lines should not assume future blocklist coverage for newly reported gadget classes.

## Dependencies of Note

- `jackson-databind` is a foundational transitive dependency across Java web frameworks, data platforms, and enterprise middleware. Exposure often comes through transitive dependency trees rather than direct application code.
- Gadget-chain exploitability depends on the broader runtime classpath, so SBOM review should include both the Jackson version and high-risk gadget libraries present in the same application.

## Open Questions

- Which high-download Maven packages in this KB pull `jackson-databind` transitively below 2.13.4.2 or still use 2.9.x-era lines?
- Should the KB add a cross-package note for unsafe polymorphic deserialization patterns across Java serializers and JSON/XML binders?
- Which public Spring Boot / Dropwizard / Hadoop-family advisories explicitly cite vulnerable `jackson-databind` reachability through application endpoints rather than dependency presence alone?

## Related Pages

- [[maven/index]]
- [[npm/serialize-javascript]]
- [[python/pyyaml]]

---
*Last updated: 2026-05-07 | Sources: 5 (OSV package query and individual vulnerability records, GitHub Advisory Database public aliases, public CVE aliases referenced by OSV/GHSA records, FasterXML maintainer CVE-criteria wiki, Maven Central metadata)*
