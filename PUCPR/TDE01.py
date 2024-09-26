maisAlunos = "S"
notasAlunos = []
alunosAprovados = 0
alunosRecuperação = 0
alunosReprovados = 0
i = 0


print("Lembre-se que para digitar números com decimais deverá ser usada o ponto! (Exemplo: 6.5)")

#Loop while para adicionar as notas dos alunos em uma lista
while maisAlunos == "S":

    notasAlunos.append(float(input("Nota " + str((i+1)) +":")))
    while notasAlunos[i] < 1 or notasAlunos[i] > 10:
        print("Nota Inválida (Valor deve ser maior que 1 e menor que 10)")
        notasAlunos[i] = float(input("Nota " + str((i+1)) +":"))

    #Cálculo para poder printar a quantidade e porcentagem de alunos em cada situação
    if notasAlunos[i] >= 7:
        alunosAprovados +=1
    elif notasAlunos[i] < 4:
        alunosReprovados +=1
    else:
        alunosRecuperação +=1


    i +=1

    #Loop while que pergunta ao usuário se ele deseja incluir mais notas ou não, limitando-o a somente duas alternativas
    maisAlunos = input("Deseja incluir mais notas? (S/N): ")
    while maisAlunos != "S" and maisAlunos != "N":
        print("Resposta Inválida!")
        maisAlunos = "S"
        maisAlunos = input("Deseja incluir mais notas? (S/N): ")

tamanhoTurma = len(notasAlunos)


#Cálculo da soma de todas as notas para fazer a média
somaNotas = 0
for nota in notasAlunos:
    somaNotas = somaNotas + nota

médiaTurma = (somaNotas/len(notasAlunos))


#Ordenação da lista em ordem crescente usando do algoritmo Bubble Sort
for notas in range(i):
    for j in range(0, i-notas-1):
        if notasAlunos[j] > notasAlunos[j+1]:
            notasAlunos[j], notasAlunos[j+1] = notasAlunos[j+1], notasAlunos[j]


print("Total de notas lidas: " + str(len(notasAlunos)))

print(f"Nota média da turma: {médiaTurma:.2f}")

print("Maior nota da turma: " + str(notasAlunos[tamanhoTurma - 1]))

print("Segunda maior nota da turma: " + str(notasAlunos[tamanhoTurma - 2]))

print(f"Quantidade de alunos aprovados é {alunosAprovados} e o percentual é {((alunosAprovados*100)/tamanhoTurma):.2f}%")

print(f"Quantidade de alunos em recuperação é {alunosRecuperação} e o percentual é {((alunosRecuperação*100)/tamanhoTurma):.2f}%")

print(f"Quantidade de alunos reprovados é {alunosReprovados} e o percentual é {((alunosReprovados*100)/tamanhoTurma):.2f}%")