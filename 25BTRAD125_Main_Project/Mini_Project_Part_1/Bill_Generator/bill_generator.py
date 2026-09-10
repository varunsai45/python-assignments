print("========== BILL GENERATOR ==========")

items = []
total = 0

print("Available items:")
print("1. Rice       - Rs.40/kg")
print("2. Wheat      - Rs.35/kg")
print("3. Sugar      - Rs.50/kg")
print("4. Oil        - Rs.120/liter")
print("5. Milk       - Rs.56/liter")
print("6. Eggs       - Rs.6/piece")

prices = {
    1: ("Rice", 40),
    2: ("Wheat", 35),
    3: ("Sugar", 50),
    4: ("Oil", 120),
    5: ("Milk", 56),
    6: ("Eggs", 6),
}

while True:
    item_no = int(input("\nEnter item number (1-6, 0 to finish): "))
    if item_no == 0:
        break
    if item_no not in prices:
        print("Invalid item!")
        continue
    qty = float(input(f"Enter quantity for {prices[item_no][0]}: "))
    price = prices[item_no][1] * qty
    items.append((prices[item_no][0], qty, prices[item_no][1], price))
    total += price
    print(f"Added: {prices[item_no][0]} x {qty} = Rs.{price}")

print("\n" + "=" * 50)
print("              BILL RECEIPT")
print("=" * 50)
print(f"{'Item':<12} {'Qty':<8} {'Rate':<10} {'Amount':<10}")
print("-" * 50)

for item in items:
    print(f"{item[0]:<12} {item[1]:<8} Rs.{item[2]:<8} Rs.{item[3]:<8}")

print("-" * 50)
print(f"{'TOTAL':>30} Rs.{total}")
print("=" * 50)
print("Thank you for shopping!")
