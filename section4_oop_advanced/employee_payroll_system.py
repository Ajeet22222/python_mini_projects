import datetime


def log_salary(func):
    def wrapper(self):
        salary = func(self)
        with open("payroll.txt", "a") as file:
            file.write(f"{datetime.date.today()} | {self.name} | {self.__class__.__name__} | Salary: Rs.{salary:.2f}\n")
        return salary
    return wrapper


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        pass

    def display(self):
        salary = self.calculate_salary()
        print(f"  Name        : {self.name}")
        print(f"  ID          : {self.employee_id}")
        print(f"  Type        : {self.__class__.__name__}")
        print(f"  Salary      : Rs.{salary:.2f}")


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    @log_salary
    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @log_salary
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


def main():
    employees = []

    print("=" * 40)
    print("      Employee Payroll System")
    print("=" * 40)

    while True:
        print("\n1. Add Full Time Employee")
        print("2. Add Part Time Employee")
        print("3. Show All Salaries")
        print("4. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            emp_id = input("Enter employee ID: ").strip()
            salary = float(input("Enter monthly salary: Rs."))
            employees.append(FullTimeEmployee(name, emp_id, salary))
            print("Full time employee added.")

        elif choice == "2":
            name = input("Enter name: ").strip()
            emp_id = input("Enter employee ID: ").strip()
            rate = float(input("Enter hourly rate: Rs."))
            hours = float(input("Enter hours worked: "))
            employees.append(PartTimeEmployee(name, emp_id, rate, hours))
            print("Part time employee added.")

        elif choice == "3":
            if not employees:
                print("No employees added yet.")
            else:
                print("\n" + "=" * 40)
                print("         PAYROLL REPORT")
                print("=" * 40)
                for emp in employees:
                    emp.display()
                    print("-" * 40)
                print("Salary log saved to payroll.txt")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


main()