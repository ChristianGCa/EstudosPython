import json

# Abrindo o arquivo teste.json
arq = open("teste.json")

# Carregando o conteúdo de teste.json para a variável dados
dados = json.load(arq)

print(dados)
print(type(dados))