from random import randint

a = 0

for i in range(0, 200):
    a += 1
    if a == 5:
        print(randint(0,1), end = " ")
        a = 0
    else:
        print(randint(0,1), end = "")      
        continue