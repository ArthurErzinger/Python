import random

rollAgain = True

while rollAgain == True:
    dice = random.randint(1,6)
    print(dice)
    rollAgain = input("Wanna roll again? (y/n): ")

    while not(rollAgain == "y" or rollAgain == "n"):
        rollAgain = input("Wanna roll again? (y/n): ")
        
    if rollAgain == "n":
        rollAgain = False
    elif rollAgain == "y":
        rollAgain = True
