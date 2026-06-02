n=int(input("enter a number:"))
rev=0
temp=n
while n>0:
    num=n%10
    rev=rev*10+num
    n=n//10
if temp==rev:
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")