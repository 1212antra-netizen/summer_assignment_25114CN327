rows = int(input("Rows: "))
cols = int(input("Cols: "))

print("Enter matrix:")
n = [list(map(int, input().split())) for i in range(rows)]

print("Transpose of matrix:")

for j in range(cols):
    for i in range(rows):
        print(n[i][j], end=" ")
    print()