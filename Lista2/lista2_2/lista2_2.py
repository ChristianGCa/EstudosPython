print("/////////////////////////////////////////")
print("////////// LOJINHA DO SEU ZÉ ////////////")
print("/////////// 100% ATUALIZADA /////////////")
print("/////////////////////////////////////////\n")

# Inicializa uma matriz vazia para armazenar os itens
matriz_produtos = []

# Abre o arquivo dos produtos para ler
arq = open("produtos.txt", "r")

# Percorre as linhas do arquivo, remove espaços em branco e adiciona a matriz_produtos
for linha in arq:
    itens = linha.strip().split('-')
    matriz_produtos.append(itens)

# Exibe os itens da matriz formatados
for item in matriz_produtos:
    codigo, nome, preco = item
    print(f"Código: {codigo}")
    print(f"Nome: {nome}")
    print(f"Preço: {preco}")
    print()  # Adiciona uma linha em branco entre os produtos

# Variável para guardar os produtos desejados e a quantidade
produtos_selecionados = {}

while True:
    escolha = input("Digite o código do produto (0 para finalizar): ")
    if escolha == '0':
        break
    encontrado = False
    for codigo, nome, preco in matriz_produtos:
        if escolha == codigo:
            quantidade = int(input(f"Digite a quantidade desejada de {nome}: "))
            produtos_selecionados[codigo] = {'nome': nome, 'quantidade': quantidade, 'preco': float(preco)}
            encontrado = True
            break
    if not encontrado:
        print("Código inválido. Por favor, digite um código de produto válido.")

# Calcula o valor total com base nas escolhas do usuário
total = sum(item['preco'] * item['quantidade'] for item in produtos_selecionados.values())

# Mostra os produtos selecionados e o valor total da compra
print("\nCarrinho de Compras:")
for codigo, item in produtos_selecionados.items():
    print(f"{item['nome']} - Preço unitário: {item['preco']} - Quantidade: {item['quantidade']}")
print(f"Valor Total: {total}")

arq = open("carrinho_de_compras.txt", "w")
arq.write("Carrinho de Compras\n\n")
for codigo, item in produtos_selecionados.items():
    arq.write(f"{item['nome']} - Preço unitário: {item['preco']} - Quantidade: {item['quantidade']}\n")
arq.write(f"\nValor Total: {total}")

