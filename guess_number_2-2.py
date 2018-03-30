#strike, ball 판단 - upgrade

import random
number = str(random.randint(1,999)).zfill(3)
found = False
print('answer :', number)

print('strike ball')
while not found:
    guess = input("input number :").zfill(3)
    if guess == number:
        print("You got it")
        found = True
    else:
        strike = 0
        ball = 0
        for i in range(3):
            if guess[i] == number[i]:
                strike += 1
            elif guess[i] in number:
                ball+=1
        print("{:2d}{:5d}".format(strike,ball))