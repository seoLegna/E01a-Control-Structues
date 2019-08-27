#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #prints out Greetings!
colors = ['red','orange','yellow','green','blue','violet','purple'] #adds values to the variable.
play_again = ''  #tells the loop to keep playing
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):
    match_color = random.choice(colors)
    count = 0
    color = ''
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()
        count += 1
        if (color == match_color):
            print('Correct!')
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    print('\nYou guessed it in {0} tries!'.format(count))
    if (count < best_count):
        print('This was your best guess so far!')
        best_count = count
    play_again = input("\nWould you like to play again? ").lower().strip()
print('Thanks for playing!') #prints out Thanks for playing!