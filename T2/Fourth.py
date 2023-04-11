"""
Write a program in Python to break and continue if the following cases occurs:
If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”

"""
#if a  0 :

while True:
    
    a = float(input("Enter a number: "))
    if a < 0:
        
        break
    else:
        print("good going")
        continue
print("It's Over")  