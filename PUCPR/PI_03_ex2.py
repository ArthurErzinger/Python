N = int(input("Digite um número inteiro positivo: "))

print("Números pares de 0 até", N, ":")
for i in range(0, N + 1, 2):
    print(i)

print("\nNúmeros múltiplos de 3 até", N)
for i in range(N, -1, -1):
    if i % 3 == 0 and i != 0:
        print(i)