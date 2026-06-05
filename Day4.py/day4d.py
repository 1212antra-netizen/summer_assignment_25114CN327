def armstron(num):
    sum = 0
    temp = num
    order=len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum
start = int(input("Enter a number: "))
end = int(input("Enter another number: "))
print(f"Armstrong numbers between {start} and {end} are:")
for n in range(start, end + 1):
    if armstron(n):
        print(n)

