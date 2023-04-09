# Write a program to complete the task given below:
'''  
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output. '''

a = input("Enter a number between 1 and 10:")
b = input("Enter second number between 1 and 10:")
z = int(a) + int(b)
result = z + 30
print("Final result: ", result)