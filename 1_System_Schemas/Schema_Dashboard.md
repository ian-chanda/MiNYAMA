# Dashboard: Operational Inference Schemas

This document provides a high-level summary of the world model for each economic sector, framed from the perspective of an operationalized active inference agent. It distills each schema into its core **Beliefs**, **Sensory Inputs**, and potential **Actions**.

---

## High-Level Operational Models

For an active inference agent, the goal is to minimize "surprise" (the difference between its beliefs and what it senses). It does this by continuously updating its beliefs or by acting on the world to make reality match its predictions.

### Finance
-   **Core Belief**: The "true" value and risk of financial `Assets`, driven by the predicted behavior of `EconomicAgents`.
-   **Sensory Inputs**: `Transactions` from markets, `Signals` from news and filings.
-   **Potential Actions**: Execute trades (buy/sell `Assets`) to maximize value and minimize risk exposure.
-   **[[_Optics/Minyama/Minyama_System_Schemas/Finance_Sector_Schema|Details...]]**

### Healthcare
-   **Core Belief**: A `Patient's` evolving `HealthState` and prognosis based on their unique characteristics.
-   **Sensory Inputs**: `Encounters` (doctor visits, tests), vital signs from medical devices, `Assessment` results.
-   **Potential Actions**: Recommend or schedule a specific `Intervention` (treatment, test, medication) to improve the predicted `HealthState`.
-   **[[_Optics/Minyama/Minyama_System_Schemas/Healthcare_Sector_Schema|Details...]]**

### Manufacturing
-   **Core Belief**: The operational health and predictive maintenance needs of `PhysicalAssets` and the real-time status of `Materials` in the production line.
-   **Sensory Inputs**: Telemetry from `Equipment`, `WorkOrder` status updates, quality control pass/fail results.
-   **Potential Actions**: Initiate a `WorkOrder`, schedule maintenance for a `PhysicalAsset`, re-order `Materials` from a supplier.
-   **[[_Optics/Minyama/Minyama_System_Schemas/Manufacturing_Sector_Schema|Details...]]**

### Retail
-   **Core Belief**: The future customer demand for each `Product` and the precise state (`quantity`, `location`) of all `InventoryItems`.
-   **Sensory Inputs**: `CustomerInteractions` (clicks, searches, cart additions), completed `Transactions`.
-   **Potential Actions**: Adjust `Product` price, launch a promotion, trigger a new inventory order from a supplier, personalize a customer recommendation.
-   **[[_Optics/Minyama/Minyama_System_Schemas/Retail_Sector_Schema|Details...]]**

### Education
-   **Core Belief**: A `Learner's` current `MasteryState` across a graph of `KnowledgeConcepts`.
-   **Sensory Inputs**: `Assessment` results, `LearningInteraction` durations, submitted assignments, quiz scores.
-   **Potential Actions**: Recommend the next `LearningResource`, suggest a prerequisite `KnowledgeConcept`, or trigger a formal `Assessment` to verify mastery.
-   **[[_Optics/Minyama/Minyama_System_Schemas/Education_Sector_Schema|Details...]]**

### Agriculture
-   **Core Belief**: The predicted growth stage, health, and final `Yield` of a `Crop` within a specific `Zone`.
-   **Sensory Inputs**: `EnvironmentalData` (weather, soil moisture), satellite imagery (NDVI), telemetry from `Equipment`.
-   **Potential Actions**: Trigger an `Intervention` (e.g., irrigate a `Zone`, apply fertilizer, dispatch a pest-control drone).
-   **[[_Optics/Minyama/Minyama_System_Schemas/Agriculture_Sector_Schema|Details...]]**

---
## Detailed Schema Documents

For a full breakdown of the entities and attributes in each model, please refer to the detailed documents:

*   [[_Optics/Minyama/Minyama_System_Schemas/Finance_Sector_Schema]]
*   [[_Optics/Minyama/Minyama_System_Schemas/Healthcare_Sector_Schema]]
*   [[_Optics/Minyama/Minyama_System_Schemas/Manufacturing_Sector_Schema]]
*   [[_Optics/Minyama/Minyama_System_Schemas/Retail_Sector_Schema]]
*   [[_Optics/Minyama/Minyama_System_Schemas/Education_Sector_Schema]]
*   [[_Optics/Minyama/Minyama_System_Schemas/Agriculture_Sector_Schema]]
