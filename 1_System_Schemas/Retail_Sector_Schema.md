# System Architecture: Retail Sector World Model

## 1. Overview

This document outlines the baseline data architecture for an **Active Inference World Model** tailored to the Retail sector. The system's primary objective is to minimize "surprise" by accurately modeling the flow of goods to meet customer demand. In this context, "surprise" refers to unpredicted stockouts (lost sales), excess inventory (carrying costs), or sudden shifts in customer purchasing behavior.

This architecture enables the system to maintain a "belief state" about inventory levels, customer intent, and future demand, allowing it to optimize pricing, promotions, and supply chain logistics.

## 2. Entity Relationship Diagram

The following diagram illustrates the high-level relationships. A `Customer` engages in `Interactions`, which may lead to a `Transaction`. A `Transaction` converts an `InventoryItem` (an instance of a `Product`) from available to sold. The `DemandForecast` is the system's core belief about future `Transactions`.

```
+-----------+      +---------------------+      +-------------+
| Customer  |----->| CustomerInteraction |----->| Transaction |
+-----------+      +---------------------+      +-------------+
      ^                                               |
      |                                               |
      |                                               v
+---------------+                            +---------------+
| DemandForecast|--------------------------->| InventoryItem |
+---------------+                            +---------------+
                                                    |
                                                    |
                                                    v
                                               +---------+
                                               | Product |
                                               +---------+
```

## 3. Core Entities

### 3.1. `Customer`

*   **Economic Definition**: Represents the demand side of the retail economy. Customers have preferences, purchasing power, and make decisions based on price, promotion, and perceived value.
*   **System Role**: The primary agent whose behavior the system seeks to predict. Understanding customer intent is key to minimizing demand-related "surprise."

| Attribute                 | Data Type         | Description                                                               |
| ------------------------- | ----------------- | ------------------------------------------------------------------------- |
| `customer_id`             | `String`          | A unique, anonymized identifier for the customer.                         |
| `demographics`            | `Object`          | Age, location, and other data for segmentation.                           |
| `purchase_history`        | `Array<Txn_Ref>`  | A list of past `Transaction` IDs.                                         |
| `loyalty_status`          | `Enum`            | e.g., `NEW`, `ACTIVE`, `CHURN_RISK`.                                      |
| `propensity_to_buy_model` | `Model`           | The system's **belief** about this customer's likelihood to purchase.     |

---

### 3.2. `Product`

*   **Economic Definition**: The good or service being sold; the core unit of the retailer's offering. Its value is realized when exchanged.
*   **System Role**: A static entity defining the properties of what is sold. The system's goal is to manage the flow of tangible instances of this product.

| Attribute          | Data Type     | Description                                                          |
| ------------------ | ------------- | -------------------------------------------------------------------- |
| `product_id`       | `String`      | A unique identifier for the product (e.g., SKU, UPC).                |
| `description`      | `String`      | Product name, brand, and other descriptive attributes.               |
| `category`         | `String`      | Product category for hierarchical analysis (e.g., `Electronics`).      |
| `price`            | `Float`       | The current selling price of the product.                            |
| `cost_of_goods_sold`| `Float`       | The cost to acquire the product from a supplier.                     |
| `supplier_id`      | `String`      | An identifier for the external supplier.                             |

---

### 3.3. `InventoryItem`

*   **Economic Definition**: A tangible, countable instance of a `Product` at a specific location. This is the physical asset that constitutes the retailer's inventory.
*   **System Role**: The core belief state of the system revolves around the quantity and location of these items. A stockout is a "surprise" where the `quantity` of an `AVAILABLE` item is zero when demand occurs.

| Attribute     | Data Type     | Description                                                               |
| ------------- | ------------- | ------------------------------------------------------------------------- |
| `inventory_id`| `String`      | A unique identifier for a specific batch or unit.                         |
| `product_id`  | `Product_Ref` | The `Product` this item is an instance of.                                |
| `location_id` | `String`      | The system's **belief** of its location (e.g., `WAREHOUSE_B`, `STORE_5`). |
| `quantity`    | `Int`         | The number of units at this location.                                     |
| `status`      | `Enum`        | The system's **belief** of its status: `AVAILABLE`, `IN_TRANSIT`, `SOLD`. |

---

### 3.4. `CustomerInteraction` (Observable Event)

*   **Economic Definition**: Any engagement a customer has with the retailer, whether it results in a sale or not. These are signals of interest and purchase intent.
*   **System Role**: A key **sensory input**. The system observes these interactions to update its beliefs about customer intent and the accuracy of its `DemandForecast`. A cart abandonment is a "surprise" if a purchase was predicted.

| Attribute         | Data Type     | Description                                                               |
| ----------------- | ------------- | ------------------------------------------------------------------------- |
| `interaction_id`  | `String`      | A unique identifier for the session or event.                             |
| `customer_id`     | `Customer_Ref`| The customer who initiated the interaction.                               |
| `channel`         | `Enum`        | `ONLINE`, `IN_STORE`, `MOBILE_APP`.                                       |
| `timestamp`       | `DateTime`    | The time the interaction occurred.                                        |
| `interaction_type`| `Enum`        | `PAGE_VIEW`, `ADD_TO_CART`, `SEARCH_QUERY`, `PROMO_CODE_APPLIED`.         |
| `outcome`         | `Enum`        | `PURCHASE`, `CART_ABANDONMENT`, `BOUNCE`.                                 |

---

### 3.5. `Transaction` (Observable Event)

*   **Economic Definition**: A completed sale, where a customer exchanges payment for a product. This is the ultimate realization of value in the retail cycle.
*   **System Role**: The most important **sensory input**, confirming a successful prediction from the `DemandForecast` and triggering an update to the `InventoryItem` state.

| Attribute         | Data Type                 | Description                                                               |
| ----------------- | ------------------------- | ------------------------------------------------------------------------- |
| `transaction_id`  | `String`                  | A unique identifier for the sale.                                         |
| `customer_id`     | `Customer_Ref`            | The customer who made the purchase.                                       |
| `items_purchased` | `Array<{Product, Qty}>`   | A list of the `Product`s and quantities sold.                             |
| `total_price`     | `Float`                   | The final amount paid by the customer.                                    |
| `timestamp`       | `DateTime`                | The time the sale was completed.                                          |
| `channel`         | `Enum`                    | The channel where the transaction occurred (`ONLINE`, `IN_STORE`).        |

---

### 3.6. `DemandForecast`

*   **Economic Definition**: A prediction of future sales for a product. This forecast is the primary driver for all operational decisions, including ordering, pricing, and marketing.
*   **System Role**: This is the system's core **belief** about the future. The system's actions are all aimed at preparing for this predicted future. The difference between the forecast and actual sales is the "surprise" the system learns from.

| Attribute                       | Data Type         | Description                                                              |
| ------------------------------- | ----------------- | ------------------------------------------------------------------------ |
| `forecast_id`                   | `String`          | A unique ID for this forecast version.                                   |
| `product_id`                    | `Product_Ref`     | The `Product` this forecast applies to.                                  |
| `time_horizon`                  | `TimeRange`       | The future period this forecast covers (e.g., next 7 days).              |
| `predicted_sales_distribution`  | `ProbabilityDist` | The system's **belief** about the likely range of sales, not just a single number. |
| `seasonality_model`             | `Model`           | A model of cyclical demand patterns.                                     |
| `promotional_lift_model`        | `Model`           | The system's **belief** about how promotions will impact sales.          |
