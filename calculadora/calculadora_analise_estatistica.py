import math
import pandas as pd
import tkinter as tk
from tkinter import messagebox

def menorValor(dados):

    return min(dados)

def maiorValor(dados):

    return max(dados)

def amplitudeTotal(dados):
    
    maior = max(dados)
    menor = min(dados)
    at = maior - menor
    return at

def quantidadeDados(dados):

    return len(dados)

def quantidadeClasses(n):

    if (n >= 25):
        k = math.sqrt(n)
    else:
        k = 5

    return k

def amplitudeClasse(at, k):

    h = at / k
    return math.ceil(h)

def criarClasses(h, minval, maxval):

    classes = []
    for i in range(int(minval), int(maxval), h):
        classe = [i, i+h]
        classes.append(classe)
    return classes

def criarTabelaFrequencias(dados, h, minval, maxval):
    
    classes = criarClasses(h, minval, maxval)
    tabela = pd.DataFrame(columns=['Classe', 'li', 'ls', 'fi', 'xi', 'fa', 'fa%', 'fr', 'fr%', 'fi.xi', 'xi²', 'fi.xi²'])
    fa = 0
    
    for i in range(len(classes)):

        classe = classes[i]
        li = classe[0]
        ls = classe[1]
        fi = 0

        for dado in dados:
            if (dado >= li and dado < ls):
                fi += 1

        xi = (li + ls) / 2
        fa += fi
        fap = (fa / len(dados)) * 100
        fr = fi / len(dados)
        frp = fr * 100
        fixi = fi * xi
        xi2 = xi ** 2
        fixi2 = fi * xi2

        tabela.loc[i] = [classe, li, ls, fi, xi, fa, fap, fr, frp, fixi, xi2, fixi2]

    return tabela

def somasTabela(tabela):

    somafi = tabela['fi'].sum()
    somafr = tabela['fr'].sum()
    somafrp = tabela['fr%'].sum()
    somafixi = tabela['fi.xi'].sum()
    somafixi2 = tabela['fi.xi²'].sum()

    somas = [somafi, somafr, somafrp, somafixi, somafixi2]

    return somas

def addSomaTabela(tabela, somas):

    tabela.loc[tabela.shape[0]] = ['Total', '', '', somas[0], '', '', '', somas[1], somas[2], somas[3], '', somas[4]]

    return tabela

def media(somas):

    x = somas[3] / somas[0]
    return x

def mediana(somas, tabela, h):

    n = somas[0]
    if (n % 2 == 0):
        posicao = int(n / 2)
    else:
        posicao = int((n + 1) / 2)

    for i in range(len(tabela)):
        if (tabela['fa'].iloc[i] >= posicao):
            classe = i
            break

    li = tabela['li'].iloc[classe]
    faant = tabela['fa'].iloc[classe - 1]
    fi = tabela['fi'].iloc[classe]

    mediana = li + (((posicao - faant) / fi) * h)

    return mediana

def moda(tabela, h):

    fi = tabela['fi']
    classe = fi.idxmax()
    li = tabela['li'].iloc[classe]
    d1 = fi.iloc[classe] - tabela['fi'].iloc[classe - 1]
    d2 = fi.iloc[classe] - tabela['fi'].iloc[classe + 1]

    moda = li + ((d1 / (d1 + d2)) * h)

    return moda

def varianciaPopulacional(somas):

    n = somas[0]
    somafixi2 = somas[4]
    media = somas[3] / n

    variancia = (somafixi2 / n) - (media ** 2)

    return variancia

def varianciaAmostral(somas):

    n = somas[0]
    somafixi2 = somas[4]
    media = somas[3] / n

    variancia = ((somafixi2 / n) - (media ** 2)) * (n / (n - 1))

    return variancia

def desvioPadrao(variancia):

    desvio = math.sqrt(variancia)

    return desvio

def coeficienteVariacao(desvio, media):

    cv = (desvio / media) * 100

    return cv

# Função para lidar com o botão "Calcular"
def calcular():
    try:
        # Obtendo os dados inseridos pelo usuário
        dados = list(map(float, entrada_dados.get().split()))
        
        # Realizando os cálculos
        n = quantidadeDados(dados)
        at = amplitudeTotal(dados)
        k = quantidadeClasses(n)
        h = amplitudeClasse(at, k)
        minVal = menorValor(dados)
        maxVal = maiorValor(dados)

        tabela = criarTabelaFrequencias(dados, h, minVal, maxVal)
        somas = somasTabela(tabela)

        x = media(somas)
        md = mediana(somas, tabela, h)
        mo = moda(tabela, h)
        variPop = varianciaPopulacional(somas)
        variAmo = varianciaAmostral(somas)
        desvio = desvioPadrao(variAmo)
        cv = coeficienteVariacao(desvio, x)

        tabela = addSomaTabela(tabela, somas)

        # Exibindo os resultados na interface gráfica
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, str(tabela) + '\n\n')
        resultado_text.insert(tk.END, f'Média: {x:.5f}\n')
        resultado_text.insert(tk.END, f'Mediana: {md:.5f}\n')
        resultado_text.insert(tk.END, f'Moda: {mo:.5f}\n')
        resultado_text.insert(tk.END, f'Variância populacional: {variPop:.5f}\n')
        resultado_text.insert(tk.END, f'Variância amostral: {variAmo:.5f}\n')
        resultado_text.insert(tk.END, f'Desvio padrão: {desvio:.5f}\n')
        resultado_text.insert(tk.END, f'Coeficiente de variação: {cv:.5f}%\n')

    except ValueError:
        messagebox.showerror('Erro', 'Certifique-se de inserir dados numéricos válidos.')

# Criando a interface gráfica
root = tk.Tk()
root.title('Análise Estatística')

# Criando os elementos da interface
tk.Label(root, text='Insira os dados separados por espaço:').pack()
entrada_dados = tk.Entry(root)
entrada_dados.pack()

calcular_button = tk.Button(root, text='Calcular', command=calcular)
calcular_button.pack()

resultado_text = tk.Text(root, height=15, width=200)
resultado_text.pack()

root.mainloop()