import json

# Abrindo o arquivo teste2.json
arq = open("teste2.json")

# Carregando o conteúdo de teste2.json para a variável dados2
dados2 = json.load(arq)

print(dados2[0]['municipios'][1]['nome_municipio'])