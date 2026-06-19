# Claude Code — Project Instructions

This file is read automatically at the start of every Claude Code session in this repository. It captures validated environment behaviour so each run doesn't have to rediscover it.

## Environment constraints (validated 2026-06-18)

### Git / push
`git push` via the local git proxy (`127.0.0.1:44641`) returns **HTTP 403** and cannot push to remote. Do **not** use `git push`, `git push -u origin`, or `gh` for any remote operation.

Use the MCP GitHub tools for all remote writes:
- **Create branch:** `mcp__github__create_branch`
- **Push files:** `mcp__github__push_files` (single call with all files; commits atomically)
- **Open PR:** `mcp__github__create_pull_request`
- **Merge PR:** `mcp__github__merge_pull_request` with `merge_method: squash`
- **Delete branch:** branch is removed automatically by the squash merge when `delete_branch` is set, or leave it; it is cheap

Local `git` commands (status, diff, log, add, commit) still work fine for staging and reading state, but nothing reaches the remote.

### `gh` CLI
`gh` is **not installed** in this environment. All GitHub operations must go through `mcp__github__*` tools.

### OSV.dev API
`https://api.osv.dev` returns **HTTP 403** (blocked by network policy). Use these fallbacks:
- **RustSec advisories:** fetch `https://raw.githubusercontent.com/rustsec/advisory-db/main/crates/<crate>/<ID>.md` directly via WebFetch, or use `mcp__github__search_code` with `repo:rustsec/advisory-db`.
- **GHSA records:** fetch `https://raw.githubusercontent.com/github/advisory-database/main/advisories/.../<GHSA-id>/<GHSA-id>.json` via WebFetch, or use `mcp__github__search_code` with `repo:github/advisory-database`.
- `mcp__github__get_file_contents` is restricted to `travis-burmaster/oss-security-kb` only; it cannot read advisory databases. Use `mcp__github__search_code` (which is cross-repo) + WebFetch instead.

### Notification
After a successful nightly pass, send a push notification via PushNotification so the owner sees results on mobile / email. Always send one — either on success (pages added, PR merged) or on failure (what blocked the run).

## Advisory-review pass — working procedure

1. **Read state:** `wiki/index.md`, `wiki/log.md` (newest-first), and the relevant ecosystem index files to establish what is already covered.
2. **Select targets:** 1–3 packages from under-covered ecosystems; prefer those with no existing KB page and high download counts or CNCF/critical-infrastructure importance.
3. **Research advisories:** Use `mcp__github__search_code` + WebFetch (raw.githubusercontent.com) for rustsec/advisory-db and github/advisory-database. Use crates.io API, pkg.go.dev, and registry metadata via WebFetch.
4. **Write pages** under `wiki/<ecosystem>/` following `SCHEMA.md`. Every vulnerability row must cite a primary source (GHSA, RUSTSEC, OSV, or upstream advisory). No invented findings.
5. **Update indexes:** ecosystem index file, `wiki/index.md` (page count), `wiki/log.md` (prepend entry, newest-first).
6. **Save evidence:** `raw/advisory-review-<YYYYMMDD-HHMM>/notes.md` with all URLs consulted.
7. **Ship:**
   a. `mcp__github__create_branch` — branch name `nightly/oss-kb-4h-<UTC YYYYMMDD-HHMM>` from current main SHA (get it via `mcp__github__list_commits`).
   b. `mcp__github__push_files` — all changed/new files in one call with a descriptive commit message.
   c. `mcp__github__create_pull_request` — base `main`, include self-review checklist in body.
   d. `mcp__github__merge_pull_request` — `merge_method: squash`.
8. **Notify** via PushNotification with PR number, pages added, and advisory counts.

## Ground rules

- **Advisory mapping only.** Every vulnerability row must be backed by a named public source. Do not infer or fabricate findings.
- **Own wiki only.** Only write to `wiki/` and `raw/` in this repository. Do not attempt to push to `rustsec/advisory-db`, `github/advisory-database`, or any other repo.
- **SCHEMA.md and METHODOLOGY.md compliance.** Page structure must match the schema.
- **No OSV.dev dependency.** Treat OSV as a nice-to-have; the pass must complete without it.
