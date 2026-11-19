import os

print("========== LOG FILE READER ==========")

KEYWORDS = ("ERROR", "WARNING", "INFO", "DEBUG")


def read_log_file(path):
    if not os.path.exists(path):
        print(f"Error: File '{path}' was not found.")
        return None

    if os.path.getsize(path) == 0:
        print(f"Warning: File '{path}' is empty. Nothing to analyse.")
        return []

    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readlines()
    except OSError as error:
        print("Error reading file:", error)
        return None


def summarize_log(lines):
    counts = {keyword: 0 for keyword in KEYWORDS}
    other_count = 0
    error_lines = []

    for line in lines:
        text = line.strip()
        if not text:
            continue

        upper_text = text.upper()
        matched = False

        for keyword in KEYWORDS:
            if keyword in upper_text:
                counts[keyword] += 1
                matched = True

        if not matched:
            other_count += 1

        if "ERROR" in upper_text:
            error_lines.append(text)

    return counts, other_count, error_lines


def display_summary(lines):
    counts, other_count, error_lines = summarize_log(lines)
    total_lines = len([line for line in lines if line.strip()])

    if total_lines == 0:
        print("The file contains no log entries.")
        return

    print("\n" + "=" * 60)
    print("LOG SUMMARY")
    print("=" * 60)
    print(f"  File name    : {os.path.basename(log_path)}")
    print(f"  Total entries: {total_lines}")
    print("-" * 60)
    print(f"  {'Category':<12} {'Count':>8} {'Percent':>10}  Chart")
    print("-" * 60)

    for keyword in KEYWORDS:
        count = counts[keyword]
        percentage = count / total_lines * 100
        print(
            f"  {keyword:<12} {count:>8} {percentage:>9.2f}%  "
            f"{'#' * min(count, 40)}"
        )

    print(
        f"  {'OTHER':<12} {other_count:>8} "
        f"{other_count / total_lines * 100:>9.2f}%"
    )
    print("-" * 60)
    print(f"  Errors detected: {counts['ERROR']}")
    print(f"  Warnings detected: {counts['WARNING']}")

    if error_lines:
        print("\n  Recent ERROR entries:")
        for entry in error_lines[:5]:
            print(f"    - {entry}")

    if counts["ERROR"] == 0:
        print("\n  System status: Healthy (no errors found).")
    elif counts["ERROR"] <= 2:
        print("\n  System status: Needs attention (a few errors found).")
    else:
        print("\n  System status: Critical (multiple errors found).")

    print("=" * 60)


log_path = input("Enter log file name (press Enter for sample.log): ").strip()
if not log_path:
    log_path = "sample.log"

if not os.path.isabs(log_path):
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), log_path)

lines = read_log_file(log_path)
if lines:
    display_summary(lines)
