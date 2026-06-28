import os

class Student:
    def __init__(self, roll, name, m1, m2, m3, m4, m5):
        self.roll = roll
        self.name = name
        self.marks = [m1, m2, m3, m4, m5]

    def calculate(self):
        total = sum(self.marks)
        percentage = total / 5

        if percentage >= 90:
            grade = 'A'
        elif percentage >= 75:
            grade = 'B'
        elif percentage >= 50:
            grade = 'C'
        else:
            grade = 'Fail'

        return total, percentage, grade

    def display(self):
        total, percentage, grade = self.calculate()
        print(f"{self.roll}\t{self.name}\t{self.marks}\t{total}\t{percentage:.2f}\t{grade}")


class MarksheetSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        print("\n--- Add Student ---")
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")

        m1 = int(input("Enter marks for Subject 1: "))
        m2 = int(input("Enter marks for Subject 2: "))
        m3 = int(input("Enter marks for Subject 3: "))
        m4 = int(input("Enter marks for Subject 4: "))
        m5 = int(input("Enter marks for Subject 5: "))

        self.students.append(Student(roll, name, m1, m2, m3, m4, m5))
        print("✅ Student added!")
        input("Press Enter to continue...")

    def view_marksheets(self):
        print("\n--- Marksheet ---")
        if not self.students:
            print("No records found.")
        else:
            print("Roll\tName\tMarks\t\tTotal\t%\tGrade")
            print("-" * 100)
            for stu in self.students:
                stu.display()
        input("\nPress Enter to continue...")

    def search_student(self):
        roll = input("\nEnter Roll No: ")
        for stu in self.students:
            if stu.roll == roll:
                print("\nStudent Found:")
                stu.display()
                break
        else:
            print("Student not found.")
        input("\nPress Enter to continue...")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main Program
ms = MarksheetSystem()

while True:
    clear_screen()
    print("====== MARKSHEET SYSTEM ======")
    print("1. Add Student")
    print("2. View Marksheet")
    print("3. Search Student")
    print("4. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == '1':
        clear_screen()
        ms.add_student()
    elif choice == '2':
        clear_screen()
        ms.view_marksheets()
    elif choice == '3':
        clear_screen()
        ms.search_student()
    elif choice == '4':
        print(" Exiting program...")
        break
    else:
        print(" Invalid choice!")
        input("Press Enter to continue...")