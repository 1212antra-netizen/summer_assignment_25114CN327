x=int(input("enter number of elements for array 1="))
arr1=[]
for i in range(x):
    num=int(input("enter elements:"))
    arr1.append(num)
y=int(input("enter number of elements for array 2="))
arr2=[]
for i in range(y):
    num=int(input("enter elements:"))
    arr2.append(num)
set1 = set(arr1)
result = []

for num in arr2:
    if num in set1:
        result.append(num)
        set1.remove(num)

print("Intersection:", result)
