import conectar

# armazenando a conexão na variável conexao para usar
conexao = conectar.getConexao()

# Cursor para usar instruções no banco de dados
cursor = conexao.cursor()

# Comando sql para o banco de dados
sql = """
    SELECT vdor.nome_vendedor, sale.id_venda, sale.dt_venda, c.nome_cliente, sale.vl_total_venda FROM venda sale
    INNER JOIN vendedor vdor ON sale.id_vendedor = vdor.id_vendedor
    INNER JOIN cliente c ON sale.id_cliente = c.id_cliente
    WHERE vdor.id_vendedor = %s
    AND YEAR(sale.dt_venda) = %s
    AND MONTH(sale.dt_venda) = %s
"""
# pedindo ao usuário as informações para a consulta
n_vendedor = input("Informe o id do vendedor para consulta: ")
ano = input("Informe o ano: ")
mes = input("Informe o mês: ")

# Executando
cursor.execute(sql, (n_vendedor, ano, mes))
a = cursor.fetchall()
cursor.close()

# Mostrando na tela
for linhas in a:
    print(f"Vendedor(a): {linhas[0]} - Data da venda: {linhas[2]} - Cliente: {linhas[3]} - Valor total: {linhas[4]}")