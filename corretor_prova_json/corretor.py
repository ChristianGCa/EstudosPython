import json

print('//////////////////////////////////////////////////////////////////////////')
print('///////////////////////  CORRETOR DE PROVAS json  ////////////////////////')
print('//////////////////////////////////////////////////////////////////////////')

# Abrindo e armazenando o conteúdo do gabarito (gabarito correto e respostas dos alunos) em uma variável
arq = open('gabarito.json')
gab = json.load(arq)

# Armazenando a parte do gabarito em uma variável
gabarito = gab['gabarito']

# Armazenando a parte do gabarito dos alunos em outra variável
gabarito_alunos = gab['alunos']

# Armazena as alternativas permitidas (A - E)
alternativas_permitidas = ['A', 'B', 'C', 'D', 'E']

# Função para certificar alternativas inválidas dos alunos
def verificarGabarito(letra):

    if alternativas_permitidas.__contains__(letra):
        return True
    else:
        return False

# Correção da prova
for aluno in gabarito_alunos:

    acertos = 0

    # Contador
    c = 0
    print("\nCorreção do(a) aluno(a)", aluno['nome'])
    print()

    for questao in aluno['respostas']:
        
        # Armazenando as respostas dos gabaritos em variáveis
        alternativa_gabarito = (gabarito[c]['resposta']).upper()
        alternativa_aluno = (questao['resposta']).upper()

        # Verifica alternativas inválidas
        if verificarGabarito(alternativa_aluno):

            # Mostra na tela a resposta do gabarito e a do aluno
            print(f"Gabarito: {alternativa_gabarito}; Resposta do aluno: {alternativa_aluno}")

            # Se as respostas forem iguais, soma-se um (1) na variável acertos
            if alternativa_aluno == alternativa_gabarito:
                acertos += 1
                print("Resposta CERTA")
            else:
                print("Resposta ERRADA")

            # Incrementando contador
            c += 1

        else:
            print("Gabarito do aluno contém alternativa inválida")
    print("ACERTOS: ", acertos)

    # Adicionando um novo campo com os acertos em cada aluno
    aluno['acertos'] = acertos

# Reescrevendo o gabarito original em outro arquivo, porém com os acertos de cada aluno
with open('resultado.json', 'w') as arq2:
    json.dump(gab, arq2, indent = 4)
    
# Fechar o arquivo
arq.close()

