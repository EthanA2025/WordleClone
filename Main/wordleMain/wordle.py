'''
@Author Ethan Abbate
A game that is a clone of the popular website 'wordle'
'''
import csv


def chooseSecret(filename):
    #with open(filename) as csv_file:
    return 0

'''
Prints the inital welcome message to the user
'''
def printWelcome(): 
    print("Welcome to wordleClone! Time to guess your 5 letter word.")
    print(['_', '_', '_', '_', '_'])

'''
Prompts the user to enter a guess for the word
'''
def enterguess(secretWord):

    guess = input("Enter guess: ")
    for i in range(0, len(guess)):
        if (guess[i] == secretWord[i]):
            print("here")
        elif (guess[i] in secretWord[i]):
            print("in word")
        else:
            print("not in word")

    return -1

def main():
    tries = 6 # the user has 6 tries to get the word correct

    printWelcome()
    while (tries > 1):
        enterguess()
        tries -= 1
    
main()