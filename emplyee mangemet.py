# Employee Management System

# Step 1 - Initial Data
employees = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Rajnish", "age": 30, "department": "IT", "salary": 65000},
    103: {"name": "Anita", "age": 25, "department": "Finance", "salary": 55000},
    104: {"name": "Kiran", "age": 28, "department": "Marketing", "salary": 60000}
}


# Step 3 - Add Employee Function
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("❌ Employee ID already exists. Please try again with a new ID.")
            return
        
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        employees[emp_id] = {
            "name": name,
            "age": age,
            "department": department,
            "salary": salary
        }
        print(f"✅ Employee {name} added successfully!\n")

    except ValueError:
        print("❌ Invalid input. Please try again.\n")


# Step 4 - View All Employees
def view_all_employees():
    if not employees:
        print("No employees available.\n")
        return

    print("\n--- Employee Records ---")
    print(f"{'ID':<6} {'Name':<15} {'Age':<5} {'Department':<12} {'Salary':<10}")
    print("-"*50)
    for emp_id, details in employees.items():
        print(f"{emp_id:<6} {details['name']:<15} {details['age']:<5} {details['department']:<12} {details['salary']:<10}")
    print()


# Step 5 - Search Employee
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print("\n--- Employee Found ---")
            print(f"ID        : {emp_id}")
            print(f"Name      : {details['name']}")
            print(f"Age       : {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary    : {details['salary']}\n")
        else:
            print("❌ Employee not found.\n")
    except ValueError:
        print("❌ Invalid input. Please enter a valid ID.\n")


# Step 2 & 6 - Menu System
def menu():
    while True:
        print("====== Employee Management System ======")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("🙏 Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.\n")


# Run the Program
menu()
