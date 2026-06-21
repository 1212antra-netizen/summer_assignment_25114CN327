n=int(input("enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter elements:"))
    arr.append(num)
arr.sort()
max_count=1
current_count=1
max_element=arr[0]
for i in range(1,n):
    if arr[i]==arr[i-1]:
        current_count+=1
    else:
        current_count=1
    if current_count>max_count:
        max_count=current_count
        max_element=arr[i]
print("maximum frequency element:",max_element)
print("maximum frequency is:",max_count)