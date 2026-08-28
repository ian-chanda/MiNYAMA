# `Provider`

*Parent schema: [Healthcare Sector Schema](Healthcare_Sector_Schema.md)*

## Economic Definition

The supplier of healthcare services (e.g., doctors, hospitals, clinics). They possess resources, expertise, and objectives (e.g., patient outcomes, efficiency).

## System Role

An agent whose capacity and decisions are modeled to predict the availability and quality of care. A provider running out of a resource is a key "surprise."

## Table

| Attribute                 | Data Type         | Description                                                              |
| ------------------------- | ----------------- | ------------------------------------------------------------------------ |
| `provider_id`             | `String`          | A unique identifier for the provider (e.g., NPI).                        |
| `provider_type`           | `Enum`            | `HOSPITAL`, `CLINIC`, `INDIVIDUAL_PRACTITIONER`.                         |
| `specialization`          | `Array<String>`   | List of medical specializations (e.g., `Cardiology`, `Oncology`).        |
| `resource_capacity`       | `Object`          | The system's **belief** about available beds, staff, equipment, etc.     |
| `treatment_efficacy_model`| `Model`           | The system's **belief** about the effectiveness of this provider's care. |
