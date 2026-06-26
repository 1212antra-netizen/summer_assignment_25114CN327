print("let's start the quiz!!")
name = input("Enter your name: ")
print("Hi", name, "! Let's start the quiz.\n")
score=0
print("1.who was the first prime minister of india")
print("a] lal bahadur shastri")
print("b] jawahar lal nehru")
print("c] Rajeev gandhi")
print("d] Indira gandhi")
answer=input("your answer:")
if answer=="b":
    print("correct")
    score+=1
else:
    print("wrong! correct answer is jawahar lal nehru")

print("2. Who is known as the Father of Computer?")
print("a) Charles Babbage")
print("b) Elon Musk")
print("c) Bill Gates")
ans = input("Your answer: ")

if ans.lower() == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is Charles Babbage\n")
print("3. Which is the largest ocean in the world?")
print("a) Indian Ocean")
print("b) Atlantic Ocean")
print("c) Pacific Ocean")
ans = input("Your answer: ")

if ans.lower() == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is Pacific Ocean\n")

 
print("4. What is the square root of 64?")
print("a) 6")
print("b) 8")
print("c) 10")
ans = input("Your answer: ")

if ans.lower() == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is 8\n")
print( name, ", your score is:", score, "/4")

if score == 4:
    print(" Excellent!")
elif score >= 2:
    print(" Good job!")
else:
    print("Keep practicing!")
