# `KnowledgeConcept`

*Parent schema: [Education Sector Schema](Education_Sector_Schema.md)*

## Economic Definition

The fundamental unit of knowledge or skill to be learned (e.g., "Newton's First Law," "Verb Conjugation"). This is the intangible "good" being transferred.

## System Role

Forms the nodes of a curriculum graph. The system's goal is to guide the learner through this graph, ensuring prerequisite concepts are mastered before moving on.

## Table

| Attribute           | Data Type            | Description                                                               |
| ------------------- | -------------------- | ------------------------------------------------------------------------- |
| `concept_id`        | `String`             | A unique identifier for the unit of knowledge.                            |
| `description`       | `String`             | A summary of the concept.                                                 |
| `dependency_graph`  | `Array<Concept_Ref>` | A list of prerequisite `KnowledgeConcept`s that must be mastered first.   |
| `associated_resources`| `Array<Resource_Ref>`| A list of `LearningResource`s that teach this concept.                    |
