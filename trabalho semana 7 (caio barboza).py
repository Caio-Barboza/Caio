def calcular_soma_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

numeros = [10, 20, 30, 40]
soma, media = calcular_soma_media(numeros)

print("Soma dos números:", soma)
print("Média dos números:", media)

def substituir_palavra(lista, palavra_antiga, palavra_nova):
    for i in range(len(lista)):
        if lista[i] == palavra_antiga:
            lista[i] = palavra_nova

palavras = ["banana", "limão", "pera", "abacaxi"]
substituir_palavra(palavras, "banana", "manga")

print("Lista de palavras após substituição:", palavras)

def imprimir_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print(" " * (num_linhas - i) + "*" * (2*i - 1))

# Chame a função para imprimir um triângulo com 6 linhas
imprimir_triangulo(6)