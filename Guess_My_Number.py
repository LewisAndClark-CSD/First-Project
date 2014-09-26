# Program Name:
# Author:
# Date:

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
guess = int(input('Enter your guess here!: '))
tries = 1

# guessing loop
while guess != the_number:
    if guess < the_number:
        print('Your guess is to low..')
    if guess > the_number:
        print('Your guess is to high..')
            
    tries += 1
    if guess = the_number:
        print("You guessed it!  The number was", the_number)
        print("And it only took you", tries, "tries!")

#Program Closing  
input("Press the enter key to exit.")
