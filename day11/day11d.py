def factorial(n):
    if n<0:
        return "the factorial does not exist"
    elif n==0:
        return 1
    else:
        fact=1
        for i in range (1,n+1):
            fact*=i
        return fact
x=int(input("enter a number:"))
print("factorial is :", factorial(x))