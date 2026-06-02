n=int(input("enter a number:"))
sum=0
while n>0:
    num=n%10
    sum=sum+num
    n=n//10
print("the sum of digits of a number is=",sum)