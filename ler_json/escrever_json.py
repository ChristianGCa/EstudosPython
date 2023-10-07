import json

# Armazena em uma variável a seguinte lista
dados = [
    {
        "nome": "Alberto",
        "idade": 70
    },

    {
        "nome": "Julio",
        "idade": 19
    }
]

with open('escrever.json', 'w') as arq:
    # Gravar em arquivo
    json.dump(dados, arq)
