# Program Name: Guess_My_Number
# Author: Dennis Gordick
# Date: 9/26/2014

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
# Create the priming read here
guess = input("Enter your guess:")
tries = 1

if int(guess) == int(the_number):
    print("Your right on the money!")
elif int(guess) > int(the_number):
    print("To high!")
elif int(guess) < int(the_number):
    print("To low!")
# guessing loop
while guess != the_number:
    tries += 1
    #put the guessing game logic here
    #Create the following read here
    guess = input("Guess again!")
#Didnt know how to make it reloop to the start...
print("You guessed it!  The number was", the_number)
print("And it only took you", tries, "tries!")

#Program Closing  
input("Press the enter key to exit.")
