print("========== STUDENT GRADING SYSTEM ==========")

SUBJECTS = ("Maths", "Science", "English")

students = {
    "Aarav Sharma": [85, 90, 78],
    "Diya Patel": [92, 88, 95],
    "Kabir Rao": [45, 38, 52],
    "Meera Iyer": [70, 65, 72],
}


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def evaluate_student(marks):
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)
    failed_subjects = [
        SUBJECTS[index] for index, mark in enumerate(marks) if mark < 40
    ]
    result = "PASS" if average >= 40 and not failed_subjects else "FAIL"
    return total, average, grade, result, failed_subjects


def read_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if 0 <= mark <= 100:
            return mark

        print("Marks must be between 0 and 100.")


def add_student():
    name = input("Enter student name: ").strip().title()
    if not name:
        print("Student name cannot be empty!")
        return

    if name in students:
        print(f"Student '{name}' already exists. Updating marks.")

    marks = [read_mark(subject) for subject in SUBJECTS]
    students[name] = marks
    print(f"Marks saved for {name}.")


def search_student():
    name = input("Enter student name to search: ").strip().title()
    if name not in students:
        print("Student not found.")
        return

    total, average, grade, result, failed_subjects = evaluate_student(students[name])
    print(f"\nStudent : {name}")
    for index, subject in enumerate(SUBJECTS):
        print(f"  {subject:<10}: {students[name][index]:.1f}")
    print(f"  Total     : {total:.1f}")
    print(f"  Average   : {average:.2f}")
    print(f"  Grade     : {grade}")
    print(f"  Result    : {result}")
    if failed_subjects:
        print(f"  Failed in : {', '.join(failed_subjects)}")


def display_results():
    if not students:
        print("No student records available.")
        return

    print("\n" + "=" * 100)
    print("STUDENT RESULTS")
    print("=" * 100)
    print(
        f"{'Name':<18} {'Maths':>7} {'Science':>8} {'English':>8} "
        f"{'Total':>8} {'Average':>9} {'Grade':>7} {'Result':>8}"
    )
    print("-" * 100)

    for name in sorted(students):
        total, average, grade, result, _ = evaluate_student(students[name])
        marks = students[name]
        print(
            f"{name:<18} {marks[0]:>7.1f} {marks[1]:>8.1f} {marks[2]:>8.1f} "
            f"{total:>8.1f} {average:>9.2f} {grade:>7} {result:>8}"
        )

    print("=" * 100)


def show_class_summary():
    if not students:
        print("No student records available.")
        return

    grade_counts = {}
    class_total = 0
    pass_count = 0
    topper_name = None
    topper_average = -1

    for name, marks in students.items():
        total, average, grade, result, _ = evaluate_student(marks)
        class_total += average
        grade_counts[grade] = grade_counts.get(grade, 0) + 1

        if result == "PASS":
            pass_count += 1

        if average > topper_average:
            topper_average = average
            topper_name = name

    class_average = class_total / len(students)

    print("\n" + "=" * 50)
    print("CLASS SUMMARY")
    print("=" * 50)
    print(f"  Total students   : {len(students)}")
    print(f"  Class average    : {class_average:.2f}")
    print(f"  Students passed  : {pass_count}")
    print(f"  Students failed  : {len(students) - pass_count}")
    print(f"  Class topper     : {topper_name} ({topper_average:.2f})")
    print("-" * 50)
    print("  Grade distribution:")
    for grade in ("A+", "A", "B+", "B", "C", "D", "F"):
        count = grade_counts.get(grade, 0)
        print(f"    {grade:<3} : {count} student(s) {'#' * count}")
    print("=" * 50)


while True:
    print("\n1. Add / Update Student Marks")
    print("2. Search Student")
    print("3. Display All Results")
    print("4. Show Class Summary")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        display_results()
    elif choice == "4":
        show_class_summary()
    elif choice == "5":
        print("Exiting Student Grading System. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
