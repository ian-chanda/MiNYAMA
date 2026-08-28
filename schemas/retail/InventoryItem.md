# `InventoryItem`

*Parent schema: [Retail Sector Schema](Retail_Sector_Schema.md)*

## Economic Definition

A tangible, countable instance of a `Product` at a specific location. This is the physical asset that constitutes the retailer's inventory.

## System Role

The core belief state of the system revolves around the quantity and location of these items. A stockout is a "surprise" where the `quantity` of an `AVAILABLE` item is zero when demand occurs.

## Table

| Attribute     | Data Type     | Description                                                               |
| ------------- | ------------- | ------------------------------------------------------------------------- |
| `inventory_id`| `String`      | A unique identifier for a specific batch or unit.                         |
| `product_id`  | `Product_Ref` | The `Product` this item is an instance of.                                |
| `location_id` | `String`      | The system's **belief** of its location (e.g., `WAREHOUSE_B`, `STORE_5`). |
| `quantity`    | `Int`         | The number of units at this location.                                     |
| `status`      | `Enum`        | The system's **belief** of its status: `AVAILABLE`, `IN_TRANSIT`, `SOLD`. |
