# `HealthState`

*Parent schema: [Healthcare Sector Schema](Healthcare_Sector_Schema.md)*

## Economic Definition

This represents the central "asset" of value in the healthcare economy. It is a complex, evolving state that services aim to improve or maintain.

## System Role

This is the core belief state that the system tries to model and predict. Any deviation from the predicted trajectory of the `HealthState` is a significant "surprise."

## Table

| Attribute         | Data Type      | Description                                                              |
| ----------------- | -------------- | ------------------------------------------------------------------------ |
| `state_id`        | `String`       | A unique ID for this snapshot of the patient's health, linked to a patient. |
| `timestamp`       | `DateTime`     | The time this health state was recorded or inferred.                     |
| `vital_signs`     | `TimeSeries`   | Time-series data of vital signs (heart rate, blood pressure, etc.).      |
| `diagnoses`       | `Array<String>`| A list of active diagnoses (e.g., ICD-10 codes).                         |
| `prognosis_model` | `Model`        | The system's **belief** about the future evolution of this health state.   |
| `quality_of_life` | `Float`        | A score representing the system's belief about the patient's QoL.        |
