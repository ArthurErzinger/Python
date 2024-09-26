n = int(input("Digite um número para imprimir sua tabela de multiplicação (de 1 a 10): "))

print("Tabela de multiplicação de", n, ":")
for i in range(1, 11):
    print(n, "x", i, "=", n*i)