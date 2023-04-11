        
""" 
Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as

counter = 1
While counter <= 5:
print(“Type in the”, counter, “number”
counter=counter+1

The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”.

"""

import random

counter = 1

NumberToGuess = random.randint(1,15)
while counter <= 5:
    number = int(input("Guess the lucky number: "))
    print(NumberToGuess)
    if counter != 5:
        if number == NumberToGuess:
            print("Good Guess")
        else:
            print("Try Again")
        counter += 1 
    else:
        print("Game Over")
        break  
