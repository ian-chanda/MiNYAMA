# Manufacturing Population — Data Requirements

> **Scope**: Defines the data needed to populate the Manufacturing sector schema in a way that is valid, traceable, and useful for Active Inference / surprise analysis.  
> **Source Schema**: [[Manufacturing_Sector_Schema]]  
> **Template**: [[Manufacturing_Sector_Schema_Population_Template]]  
> **CSV Seed**: [[Manufacturing_Sector_Schema_Population]]  

---

## 1. Minimum Data to Instantiate One Record Per Entity

To create a single valid scenario, the following values are required for each entity:

### 1.1 PhysicalAsset
- `asset_id`: unique machine identifier
- `asset_type`: one of `CNC_MACHINE`, `ROBOTIC_ARM`, `CONVEYOR_BELT`, `INSPECTION_CAMERA`
- `operational_state`: one of `RUNNING`, `IDLE`, `MAINTENANCE`, `FAILED`
- `throughput_capacity`: numeric rate (units per hour)
- (Optional but recommended) `maintenance_model` name and `telemetry_feed` sample

### 1.2 Material
- `material_id`: unique batch/SKU
- `material_type`: one of `RAW`, `WORK_IN_PROGRESS`, `FINISHED_GOOD`
- `quantity`: amount on hand
- `location`: warehouse or line location
- `quality_status`: one of `PASSED`, `FAILED`, `UNTESTED`
- `specifications`: at minimum a grade or dimension object

### 1.3 WorkOrder
- `order_id`: unique job identifier
- `product_to_produce`: must reference an existing `Material.material_id` of type `FINISHED_GOOD`
- `quantity_required`: integer target
- `input_materials`: array referencing existing `Material.material_id` values of type `RAW` or `WORK_IN_PROGRESS`
- `assigned_assets`: array referencing existing `PhysicalAsset.asset_id` values
- `status`: one of `PENDING`, `IN_PROGRESS`, `COMPLETED`, `FAILED`
- `expected_duration`: ISO 8601 duration (prior belief)
- `actual_duration`: ISO 8601 duration (observed)

### 1.4 Process
- `process_id`: unique process identifier
- `process_name`: human-readable name
- `steps`: ordered array linking `asset_type`, `material`, and `duration`
- `quality_checkpoints`: array linked to `steps` indices

### 1.5 SupplyChainLink
- `link_id`: unique supplier-relationship identifier
- `supplier_id`: external supplier identifier
- `supplied_material`: must reference an existing `Material.material_id` of type `RAW`
- `lead_time_model`: distribution or model reference
- `reliability_score`: float in `[0.0, 1.0]`
- `cost_per_unit`: non-negative float

---

## 2. Data Needed for a Meaningful Active Inference Run

Active Inference depends on comparing **beliefs/predictions** with **observations**. Therefore, population should include both:

### 2.1 Beliefs (Priors / Environmental Priors)

Stored in `evidence/environmental_priors/` as JSON:

| Belief | Example | Used For |
| :-- | :-- | :-- |
| Expected asset uptime / failure model | `Mean time between failures = 720h` | Predicting `PhysicalAsset.operational_state` |
| Expected process duration | `Process step 1 = PT1H` | `WorkOrder.expected_duration` |
| Expected supplier lead time | `Normal(μ=5d, σ=1d)` | `SupplyChainLink.lead_time_model` |
| Expected material quality pass rate | `0.96` | `Material.quality_status` |
| Expected throughput capacity | `120.5 units/hour` | `PhysicalAsset.throughput_capacity` |
| Inventory policy / reorder points | `Reorder at 100 units` | Material flow decisions |

### 2.2 Observations (Sensory Evidence)

Stored in `evidence/observations/` as JSON:

| Observation | Example | Source |
| :-- | :-- | :-- |
| Actual telemetry readings | `{timestamp, temperature_c, vibration_ms2, error_codes}` | `PhysicalAsset.telemetry_feed` |
| Actual work-order completion times | `actual_duration = PT4H15M` | MES / ERP |
| Actual material quality inspection results | `FAILED` at checkpoint 2 | QC system |
| Actual supplier delivery times | `Delivered 2026-08-30` | Procurement system |
| Actual asset state transitions | `RUNNING → FAILED at 14:32` | SCADA / IoT |
| Demand signals | `Customer order for 500 units` | Sales / ERP |

