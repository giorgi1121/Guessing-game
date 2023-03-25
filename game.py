#import random module
import random

#make loop for asking range number and define value of "random"
while True:
    try:
        range_number = int(input("What is range: "))
        random = random.randrange(1, range_number)
    except:
        pass
    else:
        break

#make loop for asking guess number and check if it is same or not
while True:
    try:
        guess = int(input("Guess number: "))
        if guess < 0:
            continue
        elif guess < random:
            print("Too small!")
            continue
        elif guess > random:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
    except:
        continue
