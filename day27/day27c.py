import os
class Employee:
    def __init__(self,eid,name,salary):
        self.eid=id
        self.name=name
        self.salary=salary
    def calculate_salary(self):
        hra=0.20*self.salary
        da=0.10*self.salary
        gross=self.salary+hra+da
        return hra,da,gross
    def display(self):
        hra,da,gross=self.calculate_salary()
        print(f"{self.eid}\t,{self.name}\t,{self.salary}\t,{hra}\t,{da}\t,{gross}")
    
class Salarymanagementsystem:
    def __init__(self):
        self.employees=[]
    def add_employee(self):
        print("add employee")
        eid=input("employee id:")
        name=input("name:")
        salary=float(input("enter salary:"))
        self.employees.append(Employee(eid,name,salary)) 
        print("employee added!")
    def view_employees(self):
        if not self.employees:
            print("no records found")
        else:
            print("ID\tName\tBasic\tHRA\tDA\tGross")
            print("-" * 50)
            for emp in self.employees:
                emp.display()
        input("\nPress Enter to continue...")

    def search_employee(self):
        eid = input("\nEnter Employee ID: ")
        for emp in self.employees:
            if emp.eid == eid:
                print("\nEmployee Found:")
                print("ID\tName\tBasic\tHRA\tDA\tGross")
                emp.display()
                break
        else:
            print("Employee not found.")
        input("\nPress Enter to continue...")

    def delete_employee(self):
        eid = input("\nEnter Employee ID to delete: ")
        for emp in self.employees:
            if emp.eid == eid:
                self.employees.remove(emp)
                print("✅ Employee Deleted!")
                break
        else:
            print("Employee not found.")
        input("\nPress Enter to continue...")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

sms = Salarymanagementsystem()

while True:
    clear_screen()
    print("====== SALARY MANAGEMENT SYSTEM ======")
    print("1. Add Employee")
    print("2. View Salary Details")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")
    print("=====================================")

    choice = input("Enter your choice: ")

    if choice == '1':
        clear_screen()
        sms.add_employee()
    elif choice == '2':
        clear_screen()
        sms.view_employees()
    elif choice == '3':
        clear_screen()
        sms.search_employee()
    elif choice == '4':
        clear_screen()
        sms.delete_employee()
    elif choice == '5':
        print(" Exiting program...")
        break
    else:
        print("Invalid choice!")
        input("Press Enter to continue...")
             

    