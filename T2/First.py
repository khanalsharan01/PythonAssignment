"""
  Write a program in Python to perform the following operation:
  If a number is divisible by 3 it should print “Consultadd” as a string
  If a number is divisible by 5 it should print “Python Training” as a string
  If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.  
    
"""

a = input("Enter a number:")
b = int(a)

if b%3 == 0 & b%5 == 0 :
    print("Consultadd-Python Training")
elif (b%3 == 0) :
    print("Consultadd")
elif b%5 == 0:
    print("Python Training")
else:
    print("Number is neither divisible by 3 nor by 5")

