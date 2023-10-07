a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

if a > b:
    diferenca = a - b
    print("O maior é", a, "e a diferença entre os números é", diferenca)
elif b > a:
    diferenca = b - a
    print("O maior é", b, "e a diferença entre os números é", diferenca)
else:
    print("Os números são iguais")

