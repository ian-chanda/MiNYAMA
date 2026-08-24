---
timestamp: 2026-08-24T03:06:59Z
artifact_ref: docs/mcp-obsidian-setup.md
event_type: DRIFT_RESOLUTION
traceability_id: AUD-20260824-HOSTPATH-01
integrity_hash: e5a3ad2148505c433bbcee28f9276fc8c49678c15cbb0d79811798e0dc7429d1
tags:
  - "#SEV-2"
  - security-hygiene
---

# Audit: Host-Device Path Leakage & History Sanitization

## Delta Summary

During review of PR #3, two host-device internal paths were discovered in the newly added `docs/mcp-obsidian-setup.md`:

1. An absolute Windows user-config path (`C:\Users\…\.config\opencode\opencode.jsonc`)
2. A non-standard tooling install path (`C:\Users\…\AppData\Local\hermes\bin\uvx.exe`)

Both disclosed the OS platform, username, and local directory structure to the public repository.

## Resolution Timeline (UTC)

| Time | Event |
| :--- | :--- |
| 2026-08-23 | Leaked paths introduced in commit `0a33db9` (PR #3 first push) |
| 2026-08-23 | Partial fix pushed as `6f30750` — tips sanitized, taint remained in history |
| 2026-08-24 | Full-history scan across all refs: taint confined to `0a33db9` |
| 2026-08-24 | Branch rewritten to `bf5c2ae` (single sanitized commit); force-pushed with lease |
| 2026-08-24 | Discovered GitHub had merged PR #3 using the **pre-redaction** head; merge commit `768ba27` re-introduced leaked content into `origin/Runtime` tip and ancestry |
| 2026-08-24 | `origin/Runtime` rebuilt from sanitized branch and force-pushed; diff vs tainted merge verified byte-identical except the two redactions |
| 2026-08-24 | Final verification sweep: zero host-path matches across all commits on all refs |

## Verification

- Pattern scan (`AppData`, `hermes`, `[A-Z]:\Users`) executed per-commit against every ref post-rewrite: **clean**
- Sanitized file state recorded in `integrity_hash` above

## Residual Risk / Follow-ups

- [ ] Unreachable objects persist server-side (GitHub) until provider GC; PR #3's page retains old commits as an immutable audit artifact
- [ ] Any clone pulled between merge and rewrite may hold the tainted objects locally
- [ ] Consider a pre-commit secret/path scanner to catch host-specific absolute paths before push (Category C evidence-integrity check candidate)

## Classification Note

Logged as SEV-2 per `audit_logs/README.md` severity examples (synchronization correction class): no credentials were exposed, but structural hygiene of the public-facing repository was compromised and required destructive history repair.
