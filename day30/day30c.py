employees = []

# Add Employee
def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = int(input("Enter Salary: "))

    emp = {
        "id": emp_id,
        "name": name,
        "salary": salary
    }

    employees.append(emp)
    print("Employee added successfully!")


# Display Employees
def display_employees():
    if len(employees) == 0:
        print("No employees found")
        return

    for e in employees:
        print("ID:", e["id"], "| Name:", e["name"], "| Salary:", e["salary"])


# Search Employee
def search_employee():
    emp_id = int(input("Enter Employee ID: "))

    for e in employees:
        if e["id"] == emp_id:
            print("Found:", e["name"], "| Salary:", e["salary"])
            return

    print("Employee not found")


# Update Salary
def update_salary():
    emp_id = int(input("Enter Employee ID: "))

    for e in employees:
        if e["id"] == emp_id:
            new_salary = int(input("Enter New Salary: "))
            e["salary"] = new_salary
            print("Salary updated")
            return

    print("Employee not found")


# Delete Employee
def delete_employee():
    emp_id = int(input("Enter Employee ID: "))

    for e in employees:
        if e["id"] == emp_id:
            employees.remove(e)
            print("Employee deleted")
            return

    print("Employee not found")


# Menu
while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        display_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        update_salary()
    elif choice == '5':
        delete_employee()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")