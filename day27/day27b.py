class Employee:
    def __init__(self, eid, name, age, department, salary):
        self.eid = eid
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def display(self):
        print(f"ID: {self.eid}, Name: {self.name}, Age: {self.age}, Dept: {self.department}, Salary: {self.salary}")


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = [] 

    def add_employee(self):
        eid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        dept = input("Enter Department: ")
        salary = input("Enter Salary: ")

        emp = Employee(eid, name, age, dept, salary)
        self.employees.append(emp)
        print("Employee added successfully!\n")

    def view_employees(self):
        if not self.employees:
            print("No records found.\n")
            return

        for emp in self.employees:
            emp.display()
        print()

    def search_employee(self):
        eid = input("Enter Employee ID to search: ")
        for emp in self.employees:
            if emp.eid == eid:
                print("Employee found:")
                emp.display()
                print()
                return
        print("Employee not found.\n")

    def update_employee(self):
        eid = input("Enter Employee ID to update: ")
        for emp in self.employees:
            if emp.eid == eid:
                emp.name = input("Enter new Name: ")
                emp.age = input("Enter new Age: ")
                emp.department = input("Enter new Department: ")
                emp.salary = input("Enter new Salary: ")
                print("Employee updated successfully!\n")
                return
        print("Employee not found.\n")

    def delete_employee(self):
        eid = input("Enter Employee ID to delete: ")
        for emp in self.employees:
            if emp.eid == eid:
                self.employees.remove(emp)
                print("Employee deleted successfully!\n")
                return
        print("Employee not found.\n")

ems = EmployeeManagementSystem()

while True:
    print("===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        ems.add_employee()
    elif choice == '2':
        ems.view_employees()
    elif choice == '3':
        ems.search_employee()
    elif choice == '4':
        ems.update_employee()
    elif choice == '5':
        ems.delete_employee()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")