import csv
import os

print("========== CSV-BASED PAYROLL MANAGEMENT SYSTEM ==========")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, "employees.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "salary_summary.csv")

HRA_RATE = 0.20
DA_RATE = 0.10
PF_RATE = 0.12
PROFESSIONAL_TAX = 200


def calculate_salary(basic):
    hra = basic * HRA_RATE
    da = basic * DA_RATE
    gross_salary = basic + hra + da
    pf = basic * PF_RATE

    if gross_salary <= 30000:
        tax_rate = 0.05
    elif gross_salary <= 50000:
        tax_rate = 0.10
    elif gross_salary <= 80000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

    income_tax = gross_salary * tax_rate
    total_deductions = pf + income_tax + PROFESSIONAL_TAX
    net_salary = gross_salary - total_deductions

    return {
        "hra": hra,
        "da": da,
        "gross": gross_salary,
        "pf": pf,
        "tax": income_tax,
        "professional_tax": PROFESSIONAL_TAX,
        "deductions": total_deductions,
        "net": net_salary,
    }


def read_employees(path):
    if not os.path.exists(path):
        print(f"Error: Input file '{os.path.basename(path)}' was not found.")
        return None

    if os.path.getsize(path) == 0:
        print("Error: Input file is empty.")
        return None

    employees = []

    try:
        with open(path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("Error: CSV file has no header row.")
                return None

            required_fields = {"emp_id", "name", "basic_salary"}
            missing_fields = required_fields - set(reader.fieldnames)
            if missing_fields:
                print(f"Error: Missing CSV columns: {', '.join(sorted(missing_fields))}")
                return None

            for row_number, row in enumerate(reader, start=2):
                emp_id = (row.get("emp_id") or "").strip()
                name = (row.get("name") or "").strip()
                basic_text = (row.get("basic_salary") or "").strip()

                if not emp_id or not name or not basic_text:
                    print(f"Skipping row {row_number}: missing required data.")
                    continue

                try:
                    basic = float(basic_text)
                except ValueError:
                    print(f"Skipping row {row_number}: invalid salary '{basic_text}'.")
                    continue

                if basic <= 0:
                    print(f"Skipping row {row_number}: salary must be positive.")
                    continue

                salary = calculate_salary(basic)
                employees.append(
                    {
                        "emp_id": emp_id,
                        "name": name.title(),
                        "basic": basic,
                        **salary,
                    }
                )
    except (OSError, csv.Error) as error:
        print("Error reading CSV file:", error)
        return None

    return employees


def display_salary_summary(employees):
    if not employees:
        print("No valid employee records to display.")
        return

    print("\n" + "=" * 125)
    print("SALARY SUMMARY")
    print("=" * 125)
    print(
        f"{'ID':<7} {'Name':<18} {'Basic':>10} {'HRA':>9} {'DA':>9} "
        f"{'Gross':>11} {'PF':>9} {'Tax':>10} {'Deductions':>11} {'Net':>11}"
    )
    print("-" * 125)

    for employee in employees:
        print(
            f"{employee['emp_id']:<7} {employee['name']:<18} "
            f"{employee['basic']:>10.2f} {employee['hra']:>9.2f} "
            f"{employee['da']:>9.2f} {employee['gross']:>11.2f} "
            f"{employee['pf']:>9.2f} {employee['tax']:>10.2f} "
            f"{employee['deductions']:>11.2f} {employee['net']:>11.2f}"
        )

    print("-" * 125)

    total_basic = sum(employee["basic"] for employee in employees)
    total_gross = sum(employee["gross"] for employee in employees)
    total_deductions = sum(employee["deductions"] for employee in employees)
    total_net = sum(employee["net"] for employee in employees)

    print(
        f"{'TOTAL':<26} {total_basic:>10.2f} {'':>9} {'':>9} "
        f"{total_gross:>11.2f} {'':>9} {'':>10} "
        f"{total_deductions:>11.2f} {total_net:>11.2f}"
    )
    print("=" * 125)

    highest_paid = max(employees, key=lambda employee: employee["net"])
    average_net = total_net / len(employees)

    print(f"Employees processed : {len(employees)}")
    print(f"Total gross salary  : Rs.{total_gross:.2f}")
    print(f"Total deductions    : Rs.{total_deductions:.2f}")
    print(f"Total net payable   : Rs.{total_net:.2f}")
    print(f"Average net salary  : Rs.{average_net:.2f}")
    print(
        f"Highest net salary  : {highest_paid['name']} "
        f"(Rs.{highest_paid['net']:.2f})"
    )


def write_summary_file(employees):
    if not employees:
        return

    try:
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "emp_id",
                    "name",
                    "basic_salary",
                    "hra",
                    "da",
                    "gross_salary",
                    "pf",
                    "income_tax",
                    "professional_tax",
                    "total_deductions",
                    "net_salary",
                ]
            )

            for employee in employees:
                writer.writerow(
                    [
                        employee["emp_id"],
                        employee["name"],
                        f"{employee['basic']:.2f}",
                        f"{employee['hra']:.2f}",
                        f"{employee['da']:.2f}",
                        f"{employee['gross']:.2f}",
                        f"{employee['pf']:.2f}",
                        f"{employee['tax']:.2f}",
                        f"{employee['professional_tax']:.2f}",
                        f"{employee['deductions']:.2f}",
                        f"{employee['net']:.2f}",
                    ]
                )
        print(f"\nSalary summary written to {os.path.basename(OUTPUT_FILE)}.")
    except OSError as error:
        print("Error writing summary file:", error)


employees = read_employees(INPUT_FILE)
if employees is not None:
    display_salary_summary(employees)
    write_summary_file(employees)
