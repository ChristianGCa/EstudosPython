print("/////////////////////////////////////////")
print("////////// LOJINHA DO SEU ZÉ ////////////")
print("/////////////////////////////////////////\n")

#Armazenando os produtos disponíveis em um dicionário
produtos_disponiveis = [
   {"codigo": 100, "nome": "Mouse Logitech", "preco": 35.90},
   {"codigo": 101, "nome": "Cabo USB", "preco": 12.90},
   {"codigo": 102, "nome": "PenDrive 16Gb Sandisk", "preco": 47.90}
]

#mostra na tela a lista de produtos
print(produtos_disponiveis[0])
print(produtos_disponiveis[1])
print(produtos_disponiveis[2])
print()

#variável para guardar os produtos desejados e a quantidade
produtos_selecionados = []

#função para encontrar um produto
def encontrar_produto(codigo):
    for produto in produtos_disponiveis:
        if produto["codigo"] == codigo:
            return produto
    return None

#usuario solicita o produto e a quantidade
while True:
    codigo_produto = int(input("Digite o código do produto (0 para finalizar): "))
    
    if codigo_produto == 0:
        break

    #chama a função encontrar_produto para ver se o produto está disponível
    produto_encontrado = encontrar_produto(codigo_produto)

    #se o produto foi encontrado, pede a quantidade. Se não, mostra uma mensagem de codigo inválido.
    if produto_encontrado:
        quantidade = int(input("Digite a quantidade: "))
        valor_total_produto = quantidade * produto_encontrado["preco"]
        produtos_selecionados.append({"produto": produto_encontrado, "quantidade": quantidade, "valor_total": valor_total_produto})
    else:
        print("Código de produto inválido.")

#exibir os itens da venda
print("\nItens da Venda:")
for item in produtos_selecionados:
    produto = item["produto"]
    print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Valor Unitário: R${produto['preco']:.2f}, Quantidade: {item['quantidade']}, Valor Total: R${item['valor_total']:.2f}")

#calcula e exibir o valor total da venda
valor_total_venda = sum(item["valor_total"] for item in produtos_selecionados)
print(f"\nValor Total da Venda: R${valor_total_venda:.2f}")
