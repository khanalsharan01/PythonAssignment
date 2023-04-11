"""
In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.    
    
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
            break
        else:
            print("Try Again")
        counter += 1 
    else:
        print("Sorry but that was not very successful")
        break  