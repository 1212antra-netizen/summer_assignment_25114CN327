n=int(input("Enter a number: "))
i=2
largest=0
while i*i<=n:
    if n%i==0:
        largest=i
        n=n//i
    else:
        i+=1
if n>largest:
    largest=n
print("largest prime factor is:", largest)

            
