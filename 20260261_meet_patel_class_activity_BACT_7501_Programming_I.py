class EmployeeSystem:
    def __init__(self):
        # Private list to store all employee records
        self.__employees = []

    def add_employee(self, name, position, salary):
        employee = {
            "name": name.strip().title(),
            "position": position.strip().title(),
            "salary": salary
        }

        self.__employees.append(employee)
        print(f"\nEmployee '{employee['name']}' added successfully.")

    def display_employees(self):
        if not self.__employees:
            print("\nNo employee records found.")
            return

        print("\n========== EMPLOYEE RECORDS ==========")

        for index, employee in enumerate(self.__employees, start=1):
            print(f"\nEmployee #{index}")
            print(f"Name     : {employee['name']}")
            print(f"Position : {employee['position']}")
            print(f"Salary   : ${employee['salary']:,.2f}")

        print("======================================")

    def search_employee(self, name):
        name = name.strip().lower()

        for employee in self.__employees:
            if employee["name"].lower() == name:
                print("\nEmployee Found")
                print("--------------------------------------")
                print(f"Name     : {employee['name']}")
                print(f"Position : {employee['position']}")
                print(f"Salary   : ${employee['salary']:,.2f}")
                return

        print("\nEmployee not found.")

    def increase_salary(self, name, amount):
        name = name.strip().lower()

        for employee in self.__employees:
            if employee["name"].lower() == name:
                employee["salary"] += amount
                print(f"\nSalary increased successfully for {employee['name']}.")
                print(f"Updated Salary: ${employee['salary']:,.2f}")
                return

        print("\nEmployee not found.")


def get_valid_salary(message):
    while True:
        try:
            salary = float(input(message))

            if salary >= 0:
                return salary
            else:
                print("Amount cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")


# Main program
employee_system = EmployeeSystem()

while True:
    print("\n========== EMPLOYEE SALARY SYSTEM ==========")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Increase Employee Salary")
    print("5. Exit")
    print("============================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        salary = get_valid_salary("Enter employee salary: ")

        employee_system.add_employee(name, position, salary)

    elif choice == "2":
        employee_system.display_employees()

    elif choice == "3":
        name = input("Enter employee name to search: ")
        employee_system.search_employee(name)

    elif choice == "4":
        name = input("Enter employee name to increase salary: ")
        amount = get_valid_salary("Enter salary increase amount: ")

        employee_system.increase_salary(name, amount)

    elif choice == "5":
        print("\nThank you for using the Employee Salary System.")
        break

    else:
        print("\nInvalid choice. Please select a number from 1 to 5.")