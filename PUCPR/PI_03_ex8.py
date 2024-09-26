# Solicita o número de elementos N ao usuário
n = int(input("Digite o número de elementos (N): "))

# Inicializa a variável para armazenar a soma
total = 0

# Loop para ler os N números e somá-los
for i in range(n):
    numero = float(input(f"Digite o número {i+1}: "))
    total += numero

# Exibe o resultado
print(f"A soma dos {n} números é: {total}")
