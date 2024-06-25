import mysql.connector

import banco

con = banco.getConexao()
cursor = con.cursor(prepared=True)

nome = input("Informe o nome para consulta:")

sql = "select * from cliente where nome_cliente like ?"
par = ["%"+nome+"%"]
cursor.execute(sql, par)

resultado = cursor.fetchall()
for x in resultado:
  print(" {nome_cliente}")

print("\nLinhas retornadas:", cursor.rowcount)

con.close