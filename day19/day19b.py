rows = int(input("Rows: "))
cols = int(input("Cols: "))

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
print("Subtraction of matrices (A - B):")
for i in range(rows):
    for j in range(cols):
        print(a[i][j] - b[i][j], end=" ")
    print()