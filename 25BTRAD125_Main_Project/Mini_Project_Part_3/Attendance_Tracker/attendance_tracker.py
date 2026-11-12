print("========== ATTENDANCE TRACKER ==========")

attendance = {
    "Aarav Sharma": {
        "2026-11-09": "P",
        "2026-11-10": "P",
        "2026-11-11": "A",
    },
    "Diya Patel": {
        "2026-11-09": "P",
        "2026-11-10": "P",
        "2026-11-11": "P",
    },
    "Kabir Rao": {
        "2026-11-09": "A",
        "2026-11-10": "A",
        "2026-11-11": "P",
    },
    "Meera Iyer": {
        "2026-11-09": "P",
        "2026-11-10": "A",
        "2026-11-11": "P",
    },
}


def add_student():
    name = input("Enter student name: ").strip().title()
    if not name:
        print("Student name cannot be empty!")
        return
    if name in attendance:
        print(f"Student '{name}' already exists.")
        return

    attendance[name] = {}
    print(f"Student '{name}' added successfully.")


def read_status(prompt):
    status = input(prompt).strip().upper()
    if status == "":
        return "P"
    if status not in ("P", "A"):
        print("Invalid status! Enter P or A.")
        return None
    return status


def mark_attendance():
    if not attendance:
        print("No students added yet.")
        return

    name = input("Enter student name: ").strip().title()
    if name not in attendance:
        print("Student not found.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not date:
        print("Date cannot be empty!")
        return

    status = read_status("Enter status (P = Present, A = Absent): ")
    if status is None:
        return

    if date in attendance[name]:
        print(
            f"Attendance for {name} on {date} updated "
            f"from {attendance[name][date]} to {status}."
        )
    else:
        print(f"Attendance marked for {name} on {date}: {status}.")

    attendance[name][date] = status


def mark_class_attendance():
    if not attendance:
        print("No students added yet.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not date:
        print("Date cannot be empty!")
        return

    for name in sorted(attendance):
        status = read_status(f"{name} (P/A, blank = P): ")
        if status is None:
            status = "A"
            print(f"Invalid status for {name}. Marked as Absent.")
        attendance[name][date] = status

    print(f"Attendance saved for {len(attendance)} students on {date}.")


def display_records():
    if not attendance:
        print("No attendance records to display.")
        return

    dates = sorted({date for records in attendance.values() for date in records})
    if not dates:
        print("No attendance records to display.")
        return

    print("\n" + "=" * 80)
    print("ATTENDANCE REGISTER")
    print("=" * 80)
    print(f"{'Student':<20}", end="")
    for date in dates:
        print(f"{date:<12}", end="")
    print()
    print("-" * 80)

    for name in sorted(attendance):
        print(f"{name:<20}", end="")
        for date in dates:
            print(f"{attendance[name].get(date, '-'):<12}", end="")
        print()

    print("=" * 80)
    print("P = Present, A = Absent, - = Not marked")


def show_percentages():
    if not attendance:
        print("No students added yet.")
        return

    print("\n" + "=" * 65)
    print("ATTENDANCE PERCENTAGES")
    print("=" * 65)
    print(f"{'Student':<22} {'Present':>9} {'Total':>7} {'Percent':>10}")
    print("-" * 65)

    for name in sorted(attendance):
        records = attendance[name]
        total = len(records)
        if total == 0:
            print(f"{name:<22} {'No records':>27}")
            continue

        present = sum(1 for status in records.values() if status == "P")
        percentage = present / total * 100
        print(f"{name:<22} {present:>9} {total:>7} {percentage:>9.2f}%")

    print("=" * 65)


def show_below_threshold():
    if not attendance:
        print("No students added yet.")
        return

    threshold_input = input("Enter attendance threshold % (press Enter for 75): ").strip()
    if threshold_input == "":
        threshold = 75.0
    else:
        try:
            threshold = float(threshold_input)
        except ValueError:
            print("Invalid threshold! Enter a number.")
            return

    if not 0 <= threshold <= 100:
        print("Threshold must be between 0 and 100.")
        return

    print(f"\nStudents below {threshold:.0f}% attendance:")
    print("-" * 45)
    found = False

    for name in sorted(attendance):
        records = attendance[name]
        total = len(records)
        if total == 0:
            print(f"  {name:<22} No records yet")
            found = True
            continue

        present = sum(1 for status in records.values() if status == "P")
        percentage = present / total * 100
        if percentage < threshold:
            print(f"  {name:<22} {percentage:.2f}%")
            found = True

    if not found:
        print("  None. Every student meets the threshold.")
    print("-" * 45)


while True:
    print("\n1. Add Student")
    print("2. Mark / Update Attendance")
    print("3. Mark Attendance for Whole Class")
    print("4. Display Attendance Records")
    print("5. Show Attendance Percentages")
    print("6. Show Students Below Threshold")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        mark_class_attendance()
    elif choice == "4":
        display_records()
    elif choice == "5":
        show_percentages()
    elif choice == "6":
        show_below_threshold()
    elif choice == "7":
        print("Exiting Attendance Tracker. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
