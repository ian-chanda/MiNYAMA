# `EnvironmentalData` (Sensory Input)

*Parent schema: [Agriculture Sector Schema](Agriculture_Sector_Schema.md)*

## Economic Definition

Represents the external, uncontrollable environmental factors that are a primary source of risk and uncertainty in the agricultural production function.

## System Role

The primary source of **sensory input** about the external world. The system constantly observes this data to update its predictions. An unpredicted weather event is the most significant source of external "surprise."

## Table

| Attribute        | Data Type         | Description                                                                  |
| ---------------- | ----------------- | ---------------------------------------------------------------------------- |
| `data_id`        | `String`          | A unique ID for the data point or forecast.                                  |
| `timestamp`      | `DateTime`        | The time the data was recorded or is forecasted for.                         |
| `source`         | `Enum`            | `WEATHER_STATION`, `SATELLITE_IMAGERY`, `SOIL_SENSOR`, `WEATHER_FORECAST`.     |
| `data_type`      | `Enum`            | `TEMPERATURE`, `RAINFALL`, `SOLAR_RADIATION`, `WIND_SPEED`, `NDVI`.            |
| `value`          | `Float`           | The measured or predicted value of the data type.                            |
| `forecast_model` | `Model`           | If the source is a forecast, this holds the model of its future values.      |
