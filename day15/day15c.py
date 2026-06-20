def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
def left_rotate(arr,k):
    n=len(arr)
    k=k%n

    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    return arr
n=int(input("enter number of elements:"))
arr=[]
for i in range(n):
    num=int(input("enter elements:"))
    arr.append(num)
print("original array:",arr) 
k=int(input("enter rotation value k:"))
result=left_rotate(arr,k)
print("right rotated result is:",result)