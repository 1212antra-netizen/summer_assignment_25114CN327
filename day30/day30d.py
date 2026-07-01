# Student Management System

students = []

# Add Student
def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    student = [roll, name, marks]   # array (list)
    students.append(student)

    print("Student added successfully!")


# Display Students
def display_students():
    if len(students) == 0:
        print("No students found")
        return

    print("\n--- Student List ---")
    for s in students:
        print("Roll:", s[0], "| Name:", s[1], "| Marks:", s[2])
    print("--------------------")

# Search Student
def search_student():
    roll = int(input("Enter Roll Number: "))

    for s in students:
        if s[0] == roll:
            print("Found:", s[1], "| Marks:", s[2])
            return

    print("Student not found")


# Update Marks
def update_marks():
    roll = int(input("Enter Roll Number: "))

    for s in students:
        if s[0] == roll:
            new_marks = int(input("Enter New Marks: "))
            s[2] = new_marks
            print("Marks updated")
            return

    print("Student not found")


# Delete Student
def delete_student():
    roll = int(input("Enter Roll Number: "))

    for s in students:
        if s[0] == roll:
            students.remove(s)
            print("Student deleted")
            return

    print("Student not found")


# Main Menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_marks()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")