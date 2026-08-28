# `Intervention`

*Parent schema: [Healthcare Sector Schema](Healthcare_Sector_Schema.md)*

## Economic Definition

Represents a specific treatment, therapy, or medication that can be applied to alter a `HealthState`. It has associated costs and expected benefits (utility).

## System Role

An "action" that can be taken. The system models the likely effect of an intervention to decide on the best course of action to minimize future "surprise" (i.e., poor health outcomes).

## Table

| Attribute               | Data Type         | Description                                                              |
| ----------------------- | ----------------- | ------------------------------------------------------------------------ |
| `intervention_id`       | `String`          | Unique ID for the intervention (e.g., RxNorm for drugs).                 |
| `intervention_type`     | `Enum`            | `MEDICATION`, `PHYSICAL_THERAPY`, `SURGICAL_PROCEDURE`, `DIAGNOSTIC`.    |
| `cost_model`            | `Model`           | A model of the financial cost of the intervention.                       |
| `expected_efficacy_model`| `Model`           | The system's **belief** about the intervention's effectiveness on a `HealthState`.|
| `known_side_effects`    | `Array<String>`   | A list of potential adverse effects.                                     |
