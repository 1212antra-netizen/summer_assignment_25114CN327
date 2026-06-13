
n = int(input("Enter number of element:"))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

total = sum(arr)
average = total/n

print("Sum =", total)
print("Average =", average)