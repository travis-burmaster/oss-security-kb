## GHSA-3pxv-7cmr-fjr4 CVE-2026-34480
Summary: Apache Log4j Core: Silent log event loss in XmlLayout due to unescaped XML 1.0 forbidden characters
Severity: CVSS_V4 CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:N/SC:N/SI:L/SA:N
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j-core
Fixed: 2.25.4
Details: Apache Log4j Core's [`XmlLayout`](https://logging.apache.org/log4j/2.x/manual/layouts.html#XmlLayout), in versions up to and including 2.25.3, fails to sanitize characters forbidden by the [XML 1.0 specification](https://www.w3.org/TR/xml/#charsets), producing invalid XML output whenever a log message or MDC value contains such characters.  The impact depends on the StAX implementation in use:    *  **JRE built-in StAX**: Forbidden characters are silently written to the output, producing malformed XML. Conforming parsers must reject such documents with a fatal error, which may cause downstream log-processing systems to drop the affected records.   *  **Alternative StAX implementations** (e.g., [Woodstox](https://github.com/FasterXML/woodstox), a transitive dependency of the Jackson XML Dat
Refs: https://nvd.nist.gov/vuln/detail/CVE-2026-34480, https://github.com/apache/logging-log4j2/pull/4077, https://github.com/apache/logging-log4j2, https://lists.apache.org/thread/5x0hcnng0chhghp6jgjdp3qmbbhfjzhb, https://logging.apache.org/cyclonedx/vdr.xml, https://logging.apache.org/log4j/2.x/manual/layouts.html#XmlLayout

## GHSA-445c-vh5m-36rj CVE-2026-34478
Summary: Apache Log4j Core: log injection in `Rfc5424Layout` due to silent configuration incompatibility
Severity: CVSS_V4 CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:N/SC:N/SI:L/SA:N
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j-core
Fixed: 2.25.4
Details: Apache Log4j Core's [`Rfc5424Layout`](https://logging.apache.org/log4j/2.x/manual/layouts.html#RFC5424Layout), in versions 2.21.0 through 2.25.3, is vulnerable to log injection via CRLF sequences due to undocumented renames of security-relevant configuration attributes.  Two distinct issues affect users of stream-based syslog services who configure Rfc5424Layout directly:    *  The `newLineEscape` attribute was silently renamed, causing newline escaping to stop working for users of TCP framing (RFC 6587), exposing them to CRLF injection in log output.   *  The `useTlsMessageFormat` attribute was silently renamed, causing users of TLS framing (RFC 5425) to be silently downgraded to unframed TCP (RFC 6587), without newline escaping.  Users of the `SyslogAppender` are not affected, as its con
Refs: https://nvd.nist.gov/vuln/detail/CVE-2026-34478, https://github.com/apache/logging-log4j2/pull/4074, https://github.com/apache/logging-log4j2, https://lists.apache.org/thread/3k1clr2l6vkdnl4cbhjrnt1nyjvb5gwt, https://logging.apache.org/cyclonedx/vdr.xml, https://logging.apache.org/log4j/2.x/manual/layouts.html#RFC5424Layout

