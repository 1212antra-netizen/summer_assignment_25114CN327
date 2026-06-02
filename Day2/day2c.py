n=int(input("enter a number:"))
product=1
while n>0:
    num=n%10
    product=product*num
    n=n//10
print("product of digits is =",product)
    
    