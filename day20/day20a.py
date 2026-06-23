# Input size
r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

# First matrix input
A = []
print("Enter elements of first matrix:")
for i in range(r1):
    row = []
    for j in range(c1):
        val = int(input())
        row.append(val)
    A.append(row)

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

# Check condition
if c1 != r2:
    print("Multiplication not possible")
    

B = []
print("Enter elements of second matrix:")
for i in range(r2):
    row = []
    for j in range(c2):
        val = int(input())
        row.append(val)
    B.append(row)

result = []
for i in range(r1):
    row = []
    for j in range(c2):
        row.append(0)
    result.append(row)

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j] = result[i][j] + A[i][k] * B[k][j]
print("Resultant matrix:")
for i in range(r1):
    for j in range(c2):
        print(result[i][j], end=" ")
    print()