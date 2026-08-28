# `Patient`

*Parent schema: [Healthcare Sector Schema](Healthcare_Sector_Schema.md)*

## Economic Definition

The primary consumer of healthcare services. Their "HealthState" is the core asset to be preserved or improved. They have preferences and behaviors (e.g., treatment adherence) that influence outcomes.

## System Role

The central entity whose state the system aims to predict and stabilize. Unexpected changes in a patient's health or behavior are a primary source of "surprise."

## Table

| Attribute               | Data Type         | Description                                                               |
| ----------------------- | ----------------- | ------------------------------------------------------------------------- |
| `patient_id`            | `String`          | A unique, anonymized identifier for the patient.                          |
| `demographics`          | `Object`          | Age, sex, and other relevant demographic data for risk stratification.    |
| `health_state_ref`      | `HealthState_Ref` | A reference to the patient's current, evolving `HealthState`.             |
| `care_plan_adherence`   | `ProbabilityDist` | The system's **belief** about the patient's likelihood to follow treatments.|
| `insurance_provider_id` | `String`          | Identifier for the patient's insurer, linking to payment models.          |
