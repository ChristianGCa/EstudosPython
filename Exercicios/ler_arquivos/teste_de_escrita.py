
# Criando o arquivo ex2.txt vazio em modo de gravação. Se executado de novo, ele sobrescreve.
arquivo = open("ex2.txt", "w")

# Escrevendo no arquivo
arquivo.write("Olá mundo\n")
arquivo.write("Beba água!")

# Fechando o arquivo
arquivo.close()