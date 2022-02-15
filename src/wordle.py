'''
@Author Ethan Abbate
A game that is a clone of the popular website 'wordle'
'''
import random

'''
Chooses a random secret word from a csv file
'''

def choose_secret(filename):

    with open(filename) as file:
        word_bank = file.read().strip().split()
    secret_word = random.choice(word_bank)
    
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
Prompts the user to enter a guess for the word
'''
def enter_guess(guess, secret_word):
    correct = False
    if guess == secret_word:
        print("This is the correct word!")
        print(f"\u001b[32m{secret_word}\u001b[0m")
        correct = True
        return correct # stops game loop and the user wins if guess and secret are equal.
    else:
        for i in range(0, len(guess)): # check if the letters are in the right spot or in the word wrong spot
            if (guess[i] == secret_word[i]):
                green = guess[i]
                guess[i] = "\u001b[32m" + green + "\u001b[0m" # change to green
            elif (guess[i] in secret_word[i]):
                yellow = guess[i]
                guess[i] = "\u001b[33m" + yellow + "\u001b[0m" # change to yellow
        
        print("Your guess results: " + guess)    
        return correct

def game():
    tries = 6 # the user has 6 tries to get the word correct
    correct = False

    printWelcome()
    secret = choose_secret("words/words.txt")
    print(secret)
    while tries > 1 and correct == False:
        guess = input("\nenter guess: ")
        correct = enter_guess(guess, secret)
        tries -= 1

def main():
    game()
    
main()