# System Architecture: Healthcare Sector World Model

## 1. Overview

This document outlines the baseline data architecture for an **Active Inference World Model** tailored to the Healthcare sector. The system's primary objective is to minimize "surprise" by accurately modeling the healthcare ecosystem. In this context, "surprise" refers to unpredicted patient outcomes, treatment failures, or resource shortages.

The architecture defines the core entities that form the agent's internal "belief state" about the health of patients and the capacity of providers.

## 2. Entity Relationship Diagram

The following diagram illustrates the high-level relationships between the core entities. An `Encounter` is the central event where a `Provider` applies an `Intervention` to a `Patient`, influencing their `HealthState`.

```
+----------+      +-----------------+      +---------+
| Provider |----->|    Encounter    |<-----| Patient |
+----------+      +-----------------+      +---------+
                     |         ^                |
                     |         |                |
                     v         |                v
              +--------------+         +-------------+
              | Intervention |         | HealthState |
              +--------------+         +-------------+
```

## 3. Core Entities

### 3.1. `Patient`

*   **Economic Definition**: The primary consumer of healthcare services. Their "HealthState" is the core asset to be preserved or improved. They have preferences and behaviors (e.g., treatment adherence) that influence outcomes.
*   **System Role**: The central entity whose state the system aims to predict and stabilize. Unexpected changes in a patient's health or behavior are a primary source of "surprise."

| Attribute               | Data Type         | Description                                                               |
| ----------------------- | ----------------- | ------------------------------------------------------------------------- |
| `patient_id`            | `String`          | A unique, anonymized identifier for the patient.                          |
| `demographics`          | `Object`          | Age, sex, and other relevant demographic data for risk stratification.    |
| `health_state_ref`      | `HealthState_Ref` | A reference to the patient's current, evolving `HealthState`.             |
| `care_plan_adherence`   | `ProbabilityDist` | The system's **belief** about the patient's likelihood to follow treatments.|
| `insurance_provider_id` | `String`          | Identifier for the patient's insurer, linking to payment models.          |

---

### 3.2. `Provider`

*   **Economic Definition**: The supplier of healthcare services (e.g., doctors, hospitals, clinics). They possess resources, expertise, and objectives (e.g., patient outcomes, efficiency).
*   **System Role**: An agent whose capacity and decisions are modeled to predict the availability and quality of care. A provider running out of a resource is a key "surprise."

| Attribute                 | Data Type         | Description                                                              |
| ------------------------- | ----------------- | ------------------------------------------------------------------------ |
| `provider_id`             | `String`          | A unique identifier for the provider (e.g., NPI).                        |
| `provider_type`           | `Enum`            | `HOSPITAL`, `CLINIC`, `INDIVIDUAL_PRACTITIONER`.                         |
| `specialization`          | `Array<String>`   | List of medical specializations (e.g., `Cardiology`, `Oncology`).        |
| `resource_capacity`       | `Object`          | The system's **belief** about available beds, staff, equipment, etc.     |
| `treatment_efficacy_model`| `Model`           | The system's **belief** about the effectiveness of this provider's care. |

---

### 3.3. `Encounter` (Observable Event)

*   **Economic Definition**: A specific interaction where a service is delivered by a `Provider` to a `Patient`. This is the observable "exchange" in the healthcare economy.
*   **System Role**: This is a primary **sensory input**. Encounters provide new data that confirms or refutes the system's predictions about disease progression and treatment effectiveness.

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

---

### 3.4. `Intervention`

*   **Economic Definition**: Represents a specific treatment, therapy, or medication that can be applied to alter a `HealthState`. It has associated costs and expected benefits (utility).
*   **System Role**: An "action" that can be taken. The system models the likely effect of an intervention to decide on the best course of action to minimize future "surprise" (i.e., poor health outcomes).

| Attribute               | Data Type         | Description                                                              |
| ----------------------- | ----------------- | ------------------------------------------------------------------------ |
| `intervention_id`       | `String`          | Unique ID for the intervention (e.g., RxNorm for drugs).                 |
| `intervention_type`     | `Enum`            | `MEDICATION`, `PHYSICAL_THERAPY`, `SURGICAL_PROCEDURE`, `DIAGNOSTIC`.    |
| `cost_model`            | `Model`           | A model of the financial cost of the intervention.                       |
| `expected_efficacy_model`| `Model`           | The system's **belief** about the intervention's effectiveness on a `HealthState`.|
| `known_side_effects`    | `Array<String>`   | A list of potential adverse effects.                                     |

---

### 3.5. `HealthState`

*   **Economic Definition**: This represents the central "asset" of value in the healthcare economy. It is a complex, evolving state that services aim to improve or maintain.
*   **System Role**: This is the core belief state that the system tries to model and predict. Any deviation from the predicted trajectory of the `HealthState` is a significant "surprise."

| Attribute         | Data Type      | Description                                                              |
| ----------------- | -------------- | ------------------------------------------------------------------------ |
| `state_id`        | `String`       | A unique ID for this snapshot of the patient's health, linked to a patient. |
| `timestamp`       | `DateTime`     | The time this health state was recorded or inferred.                     |
| `vital_signs`     | `TimeSeries`   | Time-series data of vital signs (heart rate, blood pressure, etc.).      |
| `diagnoses`       | `Array<String>`| A list of active diagnoses (e.g., ICD-10 codes).                         |
| `prognosis_model` | `Model`        | The system's **belief** about the future evolution of this health state.   |
| `quality_of_life` | `Float`        | A score representing the system's belief about the patient's QoL.        |
