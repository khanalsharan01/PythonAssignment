"""
Read the two parts of the question below:
 Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.

Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number)

"""


import random

"""
NumberToGuess = random.randint(1,10)

while True:
    a = int(input("Guess the lucky number: "))
    print(NumberToGuess)
    if a != NumberToGuess: 
       continue
    else:
        break

"""
#b = input("Do you want to guess")

NumberToGuess = random.randint(1,55)
number = 0
Answer = 0

while True:
    print(NumberToGuess)
    number = int(input("Guess the lucky number: "))
    Answer = str(input("Do you want to guess again?: "))
    if NumberToGuess == number or Answer == "no":
        break
    else:
        continue
    





