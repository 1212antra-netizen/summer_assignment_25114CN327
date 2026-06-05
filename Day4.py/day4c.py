n=int(input("Enter a number: "))
order=len(str(n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10   
if n==sum:
    print(f"{n} is an Armstrong number.")
else:    
    print(f"{n} is not an Armstrong number.")