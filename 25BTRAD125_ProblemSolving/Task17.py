# ============================================================
# ASSIGNMENT TASK UNIT 1
# USN        : 25BTRAD125
# NAME       : Varun Sai M
# COLLEGE    : JAIN (Deemed-to-be University)
# DEPARTMENT : B.Tech CSE - Artificial Intelligence and Data Engineering
# ============================================================

# ============================================================
# TASK 17
# Accept temperature in Celsius
# Convert to Fahrenheit using F = (C x 9/5) + 32
# Display result using f-string with two decimal places
# ============================================================

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
