# Manufacturing Sector Schema — Population Template

> **Source Schema**: [[Manufacturing_Sector_Schema]]  
> **Purpose**: Template for generating valid, schema-aligned population records for the Manufacturing world model.  
> **Population CSV**: [[Manufacturing_Sector_Schema_Population]]  

## How to Use This Template

1. Each section below corresponds to one core entity from the Manufacturing schema.
2. Use the **Attribute Table** to understand required fields, data types, and constraints.
3. Use the **Example Record (JSON)** as a seed for synthetic data generation.
4. When populating multiple records, ensure foreign-key references remain consistent:
   - `Material.material_id` → referenced by `WorkOrder.product_to_produce`, `WorkOrder.input_materials`, `Process.steps.material`, `SupplyChainLink.supplied_material`
   - `PhysicalAsset.asset_id` → referenced by `WorkOrder.assigned_assets`, `Process.steps.asset_type`
   - `Process.process_id` → referenced implicitly by `WorkOrder` via the product being produced
5. Append a `traceability_id` and ISO 8601 `created_at` / `updated_at` timestamp to every record for audit and surprise-analysis.

---

## 1. PhysicalAsset

**Economic role**: Capital equipment that performs work.  
**System role**: Internal agent whose state changes are a primary source of production "surprise."

### 1.1 Attribute Table

| Attribute | Data Type | Description | Example Value | Constraints |
| :-- | :-- | :-- | :-- | :-- |
| `asset_id` | `String` | Unique machine/equipment identifier | `PA-CNC-001` | Required, unique |
| `asset_type` | `Enum` | Type of capital equipment | `CNC_MACHINE` | `CNC_MACHINE`, `ROBOTIC_ARM`, `CONVEYOR_BELT`, `INSPECTION_CAMERA` |
| `operational_state` | `Enum` | System belief about current state | `RUNNING` | `RUNNING`, `IDLE`, `MAINTENANCE`, `FAILED` |
| `maintenance_model` | `Model` | Belief predicting next maintenance | `PREDICTIVE_VIBRATION_MODEL_7D` | Reference to a predictive-maintenance model |
| `throughput_capacity` | `Float` | Expected production rate (units/hour) | `120.5` | Positive number |
| `telemetry_feed` | `TimeSeries` | Real-time sensor data | `{temperature_c: 65.2, vibration_ms2: 0.03, error_codes: []}` | ISO 8601 timestamped readings |

### 1.2 Example Record (JSON)

```json
{
  "asset_id": "PA-CNC-001",
  "asset_type": "CNC_MACHINE",
  "operational_state": "RUNNING",
  "maintenance_model": "PREDICTIVE_VIBRATION_MODEL_7D",
  "throughput_capacity": 120.5,
  "telemetry_feed": {
    "sensor_id": "PA-CNC-001-TELEMETRY",
    "readings": [
      {"timestamp": "2026-08-27T08:00:00Z", "temperature_c": 65.2, "vibration_ms2": 0.03, "error_codes": []},
      {"timestamp": "2026-08-27T09:00:00Z", "temperature_c": 66.1, "vibration_ms2": 0.04, "error_codes": []}
    ]
  },
  "traceability_id": "trace-PA-CNC-001-20260827",
  "created_at": "2026-08-27T08:00:00Z",
  "updated_at": "2026-08-27T09:00:00Z"
}
```

---

## 2. Material

**Economic role**: Physical goods at any production stage.  
**System role**: Object being acted upon; shortages or quality failures are major "surprises."

### 2.1 Attribute Table

| Attribute | Data Type | Description | Example Value | Constraints |
| :-- | :-- | :-- | :-- | :-- |
| `material_id` | `String` | Unique batch, SKU, or serial number | `MAT-RAW-ALU-001` | Required, unique |
| `material_type` | `Enum` | Production stage of the material | `RAW` | `RAW`, `WORK_IN_PROGRESS`, `FINISHED_GOOD` |
| `specifications` | `Object` | Required physical/chemical properties | `{grade: "A6061-T6", dimensions_cm: {length: 100, width: 50, thickness: 2}}` | Schema-defined object |
| `quantity` | `Float` / `Int` | Amount of material | `500.0` | Positive number; unit implied by context |
| `location` | `String` | System belief about current physical location | `WAREHOUSE_A` | Free-text location identifier |
| `quality_status` | `Enum` | System belief about quality | `PASSED` | `PASSED`, `FAILED`, `UNTESTED` |

