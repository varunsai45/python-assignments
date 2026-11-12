print("========== SALES DATA ANALYZER ==========")

products = {
    "Laptop": {"quantity": 12, "price": 55000.0},
    "Mobile": {"quantity": 30, "price": 18000.0},
    "Headphones": {"quantity": 45, "price": 2500.0},
    "Keyboard": {"quantity": 25, "price": 1200.0},
}


def calculate_revenue(record):
    return record["quantity"] * record["price"]


def read_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if value <= 0:
            print("Value must be greater than zero.")
            continue

        return value


def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input! Enter a whole number.")
            continue

        if value <= 0:
            print("Quantity must be greater than zero.")
            continue

        return value


def add_or_update_sale():
    name = input("Enter product name: ").strip().title()
    if not name:
        print("Product name cannot be empty!")
        return

    if name in products:
        quantity = read_positive_int("Enter quantity sold to add: ")
        products[name]["quantity"] += quantity

        new_price = input(
            f"Enter new price per unit (blank to keep Rs.{products[name]['price']:.2f}): "
        ).strip()
        if new_price:
            try:
                price = float(new_price)
                if price > 0:
                    products[name]["price"] = price
                else:
                    print("Price must be positive. Old price kept.")
            except ValueError:
                print("Invalid price. Old price kept.")

        print(
            f"Sale updated for {name}. "
            f"Total quantity sold: {products[name]['quantity']}."
        )
    else:
        quantity = read_positive_int("Enter quantity sold: ")
        price = read_positive_float("Enter price per unit: ")
        products[name] = {"quantity": quantity, "price": price}
        print(f"Product '{name}' added successfully.")


def display_products():
    if not products:
        print("No product sales records available.")
        return

    total_revenue = sum(calculate_revenue(record) for record in products.values())

    print("\n" + "=" * 85)
    print("PRODUCT-WISE SALES PERFORMANCE")
    print("=" * 85)
    print(
        f"{'Product':<20} {'Quantity':>10} {'Price':>12} "
        f"{'Revenue':>15} {'Share':>9}"
    )
    print("-" * 85)

    for name in sorted(products, key=lambda product: calculate_revenue(products[product]), reverse=True):
        record = products[name]
        revenue = calculate_revenue(record)
        share = revenue / total_revenue * 100 if total_revenue else 0
        print(
            f"{name:<20} {record['quantity']:>10} {record['price']:>12.2f} "
            f"{revenue:>15.2f} {share:>8.2f}%"
        )

    print("-" * 85)
    print(f"{'TOTAL':<20} {'':>10} {'':>12} {total_revenue:>15.2f} {'100.00%':>9}")
    print("=" * 85)


def show_summary():
    if not products:
        print("No product sales records available.")
        return

    total_revenue = sum(calculate_revenue(record) for record in products.values())
    total_quantity = sum(record["quantity"] for record in products.values())
    average_revenue = total_revenue / len(products)

    top_by_quantity = max(products, key=lambda name: products[name]["quantity"])
    top_by_revenue = max(products, key=lambda name: calculate_revenue(products[name]))
    lowest_by_revenue = min(products, key=lambda name: calculate_revenue(products[name]))

    print("\n" + "=" * 60)
    print("SALES SUMMARY")
    print("=" * 60)
    print(f"  Products tracked        : {len(products)}")
    print(f"  Total quantity sold     : {total_quantity}")
    print(f"  Total sales revenue     : Rs.{total_revenue:.2f}")
    print(f"  Average revenue/product : Rs.{average_revenue:.2f}")
    print("-" * 60)
    print(
        f"  Highest-selling product : {top_by_quantity} "
        f"({products[top_by_quantity]['quantity']} units)"
    )
    print(
        f"  Highest-revenue product : {top_by_revenue} "
        f"(Rs.{calculate_revenue(products[top_by_revenue]):.2f})"
    )
    print(
        f"  Lowest-revenue product  : {lowest_by_revenue} "
        f"(Rs.{calculate_revenue(products[lowest_by_revenue]):.2f})"
    )
    print("=" * 60)


def show_highest_selling():
    if not products:
        print("No product sales records available.")
        return

    top_by_quantity = max(products, key=lambda name: products[name]["quantity"])
    top_by_revenue = max(products, key=lambda name: calculate_revenue(products[name]))

    print("\n" + "=" * 60)
    print("BEST PERFORMING PRODUCTS")
    print("=" * 60)
    print(
        f"  By quantity : {top_by_quantity} "
        f"({products[top_by_quantity]['quantity']} units)"
    )
    print(
        f"  By revenue  : {top_by_revenue} "
        f"(Rs.{calculate_revenue(products[top_by_revenue]):.2f})"
    )
    print("=" * 60)


while True:
    print("\n1. Add / Update Product Sales")
    print("2. Display Product Performance")
    print("3. Show Sales Summary")
    print("4. Show Highest-Selling Product")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_or_update_sale()
    elif choice == "2":
        display_products()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        show_highest_selling()
    elif choice == "5":
        print("Exiting Sales Data Analyzer. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
