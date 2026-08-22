# Phase 3.3: Prediction Error Logs (The Surprise Layer)

## 1. What is Prediction Error?
In Active Inference, **Prediction Error** is the raw delta between our Belief (Prior) and the Reality (Observation). 

## 2. What is Surprise?
**Surprise** is the significance of that error. It is the "Volume" of the signal that tells the system: "Your model is wrong."
*   **Low Surprise**: Error is within expected noise levels. No update needed.
*   **High Surprise**: Reality is fundamentally different from expectations. **Model Update Required.**

## 3. Severity Classifications & Escalation

| Surprise Score | Classification | Action |
| :--- | :--- | :--- |
| 0.0 - 0.1 | **Noise** | Log for historical baseline; no update. |
| 0.1 - 0.3 | **Anomaly** | Flag for manual review in Level 3 reports. |
| 0.3 - 0.6 | **Surprise** | Trigger "Model Update" in schemas; Re-harden reports. |
| 0.6 - 1.0 | **Critical Failure** | Immediate Intervention (Phase 4) + Governance Audit. |

## 4. Hardening & Intelligence
The files in this directory are the primary evidence for **Level 4 (Semantic) Hardening**. You cannot explain *why* a model changed without referencing the Surprise identified in these logs.

## 5. Synchronization Rules
Prediction Error logs must cite both the `prior_ref` and the `observation_ref` to maintain a perfect audit trail. If either source is modified, the Log is flagged as **Stale**.
