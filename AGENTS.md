# AGENTS.md — MiNYAMA Repository Guide & State Snapshot

## Project Overview

**MiNYAMA** (System for Socio-Economic Modeling and Analysis) is an Obsidian-based knowledge repository implementing a **"Source-Sync Structural Hardening" (SSSH)** framework built on **Active Inference**. Theoretical sector schemas are progressively "hardened" into verified analytical insights by minimizing prediction error ("surprise") between beliefs and observations.

- **Primary tool**: Obsidian (`.obsidian/` vault config at root)
- **Status**: Initial Development (Skeletal) — schemas defined, engine mostly stubs
- **Methodology docs**: `governance/operational_guides/SYSTEM_DOCS.md`

## Repository Structure (The 6 Phases)

The repo is organized as a sequential "thinking process" (see root `README.md`):

| Phase | Directory | Role |
| :--- | :--- | :--- |
| 1 🟢 Blueprint | `schemas/` | Immutable source ontologies for 6 sectors: agriculture, education, finance, healthcare, manufacturing, retail (`*_Sector_Schema.md` + `README.md` extensions each). `Schema_Dashboard.md` = Active Inference profiles. Also stub dirs: `governance/`, `intervention_models/`. |
| 2 🟡 Engine | `models/` | Python implementation. `baseline_models/`, `prediction_engines/`, `extraction_flows/`. **Note:** all `.py` files are 0-byte stubs except `prediction_engines/world_model.py` (placeholder `WorldModel` class; imports a non-existent `Minyama_Active_Inference_Model` package). |
| 3 🟠 Material | `evidence/` | Sensory input: `environmental_priors/` (baseline JSONs + `Minyama_Environmental_RISC/`), `observations/` (README only), `prediction_error_logs/` (one example JSON). Naming: `{sector}_{env|obs|surprise}_{...}.json`. |
| 4 🔴 Action | `interventions/` | Action layer. README only; links to `applied_projects/` (not yet created). |
| 5 🔵 Output | `reports/` | `analytical_outputs/` (9 sector reports + dashboard + 1 write-up), `model_updates/` (empty), `surprise_analysis/` (empty). Hardening levels 1–3 (Skeletal → Functional → Semantic). |
| 6 🔘 Integrity | `contracts/`, `governance/`, `audit_logs/`, `verification_frameworks/` | `contracts/`: YAML sync rules, validation specs, semantic interfaces, `drift_detection/` (hashes + dependency map). `governance/`: philosophy + operational guides. `audit_logs/`: append-only inference histories. `verification_frameworks/`: audit test categories A/B/C. |

### Vendored subproject: `mapcn/`
A full copy of the **mapcn** React map component library (Next.js 16, React 19, MapLibre GL v5, Tailwind v4, shadcn/ui registry; `node_modules` installed). Presumably the future dashboard UI. **Follow `mapcn/AGENTS.md` for anything inside that directory** — it is a self-contained project with its own conventions and commands (`npm run dev|build|lint|registry:build`).

## Conventions When Working Here

- **Schema-first rule**: No entity/attribute may appear in `models/` or `reports/` unless defined in `schemas/`. Check `contracts/drift_detection/dependency_map.json` for downstream impact before editing schemas.
- **Semantic contract**: every model script must reference its parent schema in its header.
- **Evidence**: ISO 8601 timestamps, `traceability_id`, schema-linked attribute names.
- **Audit logs are append-only**; entries need `timestamp`, `artifact_ref`, `event_type`, `delta_summary`, `integrity_hash`.
- Markdown-heavy vault; Obsidian internal links used throughout. Don't commit `.obsidian/workspace.json` churn casually (it changes constantly).

---

## 📌 Repository State Snapshot — 2026-08-22

> Baseline for future reviews. Compare new reviews against this state.

### Git
- **Branch**: `Data/Zambia-Manufacturing` (created 2026-08-27 from `Runtime` @ `bf5c2ae`; tracks `origin/Data/Zambia-Manufacturing` after push). Local `Runtime` branch remains at `bf5c2ae`.
- **Commits**: 7 total on `Runtime` ancestry — `bf5c2ae` "Add Obsidian oversight guides and update repository snapshot" (HEAD of `Runtime`), `19ae42b` "Generalize intervention docs and add repository state snapshot", `9f71254` "Restructured repository for Version 2", `f187ecd` "Add README.md", `93725b5` "Initial commit`"
- **PR**: [#1](https://github.com/Zero0ptions/MiNYAMA/pull/1) open, `Runtime` → `Version-2` (review of the de-branding pass + prior snapshot)

### Recent material changes (2026-08-27)
- Added schema-aligned Zambia manufacturing synthetic population:
  - `evidence/environmental_priors/manufacturing_zambia_population.{json,csv}`
  - `evidence/observations/manufacturing_zambia_observations.{json,csv}`
  - `evidence/prediction_error_logs/manufacturing_zambia_surprise_log.{json,csv}`
- Added manufacturing schema companions:
  - `schemas/manufacturing/Manufacturing_Sector_Schema_Population.csv`
  - `schemas/manufacturing/Manufacturing_Sector_Schema_Population_Template.md`
  - `schemas/manufacturing/Manufacturing_Population_Data_Requirements.md`
- Added governance / hardening artifacts:
  - `audit_logs/2026-08-27_zambia_manufacturing_population.md`
  - `reports/model_updates/manufacturing_zambia_model_update.md`
- Implemented `models/prediction_engines/surprise_calculator.py` (was a 0-byte stub); now computes prediction error between priors and observations for the Manufacturing sector.

### Uncommitted working-tree changes (in progress)
- `.obsidian/workspace.json` session churn
- Untracked: `mapcn/` (vendored app), `analytical_outputs.md` (0-byte accidental), `.obsidian/graph.json`, `.obsidian/community-plugins.json`, `.obsidian/plugins/`, `docs/external-data-ingestion-design.md`, `governance/organizational_context/`, `models/extraction_flows/document_archive.py`

### Known inconsistencies / drift to watch in reviews
1. `governance/README.md` references `governance/audit_logs/` and `governance/verification_frameworks/` — both actually live at **repo root**.
2. `operational_guides/` is **duplicated**: root copy and `governance/operational_guides/` — the two `SYSTEM_DOCS.md` files differ in content (2848 vs 2359 bytes).
3. `interventions/README.md` links to `applied_projects/` — directory does not exist yet.
4. `models/` is partially populated: `surprise_calculator.py` is now functional, but `world_model.py` still imports a non-existent `Minyama_Active_Inference_Model` package and is not runnable as-is.
5. `reports/surprise_analysis/` is empty; `reports/README.md` describes 3 hardening levels while `contracts/validation_specs/report_hardening_levels.md` defines 5.
6. Root `README.md` footer says "Last Updated: May 9, 2026" but the file was edited 2026-08-20.
7. `mapcn/node_modules` exists inside the vault — heavy; relies on `mapcn/.gitignore` to stay untracked.

---
*Snapshot recorded 2026-08-27. Update the snapshot section when the repo state materially changes.*
