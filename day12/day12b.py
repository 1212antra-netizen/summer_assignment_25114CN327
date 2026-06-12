def armstrong(n):
    sum=0
    temp=n
    power=len(str(n))
    while temp>0:
        num=temp%10
        sum=sum+num**power
        temp=temp//10
    return sum==n
x=int(input("enter a number:"))
if armstrong(x):
    print("the number is armstrong")
else:
    print("the number is not armstrong")


