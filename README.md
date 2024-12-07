
# Supplier Price Comparison

This project implements a tool to compare the pricing of multiple suppliers and determine the cheapest supplier for fulfilling customer orders. The system is modular and designed to handle edge cases effectively.

## Features

- **Cost Calculation**: Calculate the total cost of fulfilling an order based on supplier pricing tiers.
- **Supplier Comparison**: Identify the cheapest supplier for a given set of products and quantities.
- **Edge Case Handling**: Robust handling for scenarios like unavailable products, zero quantities, and complex orders.
- **Modular Design**: Divided into distinct modules for cost calculation, supplier evaluation, and main application logic.

## Project Structure

```
.
├── cost_calculator.py        # Logic for calculating total costs of orders
├── supplier_evaluator.py     # Logic for finding the cheapest supplier
├── suppliers.py              # Supplier pricing data
├── main.py                   # Entry point with test cases and execution logic
└── README.md                 # Project documentation
```
