# 1. NUMBER GAME



import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the number guessing game 👍!") 
    print("Select a number between 1 to 100 😊")

# start a loop 

    while True:
        try:
            # Get the user guess
                
            user_guess = int(input("Enter your guess:"))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("The number is out of range please enter a number between 1 to 100" )

            elif user_guess < secret_number:
                print("Too low! Try to higher number;")

            elif user_guess > secret_number:
                print("Too high! Try to lower number;")

            else:
                print(f"🎉 congrats you guess the number at {attempts} attempts.")
                break
            # The loop is break here

        except ValueError:
            print("Invalid input! please enter a valid number")

number_guessing_game()



