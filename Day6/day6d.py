x=int(input("Enter a number: "))
n=int(input("enter power to which the number is to be raised: "))
result=1
for i in range(n):
    result*=x
print(f"{x} raised to the power {n} is {result}")
