# System Architecture: Finance Sector World Model

## 1. Overview

This document outlines the baseline data architecture for an **Active Inference World Model** tailored to the Finance sector. The system's primary objective is to minimize "surprise" by accurately modeling the financial ecosystem, predicting events, and taking actions to manage unpredicted risk.

This architecture is composed of several core entities that, when combined, form the agent's internal "belief state" about the world.

## 2. Entity Relationship Diagram

The following diagram illustrates the high-level relationships between the core entities. `Transactions` are the central events that connect all other entities.

```
+----------------+      +-----------------+      +---------------+
| EconomicAgent  |----->|   Transaction   |<-----| EconomicAgent |
+----------------+      +-----------------+      +---------------+
                            |         ^
                            |         |
                            v         |
                      +-------+     +--------+
                      | Asset |     | Market |
                      +-------+     +--------+
```

## 3. Core Entities

### 3.1. `EconomicAgent`

*   **Economic Definition**: Represents any actor or participant within the financial ecosystem (e.g., individuals, corporations, central banks, regulators). They are the decision-makers whose collective behavior creates the market.
*   **System Role**: The system models agents to predict their behavior. Unexpected actions by key agents are a primary source of "surprise" (risk).

| Attribute             | Data Type          | Description                                                               |
| --------------------- | ------------------ | ------------------------------------------------------------------------- |
| `agent_id`            | `String`           | A unique identifier for the agent (e.g., LEI for a corporation).          |
| `agent_type`          | `Enum`             | e.g., `CENTRAL_BANK`, `COMMERCIAL_BANK`, `INVESTOR`, `REGULATOR`.           |
| `risk_profile`        | `ProbabilityDist`  | The system's **belief** about the agent's risk tolerance.                 |
| `liquidity_preference`| `ProbabilityDist`  | The system's **belief** about the agent's need for cash-equivalent assets.|
| `capital_reserves`    | `Float`            | The believed amount of capital the agent holds.                          |
| `known_holdings`      | `Array<Asset_Ref>` | A list of `Asset` IDs this agent is known to possess.                     |

---

### 3.2. `Asset`

*   **Economic Definition**: Represents any instrument of value that can be owned and traded (e.g., stocks, bonds, currencies). Assets are the fundamental medium of the financial system.
*   **System Role**: The system models the "true" value and price behavior of assets. The difference between the predicted and observed price is a core component of "surprise."

| Attribute          | Data Type           | Description                                                               |
| ------------------ | ------------------- | ------------------------------------------------------------------------- |
| `asset_id`         | `String`            | A unique identifier for the asset (e.g., CUSIP, ISIN).                    |
| `asset_class`      | `Enum`              | e.g., `EQUITY`, `FIXED_INCOME`, `DERIVATIVE`, `CURRENCY`.                   |
| `issuer_id`        | `Agent_Ref`         | The `agent_id` of the entity that created the asset.                      |
| `valuation_model`  | `Function` / `Model`| The system's internal **belief** model for the asset's price.             |
| `price_history`    | `TimeSeries`        | A time-series of past market prices.                                      |
| `volatility_model` | `ProbabilityDist`   | The system's **belief** about the range and likelihood of price swings.   |
| `liquidity_depth`  | `Float`             | A measure of market depth for the asset.                                  |

---

### 3.3. `Transaction` (Observable Event)

*   **Economic Definition**: An executed trade or exchange of assets between agents. Transactions are the observable "heartbeat" of the market.
*   **System Role**: This is the primary **sensory input** for the system. The stream of transactions confirms or refutes the system's predictions about agent behavior and asset values.

| Attribute           | Data Type            | Description                                                               |
| ------------------- | -------------------- | ------------------------------------------------------------------------- |
| `transaction_id`    | `String`             | A unique identifier for the event.                                        |
| `involved_agents`   | `Array<Agent_Ref>`   | List of participating `agent_id`s (e.g., buyer, seller, broker).          |
| `exchanged_assets`  | `Object`             | Details of what was traded (e.g., `{from: Asset_X, to: Asset_Y}`).       |
| `price`             | `Float`              | The price at which the transaction was executed.                          |
| `timestamp`         | `DateTime`           | The time of execution.                                                    |
| `venue_id`          | `Market_Ref`         | The `Market` ID where the transaction occurred.                           |
| `settlement_status` | `Enum`               | `PENDING`, `COMPLETED`, `FAILED`. A `FAILED` status is a major surprise.  |

---

### 3.4. `Market`

*   **Economic Definition**: A formal or informal venue where assets are traded (e.g., stock exchanges). Markets have rules that govern how agents interact and how prices are discovered.
*   **System Role**: The system models the market's microstructure to understand how its own actions will affect prices. A change to market rules (e.g., a trading halt) is a structural "surprise."

| Attribute       | Data Type     | Description                                                          |
| --------------- | ------------- | -------------------------------------------------------------------- |
| `market_id`     | `String`      | Unique ID for the venue (e.g., `NASDAQ`, `NYSE`).                    |
| `market_type`   | `Enum`        | `EXCHANGE`, `OTC_MARKET`, `DARK_POOL`.                               |
| `trading_hours` | `TimeRange`   | The times when trading is permitted.                                 |
| `rules_engine`  | `Object`      | A representation of the market's rules (e.g., circuit breakers).     |
| `order_book`    | `Object`      | A snapshot of current buy and sell orders, representing supply/demand.|
