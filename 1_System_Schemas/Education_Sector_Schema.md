# System Architecture: Education Sector World Model

## 1. Overview

This document outlines the baseline data architecture for an **Active Inference World Model** tailored to the Education sector. The system's primary objective is to minimize "surprise" by accurately modeling a learner's journey towards knowledge mastery. In this context, "surprise" refers to unpredicted learning outcomes, such as a student failing an assessment they were expected to pass, disengagement from a course, or the ineffectiveness of a particular teaching resource.

This architecture enables the system to maintain a "belief state" about a learner's knowledge, allowing it to personalize learning pathways, recommend resources, and identify at-risk students.

## 2. Entity Relationship Diagram

The following diagram illustrates the high-level relationships. A `Learner` possesses a `MasteryState` (their current knowledge). They engage in a `LearningInteraction` by using a `LearningResource` to understand a `KnowledgeConcept`. This interaction, particularly an `Assessment`, updates the system's belief about their `MasteryState`.

```
+---------+      +--------------------+      +------------------+
| Learner |----->| LearningInteraction|<-----| LearningResource |
+---------+      +--------------------+      +------------------+
      |                   |                         |
      |                   |                         |
      v                   v                         v
+-------------+      +------------+      +------------------+
| MasteryState|      | Assessment |      | KnowledgeConcept |
+-------------+      +------------+      +------------------+
```

## 3. Core Entities

### 3.1. `Learner`

*   **Economic Definition**: The "consumer" of education, investing their time to increase their human capital (knowledge and skills).
*   **System Role**: The central agent whose learning trajectory the system seeks to model and optimize. Unexpected changes in their engagement or performance are a primary source of "surprise."

| Attribute                 | Data Type         | Description                                                               |
| ------------------------- | ----------------- | ------------------------------------------------------------------------- |
| `learner_id`              | `String`          | A unique, anonymized identifier for the learner.                          |
| `demographics`            | `Object`          | Age, educational background, and other data for cohort analysis.          |
| `mastery_state_ref`       | `MasteryState_Ref`| A reference to the learner's current, evolving knowledge map.             |
| `learning_style_model`    | `Model`           | The system's **belief** about the learner's preferred modality (e.g., visual, kinesthetic). |
| `engagement_level_model`  | `Model`           | The system's **belief** about the learner's current level of engagement.  |

---

### 3.2. `KnowledgeConcept`

*   **Economic Definition**: The fundamental unit of knowledge or skill to be learned (e.g., "Newton's First Law," "Verb Conjugation"). This is the intangible "good" being transferred.
*   **System Role**: Forms the nodes of a curriculum graph. The system's goal is to guide the learner through this graph, ensuring prerequisite concepts are mastered before moving on.

| Attribute           | Data Type            | Description                                                               |
| ------------------- | -------------------- | ------------------------------------------------------------------------- |
| `concept_id`        | `String`             | A unique identifier for the unit of knowledge.                            |
| `description`       | `String`             | A summary of the concept.                                                 |
| `dependency_graph`  | `Array<Concept_Ref>` | A list of prerequisite `KnowledgeConcept`s that must be mastered first.   |
| `associated_resources`| `Array<Resource_Ref>`| A list of `LearningResource`s that teach this concept.                    |

---

### 3.3. `LearningResource`

*   **Economic Definition**: The "capital equipment" of education; the tools and materials used to facilitate knowledge transfer (e.g., videos, articles, quizzes, simulations).
*   **System Role**: An "action" or tool the system can recommend to a learner. The system continuously updates its belief about the effectiveness of each resource to make better recommendations.

| Attribute         | Data Type     | Description                                                               |
| ----------------- | ------------- | ------------------------------------------------------------------------- |
| `resource_id`     | `String`      | A unique identifier for the learning asset.                               |
| `resource_type`   | `Enum`        | `VIDEO`, `TEXT`, `INTERACTIVE_SIMULATION`, `ASSESSMENT`.                  |
| `associated_concept`| `Concept_Ref` | The primary `KnowledgeConcept` this resource is designed to teach.        |
| `difficulty_level`| `Float`       | The system's **belief** about the difficulty of this resource.            |
| `efficacy_model`  | `Model`       | The system's **belief** about how effective this resource is at improving mastery. |

---

### 3.4. `LearningInteraction` (Observable Event)

*   **Economic Definition**: Any engagement a learner has with the educational system. Each interaction is an investment of the learner's time and attention in exchange for a potential increase in knowledge.
*   **System Role**: A key **sensory input**. The system observes these interactions to update its beliefs about learner engagement and mastery. Low interaction rates can be a "surprise" indicating disengagement.

| Attribute         | Data Type       | Description                                                               |
| ----------------- | --------------- | ------------------------------------------------------------------------- |
| `interaction_id`  | `String`        | A unique identifier for the event.                                        |
| `learner_id`      | `Learner_Ref`   | The learner who initiated the interaction.                                |
| `resource_id`     | `Resource_Ref`  | The `LearningResource` that was used.                                     |
| `timestamp`       | `DateTime`      | The time the interaction occurred.                                        |
| `interaction_type`| `Enum`          | `WATCH_VIDEO`, `READ_TEXT`, `TAKE_QUIZ`, `SUBMIT_ASSIGNMENT`.             |
| `duration`        | `Duration`      | The time spent on the interaction.                                        |
| `outcome`         | `Object`        | Data generated by the interaction (e.g., quiz score, submission content). |

---

### 3.5. `MasteryState`

*   **Economic Definition**: Represents the learner's current "human capital"—their demonstrated level of understanding across all `KnowledgeConcepts`. This is the core "asset" being developed.
*   **System Role**: The central **belief state** that the system tries to model. The system's primary goal is to guide actions (recommendations) that will lead to a positive evolution of this state.

| Attribute          | Data Type                        | Description                                                               |
| ------------------ | -------------------------------- | ------------------------------------------------------------------------- |
| `mastery_id`       | `String`                         | A unique ID for this instance of the learner's knowledge state.           |
| `learner_id`       | `Learner_Ref`                    | The learner this state belongs to.                                        |
| `knowledge_map`    | `Map<Concept_Ref, Mastery_Level>`| A map where each concept is assigned a **belief** about its mastery level.  |
| `mastery_level`    | `Enum`                           | `NOT_SEEN`, `INTRODUCED`, `PRACTICING`, `MASTERED`.                       |
| `confidence_model` | `Model`                          | The system's confidence in its own assessment of the learner's mastery.   |

---

### 3.6. `Assessment`

*   **Economic Definition**: A formal measurement or "audit" of a learner's `MasteryState` for a given set of concepts. It is the primary mechanism for verifying the accumulation of human capital.
*   **System Role**: A special, high-value `LearningInteraction`. A significant difference between the predicted score and the actual score is a major "surprise," triggering a strong update to the system's beliefs about the learner's `MasteryState` and the efficacy of the resources they used.

| Attribute                | Data Type               | Description                                                              |
| ------------------------ | ----------------------- | ------------------------------------------------------------------------ |
| `assessment_id`          | `String`                | A unique ID for this specific assessment instance.                       |
| `learner_id`             | `Learner_Ref`           | The learner taking the assessment.                                       |
| `assessed_concepts`      | `Array<Concept_Ref>`    | A list of the `KnowledgeConcept`s being tested.                          |
| `predicted_score_dist`   | `ProbabilityDist`       | The system's **prediction** of the learner's likely score.               |
| `actual_score`           | `Float`                 | The final score the learner achieved.                                    |
| `inferred_mastery_update`| `Map<Concept_Ref, Float>`| The calculated update to the `MasteryState` based on performance.        |
