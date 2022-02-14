import random
import sys


answer = random.randint(1,100)
guess = 0
guesses = 0
guessed = False


def new_game():
    
    print("Guess a random integer! Instead of guessing between 1 and 100 like normal, I'll let you in on a secret. The answer is " + find_clue(answer) + " 50.\n\nYou get 10 guesses.\nGood luck!")

def guess(answer, guesses):
    
    global guessed
    
    try:
        guess = int(input("\nGuess a number: "))
    except ValueError:
        print("Your input isn't an integer!")
        sys.exit()
        
    if not guess >= 1 and not guess <= 100:
        print("Your guess isn't between 1 and 100!")
        sys.exit()
        
    if guess == answer:
        print("Congratulations! You took " + str(guesses) + " guesses to get the right answer!")
        guessed = True
    elif guess > answer:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
        
def find_clue(answer):
    
    if answer >= 50:
        return "above or equal to"
    else:
        return "below"

def play_again():
    
    match input("Would you like to play again? (y/yes/n/no): "):
        
        case "y" | "yes":
            return True
        case "n" | "no":
            return False
        case _:
            print("Your input is invalid!")
            return False

# this is the equivalent of a do-while loop is other languages like C#

while True:
    
    new_game()
    
    while guesses < 10 and not guessed:
        guesses += 1
        guess(answer, guesses)
        
    if not guessed:
        print("Unfortunately, you have run out of guesses.")
        
    guessed = False
    guesses = 0
    
    if not play_again():
        break