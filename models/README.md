# Phase 2: The Engine (Active Inference Models)

This directory contains the **Mechanical Sync** layer. It translates the theoretical blueprints from `schemas/` into executable Python code for simulation and analysis.

## 🟡 Engine Components

### 1. [Baseline Models](baseline_models/)
Static representations of the system entities (Zones, Crops, Banks, Schools) as defined in the schemas. These models hold the "Belief State" of the system.

### 2. [Prediction Engines](prediction_engines/)
The core Active Inference logic.
*   **Surprise Calculator**: Measures the delta between predicted outcomes and observed reality.
*   **World Model**: Updates the system's beliefs based on incoming evidence.

### 3. [Extraction Flows](extraction_flows/)
Data pipelines that pull information from raw evidence and format it for the models.

## 🛠 Operational Standard
Every script in this directory must include a **Semantic Contract** in its header, linking it back to its parent schema in `schemas/`.
