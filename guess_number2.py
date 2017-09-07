import random

print("Guess a number between 0 and 999")
randomNumber=list(str(random.randint(0,999)).zfill(3))
print(''.join(randomNumber))
found_boolean = False


while not found_boolean:

    userGuess = list(input("Your guess:").zfill(3))
    print(''.join(userGuess))
    if randomNumber == userGuess :
        print("You got it")
        found_boolean = True
    else :
        strike = 0
        ball = 0
        userGuessTemp = list(userGuess)
        randomNumberTemp = list(randomNumber)
        for i in range(3):
            if userGuessTemp[i] ==randomNumberTemp[i]:
                userGuessTemp[i] = 's'
                randomNumberTemp[i] = 's'
                strike+=1
        print(userGuessTemp,randomNumberTemp)
        
        for j in userGuessTemp:
            if j in randomNumberTemp:
                userGuessTemp.remove(j)
                randomNumberTemp.remove(j)
                ball += 1
        print(randomNumberTemp)
        print("strike :", strike,"ball:",ball)
            
            


    