### 2.3 Actions

Stored in `interventions/` or embedded in `WorkOrder` records:

| Action | Example |
| :-- | :-- |
| Production job launched | `WorkOrder WO-2026-001` |
| Maintenance scheduled | `PhysicalAsset PA-CNC-001 → MAINTENANCE` |
| Supplier order placed | `Purchase order to SUP-ACME-METALS-001` |
| Process parameter change | `Increase CNC feed rate by 10%` |

---

## 3. Data Needed for Audit & Surprise Logging

Per repo convention, every evidence artifact should carry:

- `traceability_id`: unique trace ID
- `timestamp`: ISO 8601
- `artifact_ref`: file or entity reference
- `event_type`: e.g., `PRIOR_SET`, `OBSERVATION_RECORDED`, `SURPRISE_DETECTED`
- `delta_summary`: what changed
- `integrity_hash`: hash of the record/content

For `evidence/prediction_error_logs/`, each surprise record needs:

- `prediction`: the prior belief value
- `observation`: the actual observed value
- `prediction_error`: numeric difference
- `surprise_score`: scalar (e.g., squared error or KL divergence)
- `affected_entity`: e.g., `WorkOrder`, `PhysicalAsset`, `SupplyChainLink`
- `attribute`: the specific attribute that diverged
- `timestamp`: when the observation occurred
- `traceability_id`: link to observation and prior

---

## 4. Domain Context Needed from the User

To generate realistic and coherent population data, the following decisions are needed:

### 4.1 Sector / Product
- What is being manufactured? (e.g., automotive gearboxes, electronics PCBs, food packaging)
- What is the finished good SKU/name?
- What raw materials and WIP items exist?

### 4.2 Facility & Assets
- How many machines/assets? Of which types?
- What are their names/IDs?
- What are their throughput rates?
- Where are they located?

### 4.3 Process Definition
- What are the manufacturing steps in order?
- How long does each step take?
- Which asset type performs each step?
- Where are quality checkpoints?
- What are the pass/fail thresholds?

### 4.4 Suppliers
- Who supplies each raw material?
- What is the typical lead time and variability?
- What is the historical reliability?
- What is the cost per unit?

### 4.5 Work Orders & Demand
- What jobs are scheduled?
- What quantities are required?
- What are the planned start/end times?
- What actually happened? (for surprise analysis)

### 4.6 Time Horizon
- What date range should the data cover?
- What timezone?
- What is the simulation/observation granularity? (hourly, shift-based, daily)

### 4.7 Surprise Scenarios (Optional but Valuable)
- Are there known disruptions to model? (machine failure, supplier delay, quality defect)
- What is the magnitude of each disruption?
- When did/will it occur?

---

## 5. Suggested Data Deliverables

If you can provide the following, a full population can be generated automatically:

1. **Product BOM (Bill of Materials)** — finished good + raw materials + quantities
2. **Asset register** — machine IDs, types, capacities, locations
3. **Process routing** — step sequence, durations, asset types, quality checkpoints
4. **Supplier catalog** — supplier IDs, materials supplied, lead times, reliability, costs
5. **Work order schedule** — order IDs, products, quantities, assigned assets, expected/actual durations
6. **Observed events** — failures, quality results, deliveries, telemetry samples
7. **Time range and timezone** — for timestamp generation

---

## 6. Quick-Start Option

If no real data is available, a **synthetic baseline** can be generated from a short description:

> *"We make gearboxes. Raw steel shafts and aluminum housings are machined on CNC machines, then a robotic arm assembles them. Quality checks measure dimensional tolerance and torque. Supplier Acme Metals delivers aluminum with a 5-day lead time. We run one 8-hour shift."*

From that paragraph, all required entities and cross-references can be inferred and populated.
