# `Equipment`

*Parent schema: [Agriculture Sector Schema](Agriculture_Sector_Schema.md)*

## Economic Definition

The capital assets used to perform interventions (e.g., tractors, drones, irrigators). Their availability and efficiency are critical operational constraints.

## System Role

The physical agents that carry out the system's chosen `Interventions`. An equipment failure during a critical window (like planting or harvest) is a major "surprise."

## Table

| Attribute           | Data Type     | Description                                                                  |
| ------------------- | ------------- | ---------------------------------------------------------------------------- |
| `equipment_id`      | `String`      | A unique identifier for the piece of equipment.                              |
| `equipment_type`    | `Enum`        | `TRACTOR`, `COMBINE_HARVESTER`, `IRRIGATION_PUMP`, `DRONE`.                  |
| `operational_state` | `Enum`        | The system's **belief** about its state: `IDLE`, `ACTIVE`, `MAINTENANCE`, `FAILED`. |
| `location`          | `GeoPoint`    | The current GPS coordinates of the equipment.                                |
| `telemetry_feed`    | `TimeSeries`  | Real-time data from the equipment (e.g., fuel level, speed, task status).    |
