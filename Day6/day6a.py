n=int(input("Enter a number: "))
bin=""
while n>0:
    rem=n%2
    bin=str(rem)+bin
    n=n//2
print("decimal to binary conversion is :",bin)