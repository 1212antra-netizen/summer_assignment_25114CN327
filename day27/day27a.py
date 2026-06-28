class Student:
    def __init__(self, sid, name, age, course):
        self.sid = sid
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"ID: {self.sid}, Name: {self.name}, Age: {self.age}, Course: {self.course}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = Student(sid, name, age, course)
        self.students.append(student)
        print("Student added successfully!\n")

    def view_students(self):
        if not self.students:
            print("No records found.\n")
            return

        for student in self.students:
            student.display()
        print()

    def search_student(self):
        sid = input("Enter Student ID to search: ")
        for student in self.students:
            if student.sid == sid:
                print("Student found:")
                student.display()
                print()
                return
        print("Student not found.\n")

    def update_student(self):
        sid = input("Enter Student ID to update: ")
        for student in self.students:
            if student.sid == sid:
                student.name = input("Enter new Name: ")
                student.age = input("Enter new Age: ")
                student.course = input("Enter new Course: ")
                print("Student updated successfully!\n")
                return
        print("Student not found.\n")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ")
        for student in self.students:
            if student.sid == sid:
                self.students.remove(student)
                print("Student deleted successfully!\n")
                return
        print("Student not found.\n")

sms = StudentManagementSystem()

while True:
    print("Student Record Management System")
    print("1. Add Student")
    print("2. view student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    print("your choice is:",choice)

    if choice == '1':
        sms.add_student()
    elif choice == '2':
        sms.view_students()
    elif choice == '3':
        sms.search_student()
    elif choice == '4':
        sms.update_student()
    elif choice == '5':
        sms.delete_student()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")       
