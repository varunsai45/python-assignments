def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a Prime number")
else:
    print(num, "is NOT a Prime number")

limit = int(input("\nEnter range limit: "))
print(f"\nPrime numbers up to {limit}:")
for i in range(2, limit + 1):
    if is_prime(i):
        print(i, end=" ")
print()
