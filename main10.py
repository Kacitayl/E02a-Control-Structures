#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
# printing "Greetings!"
colors = ['red','orange','yellow','green','blue','violet','purple']
# assigning 7 colors to the value of "colors"
play_again = ''
# giving an input option for whether you want to play again or not
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'):
# creating a while condition for when the input is not "n" or "no"
    match_color = random.choice(colors)
    # assigning the match_color to a random value of the 7 colors
    count = 0
    # starting the number of tries at 0
    color = ''
    # giving you and input for guessing the random color
    while (color != match_color):
    # While condition for if your guess is not correct
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        # Asks the question
        color = color.lower().strip()
        # controls for case sensitivity and strips input of extra spaces
        count += 1
        # adds 1 to the number of tries
        if (color == match_color):
        # if condition for when the guessed color = the randomly selected color
            print('Correct!')
            # prints "Correct!"
        else:
        # condition for when the if condition is False
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
            # prints "Sorry, try again." and tells you how many times you have guessed
    
    print('\nYou guessed it in {} tries!'.format(count))
    # prints how many tries you guessed it in

    if (count < best_count):
    # if condition for when the number of tries is less than your biggest number of tries
        print('This was your best guess so far!')
        # prints "This was your best guess so far!"
        best_count = count
        # changes your best_count to the new best_count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()
    # creates and input for whether or not you would like to play again

print('Thanks for playing!')
# prints "Thanks for playing!"