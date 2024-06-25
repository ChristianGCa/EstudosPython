import json
import conectar
from datetime import date

# armazenando a conexão na variável conexao para usar
conexao = conectar.getConexao()

# Cursor para obter resultados como dicionários
cursor = conexao.cursor(dictionary=True)

# Comando sql para o banco de dados
sql = """
    SELECT sale.id_venda, sale.dt_venda, c.nome_cliente, vdor.nome_vendedor, sale.vl_total_venda
    FROM venda sale
    INNER JOIN cliente c ON sale.id_cliente = c.id_cliente
    INNER JOIN vendedor vdor ON sale.id_vendedor = vdor.id_vendedor
"""

cursor.execute(sql)
vendas = cursor.fetchall()

# Função 
def serialize_date(obj):
    if isinstance(obj, date):
        return obj.isoformat()

# Exportar para JSON
with open('vendas.json', 'w', encoding='utf-8') as json_file:
    json.dump(vendas, json_file, default=serialize_date, indent=4)

cursor.close()