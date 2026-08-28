# `Zone`

*Parent schema: [Agriculture Sector Schema](Agriculture_Sector_Schema.md)*

## Economic Definition

The primary unit of land management; the "factory floor" of the farm. Its state (soil health, moisture) determines its productive capacity.

## System Role

A core entity whose state is continuously monitored. The system models the zone's properties to understand its potential and predict its response to interventions and environmental conditions.

## Table

| Attribute          | Data Type  | Description                                                                     |
| ------------------ | ---------- | ------------------------------------------------------------------------------- |
| `zone_id`          | `String`   | A unique identifier for the field or sub-field area.                            |
| `location_polygon` | `GeoJSON`  | The precise geospatial boundary of the zone.                                    |
| `size_hectares`    | `Float`    | The area of the zone.                                                           |
| `soil_model`       | `Model`    | The system's **belief** about soil composition (nutrients, organic matter, pH). |
| `moisture_model`   | `Model`    | The system's **belief** about the current soil moisture level.                  |
| `current_crop_ref` | `Crop_Ref` | A reference to the `Crop` currently planted in this zone.                       |
