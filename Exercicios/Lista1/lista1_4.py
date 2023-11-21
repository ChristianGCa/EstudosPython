
print("\n/////////////  SUPER CORRETOR DE PROVAS  /////////////")
print('by Christian\n')

# variável de controle "continuar".
# Quando o usuário deseja parar de conferir respostas ou quando algum
# input for digitado errado, ela armazena 'f'
continuar = 's' 
n_de_questoes = int(input("Informe o número de questões: "))

#recebe uma string com o gabarito já convertido para letras maiúsculas e retira o traço (-)
gab = input("Informe as respostas no formato A-B-C-D-E: ").upper() 
gab = gab.replace('-', '')

#caracteres permitidos no gabarito
char_permitidos = "ABCDE-"

#confere se o n de questões é o mesmo do gabarito digitado
if n_de_questoes != len(gab):                 
    print("ERRO: O numero das questoes nao corresponde ao gabarito.")
    continuar = 'n'

#verifica se tem algum caractere inválido
for char in gab:
    if char not in char_permitidos:
        print("ERRO: Use Apenas A, B, C, D e E, separados por (-)")
        continuar = 'n'
        break

while continuar == 's':
    
    #captura o gabarito digitado, torna tudo maiúsculo e remove o traço (-)
    gab_aluno = input("\nDigite o gabarito do aluno: ").upper()
    gab_aluno = gab_aluno.replace('-', '')
    tudocerto = 's'

    #verifica se há caracteres não permitidos
    for char in gab_aluno:
        if char not in char_permitidos:
            print("ERRO: Use Apenas A, B, C, D e E, separados por (-)")
            tudocerto = 'n'
            break

    while tudocerto == 's':

        #confere se o n de questões é o mesmo do gabarito do aluno digitado
        if n_de_questoes != len(gab_aluno):
            print("\nERRO: O gabarito do aluno nao corresponde ao numero de questoes. Tente novamente.")
            break
        else:
            #calcula e mostra a quantidade de acertos
            acertos = 0
            i = 0
            for i in range(len(gab)):
                if  gab[i] == gab_aluno[i]:
                    acertos += 1
            print("Número de acertos: ", acertos)

            #pergunta se deseja continuar com outro gabarito
            continuar = input("\nVerificar gabarito de outro aluno? s/n: ").lower()
            break

print("\nFim do programa")

