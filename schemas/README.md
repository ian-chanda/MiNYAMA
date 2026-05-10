# Phase 1: The Blueprint (System Schemas)

This directory serves as the **Immutable Source** for the MiNYAMA system. It contains the formal definitions, ontologies, and entity-relationship models for each socio-economic sector.

## 🟢 Operational Summary
For a distilled view of the system's "Beliefs, Sensors, and Actions," see:
👉 **[Operational Schema Dashboard](Schema_Dashboard.md)**

## 📂 Sector Blueprints
Every model in this repository must descend from the technical schemas and user-defined layers found below:

1.  **Agriculture**: [Blueprint](agriculture/Agriculture_Sector_Schema.md) | [Extensions](agriculture/README.md)
2.  **Education**: [Blueprint](education/Education_Sector_Schema.md) | [Extensions](education/README.md)
3.  **Finance**: [Blueprint](finance/Finance_Sector_Schema.md) | [Extensions](finance/README.md)
4.  **Healthcare**: [Blueprint](healthcare/Healthcare_Sector_Schema.md) | [Extensions](healthcare/README.md)
5.  **Manufacturing**: [Manufacturing_Sector_Schema.md](manufacturing/Manufacturing_Sector_Schema.md) | [Extensions](manufacturing/README.md)
6.  **Retail**: [Retail_Sector_Schema.md](retail/Retail_Sector_Schema.md) | [Extensions](retail/README.md)

## 🛠 Structural Hardening Rules
*   **Source Authority**: No entity or attribute may be used in the `models/` or `reports/` that is not first defined here.
*   **Consistency**: If a schema is updated, a "Sync Audit" must be triggered in the `contracts/` layer to update the corresponding models.
