# Validation Spec: Report Hardening Levels

The MiNYAMA framework employs a **Progressive Hardening** lifecycle for all analytical reports. This ensures that insights are not merely opinions but are structurally sound, evidence-backed, and verified transformations of the world model.

---

## 🔴 Level 1: Skeletal (Structural Integrity)
**Purpose**: To establish the report's footprint and architectural alignment.
*   **Requirements**:
    *   File exists in the correct `reports/` sub-directory.
    *   Header metadata contains valid `contract` and `blueprint` references.
    *   Includes all required sections defined in the domain's `.yaml` sync rule.
*   **Failure Condition**: Missing sections or invalid schema references.
*   **Verification**: Automated check via `contracts/schema_sync_rules/`.

## 🟠 Level 2: Structural (Ontological Integrity)
**Purpose**: To ensure the report correctly maps to the entities defined in Phase 1.
*   **Requirements**:
    *   All entities mentioned (e.g., `Zone_A`, `Learner_01`) exist in the Schema.
    *   Terminology strictly adheres to the "Active Inference" glossary (Beliefs, Surprise, etc.).
    *   Placeholders are used where data is currently missing (Semantic Contracting).
*   **Failure Condition**: Use of non-schema entities or non-standard terminology.
*   **Verification**: Manual peer review against the Technical Blueprint.

## 🟡 Level 3: Functional (Data Integrity)
**Purpose**: To ground the report in empirical reality.
*   **Requirements**:
    *   "Observations" section cites specific files in `evidence/`.
    *   Data tables are populated with real-world or high-fidelity simulation output.
    *   Surprise (Prediction Error) is calculated using the system's `surprise_calculator.py`.
*   **Failure Condition**: Circular references or hallucinated data.
*   **Verification**: Audit of the `evidence/` directory links.

## 🔵 Level 4: Semantic (Analytical Integrity)
**Purpose**: To derive meaning from the surprise.
*   **Requirements**:
    *   "Model Update" section provides a technical rationale for the change in beliefs.
    *   The narrative moves from "what happened" to "why our model was wrong."
    *   Interventions (Phase 4) are linked to the identified vulnerabilities.
*   **Failure Condition**: Descriptive narrative without a "Model Update" logic.
*   **Verification**: Subject Matter Expert (SME) sign-off.

## 🟢 Level 5: Verified (Systemic Integrity)
**Purpose**: To certify the report as a "Hardened Insight" ready for decision support.
*   **Requirements**:
    *   All instructional noise, templates, and placeholder contracts have been removed.
    *   The report is immutable (signed with a hash in `drift_detection/`).
    *   Downstream models have been updated to reflect the "Model Update" recommendations.
*   **Failure Condition**: Presence of meta-text or unresolved "Document Drift."
*   **Verification**: Repository Integrity Architect (System Architect) final audit.
