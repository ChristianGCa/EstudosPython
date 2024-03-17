import tkinter as tk

def calcular_media():
    numeros = entrada.get().split()  # Obtém os números do campo de entrada
    numeros = [float(num) for num in numeros if num.strip()]  # Converte para float, removendo espaços vazios
    if numeros:  # Verifica se a lista não está vazia
        media = sum(numeros) / len(numeros)
        resultado_label.config(text=f'Média: {media:.2f}')
    else:
        resultado_label.config(text='Nenhum número válido foi inserido.')

# Cria a janela principal
janela = tk.Tk()
janela.title('Calculadora de Média')

# Cria um rótulo e um campo de entrada para os números
tk.Label(janela, text='Digite os números separados por espaços:').pack()
entrada = tk.Entry(janela)
entrada.pack()

# Cria um botão para calcular a média
calcular_botao = tk.Button(janela, text='Calcular Média', command=calcular_media)
calcular_botao.pack()

# Cria um rótulo para exibir o resultado
resultado_label = tk.Label(janela, text='')
resultado_label.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()