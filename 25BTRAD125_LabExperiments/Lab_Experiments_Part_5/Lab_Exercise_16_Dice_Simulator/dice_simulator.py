import random

print("========== DICE SIMULATOR ==========")


def read_int(prompt, minimum, maximum=None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input! Enter a whole number.")
            continue

        if value < minimum or (maximum is not None and value > maximum):
            if maximum is not None:
                print(f"Enter a value between {minimum} and {maximum}.")
            else:
                print(f"Enter a value of at least {minimum}.")
            continue

        return value


def roll_dice(number_of_dice, sides):
    return [random.randint(1, sides) for _ in range(number_of_dice)]


def show_rolls():
    number_of_dice = read_int("Enter number of dice (1-5): ", 1, 5)
    sides = read_int("Enter number of sides per die (minimum 2): ", 2)
    rolls = read_int("Enter number of rolls: ", 1)

    print(f"\nRolling {number_of_dice} dice with {sides} sides, {rolls} time(s):")
    print("-" * 60)

    for roll_number in range(1, rolls + 1):
        values = roll_dice(number_of_dice, sides)
        print(f"Roll {roll_number:>2}: {values}  -> Sum = {sum(values)}")

    print("-" * 60)


def show_analysis():
    number_of_dice = read_int("Enter number of dice (1-5): ", 1, 5)
    sides = read_int("Enter number of sides per die (minimum 2): ", 2)
    trials = read_int("Enter number of simulated rolls (for example 1000): ", 1)

    frequency = {}
    for _ in range(trials):
        total = sum(roll_dice(number_of_dice, sides))
        frequency[total] = frequency.get(total, 0) + 1

    minimum_total = number_of_dice
    maximum_total = number_of_dice * sides

    print(
        f"\nFrequency analysis for {number_of_dice} dice "
        f"({sides} sides) over {trials} rolls:"
    )
    print("-" * 65)
    print(f"{'Total':>6} {'Count':>8} {'Probability':>13}  Chart")
    print("-" * 65)

    for total in range(minimum_total, maximum_total + 1):
        count = frequency.get(total, 0)
        probability = count / trials * 100
        bar = "#" * int(probability / 2)
        print(f"{total:>6} {count:>8} {probability:>12.2f}%  {bar}")

    print("-" * 65)
    most_common_total = max(frequency, key=frequency.get)
    expected_value = number_of_dice * (sides + 1) / 2

    print(f"Most frequent total : {most_common_total} ({frequency[most_common_total]} times)")
    print(f"Expected average    : {expected_value:.2f}")

    if most_common_total == int(expected_value):
        print("Observation: The most frequent total matches the expected average.")
    else:
        print("Observation: Random variation shifted the most frequent total.")


while True:
    print("\n1. Roll Dice")
    print("2. Frequency / Probability Analysis")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        show_rolls()
    elif choice == "2":
        show_analysis()
    elif choice == "3":
        print("Exiting Dice Simulator. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
