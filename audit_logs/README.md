# Governance: Audit & Traceability Policy

The **Audit Logs** directory serves as the permanent, immutable memory of the MiNYAMA system's adaptive journey. It records the "Why" behind every structural change, ensuring that institutional knowledge is preserved even as the repository evolves.

## 1. Audit Purpose
Audit logs are not merely records of change; they are **Inference Histories**. They document the transformation of the system's beliefs over time, providing the "Proof of Learning" required for Active Inference governance.

## 2. Record Lifecycle
1.  **Creation**: An entry is created when a **Surprise** triggers a **Model Update**.
2.  **Attribution**: The entry must cite the specific contributor or automated process (`source_id`).
3.  **Traceability**: The record must link the `report_id`, `schema_id`, and `evidence_id` involved in the change.
4.  **Review**: High-severity updates require a "Governance Sign-off" before the log is finalized.

---

## 3. Standardized Entry Structure (JSON/Markdown)
Every audit record must contain:
*   `timestamp`: ISO 8601 UTC.
*   `artifact_ref`: Path to the file being audited.
*   `event_type`: `HARDENING_EVENT` | `SCHEMA_SYNC` | `INTERVENTION_AUDIT` | `DRIFT_RESOLUTION`.
*   `delta_summary`: A concise description of the change (e.g., "Updated Drainage Belief").
*   `integrity_hash`: The SHA-256 of the artifact at the time of log creation.

## 4. Severity & Escalation Examples

### 🟢 SEV-3: Hardening Level Elevation
*   **Event**: `Report_Agriculture_Analysis.md` moved from Level 2 to Level 3.
*   **Validation**: Evidence cited and verified.
*   **Action**: Log entry created; no escalation needed.

### 🟡 SEV-2: Synchronization Correction
*   **Event**: Model code was 2 versions behind the Schema.
*   **Conflict**: `baseline_model.py` missing `soil_pH` attribute defined in Blueprint.
*   **Resolution**: Sync performed; Drift Detection reset.

### 🔴 SEV-1: Structural Surprise (High-Severity Learning)
*   **Event**: Actual Yield was 40% below prediction.
*   **Surprise**: Massive Negative Delta (-3.4 t/ha).
*   **Escalation**: Triggered immediate Schema audit for `Agriculture_Sector`. Governance review required to determine if the "World Model" itself is fundamentally flawed.

---

## 5. Immutable History Philosophy
Audit logs in MiNYAMA are **Append-Only**. Once a verification check is signed off, the log entry is part of the system's permanent belief history. Deleting or altering logs is a violation of the **Operational Integrity Mandate**.
