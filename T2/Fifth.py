# Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.
a = []
for i in range(2000, 3200) :
    if i%7 == 0 and i%5 != 0 :
       # print(i)
        a.append(i)
    i+=1
print(a)