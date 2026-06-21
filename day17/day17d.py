x=int(input("enter number of elements for array 1="))
arr1=[]
for i in range(x):
    num=int(input("enter elements:"))
    arr1.append(num)
y=int(input("enter number of elements for array 2="))
arr2=[]
for i in range(y):
    num=int(input("enter elements:"))
    arr2.append(num)
    freq={}
    result=[]
    for num in arr1:
        freq[num] = freq.get(num,0)+1
    for num in arr2:
        if num in freq and freq[num] > 0:
           result.append(num)
           freq[num]-=1
print("common elements:",result) 