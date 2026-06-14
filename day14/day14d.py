n=int(input("enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter element:"))
    arr.append(num)
seen=set()
duplicate=set()
for num in arr:
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)
print(duplicate)
