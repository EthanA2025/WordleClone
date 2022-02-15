'''
@Author Ethan Abbate
A game that is a clone of the popular website 'wordle'
'''
import random
'''
Chooses a random secret word from a csv file
'''
def chooseSecret(filename):

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
# def enterguess(secretWord):

#     guess = input("Enter guess: ")
#     for i in range(0, len(guess)):
#         if (guess[i] == secretWord[i]):
#             print("here")
#         elif (guess[i] in secretWord[i]):
#             print("in word")
#         else:
#             print("not in word")

#     return -1

def main():
    tries = 6 # the user has 6 tries to get the word correct
    printWelcome()
    secret = chooseSecret("words/words.txt")
    while (tries > 1):
        # enterguess(secret)
        tries -= 1
    
main()