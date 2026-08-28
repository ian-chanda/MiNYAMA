# Justification: Graph-Rendered Belief State for Active Inference

## Purpose

This document justifies why the agriculture sector data was restructured from tabular (`.md`/`.csv`) form into a **JSON graph** (`agriculture_graph.json`) as the *most accurate* representation for the MiNYAMA active-inference agent. It is the machine-readable "Blueprint" counterpart the agent can actually consume.

## 1. What the agent natively operates on

The repository's only concrete agent implementation is `WorldModel` in `models/prediction_engines/world_model.py`. Its own docstring and code state the requirement directly:

- *"maintains a **generative model** of the environment, represented as a **graph**"* (`world_model.py:5-6`)
- It is initialized from a **system graph** and iterates over `self.system_graph.nodes` (`world_model.py:31`, `:37`)
- Its learning routine discusses *"modifying **edge weights** in the graph," "adding or removing **nodes/edges**"* (`world_model.py:97-100`)
- Prediction and surprise both key off the graph: `predict_future_state` mutates node state, and `update_model` recomputes beliefs from a `surprise_score` produced by `surprise_calculator.calculate_realized_surprise(predicted_state, actual_state)` (`world_model.py:132`)

**Conclusion:** the accurate substrate for this agent is a **property graph** (nodes + typed, weighted edges + node-local belief attributes) — *not* isolated CSV tables or markdown.

## 2. Why the previous format fell short

| Requirement of the agent | Previous form (`.md`/`.csv`) | Graph form |
| :--- | :--- | :--- |
| **Relations between entities** | ERD diagrams only existed as ASCII art; `_Ref` fields were bare ID strings with no cardinality/direction | `_Ref` relations become first-class **typed, weighted edges** (`planted_in`, `occupies`, `applied_to_zone`, `used_equipment`, `harvested_from`, `targets`, `alters`, `observes_*`, `records`) |
| **Beliefs amenable to surprise calculations** | Beliefs were prose (`"The system's **belief** about…"`) or `{...}` strings embedded in cells | Every `*_model`/`*_dist` is a **typed probability distribution** (`Normal`, `MultivariateNormal`, `Categorical`) with numeric `params` — directly consumable by a surprise calculator |
| **Typed attributes** | `Model`, `TimeSeries`, `ProbabilityDist`, `GeoJSON`, `GeoPoint` all flattened to the same string | Attributes carry explicit `type` + `value` + `unit`, and distinct composite types are preserved |
| **Observation vs. belief** | Indistinguishable in a plain table | `is_observation` flags separate **sensory input** (measured) from **belief** (predicted) nodes — the exact pairs a surprise computation compares |
| **Edge weights / priors** | Not representable | Every edge carries `weight` and a `prior` tag (`deterministic` vs `learned`) so the agent can update weights on surprise |

## 3. How this maps to the active-inference loop

The graph directly encodes the three operational requirements from `SYSTEM_DOCS.md`:

1. **Model the world** — every entity is a node carrying its *current belief distribution* (e.g., `Crop.yield_prediction` as a `Normal`; `Zone.soil` as a `MultivariateNormal`; `Equipment.operational_state` as a `Categorical`).
2. **Predict** — `WorldModel.predict_future_state` reads node beliefs and edges; e.g., an `Intervention` node's `targets`/`alters` edges and their weights define the transition the model simulates.
3. **Minimize surprise** — each `EnvironmentalData`/`Yield` node marked `is_observation: true` is the *actual*; the corresponding belief on a `Zone`/`Crop` is the *predicted*. `surprise_calculator` compares the two distributions; the resulting prediction error updates the connected belief nodes and edge weights (the `update_model` step).

## 4. The pilot and the propagation path

This pass implements the **agriculture pilot** only, mirroring `Zone_instances.csv`, `Crop_instances.csv`, `Yield_instances.csv` (2025 baseline + PENDING 2026 harvest), `Intervention_instances.csv`, `Equipment_instances.csv`, and `EnvironmentalData_instances.csv` into graph form. Once validated, the same generator/pattern extends to **manufacturing, education, finance, healthcare, retail**.

The layered relationship (Source-Sync Structural Hardening):

```
schemas/*/*.md        →  human-readable Blueprint (economic defs, system role)   [unchanged]
schemas/*/*.csv       →  parseable attribute tables + `<Entity>_instances.csv`    [reference data]
schemas/<sector>/*_graph.json →  machine-native belief graph for WorldModel        [new, agent substrate]
```

The graph file should be treated as the **single source of truth for the engine**; the `.md`/`.csv` remain the interpretable documentation layer. A `*_graph.json` is *not* intended to replace them.

## 5. Assumptions & choices

- **Deterministic vs learned edges:** edges known from the schema/ERD (`planted_in`, `occupies`, `applied_to_zone`, `used_equipment`, direct `harvested_from`) are `deterministic` (weight 1.0); causal/transition edges (`alters`, `targets`) that the agent should refine from data are `learned` with prior weights.
- **Historical grounding:** distinct 2025 `Crop` nodes were added so past `Yield` observations attach to their true crop, and a `records` edge carries the seasonal prior into 2026 (weight = confidence transferred).
- **Distribution parameterization:** `Normal` (scalar), `MultivariateNormal` (vector), `Categorical` (mass) cover the schema's `ProbabilityDist`/`Model` uses; time-series/geospatial are captured as typed attribute values, not flattened.

## 6. Outstanding (future) work

- Wire `models/` stubs (`graph_representation.py`, `surprise_calculator.py`) to read this graph schema.
- Migrate `.csv`/`.md` entities for the remaining five sectors to graph form.
- Define a canonical edge-type vocabulary and weight-update rule across sectors.
