n = int(input("Enter order of matrix: "))
A = []
print("Enter elements:")
for i in range(n):
    row = []
    for j in range(n):
        val = int(input())
        row.append(val)
    A.append(row)

is_symmetric = True
for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            is_symmetric = False
            break
if is_symmetric:
    print("Matrix is Symmetric")
else:
    print("Matrix is Not Symmetric")