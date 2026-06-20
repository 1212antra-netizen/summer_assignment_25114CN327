n=int(input("enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter elements:"))
    arr.append(num)
print("original array:",arr)
j=0
for i in range(n):
    if arr[i]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1
print("output is:",arr)