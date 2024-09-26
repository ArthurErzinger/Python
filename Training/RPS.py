import random

play = True

score = 0
list = ["Rock", "Paper", "Scissors"]
pc = random.choice(list)

while play == True:
    move = input("Rock, Paper or Scissors: ")
    pc = random.choice(list)
    while not(move == "Rock" or move == "Paper" or move == "Scissors"):
        print("Write as in the question")
        move = input("Rock, Paper or Scissors: ")

    print(pc)

    if move == pc:
        print("Draw!")
    elif move == "Rock":
        if pc == "Paper":
            print("You Lost!")
            score -= 1
        else:
            print("You Won!")
            score += 1
    elif move == "Paper":
        if pc == "Scissors":
            print("You Lost!")
            score -= 1
        else:
            print("You Won!")
            score += 1
    elif move == "Scissors":
        if pc == "Rock":
            print("You Lost!")
            score -= 1
        else:
            print("You Won!")
            score += 1

    playAgain = input("Wanna play again? (y/n): ")

    while not(playAgain == "y" or playAgain == "n"):
        playAgain = input("Wanna play again? (y/n): ")
        
    if playAgain == "n":
        play = False
        print("Score:" + str(score))
    elif playAgain == "y":
        play = True

    if score > 0:
        print("You Won the Game!!!")
    elif score < 0:
        print("You Lost the Game.")