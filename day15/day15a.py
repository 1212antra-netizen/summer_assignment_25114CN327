n=int(input("enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter elements:"))
    arr.append(num)
print("original array:",arr)
start=0
end=len(arr)-1
while start<end:
    arr[start],arr[end]=arr[end],arr[start]
    start=start+1
    end=end-1

print("reversed array is :",arr)