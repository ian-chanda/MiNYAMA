# `Transaction` (Observable Event)

*Parent schema: [Finance Sector Schema](Finance_Sector_Schema.md)*

## Economic Definition

An executed trade or exchange of assets between agents. Transactions are the observable "heartbeat" of the market.

## System Role

This is the primary **sensory input** for the system. The stream of transactions confirms or refutes the system's predictions about agent behavior and asset values.

## Table

| Attribute           | Data Type            | Description                                                               |
| ------------------- | -------------------- | ------------------------------------------------------------------------- |
| `transaction_id`    | `String`             | A unique identifier for the event.                                        |
| `involved_agents`   | `Array<Agent_Ref>`   | List of participating `agent_id`s (e.g., buyer, seller, broker).          |
| `exchanged_assets`  | `Object`             | Details of what was traded (e.g., `{from: Asset_X, to: Asset_Y}`).       |
| `price`             | `Float`              | The price at which the transaction was executed.                          |
| `timestamp`         | `DateTime`           | The time of execution.                                                    |
| `venue_id`          | `Market_Ref`         | The `Market` ID where the transaction occurred.                           |
| `settlement_status` | `Enum`               | `PENDING`, `COMPLETED`, `FAILED`. A `FAILED` status is a major surprise.  |
