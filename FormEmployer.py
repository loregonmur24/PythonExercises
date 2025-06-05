class Employee:
    def __init__(self, emp_id, name, position, salary,adress):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.adress=adress

    def display_info(self):
        print("Employee Information:")
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:.2f}")
        print(f"Adress: ${self.adress}")


class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print("Employee added successfully!")

    def list_employees(self):
        print("List of Employees:")
        for employee in self.employees:
            print(f"ID: {employee.emp_id}, Name: {employee.name}, Position: {employee.position}, Adress:{employee.adress}")

    def search_employee(self, name):
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                return employee
        return None


def main():
    print("Welcome to Employee Management System!")

    database = EmployeeDatabase()

    while True:
        print("\nOptions:")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Search Employee by Name")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = float(input("Enter employee salary: "))
            adress = input("Enter adress of empleyee: ")
            employee = Employee(emp_id, name, position, salary, adress)
            database.add_employee(employee)

        elif choice == '2':
            database.list_employees()

        elif choice == '3':
            search_name = input("Enter the name to search: ")
            found_employee = database.search_employee(search_name)
            if found_employee:
                found_employee.display_info()
            else:
                print("Employee not found.")

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()