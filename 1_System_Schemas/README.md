# Formalized Schema Representations

This document provides a high-level overview of the core entities and their economic and active inference roles for six key economic sectors. This schema forms the foundation of an active inference system operating in these domains, enabling it to build a world model, predict events, and act to minimize "surprise."

---

# 1. Finance Sector

### The EconomicAgent Entity
*   **Economic Definition**: Represents any actor within the financial ecosystem (e.g., banks, funds, regulators). They are decision-makers whose collective behavior creates the market.
*   **Active Inference Role**: The system models agents to predict their behavior. An unexpected action by a major agent is a significant source of "surprise."
*   **Data Schema Attributes**: `agent_id`, `agent_type`, `risk_profile`, `liquidity_preference`, `capital_reserves`, `known_holdings`.

### The Asset Entity
*   **Economic Definition**: An instrument of value that can be owned and traded (e.g., stocks, bonds).
*   **Active Inference Role**: The system models the "true" value of assets to predict price movements. The difference between predicted and observed price is a core "surprise."
*   **Data Schema Attributes**: `asset_id`, `asset_class`, `issuer_id`, `valuation_model`, `price_history`, `volatility_model`, `liquidity_depth`.

### The Transaction Entity
*   **Economic Definition**: An executed trade or exchange of assets between agents, representing the "heartbeat" of the market.
*   **Active Inference Role**: The primary sensory input. The stream of transactions confirms or refutes predictions about agent behavior and asset valuation.
*   **Data Schema Attributes**: `transaction_id`, `involved_agents`, `exchanged_assets`, `price`, `timestamp`, `venue_id`, `settlement_status`.

### The Market Entity
*   **Economic Definition**: A venue where assets are traded, with rules governing interaction and price discovery.
*   **Active Inference Role**: The system models the market's microstructure to understand how its actions will impact prices. A rule change is a structural "surprise."
*   **Data Schema Attributes**: `market_id`, `market_type`, `trading_hours`, `rules_engine`, `order_book`.

---

# 2. Healthcare Sector

### The Patient Entity
*   **Economic Definition**: The consumer of healthcare services, whose "HealthState" is the core asset to be improved.
*   **Active Inference Role**: The central agent whose health trajectory the system aims to predict. Unexpected health changes are the primary "surprise."
*   **Data Schema Attributes**: `patient_id`, `demographics`, `health_state_ref`, `care_plan_adherence`, `insurance_provider_id`.

### The Provider Entity
*   **Economic Definition**: The supplier of healthcare services (e.g., doctors, hospitals).
*   **Active Inference Role**: An agent whose capacity and decisions are modeled to predict care availability. A resource shortage is a key "surprise."
*   **Data Schema Attributes**: `provider_id`, `provider_type`, `specialization`, `resource_capacity`, `treatment_efficacy_model`.

### The Encounter Entity
*   **Economic Definition**: A specific interaction where a service is delivered by a `Provider` to a `Patient`.
*   **Active Inference Role**: A primary sensory input, providing data that confirms or refutes predictions about disease progression and treatment effectiveness.
*   **Data Schema Attributes**: `encounter_id`, `patient_id`, `provider_id`, `encounter_type`, `timestamp`, `observations`, `prescribed_interventions`.

### The Intervention Entity
*   **Economic Definition**: A specific treatment, therapy, or medication that can alter a `HealthState`.
*   **Active Inference Role**: An "action" the system can recommend. The system models the likely effect of an intervention to choose the best course of action.
*   **Data Schema Attributes**: `intervention_id`, `intervention_type`, `cost_model`, `expected_efficacy_model`, `known_side_effects`.

### The HealthState Entity
*   **Economic Definition**: The central "asset" of value, representing the patient's overall health.
*   **Active Inference Role**: The core belief state the system tries to model and predict. Any deviation from the predicted trajectory is a significant "surprise."
*   **Data Schema Attributes**: `state_id`, `timestamp`, `vital_signs`, `diagnoses`, `prognosis_model`, `quality_of_life`.

---

# 3. Manufacturing Sector

### The PhysicalAsset Entity
*   **Economic Definition**: The capital equipment that performs work (e.g., machines, robots). Their operational state determines production capacity.
*   **Active Inference Role**: Agents that act upon materials. An unexpected breakdown is a critical "surprise."
*   **Data Schema Attributes**: `asset_id`, `asset_type`, `operational_state`, `maintenance_model`, `throughput_capacity`, `telemetry_feed`.

### The Material Entity
*   **Economic Definition**: The physical goods at any stage of production, from raw inputs to finished products.
*   **Active Inference Role**: The object being acted upon. The system tracks its state and location. A shortage or quality failure is a major "surprise."
*   **Data Schema Attributes**: `material_id`, `material_type`, `specifications`, `quantity`, `location`, `quality_status`.

### The WorkOrder Entity
*   **Economic Definition**: A command to execute a production run, representing a discrete unit of value creation.
*   **Active Inference Role**: A primary "action" initiated by the system. A deviation from the `expected_duration` is a "surprise" to be minimized.
*   **Data Schema Attributes**: `order_id`, `product_to_produce`, `quantity_required`, `input_materials`, `assigned_assets`, `status`, `expected_duration`.

### The Process Entity
*   **Economic Definition**: The "recipe" or standard operating procedure for manufacturing a product.
*   **Active Inference Role**: A core part of the system's belief model, defining the expected sequence of events for a `WorkOrder`.
*   **Data Schema Attributes**: `process_id`, `process_name`, `steps`, `quality_checkpoints`.

### The SupplyChainLink Entity
*   **Economic Definition**: The relationship with an external supplier for sourcing raw materials.
*   **Active Inference Role**: Models an external, partially observable part of the world. A delivery failure is a major external "surprise."
*   **Data Schema Attributes**: `link_id`, `supplier_id`, `supplied_material`, `lead_time_model`, `reliability_score`, `cost_per_unit`.

