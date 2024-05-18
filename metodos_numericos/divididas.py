x = input("Insira os valores de x separados por espaços: ").split()
y = input("Insira os valores de y separados por espaços: ").split()

x = [float(i) for i in x]
y = [float(i) for i in y]


if len(x) != len(y):
    print("Erro: Os vetores devem ter o mesmo tamanho!")
    exit()

ordem_max = int(input("Digite a ordem máxima a ser calculada: "))
D = [y]
for ordem in range(1, ordem_max + 1):
    D_ordem = []
    for i in range(len(D[ordem - 1]) - 1):
        D_ordem.append((D[ordem - 1][i + 1] - D[ordem - 1][i]) / (x[i + ordem] - x[i]))
    D.append(D_ordem)
    print(f"D{ordem}y = ", D_ordem)
