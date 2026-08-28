# `Transaction` (Observable Event)

*Parent schema: [Retail Sector Schema](Retail_Sector_Schema.md)*

## Economic Definition

A completed sale, where a customer exchanges payment for a product. This is the ultimate realization of value in the retail cycle.

## System Role

The most important **sensory input**, confirming a successful prediction from the `DemandForecast` and triggering an update to the `InventoryItem` state.

## Table

| Attribute         | Data Type                 | Description                                                               |
| ----------------- | ------------------------- | ------------------------------------------------------------------------- |
| `transaction_id`  | `String`                  | A unique identifier for the sale.                                         |
| `customer_id`     | `Customer_Ref`            | The customer who made the purchase.                                       |
| `items_purchased` | `Array<{Product, Qty}>`   | A list of the `Product`s and quantities sold.                             |
| `total_price`     | `Float`                   | The final amount paid by the customer.                                    |
| `timestamp`       | `DateTime`                | The time the sale was completed.                                          |
| `channel`         | `Enum`                    | The channel where the transaction occurred (`ONLINE`, `IN_STORE`).        |
