s=input("enter string:")
seen=""
for ch in s:
    if ch not in seen:
        seen+=ch
print("string after duplicate removal:",seen)
