# `WorkOrder` (Observable Event)

*Parent schema: [Manufacturing Sector Schema](Manufacturing_Sector_Schema.md)*

## Economic Definition

A command to execute a production run, transforming a set of input materials into a specified quantity of finished goods. It represents a discrete unit of production and value creation.

## System Role

This is a primary **action** initiated by the system or an external demand signal. It drives the behavior of `PhysicalAssets`. Any deviation between the `expected_duration` and `actual_duration` is a "surprise" to be minimized.

## Table

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
