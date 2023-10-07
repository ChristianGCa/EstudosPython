
#abrindo o arquivo arq_exemplo em modo leitura
arquivo = open("arq_exemplo.txt", "r")

#armazenando o conteúdo do arquivo em uma variável
conteudo = arquivo.read()

#fechando o arquivo
arquivo.close()

print(conteudo)
