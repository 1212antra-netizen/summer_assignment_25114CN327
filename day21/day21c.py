str=input("enter a string:")
vow=0
consonants=0
for char in str:
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        
        if char=="a"or char=="e" or char=="i" or char=="o"or char=="u"or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
            vow+=1
        else:
            consonants=consonants+1

print("vowels=",vow) 
print("Consonants =", consonants)
        

