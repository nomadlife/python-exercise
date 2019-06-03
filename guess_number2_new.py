#strike, ball 판단 - upgrade

import random
number = str(random.randint(1,999)).zfill(3)
print(number)

while True:
    guess = input('숫자를 입력하세요 :')
    
    try:
        if len(guess) != 3:
            raise

        for i in guess:
            if i not in '0123456789':
                raise 
        
    except :
        print('0~999 사이의 숫자를 입력해주세요')

    else:
        if guess == number:
            print('정답입니다')
            break

        strike = 0
        ball = 0
        answer = list(number)
        for i in range(3):
            if guess[i] == answer[i]:
                strike += 1
                answer[i] = 's'

        for i in range(3):
            if guess[i] in answer:
                ball += 1
                answer[answer.find(guess[i])] = 'b'
        print(strike,ball)