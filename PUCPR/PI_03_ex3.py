def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

n = int(input("Digite o número de termos da sequência de Fibonacci que deseja imprimir: "))
fib_numeros = fibonacci(n)
print("Os {} primeiros termos da sequência de Fibonacci são:".format(n))
for num in fib_numeros:
    print(num)