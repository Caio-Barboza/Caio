#print("Olá", "mundo", sep="-") # Saída: Olá-mundo
#print("Olá", "Python", end="!\n") # Saída: Olá Python
#print("18", "04", "2023", sep="/") 
#print("Caio", "Barboza", "barbozacaio30@gmail.com", sep="; ") 
#print("Loading", end=" ")
#print("[OK]") 
#nome = input("Caio Barboza")
#print("Olá", nome)
#itens = input("vermelho, preto, flamengo").split(',')
#print("Itens:", itens)
#idade = int(input("25"))
#print("Daqui a cinco anos, você terá", idade + 5, "anos.")
#altura = float(input("1,88"))
#print("Sua altura é", altura, "metros.")
print("Digite números para adicionar à lista (digite 'done' para terminar):")
numeros = [1,2,3,4]
while True:
    entrada = input()
    if entrada.lower() == 'done':
        break
    else:
         numeros.append(int(entrada))
print("numeros coletados:", numeros)