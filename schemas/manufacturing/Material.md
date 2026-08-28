# `Material`

*Parent schema: [Manufacturing Sector Schema](Manufacturing_Sector_Schema.md)*

## Economic Definition

Represents the physical goods at any stage of production, from raw inputs to finished products. It is the inventory that flows through the system, holding value at each stage.

## System Role

The object that is being acted upon. The system tracks the state, location, and quality of materials to ensure the production process can proceed as planned. A shortage or quality failure is a major "surprise."

## Table

| Attribute        | Data Type     | Description                                                               |
| ---------------- | ------------- | ------------------------------------------------------------------------- |
| `material_id`    | `String`      | A unique batch, SKU, or serial number.                                    |
| `material_type`  | `Enum`        | `RAW`, `WORK_IN_PROGRESS`, `FINISHED_GOOD`.                               |
| `specifications` | `Object`      | The required physical or chemical properties of the material.             |
| `quantity`       | `Float` / `Int` | The amount of the material (e.g., in units, kg, liters).                |
| `location`       | `String`      | The system's **belief** about its current physical location (e.g., `WAREHOUSE_A`). |
| `quality_status` | `Enum`        | The system's **belief** about its quality: `PASSED`, `FAILED`, `UNTESTED`.|
