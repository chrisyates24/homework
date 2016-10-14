# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:30:22 2016

@author: chris
"""

import random

guesses=0
lownumber =0
highnumber=100
number=random.randint(lownumber,highnumber)

print("Is the number ", number, "?")
response=input("Respond 'Yes','Higher', or 'Lower':")

while response != "Yes":
    
    if guesses > 5:
        input("That is incorrect..... Type the answer here:")
        print("Dang it!")
        break
        
    if response == "Higher":
        lownumber = number
        number = random.randint(lownumber+1,highnumber)
        print("Is it ", number, "?")
        response = input("Respond 'Yes', 'Higher', or 'Lower':")
        guesses=guesses+1
        
    elif response == "Lower":
        highnumber = number
        number = random.randint(lownumber,highnumber-1)
        print("Is it ", number, "?")
        response = input("Respond 'Yes', 'Higher', or 'Lower':")
        guesses=guesses+1
        
    if response == "Yes":
        print("Yeah boi!!!!")
        
        input("Press enter to exit")
        
    
        