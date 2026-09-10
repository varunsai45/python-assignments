print("=== Data Types ===")
name = "Alice"
age = 22
height = 5.6
is_student = True

print("Name      :", name, type(name))
print("Age       :", age, type(age))
print("Height    :", height, type(height))
print("Student?  :", is_student, type(is_student))

print("\n=== Arithmetic Operators ===")
a = 15
b = 4
print("a =", a, "b =", b)
print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Power          :", a ** b)

print("\n=== Comparison Operators ===")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)

print("\n=== Logical Operators ===")
x = True
y = False
print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)

print("\n=== User Input ===")
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Hello", user_name + "! You are", user_age, "years old.")
