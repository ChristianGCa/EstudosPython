import conectar

# armazenando a conexão na variável conexao para usar
conexao = conectar.getConexao()

# Cursor para usar instruções preparadas no banco de dados
cursor = conexao.cursor(prepared=True)

# Comando para inserir dois registros de venda, sendo o primeiro a venda de duas agendas e o segundo de duas reguas de metal
sql = "INSERT INTO venda (id_venda, id_vendedor, id_cliente, dt_venda, vl_total_venda) VALUES (default, ?, ?, ?, ?)"
vendas = [ (1, 1, '2023-10-25', 13.08),
           (15, 4, '2023-11-26', 3.56)
]

# Abatendo do estoque ambos os produtos
sql2 = "UPDATE item SET qtde_estoque = qtde_estoque - 2 WHERE id_grupo = ? AND id_item = ?"
produtos = [ (4, 33),
             (4, 41)
]

# Executando tudo
cursor.executemany(sql, vendas)
cursor.executemany(sql2, produtos)
conexao.commit()
print(cursor.rowcount, "registros concluídos")