n=int(input("enter number of elements:"))
arr=[]

for i in range(n):
    num=int(input("enter element:"))
    arr.append(num)
    smallest=arr[0]
    largest=arr[0]
for num in arr:
    if num<smallest:
        smallest=num
    if num>largest:
        largest=num
print("largest element=",largest)
print("smallest element is=",smallest)