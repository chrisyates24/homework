# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:27:17 2016

@author: chris
"""
print("\t\t\tGuess my number Game!")
print("\n\nChoose a number between 1 and 100")
print("You have 5 guesses to get it right!")
print("\n\n\n")

import random

attempts = 5
number = random.randint(1, 100)

for attempt in range(attempts):
    guess = int(input('Insert guess here: '))

    if guess < number:
        print('Higher...')
    elif guess > number:
        print('Lower...')
    else:
        print()
        print('You guessed it! The number was ', number)
        print('You guessed it in', attempts, 'attempts')

        break

if guess != number:
    print()
    print('That is incorrect')
    print('The number is', number)
    
input("Press enter to exit")
