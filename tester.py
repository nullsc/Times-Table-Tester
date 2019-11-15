
# 10/11/2019
# https://docs.python.org/3/library/random.html
#
import random, sys

maxQuestions = 5
printAns = False #print the right answer after entering a wrong answer

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

random.seed()

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
        if(printAns): print("Answer is {}".format(str(ranNum * testNum)))
        wrong += 1 #could just do total questions - right

print("You got {} right out of {} [{}%]".format(right, maxQuestions, (right / maxQuestions) * 100))

