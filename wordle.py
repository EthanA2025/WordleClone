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
    print(secret_word)
    
    return secret_word
'''
Prints the inital welcome message to the user
'''
def printWelcome(): 
    print("Welcome to wordleClone! Time to guess your 5 letter word.")
    print(['_', '_', '_', '_', '_'])

'''
Prompts the user to enter a guess for the word
'''
def enter_guess(guess, secret_word):
    correct = False
    if (guess == secret_word):
        print("This is the correct word!")
        print(f"\u001b[32m{secret_word}\u001b[0m")
        correct = True
        return correct
    else:
        return correct
    
    # stops game loop and the user wins if guess and secret are equal.
    
    # for i in range(0, len(guess)):
    #     if (guess[i] == secret_word[i]):
    #         print("here")
    #     elif (guess[i] in secret_word[i]):
    #         print("in word")
    #     else:
    #         print("not in word")

    # return correct

def main():
    tries = 6 # the user has 6 tries to get the word correct
    correct = False

    printWelcome()
    secret = choose_secret("words/words.txt")
    while (tries > 1 and correct == False):
        guess = input("enter guess: ")
        correct = enter_guess(guess, secret)
        tries -= 1
    
main()