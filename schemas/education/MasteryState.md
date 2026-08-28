# `MasteryState`

*Parent schema: [Education Sector Schema](Education_Sector_Schema.md)*

## Economic Definition

Represents the learner's current "human capital"—their demonstrated level of understanding across all `KnowledgeConcepts`. This is the core "asset" being developed.

## System Role

The central **belief state** that the system tries to model. The system's primary goal is to guide actions (recommendations) that will lead to a positive evolution of this state.

## Table

| Attribute          | Data Type                        | Description                                                               |
| ------------------ | -------------------------------- | ------------------------------------------------------------------------- |
| `mastery_id`       | `String`                         | A unique ID for this instance of the learner's knowledge state.           |
| `learner_id`       | `Learner_Ref`                    | The learner this state belongs to.                                        |
| `knowledge_map`    | `Map<Concept_Ref, Mastery_Level>`| A map where each concept is assigned a **belief** about its mastery level.  |
| `mastery_level`    | `Enum`                           | `NOT_SEEN`, `INTRODUCED`, `PRACTICING`, `MASTERED`.                       |
| `confidence_model` | `Model`                          | The system's confidence in its own assessment of the learner's mastery.   |
