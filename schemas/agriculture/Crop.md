# `Crop`

*Parent schema: [Agriculture Sector Schema](Agriculture_Sector_Schema.md)*

## Economic Definition

The biological asset being cultivated. It has a growth cycle and a potential yield, which is the economic value to be realized at harvest.

## System Role

The central entity whose growth and health the system aims to predict and optimize. A deviation from the predicted growth trajectory is a key "surprise."

## Table

| Attribute                  | Data Type         | Description                                                                  |
| -------------------------- | ----------------- | ---------------------------------------------------------------------------- |
| `crop_id`                  | `String`          | A unique ID for this planting season in this zone (e.g., `ZONE_A_CORN_2025`). |
| `plant_type`               | `String`          | The type of plant (e.g., `CORN`, `WHEAT`, `SOYBEANS`).                       |
| `genetics`                 | `String`          | The specific variety or genetic makeup of the crop.                          |
| `growth_stage_model`       | `Model`           | The system's **belief** about the crop's current stage (e.g., `GERMINATION`, `VEGETATIVE`, `FLOWERING`). |
| `health_state_model`       | `Model`           | The system's **belief** about stress levels, disease, or pest presence.    |
| `yield_prediction_dist`    | `ProbabilityDist` | The system's **belief** (a distribution) about the final harvestable yield.  |
