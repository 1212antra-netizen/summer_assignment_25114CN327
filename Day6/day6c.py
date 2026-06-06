num=int(input("Enter a number: "))
count=0
while num>0:
    count+=num&1
    num=num>>1
print("number of set bits in a given binary number is :",count)