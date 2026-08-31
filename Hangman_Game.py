# Lets create Hangman Game

import random

HANGMAN_STAGES = ["""
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |

     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""]

# start with a function

def Hangman_Game():
    word_bank = ["python", "lorarbhozon", "devlopment", "knowledge", "knight", "snake", "rocket", "puzzle"] 

    secret_word = random.choice(word_bank).lower()
    guessed_letters = set()
    lives = 6

    print("Welcome to the Hangman Game 🤩🤩")

    # start a while loop

    while lives > 0:
        print(HANGMAN_STAGES[lives])
        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("Word to guess:" + "".join(display_word))
        print(f"Guess letters:{','.join(sorted(guessed_letters))if guessed_letters else 'None'}")
        print(f"Remainig lives:{lives}\n")

        # Win condition cheak
        if "_" not in display_word:
            print(f"🎉 Congratulations! You guessed the: {secret_word}")
            break

        guess = input("Guess a letter: ").strip().lower()

        if guess in guessed_letters:
            print(f"You already guess{guess} try a differnt word.\n")
            continue
        if len(guess) !=1 or not guess.isalpha():
            print("⚔️ Invalid input ! please type correctly.\n ")
            continue

        guessed_letters.add(guess)


        if guess in secret_word:
            print(f"✅ Good job !'{guess}' is in the word.")

        else:
            print(f"⚔️ Wrong guess !'{guess}' in not in the word.")
            lives -= 1

    if lives == 0:
        print(HANGMAN_STAGES[0])
        print(f"☠️  Game over ! Try your best agin.\n The word was:{secret_word}")

Hangman_Game()



        