# README: Energy Sector Systems (RISC-based Priors)

## 1. Energy as a Foundational Prior
In MiNYAMA, **Energy** is the "Master Constraint." Stability in the Agriculture, Manufacturing, and Retail sectors depends entirely on the stability of the Energy Prior. If the energy grid is unstable, all downstream prediction errors are likely cascading effects of energy failure.

## 2. Infrastructure Dependency Logic
Energy priors are modeled as a **Dependency Graph**. We assume:
*   **Grid Resilience**: A prior belief that the grid can handle a specific load variance.
*   **Volatility Expectations**: Seasonal and daily fluctuations in power generation (e.g., Solar drops at 18:00; Hydro drops in the dry season).

## 3. RISC Primitives for Energy
To ensure rapid inference, we use these optimized primitives:
1.  **`Identify_Constraint(node, metric)`**: Quickly finds the bottleneck (e.g., a specific substation's thermal limit).
2.  **`Calculate_Efficiency(input, output)`**: The performance prior. A drop in observed efficiency vs. this prior indicates hardware degradation.
3.  **`Project_State(node, rate, horizon)`**: Predicting future stability.

## 4. Surprise Generation
Energy instability generates "Surprise" in two ways:
*   **Direct Surprise**: The observed MWh flow is lower than the `Measure_Flow` prior.
*   **Cascading Surprise**: A power failure in `interventions/` leads to a yield failure in `reports/`.

The Energy Prior is the "Anchor" of the repository's adaptive intelligence. If the energy baseline is unverified, no Level 5 (Verified) reports can be produced for industrial sectors.
