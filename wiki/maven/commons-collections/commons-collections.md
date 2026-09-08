# Apache Commons Collections (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (ubiquitous transitive dependency; billions of historical downloads)
**Repository:** https://github.com/apache/commons-collections
**Security Contact:** security@apache.org
**Disclosure Policy:** https://www.apache.org/security/
**Current Status:** advisory-mapped

## Audit History

*No audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2015-7501 / GHSA-fjq5-5j5f-mvxh | Critical CVSS 9.8 | Deserialization of untrusted data via InvokerTransformer / ChainedTransformer gadget chains enables arbitrary remote code execution when the library is on the classpath of a Java application that deserializes untrusted objects. Gadget chain exposed by Frohoff & Lawrence ("Marshalling Pickles", AppSecCali 2015); exploited in the wild against JBoss, WebLogic, WebSphere, Jenkins, and others. | commons-collections 3.2.2; commons-collections4 4.1 | [GHSA-fjq5-5j5f-mvxh](https://github.com/advisories/GHSA-fjq5-5j5f-mvxh) |
| CVE-2015-6420 / GHSA-6hgm-866r-3cjv | High | Remote code execution via crafted serialized Java object leveraging Apache Commons Collections; same underlying gadget-chain root cause as CVE-2015-7501 with a distinct CVE assignment tracking exploitability through Cisco products and other systems. | commons-collections 3.2.2; commons-collections4 4.1 | [GHSA-6hgm-866r-3cjv](https://github.com/advisories/GHSA-6hgm-866r-3cjv) |

## Security Posture Notes

Apache Commons Collections is a foundational Java utility library providing transformer, predicate, and collection-factory utilities that has been a standard transitive dependency in Java enterprise stacks since the early 2000s. The 2015 deserialization crisis arose from the `InvokerTransformer` class, which invokes arbitrary Java reflection methods. When chained through Commons Collections' `TransformedMap` or `LazyMap`, it creates a "gadget chain" that allows any untrusted Java serialization stream to trigger arbitrary method invocations — and therefore arbitrary code execution — without any explicit deserialization hook in the target application's own code.

The Apache Commons team patched both branches:
- **commons-collections 3.2.2** (November 2015): restricted `InvokerTransformer` deserialization via a `UnsafeSerialization` system property that defaults to disabled.
- **commons-collections4 4.1** (November 2015): added `enableUnsafeSerialization()` gate; serialization of unsafe transformers disabled by default.

Many downstream frameworks (JBoss, WebLogic, WebSphere, Jenkins, OpenNMS, and others) required emergency patching to bundle the fixed versions. CVE-2015-6420 was assigned to track exploitability in Cisco products; CVE-2015-7501 covers the library-level root cause as disclosed by the Apache/Red Hat security teams.

**3.x line:** last release is 3.2.2 (2015), now in maintenance-only mode.
**4.x line:** current stable is 4.4 (2019), actively maintained as `org.apache.commons:commons-collections4`.

Third-party re-packagings (`net.sourceforge.collections:collections-generic` through 4.01, `org.apache.servicemix.bundles:org.apache.servicemix.bundles.commons-collections`) carry the same gadget chains and require separate tracking.

## Dependencies of Note

None flagged beyond the deserialization blast-radius concern itself. Projects using Java object serialization with untrusted data while commons-collections 3.x ≤ 3.2.1 or 4.x ≤ 4.0 is on the classpath are at risk regardless of whether they directly call commons-collections APIs.

## Open Questions

- Full gadget-chain coverage in commons-collections4 4.4 re-enable path (after calling `enableUnsafeSerialization()`) not yet mapped.
- Interaction with JEP 290 deserialization filters (added Java 9+) not documented on this page.
- commons-collections4 4.2–4.4 release history for any additional security fixes not yet confirmed.

## Related Pages

- [[maven/com.thoughtworks.xstream/xstream]] — XStream also addressed many deserialization gadget-chain exposures
- [[maven/com.fasterxml.jackson.core/jackson-databind]] — parallel polymorphic-deserialization gadget CVE history
- [[maven/org.yaml/snakeyaml]] — similar unsafe deserialization / object construction history
- [[maven/index]]

---
*Last updated: 2026-09-08 | Sources: 2*
