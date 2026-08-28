# `EconomicAgent`

*Parent schema: [Finance Sector Schema](Finance_Sector_Schema.md)*

## Economic Definition

Represents any actor or participant within the financial ecosystem (e.g., individuals, corporations, central banks, regulators). They are the decision-makers whose collective behavior creates the market.

## System Role

The system models agents to predict their behavior. Unexpected actions by key agents are a primary source of "surprise" (risk).

## Table

| Attribute             | Data Type          | Description                                                               |
| --------------------- | ------------------ | ------------------------------------------------------------------------- |
| `agent_id`            | `String`           | A unique identifier for the agent (e.g., LEI for a corporation).          |
| `agent_type`          | `Enum`             | e.g., `CENTRAL_BANK`, `COMMERCIAL_BANK`, `INVESTOR`, `REGULATOR`.           |
| `risk_profile`        | `ProbabilityDist`  | The system's **belief** about the agent's risk tolerance.                 |
| `liquidity_preference`| `ProbabilityDist`  | The system's **belief** about the agent's need for cash-equivalent assets.|
| `capital_reserves`    | `Float`            | The believed amount of capital the agent holds.                          |
| `known_holdings`      | `Array<Asset_Ref>` | A list of `Asset` IDs this agent is known to possess.                     |
