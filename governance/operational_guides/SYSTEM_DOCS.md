# MiNYAMA: System Methodology & Architecture

## 1. Project Status
**Current Phase:** Initial Development (Skeletal)
The core modeling framework is being built, and the sectoral schemas are being defined. We are currently moving from "Empty Engine" files to "Functional" simulation environments.

## 2. Core Concepts: Active Inference
The methodology is centered around **Active Inference**, a theoretical framework from computational neuroscience. In this context, the "system" (e.g., a city or region) is treated as an agent that actively seeks to maintain its own stability and order.

### 2.1. Modeling the World
Building an internal "world model" based on incoming data (priors). The system maintains a "belief state" about crop health, market stability, or societal needs.

### 2.2. Minimizing Surprise
Insight is not simply "new information." Insight is the **reduction of surprise**—the delta between what we expected to happen and what actually happened. The system constantly makes predictions and updates its model to minimize this "surprise" (prediction error).

## 3. Framework: Source-Sync Structural Hardening (SSSH)
MiNYAMA treats information as an orchestration of multiple, often conflicting, layers:

*   **The Blueprint (Hard Constraints):** The formal requirements in `schemas/`. This is non-negotiable.
*   **The Raw Evidence (Material Layer):** The raw data and CLI outputs in `evidence/`. This is the "reality" of the system.
*   **The Narrative Intent (Personal Layer):** The analytical interpretation in `reports/`.

The system "hardens" documentation in stages:
1.  **Skeletal**: Mapping headers to requirements.
2.  **Functional**: Slotting in data and tables.
3.  **Semantic**: Elevating tone from descriptive to analytical professional justification.

## 4. Usage & Tooling
The entire system is designed to be managed as a knowledge base.
*   **Primary Tool:** [Obsidian](https://obsidian.md/) is the recommended tool for navigating and editing the project's content due to its powerful internal linking and graph visualization.
*   **Interaction:** Modify **Schemas** to change the world-view; run the **Model** to update beliefs; review **Reports** to extract insights.

## 5. Contributing
Contribution guidelines will be provided as the project matures. For now, feel free to open issues to provide feedback or suggestions.
