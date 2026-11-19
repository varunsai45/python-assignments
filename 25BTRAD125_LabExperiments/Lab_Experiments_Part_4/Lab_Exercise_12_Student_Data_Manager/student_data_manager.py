import os

print("========== STUDENT DATA MANAGER ==========")

DATA_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "students.txt"
)
DELIMITER = "|"


def load_students():
    students = {}

    if not os.path.exists(DATA_FILE):
        print("Data file not found. A new file will be created on first save.")
        return students

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split(DELIMITER)
                if len(parts) != 4:
                    print(f"Skipping invalid record at line {line_number}: {line}")
                    continue

                roll, name, course, marks = parts
                try:
                    students[roll] = {
                        "name": name,
                        "course": course,
                        "marks": float(marks),
                    }
                except ValueError:
                    print(f"Skipping record with invalid marks at line {line_number}.")
    except OSError as error:
        print("Error reading data file:", error)

    return students


def save_students(students):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            for roll in sorted(students):
                record = students[roll]
                file.write(
                    f"{roll}{DELIMITER}{record['name']}{DELIMITER}"
                    f"{record['course']}{DELIMITER}{record['marks']}\n"
                )
        print(f"Records saved to {os.path.basename(DATA_FILE)}.")
    except OSError as error:
        print("Error saving data file:", error)


def read_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if 0 <= marks <= 100:
            return marks

        print("Marks must be between 0 and 100.")


def add_student(students):
    roll = input("Enter roll number: ").strip()
    if not roll:
        print("Roll number cannot be empty!")
        return

    if roll in students:
        print("A student with this roll number already exists.")
        return

    name = input("Enter student name: ").strip().title()
    course = input("Enter course: ").strip()
    if not name or not course:
        print("Name and course cannot be empty!")
        return

    marks = read_marks()
    students[roll] = {"name": name, "course": course, "marks": marks}
    save_students(students)
    print(f"Student '{name}' added successfully.")


def search_student(students):
    query = input("Enter roll number or name to search: ").strip().lower()
    if not query:
        print("Search text cannot be empty!")
        return

    matches = [
        roll
        for roll, record in students.items()
        if query in roll.lower() or query in record["name"].lower()
    ]

    if not matches:
        print("No matching student found.")
        return

    print("\n" + "=" * 70)
    print(f"{'Roll':<10} {'Name':<22} {'Course':<20} {'Marks':>8}")
    print("-" * 70)
    for roll in sorted(matches):
        record = students[roll]
        print(
            f"{roll:<10} {record['name']:<22} "
            f"{record['course']:<20} {record['marks']:>8.2f}"
        )
    print("=" * 70)


def update_student(students):
    roll = input("Enter roll number to update: ").strip()
    if roll not in students:
        print("Student not found.")
        return

    record = students[roll]
    print("Leave a field blank to keep the old value.")

    name = input(f"New name [{record['name']}]: ").strip().title()
    course = input(f"New course [{record['course']}]: ").strip()
    marks_input = input(f"New marks [{record['marks']}]: ").strip()

    if name:
        record["name"] = name
    if course:
        record["course"] = course
    if marks_input:
        try:
            marks = float(marks_input)
            if 0 <= marks <= 100:
                record["marks"] = marks
            else:
                print("Invalid marks! Old marks kept.")
        except ValueError:
            print("Invalid marks input! Old marks kept.")

    save_students(students)
    print(f"Record for roll number {roll} updated.")


def delete_student(students):
    roll = input("Enter roll number to delete: ").strip()
    if roll not in students:
        print("Student not found.")
        return

    confirm = input(f"Delete record of {students[roll]['name']}? (y/n): ").strip().lower()
    if confirm == "y":
        del students[roll]
        save_students(students)
        print("Student record deleted.")
    else:
        print("Delete cancelled.")


def display_students(students):
    if not students:
        print("No student records available.")
        return

    print("\n" + "=" * 70)
    print("STUDENT RECORDS")
    print("=" * 70)
    print(f"{'Roll':<10} {'Name':<22} {'Course':<20} {'Marks':>8}")
    print("-" * 70)
    for roll in sorted(students):
        record = students[roll]
        print(
            f"{roll:<10} {record['name']:<22} "
            f"{record['course']:<20} {record['marks']:>8.2f}"
        )
    print("=" * 70)
    print(f"Total students: {len(students)}")


students = load_students()

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_student(students)
    elif choice == "2":
        search_student(students)
    elif choice == "3":
        update_student(students)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        display_students(students)
    elif choice == "6":
        print("Exiting Student Data Manager. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
