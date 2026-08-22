# README: Consumer Resource Systems (RISC-based Priors)

## 1. Operational Context
In the MiNYAMA framework, **Consumer Resources** (Water, Food, Public Goods) are modeled as high-volatility flows. Because these systems impact human survival directly, we use a **RISC (Reduced Instruction Set Computer)** approach for priors: focusing on a small set of highly optimized analytical primitives rather than monolithic simulations.

## 2. Measurement Philosophy: Flow vs. Stock
We do not believe in static "Reserves." We model resources as **Dynamic Flows** where the primary prior is the **Depletion Rate**.

### Core Primitives for Priors
1.  **`Measure_Flow(source, sink)`**: Establishes the expected rate of replenishment (e.g., liters/sec from a reservoir).
2.  **`Calculate_PerCapita(resource, population)`**: Defines the baseline equity assumption.
3.  **`Time_To_Depletion(stockpile, rate)`**: The "Critical Surprise" indicator. If observations show a faster depletion than this prior, an intervention is triggered immediately.

## 3. Systemic Pressure Indicators
Our baseline assumptions for consumer resources include:
*   **Access Thresholds**: The minimum per-capita requirement before "Societal Surprise" (unrest/failure) occurs.
*   **Dependency Mapping**: Identifying "Single Points of Failure" in the supply chain. A prior that assumes multiple sources but observes only one creates a high-severity drift event.

## 4. Relationship to Active Inference
Consumer Resource priors provide the "Normal Heartbeat" of the city. Any deviation in `Measure_Flow` recorded in `observations/` generates a Prediction Error that forces the system to either:
1.  **Adjust Beliefs**: Accept that the resource is scarcer than previously thought.
2.  **Trigger Intervention**: Activate Phase 4 projects (e.g., infrastructure updates) to restore the flow.
