def sum(n):
    if n<=0:
        return 0
    else:
        return n+sum(n-1)
x=int(input("Enter a number: "))
print(f"The sum of first {x} natural numbers is: {sum(x)}")
