---
timestamp: 2026-08-27T11:30:00Z
artifact_ref: evidence/environmental_priors/manufacturing_zambia_population.json
event_type: DATA_POPULATION_AND_INFERENCE
traceability_id: AUD-20260827-ZMB-MFG-01
integrity_hash: 8f3e9a2b1c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f
 tags:
  - "#SEV-3"
  - synthetic-data
  - zambia-manufacturing
  - active-inference
  - schema-aligned
---

# Audit: Zambia Manufacturing Synthetic Population, Observations, and Surprise Inference

## Delta Summary

Generated a schema-aligned synthetic baseline for the Manufacturing sector, grounded in Zambian manufacturing context (ZDA agro-processing priority sub-sector, Eastern Province tomato supply chain, Lusaka industrial zone assets). The deliverables include:

1. **Population baseline**: `evidence/environmental_priors/manufacturing_zambia_population.json` and `.csv`
   - 2 `PhysicalAsset` records (CONVEYOR_BELT and CNC_MACHINE)
   - 2 `Material` records (RAW tomatoes from Eastern Province, FINISHED_GOOD ZamTomato Paste 400g)
   - 1 `WorkOrder` record (WO-ZMB-2026-001)
   - 1 `Process` record (PROC-TOMATO-PASTE-001)
   - 1 `SupplyChainLink` record (SCL-EASTERN-TOMATO-001)

2. **Observations**: `evidence/observations/manufacturing_zambia_observations.json` and `.csv`
   - 8 sensory observations from telemetry, MES, supplier delivery, and QC lab sources.

3. **Surprise inference**: `evidence/prediction_error_logs/manufacturing_zambia_surprise_log.json` and `.csv`
   - 4 prediction-error records comparing priors to observations.

## Validation Performed

- All foreign-key references resolve across `PhysicalAsset`, `Material`, `WorkOrder`, `Process`, and `SupplyChainLink`.
- All enum values match the Manufacturing sector schema exactly.
- All `traceability_id` values follow the `trace-{ENTITY_ID}-{YYYYMMDD}` pattern.
- All timestamps are valid ISO 8601 and `updated_at >= created_at`.
- Numeric fields satisfy positivity and range constraints.
- JSON outputs validated with `ConvertFrom-Json`.
- CSV and JSON outputs are semantically identical.

## Files Added / Modified

| File | Purpose |
| :--- | :--- |
| `evidence/environmental_priors/manufacturing_zambia_population.json` | Prior beliefs / synthetic master data |
| `evidence/environmental_priors/manufacturing_zambia_population.csv` | CSV mirror of population data |
| `evidence/observations/manufacturing_zambia_observations.json` | Sensory observations |
| `evidence/observations/manufacturing_zambia_observations.csv` | CSV mirror of observations |
| `evidence/prediction_error_logs/manufacturing_zambia_surprise_log.json` | Prediction errors and insights |
| `evidence/prediction_error_logs/manufacturing_zambia_surprise_log.csv` | CSV mirror of surprise log |

## Key Surprises Detected

1. **WorkOrder duration**: Expected `PT3H`, observed `PT3H20M` (+11.1%) — load-shedding and dust-induced conveyor slowdown.
2. **Supplier lead time**: Expected 2.0 days, observed 2.5 days — rainy-season road delays from Chipata to Lusaka.
3. **Brix measurement**: Expected 28.0 °Brix, observed 26.5 °Brix — early harvest due to delivery uncertainty.
4. **CNC vibration**: Expected 0.06 m/s², observed 0.10 m/s² — dust ingress and uneven factory flooring.

## Residual Risk / Follow-ups

- [ ] Integrate Zambia manufacturing population into `models/prediction_engines/surprise_calculator.py` for automated re-computation.
- [ ] Generate `reports/model_updates/manufacturing_zambia_model_update.md` documenting schema hardening recommendations.
- [ ] Add real integrity hashes (SHA-256) to evidence files and audit log once a hashing pipeline is in place.
- [ ] Consider expanding population to include maize, copper, and cashew sub-sectors for broader Zambian manufacturing coverage.

## Classification Note

Logged as SEV-3 per `audit_logs/README.md` severity examples: routine synthetic-data population and inference event with no security or structural integrity impact.
