# Input size
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

A = []
print("Enter elements:")
for i in range(r):
    row = []
    for j in range(c):
        val = int(input())
        row.append(val)
    A.append(row)
for j in range(c):
    sum = 0
    for i in range(r):
        sum = sum + A[i][j]
    print("Sum of column", j+1, "=", sum)