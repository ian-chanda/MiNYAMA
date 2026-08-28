# `Process`

*Parent schema: [Manufacturing Sector Schema](Manufacturing_Sector_Schema.md)*

## Economic Definition

The defined "recipe" or standard operating procedure for manufacturing a product. It represents the intellectual property and accumulated knowledge of production.

## System Role

A core part of the system's **belief** model. It defines the expected sequence of events for a `WorkOrder`. The system can act to optimize a `Process` to improve efficiency.

## Table

| Attribute            | Data Type     | Description                                                              |
| -------------------- | ------------- | ------------------------------------------------------------------------ |
| `process_id`         | `String`      | Unique ID for the manufacturing process.                                 |
| `process_name`       | `String`      | Human-readable name (e.g., "Assemble Main Gearbox").                     |
| `steps`              | `Array<Object>`| An ordered list of operations, linking asset types, materials, and durations. |
| `quality_checkpoints`| `Array<Object>`| Defined points within the `steps` where quality is to be assessed.       |
