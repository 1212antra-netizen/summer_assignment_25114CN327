def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print(f"lcm of {x} and {y} is: {lcm(x,y)}")