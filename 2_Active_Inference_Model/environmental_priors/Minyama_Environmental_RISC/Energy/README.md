# README: Energy Sector - A RISC-based Minyama Analysis

## From CISC to RISC for Energy Systems

The prior "CISC" architecture attempted to model the entire socio-technical energy system in one complex instruction. This is powerful but slow. For rapid, targeted insights in the energy sector, we adopt a "RISC" (Reduced Instruction Set Computer) approach.

Instead of a single, holistic `world_model`, we use a set of simple, fast, and composable analytical primitives. These are our "Reduced Instructions."

### Core RISC Primitives for Energy

These primitives are designed for high-speed analysis of energy grids, generation facilities, and resource flows.

1.  **`Measure_Flow(source, sink, unit)`**
    *   **Description:** Measures the real-time or historical rate of energy transfer between two points.
    *   **Examples:**
        *   `Measure_Flow(substation_A, substation_B, MWh)`
        *   `Measure_Flow(gas_pipeline_input, power_plant_intake, cubic_meters_per_hour)`
        *   `Measure_Flow(solar_farm, battery_storage, kW)`

2.  **`Calculate_Efficiency(input_node, output_node)`**
    *   **Description:** Calculates the energy conversion efficiency of a single process or component. It is the fundamental unit of performance.
    *   **Examples:**
        *   `Calculate_Efficiency(coal_input_BTU, turbine_output_MWh)`
        *   `Calculate_Efficiency(battery_charge_kWh, battery_discharge_kWh)`

3.  **`Identify_Constraint(node, metric)`**
    *   **Description:** Rapidly identifies the primary bottleneck for a specific component based on a single metric.
    *   **Examples:**
        *   `Identify_Constraint(transmission_line_X, thermal_capacity_MW)`
        *   `Identify_Constraint(hydro_dam_Y, reservoir_level_meters)`

4.  **`Project_State(node, rate, time_horizon)`**
    *   **Description:** A simple linear projection of a resource state into the future based on a current rate.
    *   **Examples:**
        *   `Project_State(uranium_stockpile, consumption_rate_kg_day, 365_days)`
        *   `Project_State(battery_storage_charge, discharge_rate_MW, 4_hours)`

### Application for Future Deep Dives

By composing these simple "instructions," we can build complex queries about the energy system without needing a complete, unified model. For example, to analyze grid stability, we could:

1.  Use `Measure_Flow` on all major transmission lines.
2.  Use `Identify_Constraint` on the lines showing the highest flow.
3.  Use `Calculate_Efficiency` on the power plants supplying those lines.
4.  Use `Project_State` on the fuel reserves for those plants.

This approach favors speed, modularity, and rapid, iterative analysis over monolithic, slow-moving comprehension.