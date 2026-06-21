def find_missing(arr,n):
    expected=n*(n+1)//2
    actual=sum(arr)
    return expected-actual
n=int(input("enter number of elements:"))
arr=[]
for i in range(n-1):
    num=int(input("enter elements:"))
    arr.append(num)
if len(arr) != n - 1:
    print("Error: You must enter", n - 1, "numbers")
else:
    missing=find_missing(arr,n)
    print("missing number is :",missing)
    