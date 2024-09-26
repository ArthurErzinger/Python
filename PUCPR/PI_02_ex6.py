idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Você é um não eleitor.")
elif idade >= 16 and idade <= 18 or idade > 65:
    print("Você é um eleitor facultativo.")
else:
    print("Você é um eleitor obrigatório.")