### 2.2 Example Record (JSON)

```json
{
  "material_id": "MAT-RAW-ALU-001",
  "material_type": "RAW",
  "specifications": {
    "grade": "A6061-T6",
    "dimensions_cm": {"length": 100, "width": 50, "thickness": 2},
    "density_g_cm3": 2.7
  },
  "quantity": 500.0,
  "location": "WAREHOUSE_A",
  "quality_status": "PASSED",
  "traceability_id": "trace-MAT-RAW-ALU-001-20260827",
  "created_at": "2026-08-27T08:00:00Z",
  "updated_at": "2026-08-27T08:00:00Z"
}
```

---

## 3. WorkOrder

**Economic role**: Command to execute a production run.  
**System role**: Primary action initiated by demand; deviation between expected and actual duration is a "surprise."

### 3.1 Attribute Table

| Attribute | Data Type | Description | Example Value | Constraints |
| :-- | :-- | :-- | :-- | :-- |
| `order_id` | `String` | Unique production-job identifier | `WO-2026-001` | Required, unique |
| `product_to_produce` | `Material_Ref` | Reference to final-product Material | `MAT-FG-GEARBOX-001` | Foreign key → `Material.material_id` |
| `quantity_required` | `Int` | Target number of units | `100` | Positive integer |
| `input_materials` | `Array<Material_Ref>` | Raw Materials required | `["MAT-RAW-ALU-001", "MAT-RAW-STEEL-001"]` | Array of `Material.material_id` |
| `assigned_assets` | `Array<Asset_Ref>` | PhysicalAssets tasked | `["PA-CNC-001", "PA-ROBOT-002"]` | Array of `PhysicalAsset.asset_id` |
| `status` | `Enum` | Current order state | `IN_PROGRESS` | `PENDING`, `IN_PROGRESS`, `COMPLETED`, `FAILED` |
| `expected_duration` | `Duration` | Predicted order duration | `PT4H` | ISO 8601 duration |
| `actual_duration` | `Duration` | Measured order duration | `PT4H15M` | ISO 8601 duration |

### 3.2 Example Record (JSON)

```json
{
  "order_id": "WO-2026-001",
  "product_to_produce": "MAT-FG-GEARBOX-001",
  "quantity_required": 100,
  "input_materials": ["MAT-RAW-ALU-001", "MAT-RAW-STEEL-001"],
  "assigned_assets": ["PA-CNC-001", "PA-ROBOT-002"],
  "status": "IN_PROGRESS",
  "expected_duration": "PT4H",
  "actual_duration": "PT4H15M",
  "traceability_id": "trace-WO-2026-001-20260827",
  "created_at": "2026-08-27T08:00:00Z",
  "updated_at": "2026-08-27T13:15:00Z"
}
```

---

## 4. Process

**Economic role**: Defined recipe or standard operating procedure.  
**System role**: Core belief model defining expected sequence of events for a WorkOrder.

### 4.1 Attribute Table

| Attribute | Data Type | Description | Example Value | Constraints |
| :-- | :-- | :-- | :-- | :-- |
| `process_id` | `String` | Unique process identifier | `PROC-GEARBOX-ASSEMBLY-001` | Required, unique |
| `process_name` | `String` | Human-readable name | `Assemble Main Gearbox` | Free text |
| `steps` | `Array<Object>` | Ordered list of operations | `[{step: 1, operation: "cut_shaft", asset_type: "CNC_MACHINE", material: "MAT-RAW-STEEL-001", duration: "PT1H"}, ...]` | Ordered sequence |
| `quality_checkpoints` | `Array<Object>` | Points where quality is assessed | `[{step: 1, check: "dimensional_tolerance", threshold: 0.01}, ...]` | Linked to `steps` indices |

