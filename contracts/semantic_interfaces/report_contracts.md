# Report Contracts Semantic Interface

This document defines the mandatory structural and semantic rules for all analytical reports in the MiNYAMA framework. Every report in `reports/` must be "Contract-Compliant" to ensure it can be parsed by the Integrity Layer.

---

## 1. Mandatory Header (Metadata Block)
Every report MUST begin with a YAML front-matter block. This is used for automated **Synchronization Audits**.

```yaml
---
domain: [Agriculture | Education | Finance | Healthcare | Manufacturing | Retail]
contract: contracts/schema_sync_rules/{sector}_sync.yaml
blueprint: schemas/{sector}/{sector}_sector_schema.md
version: 1.0.0
hardening_level: [1 | 2 | 3 | 4 | 5]
status: [draft | verified | hardened]
last_audit: 2026-05-09
---
```

## 2. Mandatory Section Architecture
Reports must follow this specific order to reflect the **Proof of Transformation** arc.

### I. Executive Summary
A high-level overview of the learning event (the "Surprise" and the resulting "Model Update").

### II. Baseline Expectations (The Belief)
*   **Semantic Rule**: Must reference specific `priors` from `evidence/environmental_priors/`.
*   **Requirement**: Define what the model *expected* to see before the observation.

### III. Observations (The Reality)
*   **Semantic Rule**: Must use the `👉 [SENSORY_DATA]` tag to cite evidence records.
*   **Requirement**: Present the raw, quantitative data collected from the field.

### IV. Surprise Identification (The Delta)
*   **Semantic Rule**: Must use the `👉 [SURPRISE_DELTA]` tag.
*   **Requirement**: Quantify the prediction error. Is the system "surprised" by the outcome?

### V. Model Update (The Insight)
*   **Semantic Rule**: Must use the `🛠 [SYNC_UPDATE]` tag.
*   **Requirement**: Propose a specific change to the Schema attributes or Model weights.

---

## 3. Compliance Examples

### ✅ Compliant Surpise Identification
> Based on the soil sensors cited in Section III, the actual moisture level was 0.22, while the model predicted 0.45.
> 👉 **[SURPRISE_DELTA]**: -0.23 (Negative Moisture Surprise).

### ✅ Compliant Model Update
> The consistently lower moisture levels suggest the drainage coefficient for Zone_A is set too low.
> 🛠 **[SYNC_UPDATE]**: `schemas/agriculture/Zone.drainage_coefficient` from 0.05 to 0.12.

---

## 4. Hardening Compliance Rules
1.  **Level 1 Reports** may use the `[CONTRACT_GAP]` tag for missing data.
2.  **Level 5 Reports** must remove all `[CONTRACT_GAP]` tags and metadata comments.
3.  Any report failing the **Mandatory Header** check will be flagged as "Stale" in the Drift Detection audit.
