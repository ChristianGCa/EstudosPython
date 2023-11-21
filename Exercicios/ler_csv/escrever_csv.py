import csv

lista = [
    ["nome", "idade"],
    ["João", 30],
    ["Maria", 50]
]

arq = open("novo.csv", "w")

# Cria o objeto de gravação
w = csv.writer(arq)

# Grava as linhas
for i in lista:
    w.writerow(i)

arq.close()