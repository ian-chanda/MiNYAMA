# `Customer`

*Parent schema: [Retail Sector Schema](Retail_Sector_Schema.md)*

## Economic Definition

Represents the demand side of the retail economy. Customers have preferences, purchasing power, and make decisions based on price, promotion, and perceived value.

## System Role

The primary agent whose behavior the system seeks to predict. Understanding customer intent is key to minimizing demand-related "surprise."

## Table

| Attribute                 | Data Type         | Description                                                               |
| ------------------------- | ----------------- | ------------------------------------------------------------------------- |
| `customer_id`             | `String`          | A unique, anonymized identifier for the customer.                         |
| `demographics`            | `Object`          | Age, location, and other data for segmentation.                           |
| `purchase_history`        | `Array<Txn_Ref>`  | A list of past `Transaction` IDs.                                         |
| `loyalty_status`          | `Enum`            | e.g., `NEW`, `ACTIVE`, `CHURN_RISK`.                                      |
| `propensity_to_buy_model` | `Model`           | The system's **belief** about this customer's likelihood to purchase.     |
