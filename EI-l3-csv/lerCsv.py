import csv
import json

# Abrindo o arquivo .csv
arq = open("municipios_formatado.csv")

# Armazenando o conteúdo do arquivo na variável input
input = csv.reader(arq)

# Cria o objeto de gravação
w = csv.writer(arq)

# Pula a linha de cabeçalho
next(arq, None)

# Itera sobre as linhas do arquivo
for row in arq:

    # Cria um objeto JSON para o município
    obj = {
        "uf": row[0],
        "cod_uf": row[1],
        "cod_municipio": row[2],
        "nome_municipio": row[3],
        "populacao": row[4],
    }
    print(row)