# Phase 6: The Integrity Layer (Contracts & Governance)

The **Integrity Layer** is the core synchronization engine of the MiNYAMA framework. It ensures that the "Source of Truth" (Phase 1: Schemas) is correctly propagated through the "Mechanical Sync" (Phase 2: Models) and validated against the "Sensory Input" (Phase 3: Evidence) to produce "Hardened Insights" (Phase 5: Reports).

## 1. Purpose & Philosophy

In an ontology-driven system, documentation is not passive; it is an active constraint on system behavior. The Integrity Layer prevents **Document Drift**—the divergence between theoretical models and empirical reality.

### Synchronization Principle
Every artifact in the repository (model, data record, or report) must be traceable to a specific version of a Schema. If a Schema changes, the Integrity Layer flags all downstream dependencies as "unverified" until they are re-synchronized and re-hardened.

### Hardening Lifecycle
Hardening is the process of moving from a skeletal template to a verified, evidence-backed analytical deliverable. The Integrity Layer provides the rules and specs for this transition.

---

## 2. Layer Components

### 🟢 [Schema Sync Rules](schema_sync_rules/)
Machine-readable `.yaml` files that define the mandatory structure for each sector. They act as the "Technical Contract" that models and reports must sign.

### 🟡 [Validation Specs](validation_specs/)
The grading criteria for repository content.
*   **[Hardening Levels](validation_specs/report_hardening_levels.md)**: The 5-stage progression from template to verified insight.
*   **[Evidence Requirements](validation_specs/evidence_requirements.md)**: Standards for observational data and truth tensors.
*   **[Intervention Validation](validation_specs/intervention_validation.md)**: The audit lifecycle for active projects.

### 🟡 [Semantic Interfaces](semantic_interfaces/)
The programmatic and structural bridges.
*   **[Model Contracts](semantic_interfaces/model_contracts.py)**: Python API for enforcing schema-driven class structures.
*   **[Report Contracts](semantic_interfaces/report_contracts.md)**: Markdown standards for analytical compliance.

### 🔴 [Drift Detection](drift_detection/)
The automated audit system.
*   **[Schema Hashes](drift_detection/schema_hashes.json)**: Integrity fingerprints for the Phase 1 blueprints.
*   **[Dependency Map](drift_detection/dependency_map.json)**: The relationship graph used for impact analysis.

---

## 3. Glossary of Terms

*   **Beliefs**: The internal state of the model (priors) before new evidence is introduced.
*   **Observations**: Raw sensory input collected from the environment (Phase 3).
*   **Surprise**: The calculated prediction error (The Delta) between Beliefs and Observations.
*   **Model Update**: The iterative process of adjusting Beliefs to minimize future Surprise.
*   **Intervention**: An active change (Phase 4) performed by the system to influence the world model.
*   **Synchronization**: The act of ensuring code and reports match the current Schema version.
*   **Hardening**: The progressive refinement of documentation from skeletal to verified status.

---

## 4. Contributor Expectations

1.  **Schema First**: Never create a model or report without identifying its parent schema in `schemas/`.
2.  **Contract Compliance**: Ensure your report headers and model docstrings match the rules in `contracts/schema_sync_rules/`.
3.  **Audit Awareness**: Before committing, check `contracts/drift_detection/dependency_map.json` to see if your changes trigger a re-hardening requirement in other folders.
