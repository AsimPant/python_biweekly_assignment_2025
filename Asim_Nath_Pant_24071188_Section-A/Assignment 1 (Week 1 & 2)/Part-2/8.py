'''
8. Write a program to create a number guessing game for the user. The program should ask the user to input a number. The program specifications are as mentioned below.
    I. The program should generate a random number for the answer.
    II. The program should prompt the user for a number input.
    III. The program should provide the feedback to the user after each guesses (e.g. “Too high”, “Too low” or “Correct number”).
    IV. The program should check the user input for 5 times and allow the users to guess for at most 5 times if their input don’t match the answer number.
    V. If the user is not able to guess the answer within 5 times, the program should display “Game Over” message and exit.

'''

import random   # Importing random module

# Generating a random number between 1 and 50
number = random.randint(1, 50)

print("Welcome to the Number Guessing Game!")
print("You have 5 chances to guess the correct number between 1 and 50.")

tries = 5  # Maximum number of attempts

for k in range(1, tries + 1):
    guess = int(input(f"\nAttempt ({k}/{tries}); Please enter your guess: "))

    # Checking the user's guess
    if guess == number:
        print("\nCongratulations! You guessed the right number (", number, ") in", k, "attempts.")
        break
    elif guess < number:
        print("\nThe number is low! Try again.")
    else:
        print("\nThe number is high! Try again.")

# If the user fails all attempts
else:
    print("\nGame Over! The correct number was ", number, ". Try better next time!")