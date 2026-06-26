import csv

def compute_grade(marks):
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

def read_students(input_file):
    students = []
    try:
        with open(input_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    return students

def process_students(students):
    updated = []
    for student in students:
        try:
            marks = float(student["Marks"])
            grade = compute_grade(marks)
            updated.append({
                "Name": student["Name"],
                "Marks": marks,
                "Grade": grade
            })
        except ValueError:
            print(f"Invalid marks for student: {student['Name']}. Skipping.")
    return updated

def write_results(students, output_file):
    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Marks", "Grade"])
        writer.writeheader()
        writer.writerows(students)
    print(f"Results saved to '{output_file}' successfully.")

def show_results(students):
    print("\n" + "=" * 40)
    print("         STUDENT GRADE REPORT")
    print("=" * 40)
    for student in students:
        print(f"  Name  : {student['Name']}")
        print(f"  Marks : {student['Marks']}")
        print(f"  Grade : {student['Grade']}")
        print("-" * 40)

def create_sample_input():
    with open("students_input.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Marks"])
        writer.writeheader()
        writer.writerows([
            {"Name": "Alice", "Marks": 92},
            {"Name": "Bob", "Marks": 75},
            {"Name": "Charlie", "Marks": 58},
            {"Name": "Diana", "Marks": 85},
            {"Name": "Evan", "Marks": 43}
        ])
    print("Sample input file 'students_input.csv' created.")

def main():
    print("=" * 40)
    print("    Student Grade File Manager")
    print("=" * 40)

    print("\n1. Create sample input file and process")
    print("2. Enter custom input file name")
    print("-" * 40)

    choice = input("Enter your choice (1-2): ").strip()

    if choice == "1":
        create_sample_input()
        input_file = "students_input.csv"
    elif choice == "2":
        input_file = input("Enter input CSV file name: ").strip()
    else:
        print("Invalid choice.")
        return

    students = read_students(input_file)

    if not students:
        print("No student data found.")
        return

    updated_students = process_students(students)
    show_results(updated_students)
    write_results(updated_students, "students_output.csv")

main()