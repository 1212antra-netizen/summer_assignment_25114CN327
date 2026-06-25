def longest_word(s):
    longest="" 
    current=""
    for ch in s:
        if ch!=" ":
            current+=ch
        else:
            if len(current)>len(longest):
                longest = current
                current = ""
    if len(current) > len(longest): 
        longest = current
    return longest
s=input("enter sentence:")           
print("longest word is :",longest_word(s))