---

# 4. Retail Sector

### The Customer Entity
*   **Economic Definition**: The demand side of the retail economy, making decisions based on price, preference, and value.
*   **Active Inference Role**: The primary agent whose purchasing behavior the system seeks to predict.
*   **Data Schema Attributes**: `customer_id`, `demographics`, `purchase_history`, `loyalty_status`, `propensity_to_buy_model`.

### The Product Entity
*   **Economic Definition**: The good or service being sold.
*   **Active Inference Role**: A static entity whose tangible instances (`InventoryItems`) must be managed to meet predicted demand.
*   **Data Schema Attributes**: `product_id`, `description`, `category`, `price`, `cost_of_goods_sold`, `supplier_id`.

### The InventoryItem Entity
*   **Economic Definition**: A tangible, countable instance of a `Product` at a specific location.
*   **Active Inference Role**: The core belief state revolves around the quantity and location of these items. A stockout is a "surprise."
*   **Data Schema Attributes**: `inventory_id`, `product_id`, `location_id`, `quantity`, `status`.

### The CustomerInteraction Entity
*   **Economic Definition**: Any engagement a customer has with the retailer, representing signals of purchase intent.
*   **Active Inference Role**: A key sensory input used to update beliefs about customer intent. A cart abandonment is a "surprise."
*   **Data Schema Attributes**: `interaction_id`, `customer_id`, `channel`, `timestamp`, `interaction_type`, `outcome`.

### The DemandForecast Entity
*   **Economic Definition**: A prediction of future sales, which drives all operational decisions.
*   **Active Inference Role**: The system's core belief about the future. The difference between forecast and actual sales is the "surprise" the system learns from.
*   **Data Schema Attributes**: `forecast_id`, `product_id`, `time_horizon`, `predicted_sales_distribution`, `seasonality_model`.

---

# 5. Education Sector

### The Learner Entity
*   **Economic Definition**: The "consumer" of education, investing time to increase their human capital (knowledge).
*   **Active Inference Role**: The central agent whose learning trajectory the system aims to optimize. An unexpected test failure is a "surprise."
*   **Data Schema Attributes**: `learner_id`, `demographics`, `mastery_state_ref`, `learning_style_model`, `engagement_level_model`.

### The KnowledgeConcept Entity
*   **Economic Definition**: The fundamental unit of knowledge or skill to be learned.
*   **Active Inference Role**: Forms the nodes of a curriculum graph that the system guides the learner through.
*   **Data Schema Attributes**: `concept_id`, `description`, `dependency_graph`, `associated_resources`.

### The LearningResource Entity
*   **Economic Definition**: The "capital equipment" of education; the tools used to facilitate knowledge transfer (e.g., videos, quizzes).
*   **Active Inference Role**: An "action" or tool the system can recommend. The system learns the effectiveness of each resource.
*   **Data Schema Attributes**: `resource_id`, `resource_type`, `associated_concept`, `difficulty_level`, `efficacy_model`.

### The MasteryState Entity
*   **Economic Definition**: Represents the learner's current "human capital" or knowledge.
*   **Active Inference Role**: The central belief state the system tries to model. The goal is to guide actions that improve this state.
*   **Data Schema Attributes**: `mastery_id`, `learner_id`, `knowledge_map`, `mastery_level`, `confidence_model`.

### The Assessment Entity
*   **Economic Definition**: A formal measurement or "audit" of a learner's `MasteryState`.
*   **Active Inference Role**: A high-value sensory input. A large difference between predicted and actual score is a major "surprise."
*   **Data Schema Attributes**: `assessment_id`, `learner_id`, `assessed_concepts`, `predicted_score_dist`, `actual_score`.

---

# 6. Agriculture Sector

### The Zone Entity
*   **Economic Definition**: The primary unit of land management; the "factory floor" of the farm.
*   **Active Inference Role**: A core entity whose state (soil health, moisture) is monitored to predict productive capacity.
*   **Data Schema Attributes**: `zone_id`, `location_polygon`, `size_hectares`, `soil_model`, `moisture_model`, `current_crop_ref`.

### The Crop Entity
*   **Economic Definition**: The biological asset being cultivated, with a potential yield representing its economic value.
*   **Active Inference Role**: The central entity whose growth and health the system predicts and optimizes. A deviation from the predicted growth is a "surprise."
*   **Data Schema Attributes**: `crop_id`, `plant_type`, `genetics`, `growth_stage_model`, `health_state_model`, `yield_prediction_dist`.

### The Intervention Entity
*   **Economic Definition**: A management action (e.g., irrigation, fertilization) taken to influence crop yield.
*   **Active Inference Role**: An "action" chosen by the system to guide the `Crop` towards its optimal state and minimize future "surprise" (yield loss).
*   **Data Schema Attributes**: `intervention_id`, `timestamp`, `intervention_type`, `target_zone_ref`, `applied_materials`, `equipment_used_ref`.

### The EnvironmentalData Entity
*   **Economic Definition**: External, uncontrollable factors (e.g., weather) that represent a primary source of risk.
*   **Active Inference Role**: The primary source of sensory input about the external world. An unpredicted weather event is a major "surprise."
*   **Data Schema Attributes**: `data_id`, `timestamp`, `source`, `data_type`, `value`, `forecast_model`.

### The Yield Entity
*   **Economic Definition**: The realized output and economic value from the agricultural process.
*   **Active Inference Role**: The ultimate sensory observation. The difference between predicted and actual yield is the final "surprise" that drives learning.
*   **Data Schema Attributes**: `yield_id`, `crop_ref`, `harvest_timestamp`, `quantity_measured`, `quality_grade`.
