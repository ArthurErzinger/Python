ladoA = int(input("Quanto mede o lado A do triângulo? "))
ladoB = int(input("Quanto mede o lado B do triângulo? "))
ladoC = int(input("Quanto mede o lado C do triângulo? "))

if (ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoB + ladoA):
    if (ladoA==ladoB and ladoA==ladoC and ladoB==ladoC):
        print("É um triângulo equilátero!")
    elif (ladoA == ladoB or ladoB == ladoC or ladoA == ladoC):
        print("É um triângulo isosceles!")
    else:
        print("É um triângulo escaleno")
