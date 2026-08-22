# Phase 3.2: Observations (The Reality Layer)

## 1. Purpose
The `observations/` directory represents the "Now" state of the world. It is the destination for all objective data entering the MiNYAMA system. This data is the "Sensory Input" that confirms or refutes our internal beliefs.

## 2. Acceptable Formats & Standards
All observations must be machine-readable to support automated "Surprise Calculation."

### Ingestion Standards
*   **IoT Telemetry**: Structured JSON streams from sensors (Soil, Energy, Logistics).
*   **Field Reports**: Standardized Markdown or CSV files from human agents (project leads, farmers).
*   **External APIs**: Cached responses from third-party services (Weather, Market Prices).

### Provenance Requirements
Every observation must answer: **Who/What saw this?**
*   Must include a `source_id` (e.g., `SENSOR_01`, `AGENT_NAME`).
*   Must include an `uncertainty_weight` (How much do we trust this sensor?).

---

## 3. Validation Rules

### ✅ Valid Observation
```json
{
  "source_id": "LUSAKA_PH_SENSOR_09",
  "timestamp": "2026-05-09T14:30:00Z",
  "metric": "ph_level",
  "value": 6.2,
  "unit": "pH",
  "uncertainty_weight": 0.95
}
```

### ❌ Invalid Observation
```text
"The pH was around 6 today."
- Error: No source_id, no timestamp, no precision, not machine-parsable.
```

## 4. Relationship to Hardening
A report in `reports/` cannot move past **Level 2 (Structural)** without citing a file in this directory. Observations are the physical proof required for **Level 3 (Functional)** status.
