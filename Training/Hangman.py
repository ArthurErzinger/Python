
import random

print("The theme is Fruits!")
print("The word can be: apple, banana, cherry, watermelon or grape.")

fruits = ["apple", "banana", "cherry", "watermelon", "grape"]
word = fruits[random.randint(0, len(fruits) - 1)]
j = ["_"]
w = j * len(word)
user = ""
j = True

while j == True:
    while not (user == word):
        i = -1
        user = input("Word/Letter: ")
        if user.isalpha():
            if len(user) == 1:
                for x in range(len(word)):
                    i += 1
                    if user == word[i]:
                        w[i] = user
                        v =''.join(map(str, w))
                        print(v)
                        if v == word:
                            print("Você acertou!")
                            exit()
            elif len(user) > 1 and user == word:
                print("Você acertou!")
            else:
                print("Você errou")
        elif not ((user.isalpha())):
            print("Not a letter.")
