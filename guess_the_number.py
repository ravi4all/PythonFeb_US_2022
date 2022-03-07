# mini game - guess the number
#1. cpu will generate a random number
#2. guess the number generated by cpu in 5 chances

import random

cpu = random.randint(1,100)
count = 5

while True:
    guess = int(input("Guess the number : "))
    if cpu == guess:
        print("Congrats....You have guessed the number...")
        break

    elif cpu > guess:
        print("You have entered a smaller number...")

    elif cpu < guess:
        print("You have entered a greater number...")

    else:
        print("Invalid Input...")

    count -= 1
    print("Chances Left ::",count)
    if count == 0:
        print("You lose, Number was ::",cpu)
        break


    