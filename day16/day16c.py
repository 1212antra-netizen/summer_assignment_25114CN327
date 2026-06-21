n=int(input("enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter elements:"))
    arr.append(num)
sum=int(input("enter pair sum: "))
if len(arr) != n:
    print("Error: Number of elements does not match n")
else:
    seen=set()
    found=False
    for num in arr:
        complement=sum-num
        if complement in seen:
            print("pair found:",num ,"+",complement,"=",sum)
            found=True
            break
        seen.add(num)
    if not found:
        print("no pair found")