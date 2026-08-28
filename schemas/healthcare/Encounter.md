# `Encounter` (Observable Event)

*Parent schema: [Healthcare Sector Schema](Healthcare_Sector_Schema.md)*

## Economic Definition

A specific interaction where a service is delivered by a `Provider` to a `Patient`. This is the observable "exchange" in the healthcare economy.

## System Role

This is a primary **sensory input**. Encounters provide new data that confirms or refutes the system's predictions about disease progression and treatment effectiveness.

## Table

| Attribute                  | Data Type              | Description                                                              |
| -------------------------- | ---------------------- | ------------------------------------------------------------------------ |
| `encounter_id`             | `String`               | A unique identifier for the event.                                       |
| `patient_id`               | `Patient_Ref`          | The patient involved in the encounter.                                   |
| `provider_id`              | `Provider_Ref`         | The provider who delivered the service.                                  |
| `encounter_type`           | `Enum`                 | `CONSULTATION`, `SURGERY`, `DIAGNOSTIC_TEST`, `TELEMEDICINE`.            |
| `timestamp`                | `DateTime`             | The time the encounter took place.                                       |
| `observations`             | `Object` / `Text`      | Clinical notes and observations made by the provider.                    |
| `prescribed_interventions` | `Array<Intervention_Ref>`| A list of `Intervention`s that were prescribed or administered.        |
| `outcome_assessment`       | `Object`               | An initial assessment of the encounter's outcome.                        |
