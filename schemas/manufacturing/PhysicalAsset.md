# `PhysicalAsset`

*Parent schema: [Manufacturing Sector Schema](Manufacturing_Sector_Schema.md)*

## Economic Definition

Represents the capital equipment that performs work (e.g., machines, robots, assembly lines). Their operational state is a primary determinant of production capacity and cost.

## System Role

These are agents that act upon materials. An unexpected change in their state (e.g., a breakdown) is a critical "surprise" that directly impacts production capacity.

## Table

| Attribute            | Data Type      | Description                                                                  |
| -------------------- | -------------- | ---------------------------------------------------------------------------- |
| `asset_id`           | `String`       | A unique identifier for the machine or equipment.                            |
| `asset_type`         | `Enum`         | `CNC_MACHINE`, `ROBOTIC_ARM`, `CONVEYOR_BELT`, `INSPECTION_CAMERA`.            |
| `operational_state`  | `Enum`         | The system's **belief** about the current state: `RUNNING`, `IDLE`, `MAINTENANCE`, `FAILED`. |
| `maintenance_model`  | `Model`        | The system's **belief** predicting when the next maintenance will be needed.   |
| `throughput_capacity`| `Float`        | The expected production rate (e.g., units per hour).                         |
| `telemetry_feed`     | `TimeSeries`   | Real-time sensor data (temperature, vibration, error codes).                 |
