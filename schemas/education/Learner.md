# `Learner`

*Parent schema: [Education Sector Schema](Education_Sector_Schema.md)*

## Economic Definition

The "consumer" of education, investing their time to increase their human capital (knowledge and skills).

## System Role

The central agent whose learning trajectory the system seeks to model and optimize. Unexpected changes in their engagement or performance are a primary source of "surprise."

## Table

| Attribute                 | Data Type         | Description                                                               |
| ------------------------- | ----------------- | ------------------------------------------------------------------------- |
| `learner_id`              | `String`          | A unique, anonymized identifier for the learner.                          |
| `demographics`            | `Object`          | Age, educational background, and other data for cohort analysis.          |
| `mastery_state_ref`       | `MasteryState_Ref`| A reference to the learner's current, evolving knowledge map.             |
| `learning_style_model`    | `Model`           | The system's **belief** about the learner's preferred modality (e.g., visual, kinesthetic). |
| `engagement_level_model`  | `Model`           | The system's **belief** about the learner's current level of engagement.  |
