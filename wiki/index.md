# OSS Security KB — Master Index

*2 packages with audit records. 48 stubs. Last updated: 2026-04-07.*

> **Legend:** ✅ Audited | ⚠️ Partially audited | 🔴 Known CVEs, no audit on record | 📄 Stub (not yet reviewed)

---

## npm (50 tracked)

Weekly download figures from npmjs.org as of 2026-04-07.

| Package | Weekly Downloads | Audit Status | CVEs | Notes |
|---------|-----------------|--------------|------|-------|
| [semver](npm/semver.md) | 594,317,483 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=semver) | Version parsing — ReDoS history |
| [chalk](npm/chalk.md) | 378,919,755 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=chalk) | Terminal styling |
| [commander](npm/commander.md) | 319,320,935 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=commander) | CLI argument parsing |
| [uuid](npm/uuid.md) | 217,832,505 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=uuid) | UUID generation |
| [yargs](npm/yargs.md) | 159,009,087 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=yargs) | CLI argument parsing |
| [typescript](npm/typescript.md) | 153,626,258 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=typescript) | TypeScript compiler |
| [lodash](npm/lodash.md) | 124,507,873 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=lodash) | Utility library — prototype pollution history |
| [minimist](npm/minimist.md) | 110,422,995 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=minimist) | Arg parsing — prototype pollution CVEs |
| [eslint](npm/eslint.md) | 110,308,282 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=eslint) | Linter |
| [react](npm/react.md) | 108,913,626 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=react) | UI framework |
| [dotenv](npm/dotenv.md) | 106,588,903 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=dotenv) | Env file loader |
| [axios](npm/axios.md) | 91,498,761 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=axios) | HTTP client — SSRF/redirect history |
| [express](npm/express.md) | 84,035,445 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=express) | Web framework |
| [prettier](npm/prettier.md) | 74,932,008 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=prettier) | Code formatter |
| [cors](npm/cors.md) | 44,000,776 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=cors) | CORS middleware |
| [inquirer](npm/inquirer.md) | 41,719,038 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=inquirer) | Interactive CLI prompts |
| [jest](npm/jest.md) | 40,703,887 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=jest) | Testing framework |
| [webpack](npm/webpack.md) | 40,417,443 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=webpack) | Bundler |
| [moment](npm/moment.md) | 28,285,498 | 📄 Stub | [OSV](https://osv.dev/list?ecosystem=npm&q=moment) | Date library — ReDoS history |
| [path-to-regexp](npm/path-to-regexp.md) | ~80,000,000 | ✅ Audited | [OSV](https://osv.dev/list?ecosystem=npm&q=path-to-regexp) | 2 bugs found (2026-03-31) |
| [jsonwebtoken](npm/jsonwebtoken.md) | ~14,000,000 | ✅ Audited | [OSV](https://osv.dev/list?ecosystem=npm&q=jsonwebtoken) | 4 CVEs + 1 new finding (2026-03-31) |

---

## Rust / crates.io (0 tracked — stubs coming)

*Priority targets: tokio, serde, serde_json, reqwest, rand, regex, log, clap, chrono, syn*

---

## .NET / NuGet (0 tracked — stubs coming)

*Priority targets: Newtonsoft.Json, Microsoft.AspNetCore.*, System.Text.Json, AutoMapper, Dapper*

---

## Python / PyPI (0 tracked — stubs coming)

*Priority targets: requests, boto3, numpy, pandas, django, flask, cryptography, paramiko, pyyaml, pillow*

---

## Go (0 tracked — stubs coming)

*Priority targets: gin, echo, gorm, go-jwt, grpc-go, cobra, viper*

---

## Homebrew (0 tracked — stubs coming)

*Priority targets: openssl, curl, git, wget, python, node, ffmpeg, imagemagick*

---

## Kubernetes (0 tracked — stubs coming)

*Priority targets: kube-apiserver, kubelet, etcd, containerd, kube-proxy, coredns, ingress-nginx*

---

## Linux / System (0 tracked — stubs coming)

*Priority targets: glibc, openssh, bash, sudo, openssl, curl, systemd, dbus*

---

## How to Add an Entry

1. Create `wiki/{ecosystem}/{package-name}.md` using the template in [SCHEMA.md](../SCHEMA.md)
2. Add a row to the appropriate section above
3. Append to [log.md](log.md)
4. Open a PR
