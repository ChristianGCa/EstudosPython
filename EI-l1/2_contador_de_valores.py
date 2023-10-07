# Inicializando um dicionário para armazenar a contagem de valores
contador_valores = {}

# Lê números inteiros do teclado até que um número negativo ou zero seja digitado
while True:

    # Cláusula try para tratar exceções
    try:
        numero = int(input("Digite um número inteiro (0 ou negativo para sair): "))
        
        if numero <= 0:
            break  # Sai do loop se um número negativo ou zero for digitado
        
        # Atualiza o contador para o número digitado
        if numero in contador_valores:
            contador_valores[numero] += 1
        else:
            contador_valores[numero] = 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Mostra os valores e suas contagens
print("Valores digitados e suas contagens:")
for valor, contagem in contador_valores.items():
    # Formatadno a saída
    print(f"{valor}: {contagem} vezes")
