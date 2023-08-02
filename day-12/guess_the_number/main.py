import random
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def check_answer(user_guess, answer, attempts):
  if user_guess > answer:
    print("Too high.")
    return attempts - 1
  elif user_guess < answer:
    print("Too low.")
    return attempts - 1
  else:
    print(f"You got it! The answer was {answer}") 

def set_difficulty():
  difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  
  if difficulty_level == "easy":
    return EASY_LEVEL_ATTEMPTS
  else: 
    return HARD_LEVEL_ATTEMPTS

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  random_number = random.randint(1, 100)
  remaining_attempts = set_difficulty()

  user_guess = 0
  
  while user_guess != random_number:
    print(f"You have {remaining_attempts} remaining attempts to guess the number.")
    user_guess = int(input("Make a guess: "))
    remaining_attempts = check_answer(user_guess, random_number, remaining_attempts)
    if remaining_attempts == 0:
      print(f"You've run out of guesses. You lose. The number was {random_number}")
      return
    elif user_guess != random_number:
      print("Guess again.")

game()