import csv
import json

# Abrindo o arquivo .csv
arq = open("municipios_formatado copy.csv")

# Armazenando o conteúdo do arquivo na variável input
input = csv.reader(arq)

# Pula a linha de cabeçalho
next(input)

ufs = []

# Itera sobre as linhas do arquivo
for row in input:

    # Criando variáveis para guardar o código uf e a uf da linha
    cod_uf = int(row[1])
    uf_nome = row[0]

    # Criando a variavel uf_atual vazia
    uf_atual = None

    # Verificando se a uf ja existe na lista de ufs
    for uf in ufs:
        if uf["cod_uf"] == cod_uf:
            uf_atual = uf
            break
    
    # Se a uf_atual está vazia, cria um dicionário para a uf
    if uf_atual is None:
        uf_atual = {
            'uf': uf_nome,
            'cod_uf': cod_uf,
            'municipios': []
        }

        # Adicionando a uf atual na lista de UFs
        ufs.append(uf_atual)

    # Adiciona o municipio na lisa de minicipios da uf
    uf_atual['municipios'].append({
        "cod_municipio": int(row[2]),
        "nome_municipio": row[3],
        "populacao": int(row[4])
    })

    # Salvando em json
    with open("municipios.json", "w") as json_file:
        json.dump(ufs, json_file, indent=2, ensure_ascii=False)

