# `Assessment`

*Parent schema: [Education Sector Schema](Education_Sector_Schema.md)*

## Economic Definition

A formal measurement or "audit" of a learner's `MasteryState` for a given set of concepts. It is the primary mechanism for verifying the accumulation of human capital.

## System Role

A special, high-value `LearningInteraction`. A significant difference between the predicted score and the actual score is a major "surprise," triggering a strong update to the system's beliefs about the learner's `MasteryState` and the efficacy of the resources they used.

## Table

| Attribute                | Data Type               | Description                                                              |
| ------------------------ | ----------------------- | ------------------------------------------------------------------------ |
| `assessment_id`          | `String`                | A unique ID for this specific assessment instance.                       |
| `learner_id`             | `Learner_Ref`           | The learner taking the assessment.                                       |
| `assessed_concepts`      | `Array<Concept_Ref>`    | A list of the `KnowledgeConcept`s being tested.                          |
| `predicted_score_dist`   | `ProbabilityDist`       | The system's **prediction** of the learner's likely score.               |
| `actual_score`           | `Float`                 | The final score the learner achieved.                                    |
| `inferred_mastery_update`| `Map<Concept_Ref, Float>`| The calculated update to the `MasteryState` based on performance.        |
