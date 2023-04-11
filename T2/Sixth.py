# What is the output of the following code examples?

"""x = 123
for i in x:
    print(i) 
 """    
#Output is: 
"""TypeError: 'int' object is not iterable """


""" #New Code
i = 0 
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")
"""


# Output is :
"""
0
error
1
error
2    
"""  

"""  # New Code:
count = 0 
while True:
    print(count)
    count += 1
    if count >= 5:
        break

"""

# Output is : 

"""
0
1
2
3
4   
"""