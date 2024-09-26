def mostrarCadeiras(matrizEscolhida):
    for linha in matrizEscolhida:
        linhaFormatada = ""
        for elemento in linha:
            linhaFormatada += f"{elemento:7}"
        print(linhaFormatada)


#Criação das listas que serão armazenadas as cadeiras vendidas e seus tipos de ingresso
cadeirasVendidas = []
ingressoMeia = []
ingressoInteira = []

def compraDeIngresso():
    #Loop while que só sera quebrado ao encontrar o "break"
    while True:
        cadeiraEscolhida = input("Escolha sua poltrona (1...140): ")
        #IF para checar se o input do usuário se trata de um número inteiro ou não
        if cadeiraEscolhida.isdigit():
            cadeiraEscolhida = int(cadeiraEscolhida)

            #IF que checa se a cadeira existe (está no intervalo de 1 a 140) e se está na lista de cadeiras que já foram vendidas
            if cadeiraEscolhida < 1 or cadeiraEscolhida > 140:
                print("Esta cadeira não existe!")
            elif cadeiraEscolhida in cadeirasVendidas:
                print("Cadeira já vendida!")
            else:
                #Para ser efetivamente vendida, a cadeiraEscolhida é adicionada a lista de cadeirasVendidas
                cadeirasVendidas.append(cadeiraEscolhida)
                #Ao comprar a cadeira, o usuário deve escolher o tipo de ingresso que deseja, assim o programa adiciona aquela cadeira a lista do tipo do ingresso escolhido
                tipoIngresso = input("Qual o tipo do ingresso, inteira (i) ou meia (m)? ")
                #Loop while que limita o usuário a escrever "m" ou "i"
                while tipoIngresso.lower() != "m" and tipoIngresso.lower() != "i":
                    print("Resposta Inválida!\nAs opções são i para inteira ou m para meia entrada.")
                    tipoIngresso = input("Qual o tipo do ingresso, inteira (i) ou meia (m)? ")
                
                if tipoIngresso.lower() == "m":
                    ingressoMeia.append(cadeiraEscolhida)
                elif tipoIngresso.lower() == "i":
                    ingressoInteira.append(cadeiraEscolhida)

                #Loop for para substituir a cadeira escolhida e vendida em um caractere em branco para demonstrar que ela foi vendida
                for linha in range(14):
                        for coluna in range(10):
                            if cadeirasCinema[linha][coluna] == cadeiraEscolhida:
                                    cadeirasCinema[linha][coluna] = ' '
                
                #Loop while que pergunta ao usuario se o mesmo deseja comprar mais um ingresso, se sim, a função "compraDeIngresso" começa do zero novamente, se não, o loop while encontra o break e finaliza
                maisIngressos = input("Deseja comprar mais um ingresso? (s/n) ")
                while maisIngressos.lower() != "s" and maisIngressos.lower() != "n":
                    print("Resposta Inválida!\nAs opções são s se deseja comprar mais ingressos ou n se não deseja.")
                    maisIngressos = input("Deseja comprar mais um ingresso? ")
                
                if  maisIngressos.lower() == "s":
                    print("Ficamos muito felizes com a sua escolha!")
                elif  maisIngressos.lower() == "n":
                    break
        else:
            print("Valor inválido, por favor escreva um número inteiro entre 1 e 140.")

def mostrarOcupação():
    print("----- Relatório de ocupação Cinema CineStar -----")
    #Loop for que ao contar de 1 em 1 e ao mesmo tempo iterando a lista de cadeirasVendidas, consegue substituir a cadeira pelo tipo de ingresso que foi usado para compra-la
    for cadeira in cadeirasVendidas:
        i = 0
        for linha in range(14):
            for coluna in range(10):
                i += 1
                if i == cadeira:
                    if cadeira in ingressoInteira:
                        cadeirasOcupação[linha][coluna] = 'I'
                    else:
                        cadeirasOcupação[linha][coluna] = 'M'
    mostrarCadeiras(cadeirasOcupação)
    #Usufruindo da função len(), consigo printar no terminal quantos ingressos de cada tipo foram vendidos e somando os dois, o total de ingressos vendidos
    print("""
Plateia possui 140 cadeiras
Foram vendidos """ + str((len(ingressoInteira) + len(ingressoMeia))) + " ingressos, sendo:")
    print(str(len(ingressoInteira)) + "-inteiras")
    print(str(len(ingressoMeia)) + "-meias")
        
cadeirasCinema = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    [91, 92, 93, 94, 95, 96, 97, 98, 99, 100],
    [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    [111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
    [121, 122, 123, 124, 125, 126, 127, 128, 129, 130],
    [131, 132, 133, 134, 135, 136, 137, 138, 139, 140]
]

cadeirasOcupação = [
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
]


#Loop while para o menu interativo que só será finalizado ao encontrar o "break", encontrado na opção "0-Sair"
while True:
    opçãoMenu = input("""
----- Cinema CineStar -----
0-Sair
1-Comprar ingresso
2-Mostrar plateia
3-Mostrar ocupação
                      
Qual opção deseja? """)
    
    if opçãoMenu == "0":
        print("\nO Cinema CineStar agradece sua atenção, tenha um ótimo dia!\n")
        break
    elif opçãoMenu == "1":
        print("""\n----- Venda de Ingressos Cinema CineStar -----\n
Ocupação da sala:""")
        mostrarCadeiras(cadeirasCinema)
        print("\n")
        compraDeIngresso()
    elif opçãoMenu == "2":
        print("\nOcupação da sala:")
        mostrarCadeiras(cadeirasCinema)
    elif opçãoMenu == "3":
        print("\n")
        mostrarOcupação()
    else:
        print("\nOpção inválida!")
