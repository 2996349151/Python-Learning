""" Improved simple game """

import random

counts = 0
answer = random.randint(0,10)

while counts < 10:
    temp = input("guess a number ranging from 0 to 10:  ")
    number = int(temp)

    if number == answer:
        print("correct")
        break
    else:
        if number < answer:
            print("try to guess a bigger number")
        else:
            print("try to guess a smaller number")
        counts = counts + 1

if counts == 10:
    print("no more chances")
    
print("end")
     
