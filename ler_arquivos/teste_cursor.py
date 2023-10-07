
# arq é usado para realizar operações de leitura e escrita de dados binários em arq_exemplo.txt
arq = open("arq_exemplo.txt", "rb+")

# Mostra na tela os próximos 5 bytes e a posição do cursor
print (arq.read(5))
print("Posição atual no arquivo: ", arq.tell())


arq.seek(6, 1)
print("Posição atual no arquivo: ", arq.tell())

print(arq.read(7))
print("Posição atual no arquivo: ", arq.tell())

arq.seek(10, 1)
print("Posição atual no arquivo: ", arq.tell())

print (arq.read(7))
print("Posição atual no arquivo: ", arq.tell())