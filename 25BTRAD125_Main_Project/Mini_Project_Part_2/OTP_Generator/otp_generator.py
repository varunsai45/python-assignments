import random
import string

print("========== OTP GENERATOR ==========")
print("1. Numeric OTP (4 digits)")
print("2. Numeric OTP (6 digits)")
print("3. Alphanumeric OTP")

choice = input("Enter your choice (1-3): ")

if choice == '1':
    otp = ''.join(random.choices(string.digits, k=4))
    print(f"\nYour 4-digit OTP: {otp}")

elif choice == '2':
    otp = ''.join(random.choices(string.digits, k=6))
    print(f"\nYour 6-digit OTP: {otp}")

elif choice == '3':
    length = int(input("Enter OTP length: "))
    otp = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    print(f"\nYour OTP: {otp}")

else:
    print("Invalid choice!")
