# `Intervention` (Observable Event)

*Parent schema: [Agriculture Sector Schema](Agriculture_Sector_Schema.md)*

## Economic Definition

A management action taken upon a `Zone` or `Crop` to influence its growth and eventual yield. These are the primary costs and operational activities.

## System Role

An "action" initiated by the system to guide the `Crop` towards its predicted optimal state. The system chooses interventions to minimize future "surprise" (like yield loss).

## Table

| Attribute           | Data Type       | Description                                                                  |
| ------------------- | --------------- | ---------------------------------------------------------------------------- |
| `intervention_id`   | `String`        | A unique identifier for the action taken.                                    |
| `timestamp`         | `DateTime`      | The time the action was performed.                                           |
| `intervention_type` | `Enum`          | `PLANTING`, `IRRIGATION`, `FERTILIZATION`, `PESTICIDE_APPLICATION`, `HARVEST`. |
| `target_zone_ref`   | `Zone_Ref`      | The `Zone` where the intervention was applied.                               |
| `applied_materials` | `Object`        | Details of materials used (e.g., `{material: 'Nitrogen', quantity: '20kg'}`). |
| `equipment_used_ref`| `Equipment_Ref` | The `Equipment` used to perform the action.                                  |