## GHSA-6hg6-v5c8-fphq CVE-2026-34477
Summary: Apache Log4j Core: `verifyHostName` attribute silently ignored in TLS configuration
Severity: CVSS_V4 CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:L/VI:N/VA:N/SC:N/SI:L/SA:N
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j-core
Fixed: 2.25.4
Details: The fix for  CVE-2025-68161 was incomplete: it addressed hostname verification only when enabled via the  [`log4j2.sslVerifyHostName`](https://logging.apache.org/log4j/2.x/manual/systemproperties.html#log4j2.sslVerifyHostName) system property, but not when configured through the [`verifyHostName`](https://logging.apache.org/log4j/2.x/manual/appenders/network.html#SslConfiguration-attr-verifyHostName) attribute of the `<Ssl>` element.  Although the `verifyHostName` configuration attribute was introduced in Log4j Core 2.12.0, it was silently ignored in all versions through 2.25.3, leaving TLS connections vulnerable to interception regardless of the configured value.  A network-based attacker may be able to perform a man-in-the-middle attack when all of the following conditions are met:    * 
Refs: https://nvd.nist.gov/vuln/detail/CVE-2026-34477, https://github.com/apache/logging-log4j2/pull/4075, https://github.com/apache/logging-log4j2, https://lists.apache.org/thread/lkx8cl46t2bvkcwfcb2pd43ygc097lq4, https://logging.apache.org/cyclonedx/vdr.xml, https://logging.apache.org/log4j/2.x/manual/appenders/network.html#SslConfiguration-attr-verifyHostName

## GHSA-7rjr-3q55-vv33 CVE-2021-45046
Summary: Incomplete fix for Apache Log4j vulnerability
Severity: CVSS_V3 CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H/E:H
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Fixed: 1.10.8, 1.11.11, 1.9.2, 2.0.12, 2.12.2, 2.16.0
Details: # Impact  The fix to address [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) in Apache Log4j 2.15.0 was incomplete in certain non-default configurations. This could allow attackers with control over Thread Context Map (MDC) input data when the logging configuration uses a non-default Pattern Layout with either a Context Lookup (for example, $${ctx:loginId}) or a Thread Context Map pattern (%X, %mdc, or %MDC) to craft malicious input data using a JNDI Lookup pattern resulting in a remote code execution (RCE) attack.   ## Affected packages Only the `org.apache.logging.log4j:log4j-core` package is directly affected by this vulnerability. The `org.apache.logging.log4j:log4j-api` should be kept at the same version as the `org.apache.logging.log4j:log4j-core` package to ensure 
Refs: https://nvd.nist.gov/vuln/detail/CVE-2021-45046, https://www.oracle.com/security-alerts/cpujul2022.html, https://www.oracle.com/security-alerts/cpujan2022.html, https://www.oracle.com/security-alerts/cpuapr2022.html, https://www.oracle.com/security-alerts/alert-cve-2021-44228.html, https://www.openwall.com/lists/oss-security/2021/12/14/4

## GHSA-8489-44mv-ggj8 CVE-2021-44832
Summary: Improper Input Validation and Injection in Apache Log4j2
Severity: CVSS_V3 CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Fixed: 1.10.9, 1.11.13, 1.9.2, 2.0.14, 2.12.4, 2.17.1, 2.3.2
Details: Apache Log4j2 versions 2.0-beta7 through 2.17.0 (excluding security fix releases 2.3.2 and 2.12.4) are vulnerable to an attack where an attacker with permission to modify the logging configuration file can construct a malicious configuration using a JDBC Appender with a data source referencing a JNDI URI which can execute remote code. This issue is fixed by limiting JNDI data source names to the java protocol in Log4j2 versions 2.17.1, 2.12.4, and 2.3.2.   # Affected packages Only the `org.apache.logging.log4j:log4j-core` package is directly affected by this vulnerability. The `org.apache.logging.log4j:log4j-api` should be kept at the same version as the `org.apache.logging.log4j:log4j-core` package to ensure compatability if in use.  This issue does not impact default configurations of Lo
Refs: https://nvd.nist.gov/vuln/detail/CVE-2021-44832, https://cert-portal.siemens.com/productcert/pdf/ssa-784507.pdf, https://github.com/apache/logging-log4j2, https://issues.apache.org/jira/browse/LOG4J2-3293, https://lists.apache.org/thread/s1o5vlo78ypqxnzn6p8zf6t9shtq5143, https://lists.debian.org/debian-lts-announce/2021/12/msg00036.html

## GHSA-fxph-q3j8-mv87 CVE-2017-5645
Summary: Deserialization of Untrusted Data in Log4j
Severity: CVSS_V3 CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
Package: Maven org.apache.logging.log4j:log4j
Package: Maven org.apache.logging.log4j:log4j-core
Fixed: 2.8.2
Details: In Apache Log4j 2.x before 2.8.2, when using the TCP socket server or UDP socket server to receive serialized log events from another application, a specially crafted binary payload can be sent that, when deserialized, can execute arbitrary code.
Refs: https://nvd.nist.gov/vuln/detail/CVE-2017-5645, https://www.oracle.com/technetwork/security-advisory/cpuoct2019-5072832.html, https://lists.apache.org/thread.html/rd5dbeee4808c0f2b9b51479b50de3cc6adb1072c332a200d9107f13e@%3Cissues.activemq.apache.org%3E, https://lists.apache.org/thread.html/rcbb79023a7c8494cb389cd3d95420fa9e0d531ece0b780b8c1f99422@%3Ccommits.doris.apache.org%3E, https://lists.apache.org/thread.html/rca24a281000fb681d7e26e5c031a21eb4b0593a7735f781b53dae4e2@%3Cdev.tika.apache.org%3E, https://lists.apache.org/thread.html/rc1eaed7f7d774d5d02f66e49baced31e04827a1293d61a70bd003ca7@%3Cdev.tika.apache.org%3E

## GHSA-jfh8-c2jp-5v3q CVE-2021-44228
Summary: Remote code injection in Log4j
Severity: CVSS_V3 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/E:H
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven com.guicedee.services:log4j-core
Package: Maven org.xbib.elasticsearch:log4j
Package: Maven uk.co.nichesolutions.logging.log4j:log4j-core
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Fixed: 1.10.8, 1.11.10, 1.9.2, 2.0.11, 2.12.2, 2.15.0, 2.3.1
Details: # Summary  Log4j versions prior to 2.16.0 are subject to a remote code execution vulnerability via the ldap JNDI parser. As per [Apache's Log4j security guide](https://logging.apache.org/log4j/2.x/security.html): Apache Log4j2 <=2.14.1 JNDI features used in configuration, log messages, and parameters do not protect against attacker controlled LDAP and other JNDI related endpoints. An attacker who can control log messages or log message parameters can execute arbitrary code loaded from LDAP servers when message lookup substitution is enabled. From log4j 2.16.0, this behavior has been disabled by default.  Log4j version 2.15.0 contained an earlier fix for the vulnerability, but that patch did not disable attacker-controlled JNDI lookups in all situations. For more information, see the `Updat
Refs: https://nvd.nist.gov/vuln/detail/CVE-2021-44228, https://github.com/apache/logging-log4j2/pull/608, https://github.com/github/advisory-database/pull/5501, https://cert-portal.siemens.com/productcert/pdf/ssa-397453.pdf, https://packetstormsecurity.com/files/165673/UniFi-Network-Application-Unauthenticated-Log4Shell-Remote-Code-Execution.html, https://packetstormsecurity.com/files/167794/Open-Xchange-App-Suite-7.10.x-Cross-Site-Scripting-Command-Injection.html

## GHSA-p6xc-xr62-6r2g CVE-2021-45105
Summary: Apache Log4j2 vulnerable to Improper Input Validation and Uncontrolled Recursion
Severity: CVSS_V3 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:N/A:H
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Package: Maven org.ops4j.pax.logging:pax-logging-log4j2
Fixed: 1.10.9, 1.11.12, 1.9.2, 2.0.13, 2.12.3, 2.17.0, 2.3.1
Details: Apache Log4j2 versions 2.0-alpha1 through 2.16.0 (excluding 2.12.3) did not protect from uncontrolled recursion from self-referential lookups. This allows an attacker with control over Thread Context Map data to cause a denial of service when a crafted string is interpreted. This issue was fixed in Log4j 2.17.0 and 2.12.3.   # Affected packages Only the `org.apache.logging.log4j:log4j-core` package is directly affected by this vulnerability. The `org.apache.logging.log4j:log4j-api` should be kept at the same version as the `org.apache.logging.log4j:log4j-core` package to ensure compatability if in use.
Refs: https://nvd.nist.gov/vuln/detail/CVE-2021-45105, https://cert-portal.siemens.com/productcert/pdf/ssa-479842.pdf, https://cert-portal.siemens.com/productcert/pdf/ssa-501673.pdf, https://lists.debian.org/debian-lts-announce/2021/12/msg00017.html, https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/EOKPQGV24RRBBI4TBZUDQMM4MEH7MXCY, https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/SIG7FZULMNK2XF6FZRU4VWYDQXNMUGAJ

## GHSA-vc5p-v9hr-52mj CVE-2025-68161
Summary: Apache Log4j does not verify the TLS hostname in its Socket Appender
Severity: CVSS_V4 CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:L/VI:N/VA:N/SC:N/SI:L/SA:N
Package: Maven org.apache.logging.log4j:log4j-core
Fixed: 2.25.3
Details: The Socket Appender in Apache Log4j Core versions 2.0-beta9 through 2.25.2 does not perform TLS hostname verification of the peer certificate, even when the  [verifyHostName](https://logging.apache.org/log4j/2.x/manual/appenders/network.html#SslConfiguration-attr-verifyHostName)  configuration attribute or the  [log4j2.sslVerifyHostName](https://logging.apache.org/log4j/2.x/manual/systemproperties.html#log4j2.sslVerifyHostName) system property is set to true.  This issue may allow a man-in-the-middle attacker to intercept or redirect log traffic under the following conditions:    *  The attacker is able to intercept or redirect network traffic between the client and the log receiver.   *  The attacker can present a server certificate issued by a certification authority trusted by the Socke
Refs: https://nvd.nist.gov/vuln/detail/CVE-2025-68161, https://github.com/apache/logging-log4j2/pull/4002, https://github.com/apache/logging-log4j2/commit/3b93748497e1adbbd027fda8a5e7268ec5d0d578, https://github.com/apache/logging-log4j2, https://lists.apache.org/thread/xr33kyxq3sl67lwb61ggvm1fzc8k7dvx, https://logging.apache.org/cyclonedx/vdr.xml

## GHSA-vp98-w2p3-mv35 CVE-2023-26464
Summary: Apache Log4j 1.x (EOL) allows Denial of Service (DoS)
Severity: CVSS_V3 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven log4j:log4j
Fixed: 2.0
Details: ** UNSUPPORTED WHEN ASSIGNED ** When using the Chainsaw or SocketAppender components with Log4j 1.x on JRE less than 1.7, an attacker that manages to cause a logging entry involving a specially-crafted (ie deeply nested) hashmap or hashtable (depending on which logging component is in use) to be processed could exhaust the available memory in the virtual machine and achieve Denial of Service when the object is deserialized. This issue affects Apache Log4j before 2. Affected users are recommended to update to Log4j 2.x. NOTE: This vulnerability only affects products that are no longer supported by the maintainer.
Refs: https://nvd.nist.gov/vuln/detail/CVE-2023-26464, https://github.com/apache/logging-log4j2, https://lists.apache.org/thread/wkx6grrcjkh86crr49p4blc1v1nflj3t, https://security.netapp.com/advisory/ntap-20230505-0008

## GHSA-vwqq-5vrc-xw9h CVE-2020-9488
Summary: Improper validation of certificate with host mismatch in Apache Log4j SMTP appender
Severity: CVSS_V3 CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N
Package: Maven org.apache.logging.log4j:log4j
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j
Package: Maven org.apache.logging.log4j:log4j
Package: Maven org.apache.logging.log4j:log4j-core
Package: Maven org.apache.logging.log4j:log4j-core
Fixed: 2.12.3, 2.13.2, 2.3.2
Details: Improper validation of certificate with host mismatch in Apache Log4j SMTP appender prior to version 2.13.2. This could allow an SMTPS connection to be intercepted by a man-in-the-middle attack which could leak any log messages sent through that appender.
Refs: https://nvd.nist.gov/vuln/detail/CVE-2020-9488, https://lists.apache.org/thread.html/r9a79175c393d14d760a0ae3731b4a873230a16ef321aa9ca48a810cd@%3Cissues.zookeeper.apache.org%3E, https://lists.apache.org/thread.html/ra051e07a0eea4943fa104247e69596f094951f51512d42c924e86c75@%3Cissues.hive.apache.org%3E, https://lists.apache.org/thread.html/ra632b329b2ae2324fabbad5da204c4ec2e171ff60348ec4ba698fd40@%3Cissues.hive.apache.org%3E, https://lists.apache.org/thread.html/rbc45eb0f53fd6242af3e666c2189464f848a851d408289840cecc6e3@%3Ccommits.zookeeper.apache.org%3E, https://lists.apache.org/thread.html/rbc7642b9800249553f13457e46b813bea1aec99d2bc9106510e00ff3@%3Ctorque-dev.db.apache.org%3E
