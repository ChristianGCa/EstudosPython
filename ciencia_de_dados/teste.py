# Programa para criar uma visualização usando pandas e matplotlib dos dados do arquivo CSV "menor_agua_ar_qualidade.csv".
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Carregando os dados do arquivo csv e transformando em uma lista de dicionários
with open('menor_agua_ar_qualidade.csv', 'r') as file:
    reader = csv.DictReader(file)
    dados = list(reader)



# Criando uma visualização das cidades com menor qualidade do ar (Quanto maior o valor, maior qualidade)
df = pd.DataFrame(dados)
print(df)
df['AirQuality'] = pd.to_numeric(df['AirQuality'])
df = df.sort_values(by='AirQuality', ascending=False)

plt.bar(df['City'], df['AirQuality'])
plt.xlabel('City')
plt.ylabel('Air Quality')
plt.title('Cities with Lowest Air Quality')
plt.xticks(rotation=90)
plt.show()

# Criando uma visualização das cidades com maior poluição da água (Quanto maior o valor, maior poluição)
df = df.sort_values(by='WaterPollution', ascending=False)

plt.bar(df['City'], df['WaterPollution'])
plt.xlabel('City')
plt.ylabel('Water Pollution')
plt.title('Cities with Highest Water Pollution')
plt.xticks(rotation=90)
plt.show

