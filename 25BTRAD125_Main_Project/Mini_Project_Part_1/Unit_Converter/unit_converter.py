print("========== UNIT CONVERTER ==========")
print("1. Length (meters <-> feet)")
print("2. Weight (kilograms <-> pounds)")
print("3. Temperature (Celsius <-> Fahrenheit)")
print("4. Volume (liters <-> gallons)")

choice = input("\nEnter your choice (1-4): ")

if choice == '1':
    print("\n--- Length Converter ---")
    value = float(input("Enter value: "))
    sub = input("Convert (m) meters to feet or (f) feet to meters? ").lower()
    if sub == 'm':
        result = value * 3.28084
        print(f"{value} meters = {round(result, 4)} feet")
    elif sub == 'f':
        result = value / 3.28084
        print(f"{value} feet = {round(result, 4)} meters")
    else:
        print("Invalid option!")

elif choice == '2':
    print("\n--- Weight Converter ---")
    value = float(input("Enter value: "))
    sub = input("Convert (k) kg to pounds or (p) pounds to kg? ").lower()
    if sub == 'k':
        result = value * 2.20462
        print(f"{value} kg = {round(result, 4)} pounds")
    elif sub == 'p':
        result = value / 2.20462
        print(f"{value} pounds = {round(result, 4)} kg")
    else:
        print("Invalid option!")

elif choice == '3':
    print("\n--- Temperature Converter ---")
    value = float(input("Enter value: "))
    sub = input("Convert (c) Celsius to Fahrenheit or (f) Fahrenheit to Celsius? ").lower()
    if sub == 'c':
        result = (value * 9/5) + 32
        print(f"{value}C = {round(result, 2)}F")
    elif sub == 'f':
        result = (value - 32) * 5/9
        print(f"{value}F = {round(result, 2)}C")
    else:
        print("Invalid option!")

elif choice == '4':
    print("\n--- Volume Converter ---")
    value = float(input("Enter value: "))
    sub = input("Convert (l) liters to gallons or (g) gallons to liters? ").lower()
    if sub == 'l':
        result = value * 0.264172
        print(f"{value} liters = {round(result, 4)} gallons")
    elif sub == 'g':
        result = value / 0.264172
        print(f"{value} gallons = {round(result, 4)} liters")
    else:
        print("Invalid option!")

else:
    print("Invalid choice!")
