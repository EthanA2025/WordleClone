'''
@Author Ethan Abbate
A game that is a clone of the popular website 'wordle'
'''
import random

WORD_BANK = dict() # global dictionary for all the words

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
        "\nGreen/Red indicates the letter is in the right spot in the word." + \
        "\nYellow/Blue indicates it is in the word but wrong position.")
    print(['_', '_', '_', '_', '_'])
    con = input("press 1 for high contrast: ")
    if con == '1':
        return True

'''
checks for a valid word. A valid word is not greater than 5 letters and in the WORD_BANK
'''
def check_valid(guessed_word):
    if guessed_word in WORD_BANK.values():
        return True
    return False

'''
checks the guess that the user has entered.
'''
def check_guess(guess, secret_word, contrast):
    guess = guess.lower()
    correct = False
    if guess == secret_word:
        print("This is the correct word!")
        print(f"\u001b[32m{secret_word}\u001b[0m")
        correct = 1
        return correct # stops game loop and the user wins if guess and secret are equal.
    else:
        word = ""
        for i in range(0, len(guess)):
            if guess[i] == secret_word[i]:
                if contrast:
                    color_correct = "\u001b[31m" + guess[i] + "\u001b[0m" # change to orange/green if right spot right letter
                else:
                    color_correct = "\u001b[32m" + guess[i] + "\u001b[0m"
                word += color_correct 
            elif guess[i] in secret_word:
                if contrast:
                    in_word_color = "\u001b[34m" + guess[i] + "\u001b[0m" # change to blue/yellow if right spot wrong letter
                else:
                    in_word_color = "\u001b[33m" + guess[i] + "\u001b[0m"
                word += in_word_color
            else:
                word += guess[i]
        
        print("Your guess results: " + word)    
        return correct

def game():
    tries = 6 # the user has 6 tries to get the word correct
    correct = False

    contrast = printWelcome()
    secret = choose_secret("words/words.txt")
    # print(secret)
    while tries > 0 and correct == False:
        guess = input("\nenter guess: ")
        valid = check_valid(guess)
        if valid:   
            correct = check_guess(guess, secret, contrast)
            tries -= 1
        else:
            print("invalid guess! ")
    print("the word was: " + secret)

def main():
    game()

if __name__ == "__main__":
    main()