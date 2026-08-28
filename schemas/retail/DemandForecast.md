# `DemandForecast`

*Parent schema: [Retail Sector Schema](Retail_Sector_Schema.md)*

## Economic Definition

A prediction of future sales for a product. This forecast is the primary driver for all operational decisions, including ordering, pricing, and marketing.

## System Role

This is the system's core **belief** about the future. The system's actions are all aimed at preparing for this predicted future. The difference between the forecast and actual sales is the "surprise" the system learns from.

## Table

| Attribute                       | Data Type         | Description                                                              |
| ------------------------------- | ----------------- | ------------------------------------------------------------------------ |
| `forecast_id`                   | `String`          | A unique ID for this forecast version.                                   |
| `product_id`                    | `Product_Ref`     | The `Product` this forecast applies to.                                  |
| `time_horizon`                  | `TimeRange`       | The future period this forecast covers (e.g., next 7 days).              |
| `predicted_sales_distribution`  | `ProbabilityDist` | The system's **belief** about the likely range of sales, not just a single number. |
| `seasonality_model`             | `Model`           | A model of cyclical demand patterns.                                     |
| `promotional_lift_model`        | `Model`           | The system's **belief** about how promotions will impact sales.          |
