# com.google.protobuf:protobuf-java (Maven)

**Registry:** Maven Central
**Weekly Downloads:** unknown (Maven Central does not publish download statistics; protobuf-java is a foundational dependency of gRPC-Java, Google Cloud Java SDKs, Kubernetes Java client, and hundreds of thousands of Maven/Gradle projects worldwide)
**Repository:** https://github.com/protocolbuffers/protobuf
**Security Contact:** security@google.com
**Disclosure Policy:** https://github.com/protocolbuffers/protobuf/blob/main/SECURITY.md
**Current Status:** advisory-mapped

## Audit History

| Date | Auditor | Scope | Methodology | Findings | Source |
|------|---------|-------|-------------|----------|--------|

*No formal public audits on record.*

## Known Vulnerabilities

| CVE / Issue | Severity | Description | Fixed in | Source |
|-------------|----------|-------------|----------|--------|
| CVE-2024-7254 / GHSA-735f-pc8j-v9w8 | High (CVSS 7.5 AV:N/AC:L/PR:N/UI:N/A:H) | Denial of service via StackOverflow when parsing unknown fields or extensions with excessive nesting depth. Affects `protobuf-java`, `protobuf-javalite`, `protobuf-kotlin`, `protobuf-kotlin-lite`. | 3.25.5; 4.27.5; 4.28.2 | [GHSA-735f-pc8j-v9w8](https://github.com/advisories/GHSA-735f-pc8j-v9w8) |
| CVE-2022-3510 / GHSA-4gg5-vx3j-xwc7 | High (CVSS 7.5 AV:N/AC:L/PR:N/UI:N/A:H) | Uncontrolled resource consumption in Message-Type Extensions parsing; overly large or deeply nested input causes excessive memory allocation and GC pressure, enabling remote DoS. Affects `protobuf-java` and `protobuf-javalite`. | 3.16.3; 3.19.6; 3.20.3; 3.21.7 | [GHSA-4gg5-vx3j-xwc7](https://github.com/advisories/GHSA-4gg5-vx3j-xwc7) |
| CVE-2022-3509 / GHSA-g5ww-5jh7-63cx | High (CVSS 7.5 AV:N/AC:L/PR:N/UI:N/A:H) | Uncontrolled resource consumption in text-format parsing; malformed or deeply nested text-format protobuf messages cause excessive memory allocation and GC pressure, enabling remote DoS. | 3.16.3; 3.19.6; 3.20.3; 3.21.7 | [GHSA-g5ww-5jh7-63cx](https://github.com/advisories/GHSA-g5ww-5jh7-63cx) |
| CVE-2021-22569 / GHSA-wrvw-hg22-4m67 | High (CVSS 7.5 AV:N/AC:L/PR:N/UI:N/A:H) | Denial of service via excessive GC pressure when parsing unknown fields in binary protobuf format; malformed input with a large number of unknown fields triggers quadratic allocation. | 3.16.1; 3.18.2; 3.19.2 | [GHSA-wrvw-hg22-4m67](https://github.com/advisories/GHSA-wrvw-hg22-4m67) |
| CVE-2022-3171 / GHSA-h4h5-3hr4-j3g2 | Moderate (CVSS 5.7 AV:A/AC:L/PR:L/UI:N/A:H) | Denial of service via binary or text-format repeated embedded messages; authenticated adjacent-network users can cause excessive memory allocation and GC pressure. | 3.16.3; 3.19.6; 3.20.3; 3.21.7 | [GHSA-h4h5-3hr4-j3g2](https://github.com/advisories/GHSA-h4h5-3hr4-j3g2) |
| CVE-2021-22570 / GHSA-77rm-9x9h-xj3g | — | **WITHDRAWN (2025-08-25).** Originally reported as a NULL pointer dereference in the protobuf compiler; re-attributed to a compiler build artifact, not a runtime library vulnerability. Advisory retained for reference continuity. | — | [GHSA-77rm-9x9h-xj3g](https://github.com/advisories/GHSA-77rm-9x9h-xj3g) (withdrawn) |

*OSV link: https://osv.dev/list?ecosystem=Maven&q=com.google.protobuf%3Aprotobuf-java*

## Security Posture Notes

`com.google.protobuf:protobuf-java` is Google's Java runtime library for Protocol Buffers. It is maintained by Google's Protocol Buffers team and receives regular releases alongside other language runtimes (Python, Go, C++). Security disclosures are coordinated through Google's vulnerability management process at security@google.com with a published SECURITY.md.

**Recurring vulnerability class — parser DoS via resource exhaustion:** All five non-withdrawn advisories (CVE-2021-22569, CVE-2022-3171, CVE-2022-3509, CVE-2022-3510, CVE-2024-7254) are parsing-side Denial of Service vulnerabilities: malformed or adversarially crafted protobuf messages cause stack overflows or excessive GC pressure. This pattern reflects a design tension in protobuf parsers: parsing depth and message size limits were historically not enforced by default.

**High transitive exposure:** protobuf-java is a direct dependency of gRPC-Java (`io.grpc:grpc-protobuf`), Google Cloud Java SDKs, the Kubernetes Java client, and most services that consume Google APIs. Any Maven/Gradle project depending on `io.grpc:grpc-core` or `com.google.api:gax-grpc` transitively depends on this library. The 3.x→4.x version split (renaming published artifacts) can cause version conflicts in dependency trees.

**Current stable versions:** 3.25.x (LTS-equivalent for 3.x users) and 4.x (latest). Projects on 3.x below 3.25.5 or on 4.x below 4.27.5 / 4.28.2 should upgrade.

**Note on GHSA-fjh6-p566-wr6q:** This advisory was returned by search but is for `io.github.skylot:jadx-core` (which bundles a vulnerable protobuf-java 3.11.4 as a dependency). It is not a direct protobuf-java advisory and is excluded from the vulnerability table above.

## Dependencies of Note

- `com.google.protobuf:protobuf-java` itself has minimal runtime dependencies (only `com.google.guava:guava` in older 3.x versions).
- The companion artifact `com.google.protobuf:protobuf-java-util` depends on Gson.
- gRPC-Java (`io.grpc:grpc-protobuf`) is the primary downstream consumer.

## Open Questions

- Is there a formal recursion-depth limit in the 4.x upb-based Java runtime, and is it configurable and documented for security-sensitive deployments?
- Do 3.x branch releases below 3.25.x still receive security patches, or have they reached end of life?
- Are the CVE-2022-3171/3509/3510 DoS variants independent code paths or manifestations of a single underlying parsing deficiency?

## Related Pages

- [[maven/io.netty/netty-codec-http]]
- [[maven/org.apache.kafka/kafka-clients]]
- [[go/google.golang.org/protobuf]]
- [[maven/index]]

---
*Last updated: 2026-08-22 | Sources: 6 GHSA (5 confirmed direct + 1 withdrawn)*
