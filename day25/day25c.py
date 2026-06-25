n = int(input("Enter number of names: "))
names = []

for i in range(n):
    name = input("Enter name: ")
    names.append(name)   
names.sort()

print("Names in alphabetical order:")
for name in names:
    print(name)