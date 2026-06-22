n = int(input("Enter size of square matrix: "))
print("Enter matrix:")
a = []
for i in range(n):
    row = []
    for j in range(n):
        val = int(input(f"a[{i}][{j}]: "))
        row.append(val)
    a.append(row)
primary_sum = 0
secondary_sum = 0
for i in range(n):
    primary_sum += a[i][i]              
    secondary_sum += a[i][n - i - 1] 
print("Primary diagonal sum:", primary_sum)
print("Secondary diagonal sum:", secondary_sum)