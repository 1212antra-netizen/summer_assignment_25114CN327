s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
result = ""
for ch in s1:
    if ch in s2 and ch not in result:
        result += ch
print("Common characters:", result)