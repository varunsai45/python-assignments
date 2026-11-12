import string

print("========== FREQUENCY COUNTER ==========")


def clean_word(word):
    return word.strip(string.punctuation).lower()


def count_words(text):
    words = [clean_word(word) for word in text.split()]
    words = [word for word in words if word]

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency, len(words)


def count_elements(items):
    frequency = {}
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency


def show_frequency(frequency, total, item_label):
    if not frequency:
        print("No data to count.")
        return

    print(f"\nTotal {item_label}: {total}")
    print(f"Unique {item_label}: {len(frequency)}")
    print("-" * 65)
    print(f"{'Item':<25} {'Count':>7} {'Percent':>9}  Chart")
    print("-" * 65)

    sorted_items = sorted(frequency.items(), key=lambda item: (-item[1], item[0]))
    for item, count in sorted_items:
        percentage = count / total * 100
        bar = "#" * min(count, 40)
        print(f"{item:<25} {count:>7} {percentage:>8.2f}%  {bar}")

    print("-" * 65)
    most_common_item = sorted_items[0][0]
    least_common_item = sorted_items[-1][0]
    print(f"Most frequent : '{most_common_item}' ({frequency[most_common_item]} times)")
    print(f"Least frequent: '{least_common_item}' ({frequency[least_common_item]} time(s))")


def count_sentence_words():
    text = input("Enter a sentence: ").strip()
    if not text:
        text = "Python is easy and Python is powerful. Python is fun!"
        print("Using sample sentence:", text)

    frequency, total = count_words(text)
    show_frequency(frequency, total, "words")


def count_list_items():
    raw_items = input("Enter list items separated by commas: ").strip()
    if not raw_items:
        raw_items = "Python, Java, Python, C, Java, Python, C++, Java"
        print("Using sample list:", raw_items)

    items = [item.strip().title() for item in raw_items.split(",") if item.strip()]
    frequency = count_elements(items)
    show_frequency(frequency, len(items), "elements")


while True:
    print("\n1. Count Word Frequency in a Sentence")
    print("2. Count Element Frequency in a List")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        count_sentence_words()
    elif choice == "2":
        count_list_items()
    elif choice == "3":
        print("Exiting Frequency Counter. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
