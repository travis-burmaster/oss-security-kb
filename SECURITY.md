# Security Policy

## Reporting security issues in this repository

This repository is a **knowledge base**, not a package/runtime distributed to end users. Most security findings documented here will apply to upstream open source projects, not to `oss-security-kb` itself.

If you believe you found a security issue in the KB itself, please do **not** open a public issue first.

Instead, report it privately to Travis Burmaster.

## What counts as a security issue here

Examples:
- exposed credentials or secrets committed to the repo
- CI/CD misconfiguration that could expose contributors or infrastructure
- XSS / injection risk in the future website or generated site output
- unsafe automation that could damage data or publish misleading content
- supply-chain issues in site/build dependencies

## What does NOT belong here

Do not use this policy to report vulnerabilities in third-party packages tracked by the knowledge base. Those should be reported to the relevant upstream maintainers according to their disclosure process.

## Disclosure expectations

Please include:
- affected file(s) or path(s)
- reproduction steps if applicable
- impact assessment
- suggested remediation if known

We will acknowledge receipt, evaluate severity, and coordinate a fix before public disclosure when appropriate.
