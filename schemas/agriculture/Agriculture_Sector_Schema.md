# System Architecture: Agriculture Sector World Model

## 1. Overview

This document outlines the baseline data architecture for an **Active Inference World Model** tailored to the Agriculture sector. The system's primary objective is to minimize "surprise" by accurately modeling the crop lifecycle from planting to harvest. In this context, "surprise" refers to unpredicted outcomes such as lower-than-expected yields, disease or pest outbreaks, or the negative impact of extreme weather events.

This architecture enables the system to maintain a "belief state" about crop health, soil conditions, and environmental factors, allowing it to optimize interventions like irrigation and fertilization to maximize yield and resource efficiency.

## 2. Entity Relationship Diagram

The following diagram illustrates the high-level relationships. `EnvironmentalData` (like weather) acts upon a `Zone` where a `Crop` grows. The system directs `Equipment` to perform an `Intervention` on the `Zone`/`Crop`. The cycle culminates in a `Yield` observation.

```
+-------------------+      +------+      +-------------+
| EnvironmentalData |----->| Zone |<-----| Intervention|
+-------------------+      +------+      +-------------+
                             |  ^              |  ^
                             |  |              |  |
                             v  |              v  |
                         +------+         +-----------+
                         | Crop |         | Equipment |
                         +------+         +-----------+
                             |
                             |
                             v
                         +-------+
                         | Yield |
                         +-------+
```

## 3. Core Entities

### 3.1. `Zone`

*   **Economic Definition**: The primary unit of land management; the "factory floor" of the farm. Its state (soil health, moisture) determines its productive capacity.
*   **System Role**: A core entity whose state is continuously monitored. The system models the zone's properties to understand its potential and predict its response to interventions and environmental conditions.

| Attribute          | Data Type  | Description                                                                     |
| ------------------ | ---------- | ------------------------------------------------------------------------------- |
| `zone_id`          | `String`   | A unique identifier for the field or sub-field area.                            |
| `location_polygon` | `GeoJSON`  | The precise geospatial boundary of the zone.                                    |
| `size_hectares`    | `Float`    | The area of the zone.                                                           |
| `soil_model`       | `Model`    | The system's **belief** about soil composition (nutrients, organic matter, pH). |
| `moisture_model`   | `Model`    | The system's **belief** about the current soil moisture level.                  |
| `current_crop_ref` | `Crop_Ref` | A reference to the `Crop` currently planted in this zone.                       |

---

### 3.2. `Crop`

*   **Economic Definition**: The biological asset being cultivated. It has a growth cycle and a potential yield, which is the economic value to be realized at harvest.
*   **System Role**: The central entity whose growth and health the system aims to predict and optimize. A deviation from the predicted growth trajectory is a key "surprise."

| Attribute                  | Data Type         | Description                                                                  |
| -------------------------- | ----------------- | ---------------------------------------------------------------------------- |
| `crop_id`                  | `String`          | A unique ID for this planting season in this zone (e.g., `ZONE_A_CORN_2025`). |
| `plant_type`               | `String`          | The type of plant (e.g., `CORN`, `WHEAT`, `SOYBEANS`).                       |
| `genetics`                 | `String`          | The specific variety or genetic makeup of the crop.                          |
| `growth_stage_model`       | `Model`           | The system's **belief** about the crop's current stage (e.g., `GERMINATION`, `VEGETATIVE`, `FLOWERING`). |
| `health_state_model`       | `Model`           | The system's **belief** about stress levels, disease, or pest presence.    |
| `yield_prediction_dist`    | `ProbabilityDist` | The system's **belief** (a distribution) about the final harvestable yield.  |

---

### 3.3. `Intervention` (Observable Event)

*   **Economic Definition**: A management action taken upon a `Zone` or `Crop` to influence its growth and eventual yield. These are the primary costs and operational activities.
*   **System Role**: An "action" initiated by the system to guide the `Crop` towards its predicted optimal state. The system chooses interventions to minimize future "surprise" (like yield loss).

