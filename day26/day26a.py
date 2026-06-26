import random
number = random.randint(1, 100)
print("it is a number guessing game")
print("Guess a number between 1 and 100")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed it in", attempts, "attempts.")
        break