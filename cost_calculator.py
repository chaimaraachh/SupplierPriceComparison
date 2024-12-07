def calculate_total_cost(pricing_data, orders):
    """
    Calculate the total cost for a list of product orders.
    
    :param pricing_data: Dictionary of product pricing tiers {(unit size, price)}.
    :param orders: List of (product, quantity) tuples.
    :return: Total cost to fulfill the orders, or float('inf') if not feasible.
    """
    total_cost = 0

    for product, quantity in orders:
        if product not in pricing_data:
            print(f"Error: Product '{product}' not available in supplier data.")
            return float('inf')
        
        if quantity <= 0:
            print(f"Warning: Requested quantity for '{product}' is zero or less. Skipping cost.")
            continue
        
        # Sort pricing tiers by unit size in descending order
        tiers = sorted(pricing_data[product], key=lambda x: -x[0])
        remaining_quantity = quantity
        product_cost = 0

        for unit_size, price in tiers:
            if remaining_quantity <= 0:
                break
            # Calculate how many of this unit size can be used
            num_units = remaining_quantity // unit_size
            if num_units > 0:
                product_cost += num_units * price
                remaining_quantity -= num_units * unit_size

        # If there's leftover quantity that can't be fulfilled, mark as not feasible
        if remaining_quantity > 0:
            print(f"Error: Supplier cannot fully satisfy '{product}' with quantity {quantity}.")
            return float('inf')

        total_cost += product_cost

    return total_cost