| Attribute           | Data Type       | Description                                                                  |
| ------------------- | --------------- | ---------------------------------------------------------------------------- |
| `intervention_id`   | `String`        | A unique identifier for the action taken.                                    |
| `timestamp`         | `DateTime`      | The time the action was performed.                                           |
| `intervention_type` | `Enum`          | `PLANTING`, `IRRIGATION`, `FERTILIZATION`, `PESTICIDE_APPLICATION`, `HARVEST`. |
| `target_zone_ref`   | `Zone_Ref`      | The `Zone` where the intervention was applied.                               |
| `applied_materials` | `Object`        | Details of materials used (e.g., `{material: 'Nitrogen', quantity: '20kg'}`). |
| `equipment_used_ref`| `Equipment_Ref` | The `Equipment` used to perform the action.                                  |

---

### 3.4. `Equipment`

*   **Economic Definition**: The capital assets used to perform interventions (e.g., tractors, drones, irrigators). Their availability and efficiency are critical operational constraints.
*   **System Role**: The physical agents that carry out the system's chosen `Interventions`. An equipment failure during a critical window (like planting or harvest) is a major "surprise."

| Attribute           | Data Type     | Description                                                                  |
| ------------------- | ------------- | ---------------------------------------------------------------------------- |
| `equipment_id`      | `String`      | A unique identifier for the piece of equipment.                              |
| `equipment_type`    | `Enum`        | `TRACTOR`, `COMBINE_HARVESTER`, `IRRIGATION_PUMP`, `DRONE`.                  |
| `operational_state` | `Enum`        | The system's **belief** about its state: `IDLE`, `ACTIVE`, `MAINTENANCE`, `FAILED`. |
| `location`          | `GeoPoint`    | The current GPS coordinates of the equipment.                                |
| `telemetry_feed`    | `TimeSeries`  | Real-time data from the equipment (e.g., fuel level, speed, task status).    |

---

### 3.5. `EnvironmentalData` (Sensory Input)

*   **Economic Definition**: Represents the external, uncontrollable environmental factors that are a primary source of risk and uncertainty in the agricultural production function.
*   **System Role**: The primary source of **sensory input** about the external world. The system constantly observes this data to update its predictions. An unpredicted weather event is the most significant source of external "surprise."

| Attribute        | Data Type         | Description                                                                  |
| ---------------- | ----------------- | ---------------------------------------------------------------------------- |
| `data_id`        | `String`          | A unique ID for the data point or forecast.                                  |
| `timestamp`      | `DateTime`        | The time the data was recorded or is forecasted for.                         |
| `source`         | `Enum`            | `WEATHER_STATION`, `SATELLITE_IMAGERY`, `SOIL_SENSOR`, `WEATHER_FORECAST`.     |
| `data_type`      | `Enum`            | `TEMPERATURE`, `RAINFALL`, `SOLAR_RADIATION`, `WIND_SPEED`, `NDVI`.            |
| `value`          | `Float`           | The measured or predicted value of the data type.                            |
| `forecast_model` | `Model`           | If the source is a forecast, this holds the model of its future values.      |

---

### 3.6. `Yield` (Observable Outcome)

*   **Economic Definition**: The realized output and economic value from the agricultural process. It is the final "profit" measurement against which all costs and investments are compared.
*   **System Role**: The ultimate **sensory observation** that confirms or refutes the system's performance over an entire growing season. The difference between the `yield_prediction_dist` and the `quantity_measured` is the final, most important "surprise" that drives learning for the next season.

| Attribute           | Data Type     | Description                                                                  |
| ------------------- | ------------- | ---------------------------------------------------------------------------- |
| `yield_id`          | `String`      | A unique ID for this specific harvest event.                                 |
| `crop_ref`          | `Crop_Ref`    | The `Crop` that was harvested.                                               |
| `harvest_timestamp` | `DateTime`    | The time of the harvest.                                                     |
| `quantity_measured` | `Float`       | The total measured yield (e.g., in tonnes).                                  |
| `quality_grade`     | `String`      | The assessed quality of the harvested crop.                                  |
