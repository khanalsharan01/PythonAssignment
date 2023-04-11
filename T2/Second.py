"""
Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average

Ask user to enter two numbers and keep those numbers in variables num1 and num2 respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action.


"""

a = input("Enter a number between 1 and 5: ")
a = int(a)
result = 0

if a in {1,2,3,4} :
    print(a)
    num1 = input("enter your first number:")
    num2 = input("enter your second number:")
    num1 = int(num1)
    num2 = int(num2)
    if a == 1:
            print("Addition")
            result = num1 + num2    
    elif a == 2:
            print("Subtraction")
            result = num1 - num2
    elif a == 3:
            print("Division")
            result = num1 / num2
    else:
            print("Multiplication")
            result = num1 * num2
    
    
    
    
elif a == 5: 
    first = input("first number to calculate averave: ")
    second = input("second number to calculate average: ")
    first = int(first)
    second = int(second)
    print("Average")
    result = (first + second) / 2
   
else: 
    print("mentioned operators are not selected")
    
    
if result < 0 :
    print("Negative")
else:
    print(result)
