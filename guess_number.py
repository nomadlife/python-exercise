import random
number = random.randint(1,999)
found = False

while not found:
    guess = eval(input("input number :"))
    if guess == number:
        print("You got it")
        found = True
    elif guess > number:
        print("Guess lower!")
    else:
        print("Guess higher!")

