class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"  Name   : {self.name}")
        print(f"  Age    : {self.age}")
        print(f"  Marks  : {self.marks}")
        print(f"  Grade  : {self.get_grade()}")

    def __str__(self):
        return f"STUDENT,{self.name},{self.age},{self.marks}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        print(f"  Name    : {self.name}")
        print(f"  Age     : {self.age}")
        print(f"  Subject : {self.subject}")

    def __str__(self):
        return f"TEACHER,{self.name},{self.age},{self.subject}"


class Course:
    def __init__(self, course_name, teacher_name):
        self.course_name = course_name
        self.teacher_name = teacher_name

    def display(self):
        print(f"  Course  : {self.course_name}")
        print(f"  Teacher : {self.teacher_name}")

    def __str__(self):
        return f"COURSE,{self.course_name},{self.teacher_name}"


def save_record(record):
    with open("records.txt", "a") as file:
        file.write(str(record) + "\n")
    print("Record saved.")


def view_records():
    try:
        with open("records.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No records found.")
            return

        print("\n" + "=" * 40)
        for line in lines:
            parts = line.strip().split(",")
            if parts[0] == "STUDENT":
                s = Student(parts[1], int(parts[2]), float(parts[3]))
                s.display()
            elif parts[0] == "TEACHER":
                t = Teacher(parts[1], int(parts[2]), parts[3])
                t.display()
            elif parts[0] == "COURSE":
                c = Course(parts[1], parts[2])
                c.display()
            print("-" * 40)

    except FileNotFoundError:
        print("No records file found.")


def main():
    print("=" * 40)
    print("   OOP Grade Management System")
    print("=" * 40)

    while True:
        print("\n1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. View All Records")
        print("5. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            marks = float(input("Enter marks: "))
            save_record(Student(name, age, marks))

        elif choice == "2":
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            subject = input("Enter subject: ").strip()
            save_record(Teacher(name, age, subject))

        elif choice == "3":
            course_name = input("Enter course name: ").strip()
            teacher_name = input("Enter teacher name: ").strip()
            save_record(Course(course_name, teacher_name))

        elif choice == "4":
            view_records()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()