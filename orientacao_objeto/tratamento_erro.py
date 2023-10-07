
try:
    while True:
        try:
            x = int(input('Digite um número: '))
            break
        except ValueError:
            print('Esse não é um número válido')

# Depois que tudo foi excecutado, finalmente
finally:
    print('Número OK')