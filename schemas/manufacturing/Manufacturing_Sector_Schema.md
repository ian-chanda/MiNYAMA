# System Architecture: Manufacturing Sector World Model

## 1. Overview

This document outlines the baseline data architecture for an **Active Inference World Model** tailored to the Manufacturing sector. The system's primary objective is to minimize "surprise" by accurately modeling the entire production lifecycle. In this context, "surprise" refers to unpredicted events like machine failures, supply chain disruptions, quality control issues, or deviations from production targets.

This architecture defines the core entities that form the agent's internal "belief state" about its production capacity, material flow, and operational efficiency.

## 2. Entity Relationship Diagram

The following diagram illustrates the high-level relationships. A `WorkOrder` consumes input `Materials` (often sourced via a `SupplyChainLink`) and uses a `Process` to direct `PhysicalAssets` to transform them into output `Materials`.

```
+-----------------+      +----------+      +----------------+
| SupplyChainLink |----->| Material |----->|    WorkOrder   |
+-----------------+      +----------+      +----------------+
                               |     ^         |     ^
                               |     |         |     |
                               v     |         v     |
                         +-----------+   +-------------+
                         | Process   |   | PhysicalAsset |
                         +-----------+   +-------------+
```

## 3. Core Entities

### 3.1. `PhysicalAsset`

*   **Economic Definition**: Represents the capital equipment that performs work (e.g., machines, robots, assembly lines). Their operational state is a primary determinant of production capacity and cost.
*   **System Role**: These are agents that act upon materials. An unexpected change in their state (e.g., a breakdown) is a critical "surprise" that directly impacts production capacity.

| Attribute            | Data Type      | Description                                                                  |
| -------------------- | -------------- | ---------------------------------------------------------------------------- |
| `asset_id`           | `String`       | A unique identifier for the machine or equipment.                            |
| `asset_type`         | `Enum`         | `CNC_MACHINE`, `ROBOTIC_ARM`, `CONVEYOR_BELT`, `INSPECTION_CAMERA`.            |
| `operational_state`  | `Enum`         | The system's **belief** about the current state: `RUNNING`, `IDLE`, `MAINTENANCE`, `FAILED`. |
| `maintenance_model`  | `Model`        | The system's **belief** predicting when the next maintenance will be needed.   |
| `throughput_capacity`| `Float`        | The expected production rate (e.g., units per hour).                         |
| `telemetry_feed`     | `TimeSeries`   | Real-time sensor data (temperature, vibration, error codes).                 |

---

### 3.2. `Material`

*   **Economic Definition**: Represents the physical goods at any stage of production, from raw inputs to finished products. It is the inventory that flows through the system, holding value at each stage.
*   **System Role**: The object that is being acted upon. The system tracks the state, location, and quality of materials to ensure the production process can proceed as planned. A shortage or quality failure is a major "surprise."

| Attribute        | Data Type     | Description                                                               |
| ---------------- | ------------- | ------------------------------------------------------------------------- |
| `material_id`    | `String`      | A unique batch, SKU, or serial number.                                    |
| `material_type`  | `Enum`        | `RAW`, `WORK_IN_PROGRESS`, `FINISHED_GOOD`.                               |
| `specifications` | `Object`      | The required physical or chemical properties of the material.             |
| `quantity`       | `Float` / `Int` | The amount of the material (e.g., in units, kg, liters).                |
| `location`       | `String`      | The system's **belief** about its current physical location (e.g., `WAREHOUSE_A`). |
| `quality_status` | `Enum`        | The system's **belief** about its quality: `PASSED`, `FAILED`, `UNTESTED`.|

---

### 3.3. `WorkOrder` (Observable Event)

*   **Economic Definition**: A command to execute a production run, transforming a set of input materials into a specified quantity of finished goods. It represents a discrete unit of production and value creation.
*   **System Role**: This is a primary **action** initiated by the system or an external demand signal. It drives the behavior of `PhysicalAssets`. Any deviation between the `expected_duration` and `actual_duration` is a "surprise" to be minimized.

| Attribute           | Data Type            | Description                                                               |
| ------------------- | -------------------- | ------------------------------------------------------------------------- |
| `order_id`          | `String`             | A unique identifier for the production job.                               |
| `product_to_produce`| `Material_Ref`       | A reference to the `Material` definition of the final product.            |
| `quantity_required` | `Int`                | The target number of units to produce.                                    |
| `input_materials`   | `Array<Material_Ref>`| A list of the raw `Material`s required for the order.                     |
| `assigned_assets`   | `Array<Asset_Ref>`   | The `PhysicalAsset`(s) tasked with completing the order.                  |
| `status`            | `Enum`               | `PENDING`, `IN_PROGRESS`, `COMPLETED`, `FAILED`.                          |
| `expected_duration` | `Duration`           | The system's **prediction** of how long the order will take.              |
| `actual_duration`   | `Duration`           | The measured time taken, used for model refinement.                       |

---

### 3.4. `Process`

*   **Economic Definition**: The defined "recipe" or standard operating procedure for manufacturing a product. It represents the intellectual property and accumulated knowledge of production.
*   **System Role**: A core part of the system's **belief** model. It defines the expected sequence of events for a `WorkOrder`. The system can act to optimize a `Process` to improve efficiency.

| Attribute            | Data Type     | Description                                                              |
| -------------------- | ------------- | ------------------------------------------------------------------------ |
| `process_id`         | `String`      | Unique ID for the manufacturing process.                                 |
| `process_name`       | `String`      | Human-readable name (e.g., "Assemble Main Gearbox").                     |
| `steps`              | `Array<Object>`| An ordered list of operations, linking asset types, materials, and durations. |
| `quality_checkpoints`| `Array<Object>`| Defined points within the `steps` where quality is to be assessed.       |

---

### 3.5. `SupplyChainLink`

*   **Economic Definition**: Represents the relationship with an external supplier for sourcing raw materials. This is a critical dependency that introduces external risk and uncertainty into the production system.
*   **System Role**: Models an external, partially observable part of the world. A delivery failure is a major external "surprise." The system must maintain beliefs about supplier reliability to mitigate this.

| Attribute           | Data Type         | Description                                                              |
| ------------------- | ----------------- | ------------------------------------------------------------------------ |
| `link_id`           | `String`          | A unique ID for the supplier relationship.                               |
| `supplier_id`       | `String`          | An identifier for the external supplier (an unmodeled agent).            |
| `supplied_material` | `Material_Ref`    | The `Material` that is being supplied.                                   |
| `lead_time_model`   | `ProbabilityDist` | The system's **belief** about the expected time from order to delivery.  |
| `reliability_score` | `Float`           | The system's **belief** about the supplier's dependability.              |
| `cost_per_unit`     | `Float`           | The current price for the supplied material.                             |
