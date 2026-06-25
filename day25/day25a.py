n=int(input("enter number of elements:"))
arr1=[]
for i in range(n):
    num=int(input("enter array element:"))
    arr1.append(num)
    arr1.sort()
m=int(input("enter number of elements:"))
arr2=[]
for i in range(m):
    num=int(input("enter array element:"))
    arr2.append(num)
    arr2.sort()
merged=arr1+arr2
merged.sort()
print("merged array is :",merged)