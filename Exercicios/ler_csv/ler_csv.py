import csv

# Abrindo o arquivo teste.csv
arq = open("teste.csv")

# Armazenando o conteúdo do arquivo em uma variável
dados = csv.reader(arq)
print("Dados: ", dados)
print("Tipo: ", type(dados))
print()

# Laço para mostrar o item e seu tipo
for item in dados:
    print("Item: ", item)
    print("Tipo: ", type(item))
    print()

