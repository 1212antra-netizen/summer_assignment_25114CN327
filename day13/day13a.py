n=int(input("enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter element:"))
    arr.append(num)
print("array elements are:")
for i in arr:
    print(i,end=" ")