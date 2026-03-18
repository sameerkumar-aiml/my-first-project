import random

print("Welcome to Number Guessing Game!")
number = random.randint(1, 20)
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print(f"Congratulations! You guessed it right: {number}")