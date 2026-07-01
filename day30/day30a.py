n = int(input("Enter number of students: "))
names = []
roll_numbers = []
marks = []

for i in range(n):
    print(f"\nEnter details for student {i + 1}")
    
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    mark = float(input("Enter marks: "))
    
    names.append(name)
    roll_numbers.append(roll)
    marks.append(mark)


print("\n--- Student Records ---")
for i in range(n):
    print(f"\nStudent {i + 1}")
    print("Name:", names[i])
    print("Roll Number:", roll_numbers[i])
    print("Marks:", marks[i])