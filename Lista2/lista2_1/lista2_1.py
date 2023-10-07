print("\n//////////////////////////////////////////////////////")
print("/////////////  SUPER CORRETOR DE PROVAS  /////////////")
print("//////////////////////////////////////////////////////")

# Abrindo o gabarito, armazenando em gab e removendo os espaços em branco e os traços (-)
arq = open("gabarito.txt", "r")
arq.seek(0)
gab = arq.read().strip().replace("-", "")
arq.close()

# Verifica se tem algum caractere inválido
continuar = 1
char_permitidos = "ABCDE-"
for char in gab:
    if char not in char_permitidos:
        print("ERRO: Use Apenas A, B, C, D e E no arquivo do gabarito, separados por (-) e em uma única linha.")
        continuar = 0
        break
print("Gabarito:", "-".join(gab))

# Obtendo o número de questões
n_de_questoes = len(gab)
print("Número de questões:", n_de_questoes)

if continuar == 1:
    # abre o gabarito dos alunos
    arq = open("gabarito_alunos.txt", "r")

    # Conta o número de linhas
    numero_de_linhas = 0
    for linhas in arq:
        numero_de_linhas += 1
    print("Quantidade de alunos:", numero_de_linhas)
    arq.seek(0)

    arq_resultado = open("resultado.txt", "w")
    i = 0
    while i < numero_de_linhas:
                    
        acertos = 0
        aluno_gab = arq.readline().strip().replace("-", "").split(';')
        aluno_nome = aluno_gab[0]
        aluno_gab_certo = aluno_gab[1]
        print("\nAluno:", aluno_gab[0])

        for char in aluno_gab_certo:
            if char not in char_permitidos:
                print("AVISO: O gabarito do aluno apresenta caracteres inválidos!")

        for j in range(len(gab)):
            if  gab[j] == aluno_gab_certo[j]:
                        acertos += 1
        i += 1
        
        aluno_gab_certo = "-".join(aluno_gab_certo)
        print("Gabarito do aluno:", aluno_gab_certo)
        print("Acertos: ", acertos)

        arq_resultado.write(f"{aluno_nome};{aluno_gab_certo};{acertos};\n")

arq.close()  
print("\nFim do programa")