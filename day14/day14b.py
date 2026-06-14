n=int(input("enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter elements:"))
    arr.append(num)
for i in range(n):
    count=1
    if arr[i]==-1:
        continue
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            count=count+1
            arr[j]=-1
    print(f"{arr[i]} occurs {count}")
