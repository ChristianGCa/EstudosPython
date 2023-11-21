
# Função para ler um conjunto de nomes de frutas
def ler_conjunto():
    entrada = input("Digite as frutas separadas por espaço: ")
    nomes = entrada.split() # Mesma coisa que split(" ")
    return set(nomes)

# Armazenando os conjuntos de frutas
conjunto1 = ler_conjunto()
conjunto2 = ler_conjunto()

# Operações de conjuntos
uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)
diferenca1 = conjunto1.difference(conjunto2)
diferenca2 = conjunto2.difference(conjunto1)

# Calcular a diferença no número de elementos entre os conjuntos
diferenca_num_elementos = abs(len(conjunto1) - len(conjunto2))

# Apresentar os resultados
print("\nUnião dos conjuntos:", uniao)
print("Interseção dos conjuntos:", intersecao)
print("Diferença (conjunto1 - conjunto2):", diferenca1)
print("Diferença (conjunto2 - conjunto1):", diferenca2)
print("Diferença no número de elementos entre os conjuntos:", diferenca_num_elementos)