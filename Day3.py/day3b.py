def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True
start=int(input("Enter a number: "))
end=int(input("Enter another number: "))
print(f"Prime numbers between {start} and {end} are:")
for x in range(start,end+1):
    if is_prime(x):
        print(x)