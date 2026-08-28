import random
number=random.randint(1,11)
while True:
    guess=int(input("Guess the number:"))
    if guess==number:
        print("correct! you guessed it")
        break
    elif guess<number:
        print("too low")
    else:
        print("too high!")
