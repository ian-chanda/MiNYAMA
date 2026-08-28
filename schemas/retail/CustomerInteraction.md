# `CustomerInteraction` (Observable Event)

*Parent schema: [Retail Sector Schema](Retail_Sector_Schema.md)*

## Economic Definition

Any engagement a customer has with the retailer, whether it results in a sale or not. These are signals of interest and purchase intent.

## System Role

A key **sensory input**. The system observes these interactions to update its beliefs about customer intent and the accuracy of its `DemandForecast`. A cart abandonment is a "surprise" if a purchase was predicted.

## Table

| Attribute         | Data Type     | Description                                                               |
| ----------------- | ------------- | ------------------------------------------------------------------------- |
| `interaction_id`  | `String`      | A unique identifier for the session or event.                             |
| `customer_id`     | `Customer_Ref`| The customer who initiated the interaction.                               |
| `channel`         | `Enum`        | `ONLINE`, `IN_STORE`, `MOBILE_APP`.                                       |
| `timestamp`       | `DateTime`    | The time the interaction occurred.                                        |
| `interaction_type`| `Enum`        | `PAGE_VIEW`, `ADD_TO_CART`, `SEARCH_QUERY`, `PROMO_CODE_APPLIED`.         |
| `outcome`         | `Enum`        | `PURCHASE`, `CART_ABANDONMENT`, `BOUNCE`.                                 |
