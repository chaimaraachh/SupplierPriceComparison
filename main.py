from suppliers import suppliers
from supplier_evaluator import find_cheapest_supplier

def test_case(description, orders):
    """
    Run a test case for a specific set of orders and print the result.
    
    :param description: Description of the test case.
    :param orders: List of (product, quantity) tuples for the test case.
    """
    print(f"{description}")
    best_supplier, total_cost = find_cheapest_supplier(suppliers, orders)
    if best_supplier is None or total_cost == float('inf'):
        print("Result: No supplier can fulfill the order.\n")
    else:
        print(f"Best supplier: {best_supplier}")
        print(f"Total cost: {total_cost} EUR\n")

def main():
    # Test cases
    print("Examples from the task:\n")

    # Example 1
    test_case(
        "Example 1: Customer wants to buy 5 Units Dental Floss and 12 Units Ibuprofen.",
        [("Dental Floss", 5), ("Ibuprofen", 12)]
    )
    
    # Example 2
    test_case(
        "Example 2: Customer wants to buy 105 Units Ibuprofen.",
        [("Ibuprofen", 105)]
    )

    # Additional edge test cases
    print("Additional Test Cases:\n")

    # Case 1: Product not available
    test_case(
        "Case 1: Product not available (Toothpaste).",
        [("Toothpaste", 10), ("Ibuprofen", 105)]
    )

    # Case 2: Zero quantity requested
    test_case(
        "Case 2: Zero quantity requested.",
        [("Dental Floss", 0)]
    )


if __name__ == "__main__":
    main()
