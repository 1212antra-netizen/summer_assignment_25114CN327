def max(a, b):
    if a > b:
        return a
    else:
        return b
x = int(input("enter first number:"))
y = int(input("enter second number:"))
print("maximum is :", max(x, y))