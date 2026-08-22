# Validation Spec: Intervention Validation

An **Intervention** is an active experiment performed by the MiNYAMA system to test its beliefs or improve its environment. This spec defines the audit lifecycle for all actions in `interventions/`.

---

## 1. The Intervention Lifecycle

### 🟢 Phase A: Baseline Audit (Pre-Action)
Before an intervention is authorized, the agent must document:
1.  **The Trigger**: Which "Surprise" in a `reports/` file made this action necessary?
2.  **The Belief**: What do we currently believe will happen if we take this action?
3.  **The Goal**: What is the target reduction in Prediction Error?

### 🟡 Phase B: Execution Logging (In-Action)
During the intervention, real-time telemetry must be captured:
*   **Materials/Resources**: What was consumed?
*   **Timeline**: Was the action performed within the predicted window?
*   **Deviations**: Did any unexpected events occur during execution?

### 🔴 Phase C: Surprise Calculation (Post-Action)
After the intervention, the system must perform a "Verification Audit":
1.  **Observation Sync**: Collect outcomes from `evidence/observations/`.
2.  **Surprise Identification**: Compare the "Actual Outcome" against the "Baseline Expectation."
3.  **Model Update**: Propose specific changes to the parent Schema based on the result.

---

## 2. Validation Logic: The "Learning Test"

An intervention is considered **Valid** only if it contributes to the "Source-Sync Structural Hardening" of the repository.

*   **Success**: The intervention reduced surprise and confirmed the model's predictive power.
*   **Failure**: The intervention was performed without a baseline, or the outcome was not logged.
*   **High-Value Learning**: The intervention resulted in a large surprise, forcing a significant and beneficial "Model Update" (re-hardening).

---

## 3. Operational Examples

### Technical: Irrigation Pulse (Agri)
*   **Baseline**: Belief that 20L of water will increase moisture level by 5%.
*   **Action**: Activate irrigation pump for 30 minutes.
*   **Outcome**: Moisture level increased by only 2%.
*   **Surprise**: -3% moisture delta (Negative Surprise).
*   **Model Update**: Update the "Zone Soil Model" to reflect higher-than-expected drainage/evaporation rates.
