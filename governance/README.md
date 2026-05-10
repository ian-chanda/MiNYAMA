# Phase 6: The Governance & Integrity Layer

The **Governance & Integrity Layer** is the constitutional framework of the MiNYAMA repository. It defines the protocols by which humans and systems coordinate to maintain a self-correcting, high-integrity knowledge base.

## 1. Governance Philosophy: The Self-Correcting Repo
MiNYAMA is not a static collection of files; it is a **living institutional memory system** built on Active Inference. Governance ensures that the system’s "Thinking" (Models/Reports) remains synchronized with the "World" (Evidence) by enforcing a strict hierarchy of truth.

### Contracts vs. Governance
*   **Contracts (`/contracts`)**: The machine-readable "Sync Rules" (YAML/Python). They define the *What* and *How* of technical alignment.
*   **Governance (`/governance`)**: The human-system "Protocol Layer." It defines the *Why*, the *Who*, and the *Operational Mandate* for synchronization.

---

## 2. Key Governance Definitions

*   **Document Drift**: The phenomenon where reports or models begin to describe a version of the world that no longer matches the current Schema or Evidence.
*   **Schema Desynchronization**: A critical failure where the Mechanical Sync (code) or Analytical Output (reports) references non-existent or outdated ontological entities.
*   **Hardening**: The mandatory process of moving an artifact through five levels of maturity (Skeletal to Verified).
*   **Verification**: The systemic audit process used to confirm that an artifact is "Contract-Compliant."
*   **Operational Integrity**: The state in which every claim in the repository is traceable to a baseline expectation, an empirical observation, and a resulting surprise identification.

---

## 3. Directory Walkthrough

### 🟢 [Operational Guides](operational_guides/)
The master doctrines of the repository.
*   **[SYSTEM_DOCS.md](operational_guides/SYSTEM_DOCS.md)**: The architectural constitution.
*   **[Orientation_to_Insight_Generation.md](operational_guides/Orientation_to_Insight_Generation.md)**: The "Agent Entity Zero" reasoning handbook.

### 🟡 [Audit Logs](audit_logs/)
The institutional memory of the system.
*   **Role**: Tracks every hardening event, schema update, and intervention outcome to prevent memory loss.

### 🔴 [Verification Frameworks](verification_frameworks/)
The systemic scanning layer.
*   **Role**: Coordinates with `contracts/drift_detection` to identify stale files and trigger re-hardening workflows.

---

## 4. Contributor Obligations & Escalation

### The Synchronization Lifecycle
1.  **Observe**: Identify a drift event via automated scan or manual review.
2.  **Declare**: Log the drift in `governance/audit_logs/`.
3.  **Synchronize**: Update the artifact to match the current Schema (Phase 1).
4.  **Harden**: Re-verify the artifact according to `validation_specs/`.

### Escalation Logic
*   **Low Severity**: Minor terminology mismatch. Action: Flag for next re-hardening pass.
*   **Medium Severity**: Report references outdated evidence. Action: Suspend "Verified" status.
*   **High Severity**: Schema-Model mismatch. Action: Immediate "Sync Audit" required; block downstream reports.
*   **Critical Severity**: Unverified intervention taken in the field. Action: Governance freeze; System Architect review required.

---
*MiNYAMA prevents epistemic drift by treating every update as a learning operation.*
