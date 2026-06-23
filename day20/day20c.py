# Input size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
A = []
print("Enter elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input())
        row.append(val)
    A.append(row)

for i in range(rows):
    sum = 0
    for j in range(cols):
        sum = sum + A[i][j]
    print("Sum of row", i+1, "=", sum)