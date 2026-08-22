# Phase 3: The Material Layer (Sensory Input System)

The **Material Layer** is the empirical grounding mechanism of the MiNYAMA framework. In an Active Inference system, intelligence is not just in the logic; it is in the delta between what we believe and what we sense. This directory manages that sensory reality.

## 1. The Evidence Philosophy

MiNYAMA treats evidence as a first-class architectural component. We do not store "data"; we store **Synchronized Observations** that are physically linked to the ontologies in `schemas/`.

### The Active Inference Pipeline
1.  **Prior Beliefs** (`environmental_priors/`): What the system expects based on historical context and schema definitions.
2.  **Observations** (`observations/`): The "Now" state of reality, collected from IoT sensors or field reports.
3.  **Prediction Error / Surprise** (`prediction_error_logs/`): The calculated mismatch between Step 1 and Step 2.
4.  **Model Update & Hardening**: The result of Step 3 is used to adjust the Schema and elevate the status of Reports in `reports/`.

---

## 2. Directory Walkthrough

### 🟢 [Environmental Priors](environmental_priors/)
**The "Before" State.** Contains the starting assumptions and baseline constraints for every sector. 
*   *Operational Role:* Provides the `expected_value` for all surprise calculations.

### 🟡 [Observations](observations/)
**The "Now" State.** Contains the raw sensory input from the external world.
*   *Operational Role:* Provides the `observed_value`. No report can move to Level 3 (Functional) without citing a file here.

### 🔴 [Prediction Error Logs](prediction_error_logs/)
**The "Delta" State.** Stores the output of the inference engine.
*   *Operational Role:* These logs are the "Triggers" for learning. A high surprise score here forces a systemic update in Phase 6 (Integrity).

---

## 3. Evidence Lifecycle & Validation

To maintain systemic integrity, all evidence must be:
*   **Traceable**: Every record must have a `traceability_id` linking it to a source (sensor, agent, or API).
*   **Timestamped**: All measurements must use ISO 8601 formatting.
*   **Schema-Linked**: Data fields must match the `Attribute` names in the corresponding Technical Blueprint.

### Naming Conventions
*   `{sector}_env_{region}_{version}.json` (for Priors)
*   `{sector}_obs_{source}_{timestamp}.json` (for Observations)
*   `{sector}_surprise_{entity}_{id}.json` (for Error Logs)

---

## 4. Glossary

*   **Priors**: The mathematical beliefs held by the system before new data is ingested.
*   **Observations**: The raw, objective measurements of the environment.
*   **Prediction Error**: The raw difference between the belief and the observation.
*   **Surprise**: A normalized score representing the significance of the Prediction Error relative to our confidence (precision).
*   **Model Update**: The corrective action taken to align future Priors with observed reality.
*   **Hardening**: The process of verifying a report by grounding its claims in this Material Layer.
