s = input("Enter a sentence: ")
count_word = 0
in_word= False
for char in s:
    if char != ' ' and in_word == False:
        count_word += 1
        in_word = True
    elif char == ' ':
        in_word = False

print("Number of words:", count_word)