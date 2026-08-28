# `LearningResource`

*Parent schema: [Education Sector Schema](Education_Sector_Schema.md)*

## Economic Definition

The "capital equipment" of education; the tools and materials used to facilitate knowledge transfer (e.g., videos, articles, quizzes, simulations).

## System Role

An "action" or tool the system can recommend to a learner. The system continuously updates its belief about the effectiveness of each resource to make better recommendations.

## Table

| Attribute         | Data Type     | Description                                                               |
| ----------------- | ------------- | ------------------------------------------------------------------------- |
| `resource_id`     | `String`      | A unique identifier for the learning asset.                               |
| `resource_type`   | `Enum`        | `VIDEO`, `TEXT`, `INTERACTIVE_SIMULATION`, `ASSESSMENT`.                  |
| `associated_concept`| `Concept_Ref` | The primary `KnowledgeConcept` this resource is designed to teach.        |
| `difficulty_level`| `Float`       | The system's **belief** about the difficulty of this resource.            |
| `efficacy_model`  | `Model`       | The system's **belief** about how effective this resource is at improving mastery. |
