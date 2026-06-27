import pandas as pd


def create_sample_csv():
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Diana", "Evan", "Fiona", "George", "Hannah"],
        "Marks": [92, 45, 78, 33, 85, 60, 55, 71]
    }
    df = pd.DataFrame(data)
    df.to_csv("student_marks.csv", index=False)
    print("Sample file 'student_marks.csv' created.")


def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def analyze(filename):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    df = df.dropna()

    df["Grade"] = df["Marks"].apply(get_grade)

    df["Result"] = df["Marks"].apply(lambda m: "Pass" if m >= 50 else "Fail")

    df = df.sort_values("Marks", ascending=False).reset_index(drop=True)

    passed = df[df["Result"] == "Pass"]
    failed = df[df["Result"] == "Fail"]

    print("\n" + "=" * 45)
    print("        STUDENT MARKS REPORT")
    print("=" * 45)
    print(df.to_string(index=False))

    print("\n" + "=" * 45)
    print("           PASSED STUDENTS")
    print("=" * 45)
    print(passed[["Name", "Marks", "Grade"]].to_string(index=False))

    print("\n" + "=" * 45)
    print("           FAILED STUDENTS")
    print("=" * 45)
    print(failed[["Name", "Marks", "Grade"]].to_string(index=False))

    print("\n" + "=" * 45)
    print("             SUMMARY")
    print("=" * 45)
    print(f"  Total Students  : {len(df)}")
    print(f"  Passed          : {len(passed)}")
    print(f"  Failed          : {len(failed)}")
    print(f"  Class Average   : {df['Marks'].mean():.2f}")
    print(f"  Highest Score   : {df['Marks'].max()}")
    print(f"  Lowest Score    : {df['Marks'].min()}")
    print("=" * 45)

    df.to_csv("student_marks_output.csv", index=False)
    print("\nCleaned data exported to 'student_marks_output.csv'")


def main():
    print("=" * 45)
    print("      Student Marks Analyzer")
    print("=" * 45)

    while True:
        print("\n1. Create sample CSV and analyze")
        print("2. Enter custom CSV filename")
        print("3. Exit")
        print("-" * 45)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            create_sample_csv()
            analyze("student_marks.csv")

        elif choice == "2":
            filename = input("Enter CSV filename: ").strip()
            analyze(filename)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()