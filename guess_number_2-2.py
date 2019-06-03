#strike, ball 판단 - upgrade

import random
number = str(random.randint(1,999)).zfill(3)
print(number)

while True:
    guess = input('숫자를 입력하세요 :')
    if guess == number:
        print('정답입니다')
        break
        
    strike = 0
    ball = 0
    for i in range(3):
        if guess[i] == number[i]:
            strike += 1
        elif guess[i] in number:
            ball+=1
    print(strike,ball)