# Minyama Active Inference Model: Analysis Template

## From CISC to RISC for World Modeling

The "CISC" (Complex Instruction Set Computer) approach to modeling systems involves creating a comprehensive, high-fidelity simulation of the entire environment. While thorough, this method is often too slow and computationally expensive for real-time adaptation and surprise minimization.

To build an effective **Active Inference World Model**, we adopt a "RISC" (Reduced Instruction Set Computer) framework. This approach focuses on a small set of highly optimized analytical primitives that define the core components of our data model. These primitives are the foundational building blocks for creating a lean, fast, and adaptable world model.

### Core RISC Primitives for the Active Inference Data Model

These primitives are designed for the rapid construction and analysis of a graph-based world model, enabling the system to efficiently calculate and minimize surprise.

1.  **`Define_SystemGraph(nodes, edges)`**
    *   **Description:** Defines the fundamental structure of the world model as a network of nodes (entities, concepts, actors) and edges (relationships, dependencies, flows). This aligns with the Minyama **Network View** principle.
    *   **Implementation:** See `src/data_model/graph_representation.py`.
    *   **Examples:**
        *   `Define_SystemGraph(nodes=['Factory_A', 'Town_B'], edges=[('Factory_A', 'employs_workers_from', 'Town_B')])`
        *   `Define_SystemGraph(nodes=['Water_Source', 'Community'], edges=[('Water_Source', 'supplies', 'Community')])`

2.  **`Model_HumanState(human_node, state_tensor)`**
    *   **Description:** Models the internal state of human actors within the system. This primitive treats humans not as external variables but as critical sensors and agents whose states (e.g., cognitive load, readiness, sentiment) are vital for accurate predictions. This directly implements the **Human-in-the-Loop** principle.
    *   **Implementation:** See `src/data_model/human_state_tensors.py`.
    *   **Examples:**
        *   `Model_HumanState('Operator_1', {'cognitive_load': 0.8, 'situational_awareness': 0.9})`
        *   `Model_HumanState('Community_Rep_A', {'trust_in_system': 0.3, 'urgency_level': 0.7})`

3.  **`Quantify_Flows(source_node, sink_node, unit, cost)`**
    *   **Description:** Represents the movement of resources, value, or information between nodes in the graph. This primitive is crucial for understanding the costs associated with converting value from one form to another, as per the **Value Conversion** and **Extractive Logic** principles.
    *   **Implementation:** See `src/data_model/extraction_flows.py`.
    *   **Examples:**
        *   `Quantify_Flows('Mine_X', 'Smelter_Y', 'tons_per_hour', 'energy_cost_per_ton')`
        *   `Quantify_Flows('Data_API', 'Analytics_Dashboard', 'requests_per_second', 'compute_cost_per_request')`

4.  **`Establish_Baseline(system_graph, time_window)`**
    *   **Description:** Establishes the expected "heartbeat" or normal operational rhythm of the system. This baseline model is essential for detecting "null events"—the absence of an expected action or flow—which can be as significant a source of surprise as an unexpected event. This is the core of the **Baseline Establishment** principle.
    *   **Implementation:** See `src/data_model/baseline_model.py`.
    *   **Examples:**
        *   `Establish_Baseline('power_grid_graph', '24_hours')` -> `{'peak_demand_window': [1700, 2000], 'avg_flow': 500_MW}`
        *   `Establish_Baseline('logistics_network_graph', '7_days')` -> `{'expected_shipments_per_day': 150}`

### Application for Minimizing Surprise

This RISC-based data model allows the inference engine to perform rapid, targeted analysis. To predict system states and calculate surprise, the engine would:

1.  Use **`Define_SystemGraph`** to structure the incoming sensory data.
2.  Incorporate **`Model_HumanState`** to enrich the graph with internal human context.
3.  Apply **`Quantify_Flows`** to understand the dynamics of value and resource movement.
4.  Continuously compare the live system against the output of **`Establish_Baseline`**.
5.  Feed any delta (discrepancy) between the live data and the baseline into the **`surprise_calculator.py`** to quantify the prediction error.

This method provides a structured and efficient pathway to building a world model that can learn and adapt, fulfilling the core objective of an Active Inference system: to minimize surprise.
