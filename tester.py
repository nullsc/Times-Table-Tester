
# 10/11/2019
# https://docs.python.org/3/library/random.html
#
from random import randint
import random, time, sys

maxQuestions = 5 #how many to ask

print("Tool to practise your times tables!")
print(str(maxQuestions) + " questions in total \n")

try:
    testNum = int(input("Enter a number: "))
except ValueError:
    print("You need to input a valid number! \n")
    sys.exit(1)
except:
    print("Error \n")
    sys.exit(1)

q = 1
right = wrong = 0

random.seed() #seed it using time

while(q <= maxQuestions):
    ranNum = randint(1, 10)
    print(str(ranNum) + " x " + str(testNum))
    q += 1
    ans = int(input("Enter your answer: "))
    if((ranNum * testNum) == ans):
        print("That's correct! \n")
        right += 1
    else:
        print("That's incorrect! \n")
        wrong += 1 #could just do total questions - right

print("You got {} right out of {} [{}%]".format(right, maxQuestions, (right / maxQuestions) * 100))

