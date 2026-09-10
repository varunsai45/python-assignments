# ============================================================
# ASSIGNMENT TASK UNIT 1
# USN        : 25BTRAD125
# NAME       : Varun Sai M
# COLLEGE    : JAIN (Deemed-to-be University)
# DEPARTMENT : B.Tech CSE - Artificial Intelligence and Data Engineering
# ============================================================


# ============================================================
# TASK 1
# Print Name, Department, and College on separate lines
# ============================================================

print("Varun Sai M")
print("B.Tech CSE - Artificial Intelligence and Data Engineering")
print("JAIN (Deemed-to-be University)")


# ============================================================
# TASK 2
# Print the given pattern
# ============================================================

print("---")
print("---")
print("---")


# ============================================================
# TASK 3
# Print "Python is Easy" using a single print() statement
# ============================================================

print("Python is Easy")


# ============================================================
# TASK 4
# Print the number pattern
# ============================================================

print("1")
print("12")
print("123")
print("1234")
print("12345")


# ============================================================
# TASK 5
# Use \n to print Computer, Science, Engineering
# ============================================================

print("Computer\nScience\nEngineering")


# ============================================================
# TASK 6
# Use \t to print Name Age City
# ============================================================

print("Name\tAge\tCity")


# ============================================================
# TASK 7
# Single-line comment explaining the purpose of the program
# ============================================================

# This program prints a greeting message to the user.
print("Hello, welcome to Python programming!")


# ============================================================
# TASK 8
# Program using multi-line comments
# ============================================================

"""
This is a multi-line comment.
It can span multiple lines.
This program demonstrates how to use multi-line comments in Python.
"""

print("This program demonstrates multi-line comments.")


# ============================================================
# TASK 9
# Three comments and three print statements
# ============================================================

# First comment: greeting message
print("Hello!")

# Second comment: department information
print("I am from Artificial Intelligence and Data Engineering.")

# Third comment: college information
print("I study at JAIN (Deemed-to-be University).")


# ============================================================
# TASK 10
# Create a variable called name, store the name and print it
# ============================================================

name = "Varun Sai M"
print(name)


# ============================================================
# TASK 11
# Store 10, 20, and 30 in three different variables and print them
# ============================================================

number1 = 10
number2 = 20
number3 = 30

print(number1)
print(number2)
print(number3)


# ============================================================
# TASK 12
# Convert the string "100" into an integer
# Display the value and the data type
# ============================================================

value = "100"
integer_value = int(value)

print(integer_value)
print(type(integer_value))


# ============================================================
# TASK 13
# Convert integer 25 into a float
# Display the result and its type
# ============================================================

number = 25
float_number = float(number)

print(float_number)
print(type(float_number))


# ============================================================
# TASK 14
# Accept the user's age using input()
# Convert it to an integer and display the age
# ============================================================

age = int(input("Enter your age: "))
print("Your age is:", age)


# ============================================================
# TASK 15
# Accept two numbers from the user
# Convert both to integers and display their sum
# ============================================================

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print("Sum:", total)


# ============================================================
# TASK 16
# Accept student's name, age, and CGPA using input()
# Display using an f-string
# ============================================================

s_name = input("Enter student's name: ")
s_age = int(input("Enter student's age: "))
s_cgpa = float(input("Enter student's CGPA: "))

print(f"My name is {s_name}. I am {s_age} years old and my CGPA is {s_cgpa}.")


# ============================================================
# TASK 17
# Accept temperature in Celsius
# Convert to Fahrenheit using F = (C x 9/5) + 32
# Display result using f-string with two decimal places
# ============================================================

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")


# ============================================================
# TASK 18
# Accept an integer and determine if it is even or odd using %
# ============================================================

number = int(input("Enter number: "))

if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
