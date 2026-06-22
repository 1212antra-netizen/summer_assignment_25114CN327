# Input rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
a = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"a[{i}][{j}]: "))
        row.append(val)
    a.append(row)

print("Enter elements of second matrix:")
b = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"b[{i}][{j}]: "))
        row.append(val)
    b.append(row)
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(a[i][j] + b[i][j])
    result.append(row)
print("Sum of matrices:")
for row in result:
    print(row)