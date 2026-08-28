# `Yield` (Observable Outcome)

*Parent schema: [Agriculture Sector Schema](Agriculture_Sector_Schema.md)*

## Economic Definition

The realized output and economic value from the agricultural process. It is the final "profit" measurement against which all costs and investments are compared.

## System Role

The ultimate **sensory observation** that confirms or refutes the system's performance over an entire growing season. The difference between the `yield_prediction_dist` and the `quantity_measured` is the final, most important "surprise" that drives learning for the next season.

## Table

| Attribute           | Data Type     | Description                                                                  |
| ------------------- | ------------- | ---------------------------------------------------------------------------- |
| `yield_id`          | `String`      | A unique ID for this specific harvest event.                                 |
| `crop_ref`          | `Crop_Ref`    | The `Crop` that was harvested.                                               |
| `harvest_timestamp` | `DateTime`    | The time of the harvest.                                                     |
| `quantity_measured` | `Float`       | The total measured yield (e.g., in tonnes).                                  |
| `quality_grade`     | `String`      | The assessed quality of the harvested crop.                                  |
