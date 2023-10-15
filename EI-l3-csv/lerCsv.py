import csv
import json

arq = open("municipios_formatado.csv")

dados = csv.reader(arq)

for item in dados:
    print(item)