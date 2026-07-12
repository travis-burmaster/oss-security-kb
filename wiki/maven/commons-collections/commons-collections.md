# Apache Commons Collections (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (Maven Central download-count API unavailable this pass)
**Repository:** https://github.com/apache/commons-collections
**Security Contact:** security@apache.org
**Disclosure Policy:** https://www.apache.org/security/
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|
| 2015-11-06 | Gabriel Lawrence & Chris Frohoff (FoxGlove Security) | partial-source | manual | InvokerTransformer / ChainedTransformer gadget chain enabling RCE via Java deserialization; demonstrated against WebLogic, WebSphere, JBoss, Jenkins, OpenNMS | [FoxGlove blog post](https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability) |

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2015-7501 / GHSA-fjq5-5j5f-mvxh | Critical CVSS 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | Deserialization gadget chain: `InvokerTransformer`, `ChainedTransformer`, and `LazyMap` can be composed to execute arbitrary Java methods when a Java application deserializes attacker-controlled data with commons-collections on the classpath. Exploited in the wild against WebLogic, WebSphere, JBoss, Jenkins, and OpenNMS. | commons-collections:commons-collections 3.2.2; org.apache.commons:commons-collections4 4.1 | [GHSA-fjq5-5j5f-mvxh](https://github.com/advisories/GHSA-fjq5-5j5f-mvxh) |
| CVE-2015-6420 / GHSA-6hgm-866r-3cjv | High | Insecure deserialization in Apache Commons Collections: serialized-object interfaces allow remote attackers to execute arbitrary commands via a crafted serialized Java object. Same underlying gadget-chain attack surface as CVE-2015-7501; catalogued under a separate CVE. | commons-collections:commons-collections 3.2.2; org.apache.commons:commons-collections4 4.1 | [GHSA-6hgm-866r-3cjv](https://github.com/advisories/GHSA-6hgm-866r-3cjv) |

## Security Posture Notes

Apache Commons Collections is a foundational Java utility library providing collection implementations (Bag, BidiMap, MultiMap), iterators, functors, and transformers. The `Transformer` interface hierarchy — specifically `InvokerTransformer`, `ChainedTransformer`, `ConstantTransformer`, and `LazyMap` — is the attack surface for both advisories above.

**The November 2015 FoxGlove Security research** demonstrated that any Java application server accepting serialized Java objects over the network (HTTP, RMI, JMX, etc.) and having commons-collections in the classpath was exploitable for unauthenticated RCE. The gadget chain works because Java's deserialization mechanism invokes `readObject()` on all encountered objects, and the transformer chain can be constructed to invoke arbitrary methods via reflection (`java.lang.reflect.Method.invoke`) before the application has any opportunity to validate the payload.

**Two Maven coordinates exist for this project:**
- **`commons-collections:commons-collections`** (3.x line, pre-Apache-Commons-rebranding GA coordinates): last patched release is 3.2.2. This line is mature / no active feature development.
- **`org.apache.commons:commons-collections4`** (4.x line, with generics): minimum safe version is 4.1; active development continues.

**The fix** (3.2.2 / 4.1) added a serialization check via `FunctorUtils.checkUnsafeSerialization()` that throws `UnsupportedOperationException` when the dangerous transformer types are deserialized. Applications that need to serialize these functors must explicitly enable it via the `org.apache.commons.collections.enableUnsafeSerialization` system property.

The `ysoserial` project documents multiple commons-collections gadget chains (`CommonsCollections1` through `CommonsCollections7`) that vary by classpath availability and JVM version compatibility.

Detection signatures typically look for the Java serialization magic bytes `\xac\xed\x00\x05` followed by class references to `org.apache.commons.collections.functors.InvokerTransformer`.

**Recommendation:** Upgrade to commons-collections 3.2.2+ or commons-collections4 4.1+. Use Java 9+ `ObjectInputFilter` or equivalent deserialization filter to allowlist expected types at all deserialization entry points.

## Dependencies of Note

None flagged — commons-collections is a standalone utility library with minimal transitive dependencies.

## Open Questions

- Verify whether commons-collections4 versions after 4.1 introduced additional serialization-related hardening beyond the initial fix.
- Track whether any 2020s-era libraries introduce new gadget chains using commons-collections4 generics-aware functors.

## Related Pages

- [[maven/com.fasterxml.jackson.core/jackson-databind]] — polymorphic deserialization gadget CVE history
- [[maven/org.yaml/snakeyaml]] — YAML type-tag RCE via unsafe type construction
- [[maven/org.apache.logging.log4j/log4j-core]] — Log4Shell JNDI class-loading attack surface
- [[maven/commons-fileupload/commons-fileupload]]
- [[maven/index]]

---
*Last updated: 2026-07-12 | Sources: 3*
