# Create a variable of type complex and swap it with another variable of type integer.

a = complex(2,3)
b = 10

a,b = b, a
print(a,b)