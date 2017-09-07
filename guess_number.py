import random

print("Guess a number between 1 and 100.")
number=random.randint(1,100)
found_boolean = False               # flag vaiable to see
print(number)                       # if they guessed it

while not found_boolean:
    guess = eval(input("Your guess:"))
    if number == guess :
        print("You got it")
        found_boolean = True
    elif guess > number:
        print("Guess lower!")
    else :
        print("Guess higher!")

