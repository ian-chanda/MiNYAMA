# Phase 6.3: Verification Frameworks (Systemic Integrity Specification)

The **Verification Frameworks** provide the tools and protocols for checking the integrity of the MiNYAMA knowledge base. This is the "Automated Auditor" that prevents epistemic drift.

## 1. Purpose & Relationship
While `contracts/` defines the **Rules**, Verification Frameworks define the **Tests**. They bridge the gap between static YAML rules and the dynamic state of the repository.

## 2. Verification Categories

### 🟢 Category A: Schema Synchronization (Source-to-Sync)
*   **Check**: Does every Python class in `models/` exactly match its counterpart in `schemas/`?
*   **Check**: Do all reports cite the *active* version hash of their parent schema?
*   **Fail Severity**: **CRITICAL**. Block all downstream analytical outputs.

### 🟡 Category B: Hardening Validation (Structural-to-Functional)
*   **Check**: Does a "Level 3" report actually contain links to existing files in `evidence/`?
*   **Check**: Are the mandatory semantic tags (`👉 [SURPRISE_DELTA]`, `🛠 [SYNC_UPDATE]`) present and valid?
*   **Fail Severity**: **MEDIUM**. Demote report to "Draft" status.

### 🔴 Category C: Evidence Integrity (Material-to-Inference)
*   **Check**: Does the `timestamp` in an observation match the window defined in the prior?
*   **Check**: Is the `uncertainty_weight` within the acceptable bounds for that sensor type?
*   **Fail Severity**: **HIGH**. Suspend the resulting "Surprise" score.

---

## 3. Verification Lifecycle
1.  **Scan**: Automated crawl of the repo (triggered by `git commit` or manual audit).
2.  **Compare**: Check files against `contracts/drift_detection/schema_hashes.json`.
3.  **Flag**: Identify `DriftEvents` and log them in `governance/audit_logs/`.
4.  **Remediate**: Human/Agent intervention to re-synchronize or re-harden the artifact.

## 4. Escalation Pathways

| Result | Status | Action |
| :--- | :--- | :--- |
| **Pass** | `Verified` | Update integrity hash; allow Level 5 Hardening. |
| **Minor Mismatch** | `Stale` | Flag for review; maintain current hardening level. |
| **Contract Breach** | `Invalid` | Immediate demotion to Level 1; trigger Sync Audit. |
| **Ontology Break** | `Corrupt` | Governance freeze on the affected Sector. |

---

## 5. Future Automation: The "Governance Bot"
The long-term goal for MiNYAMA is an automated **Integrity Scanner** that:
*   Generates the `dependency_map.json` dynamically.
*   Automatically calculates file hashes on save.
*   Blocks pull requests that introduce **Document Drift**.

*MiNYAMA is a self-correcting institutional learning infrastructure.*
