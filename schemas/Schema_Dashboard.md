# Dashboard: Operational Inference Schemas

This dashboard distills the complex sector schemas into actionable **Active Inference Profiles**. It serves as the bridge between the high-level Blueprint and the functional Models.

---

## ✦ Operational Profiles

Each sector is modeled as an agent striving to minimize **Surprise** (Prediction Error) by balancing its internal beliefs against sensory reality.

### 🟢 Agriculture
*   **Core Belief**: The predicted growth trajectory and final **Yield** of a **Crop** in a specific **Zone**.
*   **Sensory Inputs**: `EnvironmentalData` (Weather, Soil), `Equipment` telemetry, Satellite (NDVI).
*   **Actions**: Dispatch an **Intervention** (Irrigation, Fertilizer, Pest Control).
*   👉 **[Blueprint](agriculture/Agriculture_Sector_Schema.md)** | **[Extensions](agriculture/README.md)**

### 📚 Education
*   **Core Belief**: A **Learner's** current **MasteryState** across a graph of **KnowledgeConcepts**.
*   **Sensory Inputs**: `Assessment` results, `LearningInteraction` duration, quiz scores.
*   **Actions**: Recommend a **LearningResource** or trigger a mastery verification.
*   👉 **[Blueprint](education/Education_Sector_Schema.md)** | **[Extensions](education/README.md)**

### 💰 Finance
*   **Core Belief**: The "True" risk/value of **Assets** based on the predicted behavior of **EconomicAgents**.
*   **Sensory Inputs**: Market `Transactions`, news `Signals`, regulatory filings.
*   **Actions**: Execute trades or adjust reserve requirements to minimize systemic risk.
*   👉 **[Blueprint](finance/Finance_Sector_Schema.md)** | **[Extensions](finance/README.md)**

### 🏥 Healthcare
*   **Core Belief**: A **Patient's** evolving **HealthState** and prognostic trajectory.
*   **Sensory Inputs**: Clinical `Encounters`, vital signs, lab assessments.
*   **Actions**: Prescribe an **Intervention** (Treatment, Medication) to stabilize the health path.
*   👉 **[Blueprint](healthcare/Healthcare_Sector_Schema.md)** | **[Extensions](healthcare/README.md)**

### 🏭 Manufacturing
*   **Core Belief**: The operational health of **PhysicalAssets** and the flow of **Materials**.
*   **Sensory Inputs**: Asset telemetry, `WorkOrder` status, quality control checks.
*   **Actions**: Initiate a `WorkOrder` or schedule preventative maintenance.
*   👉 **[Blueprint](manufacturing/Manufacturing_Sector_Schema.md)** | **[Extensions](manufacturing/README.md)**

### 🛒 Retail
*   **Core Belief**: Future customer **DemandForecast** and the precise state of **InventoryItems**.
*   **Sensory Inputs**: `CustomerInteractions` (clicks/views), completed `Transactions`.
*   **Actions**: Adjust pricing, trigger restocking, or launch targeted promotions.
*   👉 **[Blueprint](retail/Retail_Sector_Schema.md)** | **[Extensions](retail/README.md)**

---

## 🛠 Usage for Modelers
1.  **Select a Sector**: Identify the "Core Belief" you intend to model.
2.  **Map Inputs**: Ensure the data in `evidence/` matches the "Sensory Inputs" defined here.
3.  **Define Surprise**: Determine what constitutes a "Surprise".
4.  **Action Sync**: Align the `interventions/` layer with the "Potential Actions".
5.  **Hardening**: Use the **[Extensions](README.md)** layer to document project-specific priors before moving to Phase 2.

---

## 📂 Detailed Schema Mapping

| Sector | Technical Blueprint | User Extensions |
| :--- | :--- | :--- |
| **Agriculture** | [Agriculture_Sector_Schema.md](agriculture/Agriculture_Sector_Schema.md) | [agriculture/README.md](agriculture/README.md) |
| **Education** | [Education_Sector_Schema.md](education/Education_Sector_Schema.md) | [education/README.md](education/README.md) |
| **Finance** | [Finance_Sector_Schema.md](finance/Finance_Sector_Schema.md) | [finance/README.md](finance/README.md) |
| **Healthcare** | [Healthcare_Sector_Schema.md](healthcare/Healthcare_Sector_Schema.md) | [healthcare/README.md](healthcare/README.md) |
| **Manufacturing** | [Manufacturing_Sector_Schema.md](manufacturing/Manufacturing_Sector_Schema.md) | [manufacturing/README.md](manufacturing/README.md) |
| **Retail** | [Retail_Sector_Schema.md](retail/Retail_Sector_Schema.md) | [retail/README.md](retail/README.md) |
