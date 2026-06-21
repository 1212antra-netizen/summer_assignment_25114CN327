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
seen=set()
union=[]
for num in arr1+arr2:
    if num not in seen:
        seen.add(num)
        union.append(num)
print("union of array is :",union) 