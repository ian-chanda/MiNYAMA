# Operational Guide: Orientation to Insight Generation (Agent Entity Zero)

This guide operationalizes the **Agent Entity Zero** reasoning model. It is the "Manual of Thinking" for all MiNYAMA contributors, defining how to transform raw observations into hardened insights.

---

## 1. The Core Logic: Learning Through Surprise
Insight is the **reduction of surprise**—the delta between what we expected (The Belief) and what occurred (The Reality). If your report does not identify a surprise, you have not generated an insight; you have merely recorded a fact.

## 2. The Four-Step Inference Loop

### Step 1: Baseline Expectations (The Belief)
*   **Purpose**: To define the "Normal Heartbeat" before looking at data.
*   **Requirement**: You must cite a specific `prior` from `evidence/environmental_priors/`.
*   **Failure Pattern**: "I think the soil should be wet." (Vague).
*   **Correct Pattern**: "Based on `agri_env_LUSAKA_01`, the soil moisture prior is 0.45 m3/m3."

### Step 2: Observation (The Reality)
*   **Purpose**: To record objective reality without interpretation.
*   **Requirement**: Link to a specific `observation` file in `evidence/observations/`.
*   **Failure Pattern**: "The farm looked dry today." (Subjective).
*   **Correct Pattern**: "👉 [SENSORY_DATA] `agri_obs_LUSAKA_01_2026.json` records moisture at 0.28."

### Step 3: Surprise Identification (The Delta)
*   **Purpose**: To quantify the mismatch.
*   **Requirement**: Use the `👉 [SURPRISE_DELTA]` tag. Calculate `Observation - Belief`.
*   **Logic**: A large delta with high confidence triggers a **Model Update**. A large delta with low confidence (bad sensor) triggers a **Governance Audit**.

### Step 4: Model Update (The Insight)
*   **Purpose**: To answer *Why* and adjust for the future.
*   **Requirement**: Use the `🛠 [SYNC_UPDATE]` tag. Propose a specific change to the Schema or Model weights.
*   **Example**: "The surprise indicates that our drainage belief was too low. Update `Zone.soil_model.drainage`."

---

## 3. Acceptable Analytical Reasoning
*   **Traceable**: Every claim must follow the path: `Schema -> Prior -> Observation -> Delta -> Update`.
*   **Ontology-Bound**: Insights must be expressed in terms of the schema's entities.
*   **Non-Circular**: You cannot use an observation to prove the belief that generated the observation.

## 4. Unsupported Claim Detection (Failure Patterns)
*   **The "Hunch"**: An insight with no linked evidence.
*   **The "Instructional Noise"**: A report that repeats the template instructions instead of providing analysis.
*   **The "Orphan Insight"**: An update proposed with no identified surprise to justify it.

---
*By following this loop, you ensure that every update to the MiNYAMA world model is an empirically verified step toward systemic maturity.*
