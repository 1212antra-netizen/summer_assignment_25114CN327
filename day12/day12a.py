def palindrome(n):
    temp=n
    rev=0
    while temp>0:
        num=temp%10
        rev=rev*10+num
        temp=temp//10
    return rev==n
x=int(input("enter a number:"))
if palindrome(x):
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")