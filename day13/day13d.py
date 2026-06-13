n=int(input("enter number of elements="))
arr=[]
for i in range (n):
    num=int(input("enter element:"))
    arr.append(num)
even_count=0
odd_count=0
for num in arr:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even element:",even_count)
print("odd element:",odd_count)
