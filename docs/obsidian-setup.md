# Obsidian Administrative Oversight Setup (MiNYAMA)

Configurations for plugin-based oversight of this vault. Install the **Dataview** and **Templater** community plugins first (Settings → Community plugins → Browse), then apply the sections below.

> Note: Obsidian cannot be driven from the CLI — plugin installation and folder settings below are one-time steps done inside the Obsidian app. Everything else is already prepared in this repo.

---

## 1. Compliance Dashboard

Create a note at `reports/compliance_dashboard.md` (or anywhere) and paste the following. Requires **Dataview**.

````markdown
# MiNYAMA Compliance Dashboard

## Audit entries missing required fields
```dataview
TABLE WITHOUT ID file.link AS "Entry", event_type AS "Type", artifact_ref AS "Artifact"
FROM "audit_logs"
WHERE !timestamp OR !artifact_ref OR !event_type OR !delta_summary OR !integrity_hash
SORT file.mtime DESC
```

## Open SEV-1 events (no #reviewed tag)
```dataview
LIST
FROM "audit_logs"
WHERE contains(file.tags, "#SEV-1") AND !contains(file.tags, "#reviewed")
SORT file.mtime DESC
```

## Unlinked files (drift candidates)
```dataview
TABLE WITHOUT ID file.link AS "File", file.mtime AS "Last Modified"
WHERE length(file.inlinks) = 0 AND length(file.outlinks) = 0
  AND !contains(file.path, ".obsidian")
SORT file.mtime DESC
```

## Audit inventory
```dataview
TABLE WITHOUT ID traceability_id AS "ID", event_type AS "Type", artifact_ref AS "Artifact", file.mtime AS "Modified"
FROM "audit_logs"
SORT traceability_id ASC
```

## Reports lacking evidence citations
```dataview
TABLE WITHOUT ID file.link AS "Report"
FROM "reports"
WHERE !evidence_id AND !contains(file.outlinks, "evidence/")
```
````

---

## 2. Audit Log Entry Template

Save as `_templates/audit_log_entry.md`, then in Settings → **Templater** set the template folder to `_templates` and enable *Trigger Templater on new file creation* only if desired (manual insert via command palette is safer).

````markdown
---
timestamp: <% new Date().toISOString().replace(/\.\d+Z$/, "Z") %>
artifact_ref: "<% tp.system.prompt('Path of audited artifact') %>"
event_type: <% tp.system.suggester(
  ["Hardening event", "Schema sync", "Intervention audit", "Drift resolution"],
  ["HARDENING_EVENT", "SCHEMA_SYNC", "INTERVENTION_AUDIT", "DRIFT_RESOLUTION"]
) %>
traceability_id: "<% tp.date.now('YYYYMMDD-HHmmss') %>"
delta_summary: ""
integrity_hash: ""
tags: []
---

# Audit Entry

## Delta Summary
<!-- concise description of the change -->

## Integrity Hash
<!-- SHA-256 of artifact at time of log creation -->
````

On insert, Templater prompts for the artifact path and lets you pick one of the four allowed `event_type` values from `audit_logs/README.md`.

---

## 3. Field Validation (Linter)

The **Linter** plugin has no native "frontmatter must contain key X" rule, so enforcement is handled by the Section 1 queries instead. If you still want save-time nudges, add a Linter **Custom Regex Replacement** per field (Settings → Linter → Custom Replacements), e.g.:

- *Name*: `audit-missing-integrity-hash`
- *Find*: `^---\n(?=(?:(?!integrity_hash:)[\s\S])*---)`
- *Replace*: leave empty (match-only flagging is not supported; prefer the dashboard)

Practical recommendation: rely on the **Compliance Dashboard** queries as the source of truth, and treat Linter purely for formatting (trailing whitespace, YAML timestamp consistency).

---

## 4. Suggested core-plugin settings

| Setting | Value | Why |
| :--- | :--- | :--- |
| Core: Backlinks | On | Drift detection |
| Core: Outgoing links | On | Evidence-citation audits |
| Core: Templates | Folder `_templates/` | Fallback for non-Templater inserts |
| Files & links: Detect all file extensions | On | So `.json` evidence files resolve in links |
| Appearance: Strict line breaks | Off | Keeps contract tables readable |
