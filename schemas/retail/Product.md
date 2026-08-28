# `Product`

*Parent schema: [Retail Sector Schema](Retail_Sector_Schema.md)*

## Economic Definition

The good or service being sold; the core unit of the retailer's offering. Its value is realized when exchanged.

## System Role

A static entity defining the properties of what is sold. The system's goal is to manage the flow of tangible instances of this product.

## Table

| Attribute          | Data Type     | Description                                                          |
| ------------------ | ------------- | -------------------------------------------------------------------- |
| `product_id`       | `String`      | A unique identifier for the product (e.g., SKU, UPC).                |
| `description`      | `String`      | Product name, brand, and other descriptive attributes.               |
| `category`         | `String`      | Product category for hierarchical analysis (e.g., `Electronics`).      |
| `price`            | `Float`       | The current selling price of the product.                            |
| `cost_of_goods_sold`| `Float`       | The cost to acquire the product from a supplier.                     |
| `supplier_id`      | `String`      | An identifier for the external supplier.                             |
