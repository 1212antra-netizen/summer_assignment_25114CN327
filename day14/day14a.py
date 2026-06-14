n=int(input("enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter element="))
    arr.append(num)
target=int(input("enter element to be searched:"))
found=False
for i in range(len(arr)):
    if arr[i]==target:
        print("element is found at index:",i)
        found=True
        break
    else:
        print("element not found") 
         
     
