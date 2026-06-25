s=input("enter a sentence:")
words=[]
current=" " 
for ch in s:
    if ch!=" ":
        current+=ch
    else:
        if current!=" ":
            words.append(current)
            current=" "
if current!=" ":
    words.append(current)
words.sort(key=len)
print("words sorted by length:")
for word in words:
    print(word)