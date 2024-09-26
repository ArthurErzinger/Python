# Project 1: Number Guessing

import random 

number = random.randint(1,10)

multiplos = []
divisores = []
score = 3
user = 1

def multiples(number):
    i = 1
    for j in range(5):
        i += 1
        n = int(number) * i
        multiplos.append(n)


def dividers(number):
    i = 1
    for j in range(5):
        i += 1
        n = round((int(number) / i), 1)
        divisores.append(n)

while score > 0:
    user = int(input("Qual é o número: "))
    if not(user == number):
        score -= 1
        print("Você errou. Seu score é " + str(score))
        if score == 2:
            multiples(number)
            multi =', '.join(map(str, multiplos))
            print("Múltiplos: " + multi + ".")
        elif score == 1:
            dividers(number)
            divi =', '.join(map(str, divisores))
            print("Divisores: " + divi + ".")
        else:
            print("Você gastou todas as suas tentativas.")
            break
    else:
        print("Você ganhou! Seu score foi: " + str(score))
        break








