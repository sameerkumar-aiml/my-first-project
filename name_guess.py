import random

print("Welcome to the Name Guessing Game!")

# 1. Create a list of names
names = ["Lucknow", "Python", "Gemini", "Robot", "Aman"]

# 2. Pick a random name from the list
target_name = random.choice(names)
guess = None

while guess != target_name:
    # 3. Input is already a string, so no need for int()
    guess = input(f"Guess a name from {names}: ")

    if guess != target_name:
        print("Incorrect! Try again.")

print(f"Congratulations! You guessed it right: {target_name}")
