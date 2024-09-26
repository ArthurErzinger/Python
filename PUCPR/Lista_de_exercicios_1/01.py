#crie uma função recursiva que aceite só um vetor como parametro e retorne o maior valor

def maiorValor(V):
    V.sort()
    n = len(V) - 1
    return V[n]

print(maiorValor([6,2,7,1000,1,-5]))