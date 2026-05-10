# MiNYAMA: System Methodology & Architecture Doctrine

## 1. System Philosophy: Ontology-First Active Inference
MiNYAMA is an **Adaptive Intelligence Infrastructure**. Unlike traditional repositories that prioritize code execution, MiNYAMA prioritizes **Ontological Synchronization**. The system is treated as an agent that maintains a "World Model" to minimize **Surprise** (Prediction Error).

### The Prime Mandate
> "If a claim is not in the Schema, it does not exist. If a result is not backed by Evidence, it is not an insight."

---

## 2. The Four Pillars of the Architecture

### I. The Blueprint (Source of Truth)
*   **Location**: `schemas/`
*   **Logic**: Immutable definitions. Every entity (Zone, Learner, Asset) is defined here with its expected attributes and behaviors.
*   **Governance**: Changes to the Blueprint trigger a "Drift Event" across the entire repo.

### II. The Material Layer (Sensory Input)
*   **Location**: `evidence/`
*   **Logic**: Reality. Stores the **Priors** (Expectations) and **Observations** (Facts).
*   **Governance**: Evidence must be traceable and timestamped. It is the only force permitted to "Surprise" the system.

### III. The Mechanical Sync (The Engine)
*   **Location**: `models/`
*   **Logic**: Executable Beliefs. Python code that implements the logic defined in the Schemas.
*   **Governance**: Models must implement `contracts/semantic_interfaces/` to ensure they don't drift from the Blueprint.

### IV. The Hardened Output (Analytical Insights)
*   **Location**: `reports/`
*   **Logic**: Verified Transformations. The narrative result of the inference process.
*   **Governance**: Reports are progressively "Hardened" until they represent a verified model update.

---

## 3. SSSH: Schema-Synchronized Systems Hardening
SSSH is the mandatory methodology for all repository activities. It follows a specific maturity lifecycle:

| State | Layer | Description |
| :--- | :--- | :--- |
| **Skeletal** | Structural | Template matching the Schema headers. No data. |
| **Functional** | Data | Populated with Evidence from Phase 3. Surprise calculated. |
| **Semantic** | Analytical | Deep rationale provided for the Model Update. |
| **Integrity** | Verified | Hardened against all contracts; audited and signed. |

---

## 4. Contributor Operating Principles
1.  **Epistemic Humility**: Assume your model is wrong. Look for the **Surprise**.
2.  **Ontological Discipline**: Use the exact names and types defined in Phase 1.
3.  **Traceability**: Every report must "show its work" by linking to the specific evidence files in `evidence/`.
4.  **Self-Correction**: If you find a drift, do not hide it—log it as a `DriftEvent` in the Audit Logs.

---
*MiNYAMA: Architecture is the code. Evidence is the truth. Surprise is the teacher.*
