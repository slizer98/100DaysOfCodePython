
import random
from art import logo

def check_answer(guess, answer, attempts):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return answer

def get_difficulty():
    """Gets difficulty from user. Returns 'easy' or 'hard'."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

attempts = get_difficulty()
number = random.randint(1, 100)
guess = 0
while guess != number:
    print(f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))
    attempts = check_answer(guess, number, attempts)
    if attempts == 0:
        print(f"You've run out of guesses, you lose. The answer was {number}.")
        number = guess
    elif guess != number:
        print("Guess again.")
  
