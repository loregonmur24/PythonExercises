"""
EMPLOYEE MANAGER - SIMPLE VERSION
=================================
A simple program to manage employee information.
Type commands to add, view, search, or remove employees.
"""

class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def display(self):
        print(f"\n📋 ID: {self.emp_id}")
        print(f"   👤 Name: {self.name}")
        print(f"   💼 Position: {self.position}")
        print(f"   💰 Salary: ${self.salary}")

class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.next_id = 1
    
    def add_employee(self):
        print("\n➕ ADD NEW EMPLOYEE")
        print("-" * 30)
        
        name = input("Employee name: ").strip()
        if not name:
            print("❌ Name cannot be empty!")
            return
        
        position = input("Position: ").strip() or "Not specified"
        
        try:
            salary = float(input("Salary: $").strip())
        except:
            print("❌ Invalid salary! Using 0")
            salary = 0
        
        # Auto-generate ID (EMP001, EMP002, etc.)
        emp_id = f"EMP{self.next_id:03d}"
        self.next_id += 1
        
        employee = Employee(emp_id, name, position, salary)
        self.employees.append(employee)
        
        print(f"\n✅ Added {name} with ID: {emp_id}")
        print(f"📊 Total employees: {len(self.employees)}")
    
    def list_employees(self):
        if not self.employees:
            print("\n📭 No employees yet!")
            return
        
        print(f"\n📋 EMPLOYEE LIST ({len(self.employees)} employees)")
        print("-" * 40)
        
        for i, emp in enumerate(self.employees, 1):
            print(f"{i:2}. {emp.emp_id} - {emp.name} ({emp.position})")
    
    def search_employee(self):
        if not self.employees:
            print("\n📭 No employees to search!")
            return
        
        print("\n🔍 SEARCH EMPLOYEE")
        print("-" * 30)
        
        search = input("Search by name or ID: ").lower().strip()
        
        found = []
        for emp in self.employees:
            if (search in emp.name.lower() or 
                search in emp.emp_id.lower()):
                found.append(emp)
        
        if found:
            print(f"\n✅ Found {len(found)} employee(s):")
            for emp in found:
                print(f"   • {emp.emp_id}: {emp.name} - {emp.position}")
            
            # Show details if only one found
            if len(found) == 1:
                show = input("\nShow details? (y/n): ").lower()
                if show == 'y':
                    found[0].display()
        else:
            print(f"\n❌ No employee found with '{search}'")
    
    def view_details(self):
        if not self.employees:
            print("\n📭 No employees yet!")
            return
        
        self.list_employees()
        
        try:
            num = int(input("\nEnter employee number to view: "))
            if 1 <= num <= len(self.employees):
                self.employees[num-1].display()
            else:
                print("❌ Invalid number!")
        except:
            print("❌ Please enter a valid number!")
    
    def remove_employee(self):
        if not self.employees:
            print("\n📭 No employees to remove!")
            return
        
        self.list_employees()
        
        try:
            num = int(input("\nEnter employee number to remove: "))
            if 1 <= num <= len(self.employees):
                removed = self.employees.pop(num-1)
                print(f"\n🗑️ Removed {removed.name} (ID: {removed.emp_id})")
                print(f"📉 Total employees: {len(self.employees)}")
            else:
                print("❌ Invalid number!")
        except:
            print("❌ Please enter a valid number!")
    
    def show_stats(self):
        if not self.employees:
            print("\n📭 No employees for statistics!")
            return
        
        total_salary = sum(emp.salary for emp in self.employees)
        avg_salary = total_salary / len(self.employees)
        
        print("\n📊 STATISTICS")
        print("-" * 30)
        print(f"Total employees: {len(self.employees)}")
        print(f"Total salary: ${total_salary:,.2f}")
        print(f"Average salary: ${avg_salary:,.2f}")
        
        # Find highest paid
        highest = max(self.employees, key=lambda x: x.salary)
        print(f"Highest paid: {highest.name} (${highest.salary:,.2f})")

def show_help():
    print("""
🆘 HELP - Available Commands:
    add     - Add new employee
    list    - Show all employees
    search  - Search by name/ID
    view    - View employee details
    remove  - Remove an employee
    stats   - Show statistics
    help    - Show this help
    exit    - Exit program
    
💡 Tip: Just type the command and press Enter!
    """)

def main():
    print("\n" + "=" * 50)
    print("💼 EMPLOYEE MANAGER v1.0")
    print("=" * 50)
    print("Manage your employees easily!")
    print("Type 'help' to see all commands")
    
    manager = EmployeeManager()
    
    # Add some sample employees to start
    sample_employees = [
        Employee("EMP001", "John Smith", "Manager", 75000),
        Employee("EMP002", "Sarah Johnson", "Developer", 65000),
        Employee("EMP003", "Mike Wilson", "Designer", 55000)
    ]
    
    add_samples = input("\nAdd sample employees to start? (y/n): ").lower()
    if add_samples == 'y':
        manager.employees.extend(sample_employees)
        manager.next_id = 4
        print("✅ Added 3 sample employees!")
        print("📊 You now have 3 employees to manage")
    
    while True:
        print("\n" + "-" * 30)
        command = input("\nEnter command: ").lower().strip()
        
        if command == "add" or command == "a":
            manager.add_employee()
        
        elif command == "list" or command == "l":
            manager.list_employees()
        
        elif command == "search" or command == "s":
            manager.search_employee()
        
        elif command == "view" or command == "v":
            manager.view_details()
        
        elif command == "remove" or command == "r" or command == "delete":
            manager.remove_employee()
        
        elif command == "stats" or command == "statistics":
            manager.show_stats()
        
        elif command == "help" or command == "h" or command == "?":
            show_help()
        
        elif command == "exit" or command == "quit" or command == "q":
            print(f"\n👋 Goodbye!")
            print(f"📊 You managed {len(manager.employees)} employee(s)")
            print("Thanks for using Employee Manager! 💼")
            break
        
        elif command == "":
            continue
        
        else:
            print(f"❌ Unknown command: '{command}'")
            print("💡 Type 'help' to see available commands")

# Run the program
if __name__ == "__main__":
    main()
