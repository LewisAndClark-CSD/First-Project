# Program Name: Guess My Number
# Author: Tyler Kapusniak
# Date: 09/29/14

# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

#Opening Remarks
print("Welcome to 'Guess My Number'!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

# set the initial values
the_number = random.randint(1, 100)
guess = # Create the priming read here
tries = 1

# guessing loop
while guess != the_number:
    #put the guessing game logic here
            
    tries += 1
    guess = #Create the following read here


print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!")

#Program Closing  
input("Press the enter key to exit.")
