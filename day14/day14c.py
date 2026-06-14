n=int(input("enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter elements:"))
    arr.append(num)
largest=arr[0]
second_largest=arr[0]
for num in arr:
    if num>largest:
            second_largest=largest
            largest=num
    elif num>second_largest and num!=largest:
            second_largest=num
print("second largest is :",second_largest)
            

