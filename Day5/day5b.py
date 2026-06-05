def is_strong_number(n):
    sum=0
    temp=n
    while n>0:
        num=n%10
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        sum=sum+fact
        n=n//10
    if temp==sum:
        return True
    else:
        return False
x=int(input("Enter a number: "))
if is_strong_number(x):
    print(f"{x} is a strong number.")
else:
    print(f"{x} is not a strong number.")