# Função para calcular se o aluno foi aprovado ou reprovado
def calcular_situacao(media):
    return "Aprovado" if media >= 60 else "Reprovado"

# Armazenar a quantidade de alunos
quantidade_alunos = int(input("Informe a quantidade de alunos: "))

# Inicializando variáveis
total_aprovados = 0
total_reprovados = 0
soma_notas1 = 0
soma_notas2 = 0
soma_medias = 0
alunos = []

# Ler os dados de cada aluno
for i in range(quantidade_alunos):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota1 = float(input("Digite a nota 1 do(a) aluno(a): "))
    nota2 = float(input("Digite a nota 2 do(a) aluno(a): "))
    media = (nota1 + nota2) / 2
    situacao = calcular_situacao(media)
    
    # Adicionar as informações do aluno à lista de alunos
    alunos.append({
        "Nome": nome,
        "Nota 1": nota1,
        "Nota 2": nota2,
        "Média": media,
        "Situação": situacao
    })
    
    # Atualizar as variáveis de contagem e cálculo da média da turma
    if situacao == "Aprovado(a)":
        total_aprovados += 1
    else:
        total_reprovados += 1
    soma_notas1 += nota1
    soma_notas2 += nota2
    soma_medias += media

# Calcular percentuais e médias da turma
percentual_aprovados = (total_aprovados / quantidade_alunos) * 100
percentual_reprovados = (total_reprovados / quantidade_alunos) * 100
media_notas1_turma = soma_notas1 / quantidade_alunos
media_notas2_turma = soma_notas2 / quantidade_alunos
media_medias_turma = soma_medias / quantidade_alunos

# Exibir informações dos alunos e estatísticas da turma
print("\nInformações dos Alunos:")
for aluno in alunos:
    print(f"Nome: {aluno['Nome']}")
    print(f"Nota 1: {aluno['Nota 1']}")
    print(f"Nota 2: {aluno['Nota 2']}")
    print(f"Média: {aluno['Média']}")
    print(f"Situação: {aluno['Situação']}\n")

print("\nEstatísticas da Turma:")
print(f"Total de Alunos Aprovados: {total_aprovados}")
print(f"Total de Alunos Reprovados: {total_reprovados}")
print(f"Percentual de Aprovação: {percentual_aprovados:.2f}%")
print(f"Percentual de Reprovação: {percentual_reprovados:.2f}%")
print(f"Média de Notas (Nota 1) da Turma: {media_notas1_turma:.2f}")
print(f"Média de Notas (Nota 2) da Turma: {media_notas2_turma:.2f}")
print(f"Média de Médias da Turma: {media_medias_turma:.2f}")
