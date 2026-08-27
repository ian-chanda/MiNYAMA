# Model Update: Zambia Manufacturing Sector

> **Source Schema**: [[Manufacturing_Sector_Schema]]  
> **Prior Baseline**: [[manufacturing_zambia_population]]  
> **Observations**: [[manufacturing_zambia_observations]]  
> **Surprise Log**: [[manufacturing_zambia_surprise_log]]  
> **Audit Log**: [[2026-08-27_zambia_manufacturing_population]]  
> **Traceability ID**: trace-MODEL-UPDATE-ZMB-MFG-20260827  

---

## 1. Executive Summary

This model update hardens the Manufacturing sector schema from **Level 1 (Skeletal)** toward **Level 2 (Structural)** by grounding the abstract `PhysicalAsset`, `Material`, `WorkOrder`, `Process`, and `SupplyChainLink` entities in a concrete Zambian agro-processing scenario. The update is driven by four detected prediction errors (surprises) between the synthetic prior baseline and simulated observations.

## 2. Surprises Driving Model Updates

| # | Entity | Attribute | Prior Belief | Observation | Surprise Score | Severity |
| :- | :- | :- | :- | :- | :- | :- |
| 1 | `WorkOrder.WO-ZMB-2026-001` | `actual_duration` | `PT3H` | `PT3H20M` | 0.111 | MEDIUM |
| 2 | `SupplyChainLink.SCL-EASTERN-TOMATO-001` | `lead_time_model` | `Normal(μ=2d, σ=0.5d)` | 2.5 days | 1.0σ | LOW |
| 3 | `Process.PROC-TOMATO-PASTE-001` | `brix_measurement` | 28.0 °Brix | 26.5 °Brix | 0.75 | MEDIUM |
| 4 | `PhysicalAsset.PA-CNC-001` | `vibration_ms2` | 0.06 m/s² | 0.10 m/s² | 0.67 | MEDIUM |

## 3. Recommended Schema / Model Changes

### 3.1 WorkOrder.expected_duration

**Issue**: The prior `PT3H` did not account for Zambian grid instability and dust-related conveyor slowdown.  
**Recommendation**: Add an `operational_context` field to `WorkOrder` capturing:

```json
{
  "operational_context": {
    "grid_stability_window": "stable",
    "ambient_temperature_c": 40.0,
    "dust_exposure_level": "HIGH"
  }
}
```

Update `expected_duration` model to condition on these context variables.

### 3.2 SupplyChainLink.lead_time_model

**Issue**: Prior assumed dry-season road conditions; observation reflects rainy-season delay.  
**Recommendation**: Replace static `Normal(μ=2d, σ=0.5d)` with a **seasonal mixture model**:

```json
{
  "lead_time_model": {
    "type": "SeasonalMixture",
    "dry_season": {"distribution": "Normal", "parameters": {"mean": "2d", "std": "0.5d"}},
    "rainy_season": {"distribution": "Normal", "parameters": {"mean": "2.8d", "std": "0.8d"}}
  }
}
```

### 3.3 Process.quality_checkpoints

**Issue**: `brix_measurement` threshold of 28.0 is unachievable with early-harvest tomatoes.  
**Recommendation**: Add a **material-condition factor** to the checkpoint:

```json
{
  "quality_checkpoints": [
    {
      "step": 3,
      "check": "brix_measurement",
      "threshold": 28.0,
      "adjustable_by_material_condition": true,
      "minimum_threshold": 25.0
    }
  ]
}
```

### 3.4 PhysicalAsset.maintenance_model

**Issue**: CNC vibration elevated due to dust ingress and rough flooring.  
**Recommendation**: Extend `maintenance_model` to include environmental exposure indices:

```json
{
  "maintenance_model": {
    "model_id": "PREDICTIVE_TOOL_WEAR_MODEL_14D",
    "environmental_exposure": {
      "dust_ingress_risk": "HIGH",
      "floor_vibration_risk": "MEDIUM",
      "voltage_fluctuation_risk": "HIGH"
    }
  }
}
```

## 4. Hardening Level Assessment

| Criterion | Before | After |
| :- | :- | :- |
| Schema entities populated | No | Yes |
| Foreign-key consistency | N/A | Validated |
| Enum conformance | N/A | Validated |
| Realistic numeric calibration | No | Zambia-grounded |
| Observations linked | No | Yes |
| Surprise calculation | No | 4 records |
| Model update recommendations | No | Yes |

**Result**: Manufacturing sector advances from **Level 1 (Skeletal)** to **Level 2 (Structural)**. Level 3 (Functional) requires live or historical data ingestion and automated re-computation.

## 5. Next Steps

1. Implement the schema changes above in `schemas/manufacturing/Manufacturing_Sector_Schema.md`.
2. Update `contracts/drift_detection/dependency_map.json` if new attributes are added.
3. Re-run `models/prediction_engines/surprise_calculator.py` against the new priors.
4. Generate a Level-3 analytical report in `reports/analytical_outputs/` once real observations are available.
