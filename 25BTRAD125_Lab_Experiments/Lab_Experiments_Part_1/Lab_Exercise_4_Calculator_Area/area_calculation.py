import math

print("=== Area Calculation ===")
print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Triangle")
print("4. Area of Square")

choice = input("Enter your choice (1-4): ")

if choice == '1':
    radius = float(input("Enter radius: "))
    area = math.pi * radius ** 2
    print("Area of Circle =", round(area, 2))
elif choice == '2':
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print("Area of Rectangle =", area)
elif choice == '3':
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)
elif choice == '4':
    side = float(input("Enter side: "))
    area = side ** 2
    print("Area of Square =", area)
else:
    print("Invalid choice!")
