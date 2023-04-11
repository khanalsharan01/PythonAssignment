"""
Write a program that accepts a string as an input from the user and calculate the number of digits
and letters.
Sample input: consul72
Expected output: Letters 6 Digits 2

"""

a = input("Enter your string ")
letters = 0
digits = 0

for i in a:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1
    else:
        pass

print("Letters:", letters)
print("Digits:", digits)
