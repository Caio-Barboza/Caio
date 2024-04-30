def imprimir_informacoes(nome, idade, cidade, sep=' - ', end='\n'):
    print("Nome:", nome, sep=sep, end=sep)
    print("Idade:", idade, sep=sep, end=sep)
    print("Cidade:", cidade + '!', sep=sep, end=end)

# Exemplo de uso:
imprimir_informacoes("Alice", 25, "São Paulo")


def calcular():
    # Solicita ao usuário os dois números
    num1 = float(input("Digite o primeiro número (10): "))
    num2 = float(input("Digite o segundo número (20): "))
    
    # Verifica se os números inseridos são realmente 10 e 20
    if num1 != 10 or num2 != 20:
        print("Os números inseridos não correspondem a 10 e 20.")
        return

    # Solicita ao usuário a operação desejada
    operacao = input("Digite a operação desejada (soma): ")

    # Verifica se a operação é de soma
    if operacao.lower() != 'soma':
        print("Operação inválida.")
        return

    # Realiza a operação de adição
    resultado = num1 + num2

    # Imprime o resultado
    print("Resultado da soma:", resultado)

# Exemplo de uso:
calcular()

def celsius_para_fahrenheit():
    # Solicita ao usuário a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converte a temperatura para Fahrenheit usando a fórmula de conversão
    fahrenheit = (celsius * 9/5) + 32

    # Imprime o resultado
    print("A temperatura em Fahrenheit é:", fahrenheit)

# Exemplo de uso:
celsius_para_fahrenheit()

def solicitar_nomes():
    nomes = []  # Lista para armazenar os nomes digitados

    # Loop infinito para solicitar nomes até que 'sair' seja digitado
    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        
        # Verifica se o nome digitado é 'sair'
        if nome.lower() == 'sair':
            break  # Sai do loop se 'sair' for digitado
        else:
            nomes.append(nome)  # Adiciona o nome à lista de nomes

    # Imprime os nomes digitados
    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Exemplo de uso:
solicitar_nomes()