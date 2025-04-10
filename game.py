# This is a simple number guessing game where the program generates a random number between 1 and 100 
import random 

low = 1
high = 100
guess_count = 0
max_guesses = 8
number = random.randint(low, high)

print(f"I'm thinking of a number between {low} and {high}. You have {max_guesses} guesses to find it.")    

while guess_count < max_guesses:
    try:
        guess = int(input(f"Enter a number between ({low} and {high}):"))
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue

    guess_count += 1

    if guess < number:
        print(f"{guess} is too low!")
    elif guess > number:
        print(f"{guess} is too high!")
    else:
        print(f"{guess} is correct! You found the number {number} in {guess_count} guesses.")
        break
else:
    print(f"❌ You've used all {max_guesses} guesses. The number was {number}.")
           



