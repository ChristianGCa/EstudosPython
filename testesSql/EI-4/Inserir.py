
import conectar
import csv

c = conectar.getConexao()
cursor = c.cursor(prepared=True)

# Abrindo o arquivo csv
arq = open("municipios_formatado.csv")

# Salvando o conteúdo do arquivo em uma variável
dados = csv.reader(arq)

# Pulando a primeira linha
next(dados)

# Lista vazia para armazenar as tuplas para inserção
lista = []

# Convertendo os valores numéricos para tipo inteiros para colocar no BD
# e adicionando cada item em uma tupla para inserção
for item in dados:
    tupla = (item[0],int(item[1]),int(item[2]),item[3],int(item[4]))
    lista.append(tupla)

# Comando sql
sql = "INSERT INTO Tabela (id, uf, cod_uf, cod_municipio, nome_municipio, populacao) VALUES (default, ?, ?, ?, ?, ?)"

# Inserindo os dados na tabela do BD
cursor.executemany(sql, lista)

# Confirmando
c.commit()

print(cursor.rowcount, "Registros inseridos com sucesso")

# Fechando a conexao
c.close()