### 4.2 Example Record (JSON)

```json
{
  "process_id": "PROC-GEARBOX-ASSEMBLY-001",
  "process_name": "Assemble Main Gearbox",
  "steps": [
    {"step": 1, "operation": "cut_shaft", "asset_type": "CNC_MACHINE", "material": "MAT-RAW-STEEL-001", "duration": "PT1H"},
    {"step": 2, "operation": "mill_housing", "asset_type": "CNC_MACHINE", "material": "MAT-RAW-ALU-001", "duration": "PT1H"},
    {"step": 3, "operation": "assemble_gear", "asset_type": "ROBOTIC_ARM", "duration": "PT2H"}
  ],
  "quality_checkpoints": [
    {"step": 1, "check": "dimensional_tolerance", "threshold": 0.01},
    {"step": 2, "check": "surface_finish_ra", "threshold": 1.6},
    {"step": 3, "check": "torque_validation", "threshold": 45.0}
  ],
  "traceability_id": "trace-PROC-GEARBOX-ASSEMBLY-001-20260827",
  "created_at": "2026-08-27T08:00:00Z",
  "updated_at": "2026-08-27T08:00:00Z"
}
```

---

## 5. SupplyChainLink

**Economic role**: Relationship with an external supplier for raw materials.  
**System role**: External, partially observable dependency; delivery failures are external "surprises."

### 5.1 Attribute Table

| Attribute | Data Type | Description | Example Value | Constraints |
| :-- | :-- | :-- | :-- | :-- |
| `link_id` | `String` | Unique supplier-relationship identifier | `SCL-ACME-ALU-001` | Required, unique |
| `supplier_id` | `String` | External supplier identifier | `SUP-ACME-METALS-001` | External reference |
| `supplied_material` | `Material_Ref` | Material being supplied | `MAT-RAW-ALU-001` | Foreign key → `Material.material_id` |
| `lead_time_model` | `ProbabilityDist` | Belief about order-to-delivery time | `Normal(mean=5d, std=1d)` | Distribution as string or JSON |
| `reliability_score` | `Float` | Belief about supplier dependability | `0.94` | Value in `[0.0, 1.0]` |
| `cost_per_unit` | `Float` | Current price for supplied material | `12.50` | Non-negative monetary value |

### 5.2 Example Record (JSON)

```json
{
  "link_id": "SCL-ACME-ALU-001",
  "supplier_id": "SUP-ACME-METALS-001",
  "supplied_material": "MAT-RAW-ALU-001",
  "lead_time_model": {
    "distribution": "Normal",
    "parameters": {"mean": "5d", "std": "1d"}
  },
  "reliability_score": 0.94,
  "cost_per_unit": 12.50,
  "traceability_id": "trace-SCL-ACME-ALU-001-20260827",
  "created_at": "2026-08-27T08:00:00Z",
  "updated_at": "2026-08-27T08:00:00Z"
}
```

---

## Cross-Reference Map

```text
PhysicalAsset.asset_id  ────────┐
                                ├──► WorkOrder.assigned_assets
PhysicalAsset.asset_type  ──────┤    Process.steps.asset_type
                                │
Material.material_id  ──────────┼──► WorkOrder.product_to_produce
                                │    WorkOrder.input_materials
                                │    Process.steps.material
                                └──► SupplyChainLink.supplied_material

Process.process_id  ────────────┐
                                └──► (implicit via WorkOrder product_to_produce)
```

## Minimum Viable Population Set

For a single runnable manufacturing scenario, populate at least:

- **2+ PhysicalAssets** (e.g., one CNC machine, one robotic arm)
- **2+ Materials** (one raw input, one finished good)
- **1 WorkOrder** linking the materials and assets
- **1 Process** describing how the finished good is produced
- **1 SupplyChainLink** sourcing the raw material

## Next Steps

1. Export populated records as JSON to `evidence/environmental_priors/` or `evidence/observations/`.
2. Run the model to compute prediction error (surprise) between `WorkOrder.expected_duration` and `WorkOrder.actual_duration`.
3. Log surprises in `evidence/prediction_error_logs/` with `traceability_id` references.
