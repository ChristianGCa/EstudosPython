import time
import random
import matplotlib.pyplot as plt
import csv

# Implementação do Bubble Sort
def ordenacao_bolha(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Implementação do Insertion Sort
def ordenacao_insercao(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i-1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

# Função para medir tempos de execução
def medir_tempos_ordenacao():
    tamanhos = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    tempos_bolha = []
    tempos_insercao = []

    for tamanho in tamanhos:
        dados = [random.randint(0, 1000000) for _ in range(tamanho)]
        
        # Medir o tempo de execução do Bubble Sort
        dados_copia_bolha = dados.copy()
        tempo_inicio_bolha = time.time()
        ordenacao_bolha(dados_copia_bolha)
        tempo_fim_bolha = time.time()
        tempos_bolha.append(tempo_fim_bolha - tempo_inicio_bolha)
        
        # Medir o tempo de execução do Insertion Sort
        dados_copia_insercao = dados.copy()
        tempo_inicio_insercao = time.time()
        ordenacao_insercao(dados_copia_insercao)
        tempo_fim_insercao = time.time()
        tempos_insercao.append(tempo_fim_insercao - tempo_inicio_insercao)

    return tamanhos, tempos_bolha, tempos_insercao

# Função para salvar em csv os tempos de execução
def salvar_csv(tamanhos, tempos_bolha, tempos_insercao):
    with open('tempos_ordenacao.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Tamanho', 'Bubble Sort', 'Insertion Sort'])
        for i in range(len(tamanhos)):
            writer.writerow([tamanhos[i], tempos_bolha[i], tempos_insercao[i]])

# Obter os tempos de execução
tamanhos, tempos_bolha, tempos_insercao = medir_tempos_ordenacao()

# Salvar em csv
salvar_csv(tamanhos, tempos_bolha, tempos_insercao)

# Plotar os resultados
plt.figure(figsize=(12, 6))
plt.plot(tamanhos, tempos_bolha, label='Bubble Sort', marker='o')
plt.plot(tamanhos, tempos_insercao, label='Insertion Sort', marker='o')
plt.xlabel('Tamanho do Vetor')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Comparação de Tempos de Execução: Bubble Sort vs Insertion Sort')
plt.legend()
plt.grid(True)
plt.show()
