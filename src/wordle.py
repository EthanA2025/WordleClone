'''
@Author Ethan Abbate
A game that is a clone of the popular website 'wordle'
'''
from ctypes.wintypes import WORD
import random

WORD_BANK = dict()

'''
Fills in the WORD_BANK dictionary and selects a random word from it
'''
def choose_secret(filename):

    with open(filename) as file:
        i = 0
        for line in file:
            line = line.strip()
            WORD_BANK[i] = line
            i += 1
    secret_word = random.choice(WORD_BANK)
    
    return secret_word
'''
Prints the inital welcome message to the user
'''
def printWelcome(): 
    print("Welcome to wordleClone!" + \
        "\nTime to guess your 5 letter word." + \
        "\nGreen indicates the letter is in the right spot in the word." + \
        "\nYellow indicates it is in the word but wrong position.")
    print(['_', '_', '_', '_', '_'])

'''
checks for a valid word.
'''
def check_valid(guessed_word):
    if guessed_word not in WORD_BANK:
        return False
    return True

'''
Prompts the user to enter a guess for the word
'''
def enter_guess(guess, secret_word):
    guess = guess.lower()
    correct = False
    valid = check_valid("words/words.txt", guess)
    if len(guess) > 5 or not valid:
        print("invalid word!")
        return correct
    if guess == secret_word:
        print("This is the correct word!")
        print(f"\u001b[32m{secret_word}\u001b[0m")
        correct = True
        return correct # stops game loop and the user wins if guess and secret are equal.
    else:
        word = ""
        for i in range(0, len(guess)):
            if guess[i] == secret_word[i]:
                green = "\u001b[32m" + guess[i] + "\u001b[0m"
                word += green # change to green
            elif guess[i] in secret_word: # multiple instances in word
                yellow = "\u001b[33m" + guess[i] + "\u001b[0m" # change to yellow
                word += yellow
            else:
                word += guess[i]
        
        print("Your guess results: " + word)    
        return correct

def game():
    tries = 6 # the user has 6 tries to get the word correct
    correct = False

    printWelcome()
    secret = choose_secret("words/words.txt")
    # print(secret)
    while tries > 1 and correct == False:
        guess = input("\nenter guess: ")
        correct = enter_guess(guess, secret)
        tries -= 1
    print("the word was: " + secret)

def main():
    game()

if __name__ == "__main__":
    main()