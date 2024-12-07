from cost_calculator import calculate_total_cost



def find_cheapest_supplier(suppliers, orders):
    """
    Determine the supplier with the cheapest cost to fulfill all orders.
    
    :param suppliers: Dictionary of suppliers and their pricing data.
    :param orders: List of (product, quantity) tuples.
    :return: (Best supplier name, Total cost)
    """
    # Check if all requested quantities are zero or negative
    if all(quantity <= 0 for _, quantity in orders):
        print("No meaningful order to process. All requested quantities are zero or negative.")
        return None, 0

    best_supplier = None
    best_cost = float('inf')

    for supplier, pricing_data in suppliers.items():
        print(f"Evaluating costs for {supplier}...")
        cost = calculate_total_cost(pricing_data, orders)
        if cost == float('inf'):
            print(f"{supplier} cannot fulfill the order. Skipping...")
            continue

        print(f"Total cost from {supplier}: {cost} EUR")
        if cost < best_cost:
            best_cost = cost
            best_supplier = supplier

    if best_supplier is None:
        print("No supplier can fulfill the order.")
        return None, float('inf')

    return best_supplier, best_cost
