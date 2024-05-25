import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, expand

def lagrange_interpolating_polynomial(x, y):
    n = len(x)
    poly = 0
    t = symbols('t')
    
    for i in range(n):
        Li = 1
        for j in range(n):
            if i != j:
                Li *= (t - x[j]) / (x[i] - x[j])
        poly += y[i] * Li
    
    return expand(poly)


# Função para plotar o polinômio interpolador e os pontos
def plot_lagrange_interpolation(x, y, poly, x_interp, y_interp):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'ro', label='Pontos dados')
    plt.plot(x_interp, y_interp, 'b-', label='Polinômio interpolador de Lagrange')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolação Polinomial de Lagrange')
    plt.legend()
    plt.grid(True)
    plt.show()

# Solicitar ao usuário os valores de x, y e o valor a ser interpolado
x = list(map(float, input("Insira os valores de x separados por espaços: ").split()))
y = list(map(float, input("Insira os valores de y separados por espaços: ").split()))
x_val = float(input("Insira o valor de x a ser interpolado: "))

# Geração de pontos para o gráfico do polinômio interpolador
x_interp = np.linspace(min(x), max(x), 500)
poly = lagrange_interpolating_polynomial(x, y)
y_interp = [poly.evalf(subs={'t': xi}) for xi in x_interp]

# Avaliação do polinômio no ponto desejado
y_val = poly.evalf(subs={'t': x_val})

print(f"O polinômio interpolador é: {poly}")
print(f"O valor interpolado no ponto x = {x_val} é y = {y_val}")

# Plotagem do polinômio interpolador e os pontos dados
plot_lagrange_interpolation(x, y, poly, x_interp, y_interp)
