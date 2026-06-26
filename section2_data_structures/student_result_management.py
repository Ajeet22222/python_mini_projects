students = {}

def add_students():
    print("=" * 40)
    print("    Student Result Management System")
    print("=" * 40)

    n = int(input("How many students do you want to enter? "))

    for i in range(n):
        print(f"\nStudent {i + 1}")
        name = input("Enter student name: ").strip()
        marks = float(input("Enter marks (out of 100): "))
        students[name] = marks


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


def show_results():
    print("\n" + "=" * 40)
    print("           RESULT REPORT")
    print("=" * 40)

    grades = [(name, marks, get_grade(marks)) for name, marks in students.items()]

    for name, marks, grade in grades:
        print(f"  Name: {name}  |  Marks: {marks}  |  Grade: {grade}")

    print("-" * 40)

    total = sum(students.values())
    average = total / len(students)
    print(f"  Class Average  : {average:.2f}")

    topper = max(students, key=lambda name: students[name])
    print(f"  Topper         : {topper} with {students[topper]} marks")

    print("=" * 40)


add_students()
show_results()