def is_perfect(n):
    sum=0
    for i in range (1,n):
        if n%i==0:
            sum=sum+i
    return sum==n
x=int(input("enter a number="))
if is_perfect(x):
    print("number is perfect")
else:
    print("number is not perfect")

             