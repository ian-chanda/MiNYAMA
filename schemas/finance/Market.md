# `Market`

*Parent schema: [Finance Sector Schema](Finance_Sector_Schema.md)*

## Economic Definition

A formal or informal venue where assets are traded (e.g., stock exchanges). Markets have rules that govern how agents interact and how prices are discovered.

## System Role

The system models the market's microstructure to understand how its own actions will affect prices. A change to market rules (e.g., a trading halt) is a structural "surprise."

## Table

| Attribute       | Data Type     | Description                                                          |
| --------------- | ------------- | -------------------------------------------------------------------- |
| `market_id`     | `String`      | Unique ID for the venue (e.g., `NASDAQ`, `NYSE`).                    |
| `market_type`   | `Enum`        | `EXCHANGE`, `OTC_MARKET`, `DARK_POOL`.                               |
| `trading_hours` | `TimeRange`   | The times when trading is permitted.                                 |
| `rules_engine`  | `Object`      | A representation of the market's rules (e.g., circuit breakers).     |
| `order_book`    | `Object`      | A snapshot of current buy and sell orders, representing supply/demand.|
