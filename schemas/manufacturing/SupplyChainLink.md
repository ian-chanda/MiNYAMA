# `SupplyChainLink`

*Parent schema: [Manufacturing Sector Schema](Manufacturing_Sector_Schema.md)*

## Economic Definition

Represents the relationship with an external supplier for sourcing raw materials. This is a critical dependency that introduces external risk and uncertainty into the production system.

## System Role

Models an external, partially observable part of the world. A delivery failure is a major external "surprise." The system must maintain beliefs about supplier reliability to mitigate this.

## Table

| Attribute           | Data Type         | Description                                                              |
| ------------------- | ----------------- | ------------------------------------------------------------------------ |
| `link_id`           | `String`          | A unique ID for the supplier relationship.                               |
| `supplier_id`       | `String`          | An identifier for the external supplier (an unmodeled agent).            |
| `supplied_material` | `Material_Ref`    | The `Material` that is being supplied.                                   |
| `lead_time_model`   | `ProbabilityDist` | The system's **belief** about the expected time from order to delivery.  |
| `reliability_score` | `Float`           | The system's **belief** about the supplier's dependability.              |
| `cost_per_unit`     | `Float`           | The current price for the supplied material.                             |
