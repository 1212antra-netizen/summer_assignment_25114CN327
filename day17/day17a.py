x=int(input("enter number of elements for array 1="))
arr1=[]
for i in range(x):
    a=int(input("enter elements:"))
    arr1.append(a)
y=int(input("enter number of elements for array 2="))
arr2=[]
for i in range(y):
    b=int(input("enter elements:"))
    arr2.append(b)
merged=arr1+arr2
print("merged array:",merged)
